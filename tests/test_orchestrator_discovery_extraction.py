"""
Tests for orchestrator wiring Step 1 (discovery) + Step 2 (extraction).
"""

from typing import Any, Iterable, List, Sequence

from case_library.pipeline.orchestrator import run_discovery_and_extraction_for_seed
from case_library.pipeline.step1_discovery import DiscoveryResult
from case_library.pipeline.step2_extraction import ExtractionResult
from case_library.schemas import MultiPageDetection, SeedEntry, SourceExtraction


def _fake_source_extraction(source_id: str, url: str) -> SourceExtraction:
    from datetime import datetime

    return SourceExtraction(
        source_id=source_id,
        source_url=url,
        fetch_timestamp=datetime.utcnow(),
        fetch_status="success",
        extraction_method="trafilatura",
        content_length=250,
        content="x" * 250,
        is_multi_page=False,
        multi_page_detection=MultiPageDetection(),
    )


def test_run_discovery_and_extraction_for_seed(monkeypatch: Any) -> None:
    """run_discovery_and_extraction_for_seed should populate both step_1 and step_2 logs."""

    from case_library.pipeline import step1_discovery, step2_extraction, orchestrator

    seed = SeedEntry(
        organisation="Example Corp",
        initiative_description="AI-powered customer support assistant",
        original_case_id="example-corp-ai-support",
        legacy_urls=["https://legacy.example.com/support"],
    )

    # Fake search: return a deterministic list of URLs per query
    def fake_search_fn(query: str, k: int) -> Sequence[str]:  # noqa: ARG001
        return [
            f"https://search.example.com/{query.replace(' ', '-').lower()}-1",
            f"https://search.example.com/{query.replace(' ', '-').lower()}-2",
        ]

    # Use the real discovery code but monkeypatch Step 2 extraction to avoid network/use of httpx.
    def fake_extract_sources(
        urls: Iterable[str],
        *,
        starting_source_index: int = 1,  # noqa: ARG001
        timeout: float = 15.0,  # noqa: ARG001
    ) -> List[ExtractionResult]:
        extracted: List[ExtractionResult] = []
        for idx, url in enumerate(urls, start=1):
            src = _fake_source_extraction(f"S{idx}", url)
            extracted.append(ExtractionResult(source=src, is_insufficient=False))
        return extracted

    monkeypatch.setattr(step2_extraction, "extract_sources_from_urls", fake_extract_sources)

    build_log, sources, discovery = run_discovery_and_extraction_for_seed(
        seed,
        search_fn=fake_search_fn,
        max_urls=3,
        per_query=5,
    )

    # Check discovery result
    assert isinstance(discovery, DiscoveryResult)
    assert discovery.seed.original_case_id == "example-corp-ai-support"
    assert any("Example Corp" in q for q in discovery.search_queries)
    assert "https://legacy.example.com/support" in discovery.candidate_urls

    # Check sources and build log
    assert len(sources) == len(discovery.candidate_urls)
    assert build_log.case_id == "example-corp-ai-support"
    assert build_log.step_1_discovery is not None
    assert build_log.step_2_extraction is not None
    assert len(build_log.step_2_extraction.sources) == len(discovery.candidate_urls)

