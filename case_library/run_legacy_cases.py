"""
Run Steps 1–4 (discovery, extraction, claim extraction, verification) for legacy
AI value cases. Optionally persist build.json, sources/text/*.txt, and claims.json
under an output directory (--out).

This script extracts seed entries from `OLD_cases_enriched/` and runs the
provenance pipeline on them. By default it processes the first 4 cases, but you
can specify a different number or specific case IDs.

Usage:
    python -m case_library.run_legacy_cases [--limit N]
    python -m case_library.run_legacy_cases --out case_library/out [--limit 2]
    python -m case_library.run_legacy_cases --indices 10 20 30 40
    python -m case_library.run_legacy_cases --case-id ID1 [--case-id ID2] ...

Search and LLM backends:
- Search: for now we rely on the `legacy_urls` from the old cases as the
  initial set of source URLs. The discovery step is still run (so you can later
  plug in a real search function), but the default `search_fn` returns no extra
  URLs, so only the `legacy_urls` are used.

- LLM (Step 3): if the environment variable `ANTHROPIC_API_KEY` is set, the
  script will call Claude via the `anthropic` Python SDK. Otherwise it will
  skip Step 3 for that case and print a warning.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import List

from case_library.pipeline.orchestrator import (
    run_discovery_and_extraction_for_seed,
    run_step4_verification_for_case,
)
from case_library.pipeline.casefile_export import write_casefile_md
from case_library.pipeline.migration_progress import (
    mark_done,
    mark_failed,
    migration_report,
)
from case_library.pipeline.persistence import (
    write_build_log,
    write_claims,
    write_sources_text,
)
from case_library.pipeline.step3_claims import run_claim_extraction
from case_library.schemas import SeedEntry, VerificationStatus
from case_library.seed import extract_seed_list
from case_library.runtime.config import build_anthropic_llm_fn, load_env

LEGACY_CASES_ROOT = Path("case_library/OLD_cases_enriched")


def default_search_fn(query: str, k: int) -> list[str]:
    """Placeholder search fn: rely on legacy_urls only."""
    _ = (query, k)
    return []


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run provenance pipeline on legacy AI value cases"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=4,
        help="Maximum number of cases to process (default: 4)",
    )
    parser.add_argument(
        "--case-id",
        action="append",
        dest="case_ids",
        help="Specific case ID(s) to process (can be used multiple times)",
    )
    parser.add_argument(
        "--indices",
        type=int,
        nargs="+",
        metavar="N",
        help="Process cases at these 1-based positions (e.g. --indices 10 20 30 40)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        metavar="DIR",
        help="Write build.json, sources/text/*.txt, claims.json, casefile.md under DIR/<case_id>",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Skip cases already marked done in migration_progress.json (use with --out)",
    )
    args = parser.parse_args()

    # Extract all seed entries from legacy cases
    all_seeds = extract_seed_list(LEGACY_CASES_ROOT)
    print(f"Found {len(all_seeds)} legacy cases in {LEGACY_CASES_ROOT}")

    # Filter to requested cases
    if args.indices is not None:
        # 1-based indices: 10 -> all_seeds[9]
        valid = [i for i in args.indices if 1 <= i <= len(all_seeds)]
        if len(valid) != len(args.indices):
            out_of_range = set(args.indices) - set(valid)
            print(f"[WARN] Indices out of range (1..{len(all_seeds)}): {sorted(out_of_range)}")
        seeds = [all_seeds[i - 1] for i in sorted(set(valid))]
    elif args.case_ids:
        seeds = [s for s in all_seeds if s.original_case_id in args.case_ids]
        if len(seeds) != len(args.case_ids):
            found_ids = {s.original_case_id for s in seeds}
            missing = set(args.case_ids) - found_ids
            if missing:
                print(f"[WARN] Case IDs not found: {missing}")
    else:
        seeds = all_seeds[: args.limit]

    if not seeds:
        print("No cases to process.")
        return

    # Migration progress (when --out set): report and optionally filter to remaining
    seeds_to_run: List[SeedEntry] = list(seeds)
    if args.out is not None:
        seed_ids = [s.original_case_id for s in seeds]
        done_count, to_process_count, to_process_ids = migration_report(
            args.out, len(seeds), seed_ids
        )
        if args.resume and to_process_count < len(seeds):
            seeds_to_run = [s for s in seeds if s.original_case_id in to_process_ids]
            print(f"\nMigration: {done_count}/{len(seeds)} complete, {len(seeds_to_run)} to process (resuming)")
        else:
            print(f"\nMigration: {done_count}/{len(seeds)} complete, {len(seeds_to_run)} to process")
    else:
        print(f"\nProcessing {len(seeds_to_run)} case(s):")

    for seed in seeds_to_run:
        print(f"  - {seed.original_case_id}: {seed.organisation}")

    load_env()
    try:
        llm_fn, model_name = build_anthropic_llm_fn()
    except Exception as exc:  # noqa: BLE001
        llm_fn = None
        model_name = os.getenv("ANTHROPIC_MODEL", "unknown-model")
        print(f"\n[WARN] Claude LLM not configured: {exc}")

    total_run = len(seeds_to_run)
    for run_index, seed in enumerate(seeds_to_run, 1):
        print("\n" + "=" * 80)
        print(f"[{run_index}/{total_run}] Building case: {seed.original_case_id}")
        print(f"Organisation: {seed.organisation}")
        print(f"Initiative:   {seed.initiative_description}")
        print(f"Legacy URLs:  {len(seed.legacy_urls)}")

        # Steps 1 & 2: discovery + extraction
        build_log_12, sources, discovery = run_discovery_and_extraction_for_seed(  # noqa: F841
            seed,
            search_fn=default_search_fn,
            max_urls=5,
            per_query=5,
            starting_source_index=1,
        )

        print(f"- Discovery queries: {discovery.search_queries}")
        print(f"- Candidate URLs ({len(discovery.candidate_urls)}): {discovery.candidate_urls}")
        print(f"- Extracted {len(sources)} sources")

        for idx, src in enumerate(sources, start=1):
            print(f"  [{idx}] {src.source_id}: {src.source_url}")

        if not llm_fn:
            print("- Skipping Step 3 (no Claude API key configured).")
            if args.out is not None:
                mark_failed(args.out, seed.original_case_id, "No LLM configured")
            continue

        # Step 3: claim extraction
        try:
            extraction, step3_log = run_claim_extraction(
                case_id=seed.original_case_id,
                sources=sources,
                llm_fn=llm_fn,
                model_name=model_name,
                prompt_version="v1.0",
            )
        except Exception as exc:  # noqa: BLE001
            print(f"[ERROR] Step 3 failed for {seed.original_case_id}: {exc}")
            if args.out is not None:
                mark_failed(args.out, seed.original_case_id, str(exc))
            continue

        num_value = len(extraction.value_claims)
        num_context = len(extraction.context_claims)
        print(f"- Extracted {num_value} value claims and {num_context} context claims")
        if num_value:
            print("  Example value claim titles:")
            for vc in extraction.value_claims[:3]:
                print(
                    f"    - {vc.claim_title} (level={vc.evidence_level}, attr={vc.ai_attribution})"
                )

        # Merge Step 3 log into build_log and run Step 4 (verification)
        build_log_12.step_3_claims = step3_log
        build_log_4, value_claims_4, context_claims_4 = run_step4_verification_for_case(
            build_log_12,
            value_claims=extraction.value_claims,
            context_claims=extraction.context_claims,
            sources=sources,
            model_name=model_name,
        )
        verified_count = sum(
            1 for v in value_claims_4 if v.verification_status == VerificationStatus.VERIFIED
        )
        print(f"- Step 4: {verified_count}/{num_value} value claims verified")

        # Persist if --out set
        if args.out is not None:
            case_dir = args.out / seed.original_case_id
            case_dir.mkdir(parents=True, exist_ok=True)
            write_build_log(case_dir, build_log_4)
            write_sources_text(case_dir, sources)
            write_claims(case_dir, value_claims_4, context_claims_4)
            write_casefile_md(
                case_dir,
                case_id=seed.original_case_id,
                organisation=seed.organisation,
                title=seed.initiative_description or seed.original_case_id,
                build_log=build_log_4,
                value_claims=value_claims_4,
                context_claims=context_claims_4,
            )
            mark_done(args.out, seed.original_case_id)
            print(f"- Wrote {case_dir}/build.json, sources/text/*.txt, claims.json, casefile.md")
            print(f"- Migration progress: {run_index}/{total_run} — {seed.original_case_id} done")


if __name__ == "__main__":
    main()
