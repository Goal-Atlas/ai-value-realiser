"""
Batch-run ISIC industry classification for the case library and write overlay.

Uses the prompt and schema from:
  case_library/Classifier_Over-layer/Industry_sectors/Instructions_Sector_Classification/

For each case: loads case_id, title, organisation, description (from casefile.md
or claims.json), calls Claude with ISIC taxonomy and structured output, then
appends to overlays/industry_sector/classifications.json.

Usage:
  python -m case_library.run_industry_classification --library case_library/out --overlays case_library/overlays
  python -m case_library.run_industry_classification --library case_library/out --limit 3 --dry-run
  python -m case_library.run_industry_classification --case-id accenture-retail-marketing-optimization

When using --case-id, existing classifications.json is always merged (never replaced).
Use --append to merge when re-running the full batch. A safety check prevents
overwriting many existing entries with fewer unless you pass --append.
"""

from __future__ import annotations

import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# Add Instructions folder so we can import classification_schemas
_CASE_LIBRARY_ROOT = Path(__file__).resolve().parent
_INSTRUCTIONS = _CASE_LIBRARY_ROOT / "Classifier_Over-layer" / "Industry_sectors" / "Instructions_Sector_Classification"
if _INSTRUCTIONS.is_dir() and str(_INSTRUCTIONS) not in sys.path:
    sys.path.insert(0, str(_INSTRUCTIONS))

from classification_schemas import ISICClassification, validate_division_matches_section  # noqa: E402

from case_library.runtime.config import get_env, load_env  # noqa: E402


def _load_yaml_frontmatter(md_path: Path) -> dict:
    """Load YAML frontmatter from a markdown file (e.g. casefile.md)."""
    if not md_path.is_file():
        return {}
    text = md_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        import yaml
        data = yaml.safe_load(parts[1]) or {}
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def _humanize_case_id(case_id: str) -> str:
    """Turn case-id-slug into a readable title (e.g. first segment)."""
    return case_id.replace("-", " ").replace("_", " ").split()[0].title() if case_id else ""


def load_case_for_classification(case_dir: Path) -> dict | None:
    """
    Load case_id, title, organisation, description for the classification user message.
    Prefers casefile.md frontmatter; falls back to claims.json.
    """
    case_dir = Path(case_dir)
    case_id = case_dir.name
    claims_path = case_dir / "claims.json"
    casefile_path = case_dir / "casefile.md"

    title = ""
    organisation = ""
    description = ""

    if casefile_path.is_file():
        fm = _load_yaml_frontmatter(casefile_path)
        title = str(fm.get("title") or "").strip()
        organisation = str(fm.get("organisation") or fm.get("org") or "").strip()
        description = str(fm.get("description") or fm.get("initiative_description") or "").strip()

    if claims_path.is_file():
        try:
            data = json.loads(claims_path.read_text(encoding="utf-8"))
            vc_list = data.get("value_claims") or []
            if vc_list:
                vc = vc_list[0]
                if not title:
                    title = str(vc.get("claim_title") or "").strip()
                if not description:
                    description = str(vc.get("claim_description") or vc.get("claim_title") or "").strip()
        except Exception:
            pass

    if not title:
        title = _humanize_case_id(case_id) or case_id
    if not organisation:
        organisation = _humanize_case_id(case_id)
    if not description:
        description = title

    return {
        "case_id": case_id,
        "title": title,
        "organisation": organisation,
        "description": description[:2000],  # cap for prompt size
    }


def load_system_prompt(instructions_dir: Path, taxonomy: dict) -> str:
    """Load classification_prompt.md and inject taxonomy JSON."""
    prompt_path = instructions_dir / "classification_prompt.md"
    if not prompt_path.is_file():
        raise FileNotFoundError(f"Prompt not found: {prompt_path}")
    text = prompt_path.read_text(encoding="utf-8")
    # Extract first fenced code block (system prompt)
    m = re.search(r"```\s*\n(.*?)```", text, re.DOTALL)
    if not m:
        raise ValueError("No code block found in classification_prompt.md")
    system_prompt = m.group(1).strip()
    placeholder = "{Insert full isic_taxonomy.json content here}"
    if placeholder not in system_prompt:
        raise ValueError(f"Placeholder {placeholder!r} not found in prompt")
    taxonomy_str = json.dumps(taxonomy, indent=2)
    return system_prompt.replace(placeholder, taxonomy_str)


def build_user_message(case: dict) -> str:
    """Build user message from case dict."""
    return (
        "Classify the following AI case study by industry:\n\n"
        f"**Case ID:** {case['case_id']}\n"
        f"**Title:** {case['title']}\n"
        f"**Organisation:** {case['organisation']}\n"
        f"**Description:**\n{case['description']}"
    )


