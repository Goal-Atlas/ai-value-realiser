"""
Run Steps 1–3 (discovery, extraction, claim extraction) for new AI value cases.

This script expects a JSON file in the format:

[
  {
    "organisation": "...",
    "initiative_description": "...",
    "original_case_id": "org-initiative-2026",
    "legacy_urls": ["https://example.com/case-study-1", "..."],
    "research_priority": "high" | "medium" | "low",
    "notes": "optional free text"
  },
  ...
]

By default it looks for `case_library/data/cases/New_AI_cases.json`.

Search and LLM backends:

- Search: for now we rely on the `legacy_urls` you provide in the JSON as the
  initial set of source URLs. The discovery step is still run (so you can later
  plug in a real search function), but the default `search_fn` returns no extra
  URLs, so only your `legacy_urls` are used.

- LLM (Step 3): if the environment variable `ANTHROPIC_API_KEY` is set, the
  script will call Claude via the `anthropic` Python SDK. Otherwise it will
  skip Step 3 for that case and print a warning.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import List

from case_library.pipeline.orchestrator import (
    run_discovery_and_extraction_for_seed,
)
from case_library.pipeline.step3_claims import run_claim_extraction
from case_library.schemas import SeedEntry
from case_library.runtime.config import build_anthropic_llm_fn, load_env


DEFAULT_SEEDS_PATH = Path("case_library/data/cases/New_AI_cases.json")


def load_seeds(path: Path = DEFAULT_SEEDS_PATH) -> List[SeedEntry]:
    data = json.loads(path.read_bytes().decode("utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"Expected a list of seed objects in {path}")
    return [SeedEntry(**item) for item in data]


def default_search_fn(query: str, k: int) -> list[str]:
    """
    Placeholder search function.

    For now, we rely on the `legacy_urls` embedded in each SeedEntry and do not
    perform external web search. This function is still invoked by the
    orchestrator (for logging and future extensibility) but always returns
    an empty list.

    To plug in a real search backend, replace this function with a call to
    your preferred search API.
    """
    _ = (query, k)
    return []


def anthropic_llm_fn() -> callable:
    llm_fn, _model = build_anthropic_llm_fn()
    return llm_fn


def main() -> None:
    load_env()
    seeds = load_seeds()
    print(f"Loaded {len(seeds)} new AI cases from {DEFAULT_SEEDS_PATH}")

    try:
        llm_fn, model_name = build_anthropic_llm_fn()
    except Exception as exc:  # noqa: BLE001
        llm_fn = None
        model_name = os.getenv("ANTHROPIC_MODEL", "unknown-model")
        print(f"[WARN] Claude LLM not configured: {exc}")

    for seed in seeds:
        print("\n" + "=" * 80)
        print(f"Building case: {seed.original_case_id}")
        print(f"Organisation: {seed.organisation}")
        print(f"Initiative:   {seed.initiative_description}")

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
            continue

        num_value = len(extraction.value_claims)
        num_context = len(extraction.context_claims)
        print(f"- Extracted {num_value} value claims and {num_context} context claims")
        if num_value:
            print("  Example value claim titles:")
            for vc in extraction.value_claims[:3]:
                print(f"    - {vc.claim_title} (level={vc.evidence_level}, attr={vc.ai_attribution})")


if __name__ == "__main__":
    main()

