"""
Pipeline orchestrator helpers.

This module wires individual pipeline steps together without performing any
network or AI work itself. For Step 2 (Content Extraction) it:

- Calls the pure `extract_sources_from_urls` function
- Wraps the results into a `BuildLog` structure suitable for `build.json`

Disk I/O (writing `cases/{case-id}/sources/*` and `build.json`) is left to
higher-level application code or CLI commands.
"""

from __future__ import annotations

from datetime import datetime
from typing import Iterable, List, Tuple

from case_library.pipeline.step1_discovery import (
    DiscoveryResult,
    SearchFn,
    discover_sources_for_seed,
)
from case_library.pipeline.step2_extraction import (
    ExtractionResult,
    extract_sources_from_urls,
)
from case_library.pipeline.step4_verification import run_step4_verification
from case_library.pipeline.step5_validation import record_human_validation
from case_library.schemas import BuildLog, SeedEntry, SourceExtraction
from case_library.schemas import ContextClaim, ValueClaim, ValidationTier


def run_step2_extraction_for_case(
    case_id: str,
    urls: Iterable[str],
    *,
    starting_source_index: int = 1,
) -> Tuple[BuildLog, List[SourceExtraction]]:
    """
    Run Step 2 (Content Extraction) for a single case and return:

    - A `BuildLog` instance with `step_2_extraction` populated
    - The list of `SourceExtraction` records produced by the step

    This function does not perform any disk I/O; callers are responsible for:
    - Writing raw and extracted text files under `cases/{case-id}/sources/*`
    - Serialising `BuildLog` to `build.json`
    """
    started = datetime.utcnow()

    extraction_results: List[ExtractionResult] = extract_sources_from_urls(
        urls,
        starting_source_index=starting_source_index,
    )

    # Build the step_2_extraction log from the in-memory results.
    step2_sources: List[BuildLog.Step2ExtractionSourceLog] = []

    for result in extraction_results:
        src = result.source
        step2_sources.append(
            BuildLog.Step2ExtractionSourceLog(
                source_id=src.source_id,
                url=src.source_url,
                http_status=None,
                retries=0,
                raw_file=None,
                text_file=None,
                extraction_method=src.extraction_method,
                extraction_quality=None,
                content_length=src.content_length,
                ocr_fallback_used=src.extraction_method == "tesseract_ocr",
                is_multi_page=src.is_multi_page,
                multi_page_detection=src.multi_page_detection,
            )
        )

    step2_log = BuildLog.Step2ExtractionLog(
        sources=step2_sources,
        multi_page_candidates=[],
        multi_page_followed=[],
    )

    build_log = BuildLog(
        case_id=case_id,
        build_started=started,
        build_completed=datetime.utcnow(),
        step_1_discovery=None,
        step_2_extraction=step2_log,
        step_3_claims=None,
        step_4_verification=None,
        step_5_human_validation=None,
    )

    extracted_sources: List[SourceExtraction] = [res.source for res in extraction_results]
    return build_log, extracted_sources


def run_discovery_and_extraction_for_seed(
    seed: SeedEntry,
    *,
    search_fn: SearchFn,
    max_urls: int = 10,
    per_query: int = 10,
    starting_source_index: int = 1,
) -> Tuple[BuildLog, List[SourceExtraction], DiscoveryResult]:
    """
    Run Step 1 (Source Discovery) + Step 2 (Content Extraction) for a seed.

    - Uses `discover_sources_for_seed` with a pluggable `search_fn`
    - Feeds discovered URLs into `run_step2_extraction_for_case`
    - Returns:
        - A `BuildLog` with both `step_1_discovery` and `step_2_extraction` populated
        - The list of `SourceExtraction` records from Step 2
        - The `DiscoveryResult` from Step 1 (for inspection/debugging)
    """
    # Step 1: discovery
    discovery: DiscoveryResult = discover_sources_for_seed(
        seed,
        search_fn=search_fn,
        max_urls=max_urls,
        per_query=per_query,
    )

    # Step 2: extraction
    build_log, sources = run_step2_extraction_for_case(
        case_id=seed.original_case_id,
        urls=discovery.candidate_urls,
        starting_source_index=starting_source_index,
    )

    # Populate step_1_discovery in the build log
    build_log.step_1_discovery = BuildLog.Step1DiscoveryLog(
        model=None,
        search_queries=discovery.search_queries,
        results_considered=len(discovery.candidate_urls),
        urls_ranked=[
            {"url": url, "rank": idx + 1} for idx, url in enumerate(discovery.candidate_urls)
        ],
        urls_selected=list(discovery.candidate_urls),
        retries=0,
    )

    return build_log, sources, discovery


def run_step4_verification_for_case(
    build_log: BuildLog,
    *,
    value_claims: Iterable[ValueClaim],
    context_claims: Iterable[ContextClaim],
    sources: Iterable[SourceExtraction],
    model_name: str | None = None,
) -> tuple[BuildLog, list[ValueClaim], list[ContextClaim]]:
    """
    Run Step 4 (Verification) and populate `build_log.step_4_verification`.

    This function verifies claim quotes against the captured extracted text
    (SourceExtraction.content) and records per-claim match attempts with offsets.
    """
    updated_value, updated_context, step4_log = run_step4_verification(
        value_claims=value_claims,
        context_claims=context_claims,
        sources=sources,
        model_name=model_name,
    )
    build_log.step_4_verification = step4_log
    return build_log, updated_value, updated_context


def run_step5_human_validation_for_case(
    build_log: BuildLog,
    value_claims: Iterable[ValueClaim],
    context_claims: Iterable[ContextClaim],
    *,
    tier: ValidationTier = ValidationTier.TIER_1,
    reviewer_id: str | None = None,
    verdicts: dict[str, str] | None = None,
    time_taken_minutes: int | None = None,
    missed_claims_added: int = 0,
    precision_score: float | None = None,
    recall_score: float | None = None,
) -> tuple[BuildLog, list[ValueClaim], list[ContextClaim]]:
    """
    Run Step 5 (Human Validation) and populate `build_log.step_5_human_validation`.

    verdicts: map claim_id -> "valid" | "invalid" | "unclear".
    Returns (updated build_log, updated value_claims, updated context_claims).
    """
    return record_human_validation(
        build_log,
        value_claims,
        context_claims,
        tier=tier,
        reviewer_id=reviewer_id,
        verdicts=verdicts,
        time_taken_minutes=time_taken_minutes,
        missed_claims_added=missed_claims_added,
        precision_score=precision_score,
        recall_score=recall_score,
    )


__all__ = [
    "run_step2_extraction_for_case",
    "run_discovery_and_extraction_for_seed",
    "run_step4_verification_for_case",
    "run_step5_human_validation_for_case",
]