def classification_to_overlay_entry(
    case_id: str,
    classification: ISICClassification,
    *,
    tagged_by: str = "llm",
    tagged_date: str | None = None,
) -> dict:
    """Convert ISICClassification to overlay classifications.json entry."""
    if tagged_date is None:
        tagged_date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    code = classification.division_code or classification.section_code
    name = classification.division_name or classification.section_name
    return {
        "case_id": case_id,
        "primary_sector": {
            "code": code,
            "name": name,
            "taxonomy": "ISIC_Rev_5",
        },
        "secondary_sectors": [],
        "confidence": classification.confidence.value if hasattr(classification.confidence, "value") else str(classification.confidence),
        "tagged_by": tagged_by,
        "tagged_date": tagged_date,
        "notes": classification.rationale,
        "key_indicators": getattr(classification, "key_indicators", []) or [],
    }


def run_classification_for_case(
    case: dict,
    system_prompt: str,
    *,
    client,
    model: str,
    delay_seconds: float = 1.0,
    use_structured_output: bool = True,
) -> dict | None:
    """
    Call Claude for one case; return overlay entry dict or None on failure.
    Tries response_format (structured output) if supported; falls back to prompt-based JSON.
    """
    user_message = build_user_message(case)
    raw = None

    # Try structured output first (newer SDK)
    if use_structured_output:
        try:
            response = client.messages.create(
                model=model,
                max_tokens=1024,
                system=system_prompt,
                messages=[{"role": "user", "content": user_message}],
                response_format={
                    "type": "json_schema",
                    "json_schema": {
                        "name": "isic_classification",
                        "schema": ISICClassification.model_json_schema(),
                    },
                },
            )
            for block in getattr(response, "content", []):
                if getattr(block, "text", None):
                    raw = block.text
                    break
        except TypeError:
            use_structured_output = False
        except Exception as e:
            print(f"  API error for {case['case_id']}: {e}")
            return None

    # Fallback: prompt-based JSON (no response_format)
    if raw is None:
        try:
            response = client.messages.create(
                model=model,
                max_tokens=1024,
                system=system_prompt + "\n\nRespond with ONLY a valid JSON object, no markdown or prose.",
                messages=[{"role": "user", "content": user_message}],
            )
            for block in getattr(response, "content", []):
                if getattr(block, "text", None):
                    raw = block.text
                    break
        except Exception as e:
            print(f"  API error for {case['case_id']}: {e}")
            return None

    if not raw:
        print(f"  Empty response for {case['case_id']}")
        return None

    # Strip markdown fences if present
    raw = raw.strip()
    if raw.startswith("```"):
        lines = raw.splitlines()
        if lines:
            lines = lines[1:]
        if lines and lines[-1].strip().startswith("```"):
            lines = lines[:-1]
        raw = "\n".join(lines).strip()
    if raw and not raw.lstrip().startswith("{"):
        start, end = raw.find("{"), raw.rfind("}")
        if start != -1 and end != -1 and end > start:
            raw = raw[start : end + 1]

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"  Parse error for {case['case_id']}: {e}")
        return None

    # Normalise LLM output to schema limits before validation
    if isinstance(data.get("rationale"), str) and len(data["rationale"]) > 500:
        data["rationale"] = data["rationale"][:500].rstrip()
    if isinstance(data.get("key_indicators"), list) and len(data["key_indicators"]) > 5:
        data["key_indicators"] = data["key_indicators"][:5]

    try:
        classification = ISICClassification.model_validate(data)
    except Exception as e:
        print(f"  Parse error for {case['case_id']}: {e}")
        return None

    if not validate_division_matches_section(classification):
        print(f"  Validation: division does not match section for {case['case_id']}")
        return None

    if delay_seconds > 0:
        time.sleep(delay_seconds)

    return classification_to_overlay_entry(case["case_id"], classification)


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description="Run ISIC industry classification on case library and write overlay"
    )
    parser.add_argument(
        "--library",
        type=Path,
        default=Path("case_library/out"),
        help="Case library root (default: case_library/out)",
    )
    parser.add_argument(
        "--overlays",
        type=Path,
        default=Path("case_library/overlays"),
        help="Overlays root (default: case_library/overlays)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Max number of cases to classify (default: all)",
    )
    parser.add_argument(
        "--case-id",
        action="append",
        dest="case_ids",
        help="Only classify these case ID(s); can be repeated",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Load cases and prompt only; do not call API or write",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=1.0,
        help="Seconds between API calls (default: 1.0)",
    )
    parser.add_argument(
        "--append",
        action="store_true",
        help="Merge with existing classifications.json (default when using --case-id if file exists)",
    )
    args = parser.parse_args()

    library_path = args.library.resolve()
    overlays_path = args.overlays.resolve()
    instructions_dir = _INSTRUCTIONS.resolve()

    if not library_path.is_dir():
        print(f"Error: library not found: {library_path}")
        return
    if not instructions_dir.is_dir():
        print(f"Error: instructions not found: {instructions_dir}")
        return

    # Case dirs (full library list first for total count and safety checks)
    all_case_dirs = sorted(
        d for d in library_path.iterdir()
        if d.is_dir() and not d.name.startswith(".") and (d / "claims.json").is_file()
    )
    total_library_cases = len(all_case_dirs)
    case_dirs = all_case_dirs
    if args.case_ids:
        case_dirs = [d for d in case_dirs if d.name in args.case_ids]
        if not case_dirs:
            print(f"No cases found matching: {args.case_ids}")
            return
    if args.limit is not None:
        case_dirs = case_dirs[: args.limit]

    print(f"Library: {library_path}")
    print(f"Cases to classify: {len(case_dirs)}" + (f" (of {total_library_cases} in library)" if args.case_ids else ""))
    if args.dry_run:
        print("Mode: dry-run (no API calls, no writes)\n")
        for d in case_dirs[:5]:
            case = load_case_for_classification(d)
            if case:
                title_preview = (case["title"] or "")[:50]
        print(f"  {case['case_id']}: org={case['organisation']!r}, title={title_preview!r}...")
        if len(case_dirs) > 5:
            print(f"  ... and {len(case_dirs) - 5} more")
        return

    # Load taxonomy and system prompt
    taxonomy_path = instructions_dir / "isic_taxonomy.json"
    if not taxonomy_path.is_file():
        print(f"Error: taxonomy not found: {taxonomy_path}")
        return
    taxonomy = json.loads(taxonomy_path.read_text(encoding="utf-8"))
    system_prompt = load_system_prompt(instructions_dir, taxonomy)

    load_env()
    import anthropic
    api_key = (
        get_env("ANTHROPIC_API_KEY")
        or get_env("ANTHROPIC_APIKEY")
        or get_env("ANTHROPIC_API_KEY_V1")
    )
    if not api_key:
        print(
            "Error: No Anthropic API key found. Set ANTHROPIC_API_KEY in .env or the environment "
            "(same as for run_legacy_cases). Use plain ASCII quotes in .env, not smart quotes."
        )
        return

    client = anthropic.Anthropic(api_key=api_key)
    model = get_env("ANTHROPIC_MODEL", "claude-sonnet-4-20250514")

    # Load existing classifications when appending or when running a subset (--case-id)
    # so we never overwrite the full overlay with fewer entries.
    overlay_dir = overlays_path / "industry_sector"
    overlay_dir.mkdir(parents=True, exist_ok=True)
    classifications_path = overlay_dir / "classifications.json"
    existing_by_case: dict[str, dict] = {}
    merge_with_existing = args.append or (
        bool(args.case_ids) and classifications_path.is_file()
    )
    if merge_with_existing and classifications_path.is_file():
        try:
            data = json.loads(classifications_path.read_text(encoding="utf-8"))
            for c in data.get("classifications", []):
                cid = c.get("case_id")
                if cid:
                    existing_by_case[cid] = c
            if existing_by_case:
                print(f"  Merging with {len(existing_by_case)} existing classification(s).")
        except Exception:
            pass

    results: list[dict] = list(existing_by_case.values())
    seen_ids = set(existing_by_case)
    done = 0
    failed = 0

    for case_dir in case_dirs:
        case = load_case_for_classification(case_dir)
        if not case:
            failed += 1
            continue
        if case["case_id"] in seen_ids and merge_with_existing:
            continue
        entry = run_classification_for_case(
            case,
            system_prompt,
            client=client,
            model=model,
            delay_seconds=args.delay,
        )
        if entry:
            results.append(entry)
            seen_ids.add(case["case_id"])
            done += 1
            print(f"  [{done}] {case['case_id']} -> {entry['primary_sector']['code']} {entry['primary_sector']['name'][:50]}...")
        else:
            failed += 1

    # Safety: refuse to overwrite many existing entries with fewer (avoids accidental data loss)
    existing_count = len(existing_by_case)
    if not merge_with_existing and classifications_path.is_file():
        try:
            existing_data = json.loads(classifications_path.read_text(encoding="utf-8"))
            existing_count = len(existing_data.get("classifications", []))
        except Exception:
            existing_count = 0
    if (
        classifications_path.is_file()
        and not merge_with_existing
        and existing_count > 0
        and len(results) < existing_count
    ):
        print(
            f"\nRefusing to overwrite: {existing_count} existing classification(s) would be "
            f"replaced by {len(results)}. Use --append to merge with existing, or run without "
            "--case-id to re-run the full batch."
        )
        return

    # Write classifications.json (skip if no new results and we would overwrite)
    if results or not merge_with_existing:
        out_data = {
            "version": "1.0",
            "taxonomy_ref": "ISIC_Rev_5",
            "classifications": results,
        }
        classifications_path.write_text(json.dumps(out_data, indent=2), encoding="utf-8")
        print(f"\nWrote {len(results)} classifications to {classifications_path}")
    else:
        print(f"\nNo classifications to write (all failed).")

    # Update metadata.json coverage (preserve total when merging)
    meta_path = overlay_dir / "metadata.json"
    if meta_path.is_file():
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            prev_total = meta.get("coverage", {}).get("total_cases", 0)
            total = (
                total_library_cases
                if not merge_with_existing
                else max(total_library_cases, prev_total, len(results))
            )
            meta["coverage"] = {
                "total_cases": total,
                "classified_cases": len(results),
                "coverage_percent": round(100.0 * len(results) / total, 1) if total else 0,
            }
            meta["last_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
        except Exception:
            pass

    if failed:
        print(f"Failed: {failed}")


if __name__ == "__main__":
    main()
