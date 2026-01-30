"""
Clean up duplicate sources in existing case library cases.

For each case:
1. Load build.json, claims.json, and sources/text/*.txt
2. Run URL + content deduplication (same logic as pipeline)
3. Build mapping: old source_id -> new source_id (renumbered S1, S2, …; dropped -> kept)
4. Update claims: source_ids and quote_source_id
5. Update build: step_2_extraction (sources + deduplication log), step_4_verification (attempts)
6. Write new sources/text/S1.txt, S2.txt, … and remove orphaned files
7. Write build.json and claims.json

Usage:
    python -m case_library.cleanup_duplicate_sources --path case_library/out --dry-run
    python -m case_library.cleanup_duplicate_sources --path case_library/out --apply
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

from case_library.pipeline.deduplication import dedupe_sources_pipeline
from case_library.pipeline.persistence import (
    BUILD_JSON,
    CLAIMS_JSON,
    SOURCES_TEXT_DIR,
    read_build_log,
    read_claims,
    read_source_text,
    write_build_log,
    write_claims,
    write_sources_text,
)
from case_library.schemas import BuildLog, ContextClaim, MultiPageDetection, SourceExtraction, ValueClaim


def load_sources_with_content(case_dir: Path, step2_sources: list[dict]) -> list[dict]:
    """Build list of source dicts with 'content' from sources/text."""
    out = []
    for s in step2_sources:
        sid = s.get("source_id", "")
        content = read_source_text(case_dir, sid) or ""
        out.append({**s, "source_id": sid, "content": content})
    return out


def build_old_to_new(
    kept: list[dict],
    dropped_url: list[tuple],
    dropped_content: list[tuple],
) -> dict[str, str]:
    """
    Build mapping old source_id -> new source_id (S1, S2, …).
    Dropped sources map to the kept source's new id.
    """
    # Renumber kept to S1, S2, S3, …
    old_to_new = {kept[i]["source_id"]: f"S{i + 1}" for i in range(len(kept))}
    # Map dropped -> kept's new id
    for dropped_src, kept_src, _ in dropped_url:
        old_id = dropped_src.get("source_id")
        kept_id = kept_src.get("source_id")
        if old_id and kept_id and kept_id in old_to_new:
            old_to_new[old_id] = old_to_new[kept_id]
    for dropped_src, kept_src, _ in dropped_content:
        old_id = dropped_src.get("source_id")
        kept_id = kept_src.get("source_id")
        if old_id and kept_id and kept_id in old_to_new:
            old_to_new[old_id] = old_to_new[kept_id]
    return old_to_new


def update_claim_source_ids(claim: dict, old_to_new: dict[str, str]) -> dict:
    """Return new claim dict with source_ids and quote_source_id updated."""
    out = dict(claim)
    if "source_ids" in out and out["source_ids"]:
        new_ids = list(dict.fromkeys(old_to_new[s] for s in out["source_ids"] if s in old_to_new))
        out["source_ids"] = new_ids
    if "quote_source_id" in out and out["quote_source_id"]:
        out["quote_source_id"] = old_to_new.get(out["quote_source_id"]) or out["quote_source_id"]
    return out


def cleanup_case(case_dir: Path, content_threshold: float = 0.85) -> dict | None:
    """
    Run deduplication and in-memory updates for one case.
    Returns summary dict (sources_before, sources_after, dropped_url, dropped_content)
    or None if case cannot be processed.
    """
    case_dir = Path(case_dir)
    build_path = case_dir / BUILD_JSON
    claims_path = case_dir / CLAIMS_JSON
    if not build_path.is_file() or not claims_path.is_file():
        return None

    build = read_build_log(case_dir)
    if build is None or build.step_2_extraction is None:
        return None

    step2 = build.step_2_extraction
    step2_sources = [s.model_dump() for s in step2.sources]
    if len(step2_sources) < 2:
        return {
            "case_dir": case_dir,
            "case_id": case_dir.name,
            "sources_before": len(step2_sources),
            "sources_after": len(step2_sources),
            "dropped_url": 0,
            "dropped_content": 0,
        }

    sources_with_content = load_sources_with_content(case_dir, step2_sources)
    dedup_result = dedupe_sources_pipeline(
        sources_with_content,
        get_url=lambda s: s.get("url", ""),
        get_content=lambda s: s.get("content", ""),
        content_threshold=content_threshold,
        get_id=lambda s: s.get("source_id"),
    )

    old_to_new = build_old_to_new(
        dedup_result.kept,
        dedup_result.dropped_url,
        dedup_result.dropped_content,
    )

    # Update claims
    value_claims, context_claims = read_claims(case_dir)
    value_claims_dicts = [update_claim_source_ids(c.model_dump(mode="json"), old_to_new) for c in value_claims]
    context_claims_dicts = [update_claim_source_ids(c.model_dump(mode="json"), old_to_new) for c in context_claims]
    value_claims_new = [ValueClaim.model_validate(d) for d in value_claims_dicts]
    context_claims_new = [ContextClaim.model_validate(d) for d in context_claims_dicts]

    # New step_2_extraction: renumbered sources + deduplication log
    new_step2_sources = []
    for i, s in enumerate(dedup_result.kept):
        orig = next((x for x in step2.sources if x.source_id == s.get("source_id")), None)
        mpd = orig.multi_page_detection if orig else MultiPageDetection()
        new_step2_sources.append(
            BuildLog.Step2ExtractionSourceLog(
                source_id=f"S{i + 1}",
                url=s.get("url", ""),
                http_status=s.get("http_status"),
                retries=s.get("retries", 0),
                raw_file=s.get("raw_file"),
                text_file=s.get("text_file") or f"sources/text/S{i + 1}.txt",
                extraction_method=s.get("extraction_method"),
                extraction_quality=s.get("extraction_quality"),
                content_length=len(s.get("content") or ""),
                ocr_fallback_used=s.get("ocr_fallback_used", False),
                is_multi_page=s.get("is_multi_page", False),
                multi_page_detection=mpd,
            )
        )

    step2_new = BuildLog.Step2ExtractionLog(
        sources=new_step2_sources,
        multi_page_candidates=step2.multi_page_candidates,
        multi_page_followed=step2.multi_page_followed,
        deduplication=dedup_result.to_log_dict() if dedup_result.total_dropped > 0 else None,
    )

    build_dict = build.model_dump(mode="json")
    build_dict["step_2_extraction"] = step2_new.model_dump(mode="json")

    # Update step_4_verification attempts: map source_id, dedupe (claim_id, source_id)
    if build.step_4_verification and build.step_4_verification.verification_attempts:
        seen = set()
        new_attempts = []
        for a in build.step_4_verification.verification_attempts:
            new_sid = old_to_new.get(a.source_id)
            if new_sid is None:
                continue
            key = (a.claim_id, new_sid)
            if key in seen:
                continue
            seen.add(key)
            new_attempts.append(
                BuildLog.VerificationAttempt(
                    claim_id=a.claim_id,
                    source_id=new_sid,
                    method=a.method,
                    result=a.result,
                    char_offset_start=a.char_offset_start,
                    char_offset_end=a.char_offset_end,
                    match_confidence=a.match_confidence,
                    ai_explanation=a.ai_explanation,
                )
            )
        build_dict["step_4_verification"] = {
            **build.step_4_verification.model_dump(mode="json"),
            "verification_attempts": [t.model_dump(mode="json") for t in new_attempts],
        }

    build_new = BuildLog.model_validate(build_dict)

    # SourceExtraction list for writing sources/text
    renumbered_sources = []
    for i, s in enumerate(dedup_result.kept):
        orig = next((x for x in step2.sources if x.source_id == s.get("source_id")), None)
        mpd = orig.multi_page_detection if orig else MultiPageDetection()
        renumbered_sources.append(
            SourceExtraction(
                source_id=f"S{i + 1}",
                source_url=s.get("url", ""),
                fetch_timestamp=datetime.now(timezone.utc),
                fetch_status="success",
                extraction_method=s.get("extraction_method"),
                content_length=len(s.get("content") or ""),
                content=s.get("content"),
                is_multi_page=s.get("is_multi_page", False),
                multi_page_detection=mpd,
            )
        )

    return {
        "case_dir": case_dir,
        "case_id": case_dir.name,
        "sources_before": len(step2_sources),
        "sources_after": len(dedup_result.kept),
        "dropped_url": len(dedup_result.dropped_url),
        "dropped_content": len(dedup_result.dropped_content),
        "build_new": build_new,
        "value_claims_new": value_claims_new,
        "context_claims_new": context_claims_new,
        "renumbered_sources": renumbered_sources,
        "old_to_new": old_to_new,
    }


def apply_cleanup(result: dict) -> None:
    """Write build, claims, sources/text and remove orphaned text files."""
    case_dir = result["case_dir"]
    text_dir = case_dir / SOURCES_TEXT_DIR
    new_ids = {s.source_id for s in result["renumbered_sources"]}

    write_build_log(case_dir, result["build_new"])
    write_claims(case_dir, result["value_claims_new"], result["context_claims_new"])
    write_sources_text(case_dir, result["renumbered_sources"])

    if text_dir.is_dir():
        for f in text_dir.glob("*.txt"):
            if f.stem not in new_ids:
                f.unlink()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Clean duplicate sources from existing case library cases"
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=Path("case_library/out"),
        help="Path to case library root",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only report what would be done; do not write files",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply cleanup (write build.json, claims.json, sources/text)",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.85,
        help="Content similarity threshold (default 0.85)",
    )
    parser.add_argument(
        "--case-id",
        type=str,
        action="append",
        dest="case_ids",
        help="Only process these case ID(s); can be repeated (default: all)",
    )
    args = parser.parse_args()

    path = args.path.resolve()
    if not path.is_dir():
        print(f"Error: not a directory: {path}")
        return

    case_dirs = sorted(
        d for d in path.iterdir()
        if d.is_dir() and not d.name.startswith(".") and (d / BUILD_JSON).is_file()
    )
    if args.case_ids:
        case_dirs = [d for d in case_dirs if d.name in args.case_ids]
        if not case_dirs:
            print(f"No cases found matching: {args.case_ids}")
            return

    print(f"Case library: {path}")
    print(f"Cases found: {len(case_dirs)}")
    if not args.apply and not args.dry_run:
        print("Use --dry-run to see what would change, or --apply to write changes.")
        return

    mode = "apply" if args.apply else "dry-run"
    print(f"Mode: {mode}\n")

    changed = 0
    for case_dir in case_dirs:
        result = cleanup_case(case_dir, content_threshold=args.threshold)
        if result is None:
            continue
        if result["sources_after"] >= result["sources_before"] and result["dropped_url"] == 0 and result["dropped_content"] == 0:
            continue
        changed += 1
        print(f"  {result['case_id']}: {result['sources_before']} -> {result['sources_after']} sources "
              f"(URL drops: {result['dropped_url']}, content drops: {result['dropped_content']})")
        if args.apply:
            apply_cleanup(result)

    print(f"\nDone. {changed} case(s) {'updated' if args.apply else 'would be updated'}.")


if __name__ == "__main__":
    main()
