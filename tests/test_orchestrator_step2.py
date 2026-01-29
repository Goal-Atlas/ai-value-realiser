"""
Tests for the Step 2 orchestrator.
"""

from typing import Any, Iterable, List

from case_library.pipeline.orchestrator import run_step2_extraction_for_case
from case_library.pipeline.step2_extraction import ExtractionResult
from case_library.schemas import MultiPageDetection, SourceExtraction


def _make_source_extraction(source_id: str, url: str, content: str) -> SourceExtraction:
    from datetime import datetime

    return SourceExtraction(
        source_id=source_id,
        source_url=url,
        fetch_timestamp=datetime.utcnow(),
        fetch_status="success",
        extraction_method="trafilatura",
        content_length=len(content),
        content=content,
        is_multi_page=False,
        multi_page_detection=MultiPageDetection(),
    )


def test_run_step2_extraction_for_case_builds_log(monkeypatch: Any) -> None:
    """Orchestrator should populate BuildLog.step_2_extraction from extraction results."""

    from case_library.pipeline import step2_extraction

    def fake_extract_sources(
        urls: Iterable[str],
        *,
        starting_source_index: int = 1,  # noqa: ARG001
        timeout: float = 15.0,  # noqa: ARG001
    ) -> List[ExtractionResult]:
        # Return two synthetic extractions regardless of input URLs
        src1 = _make_source_extraction("S1", "https://example.com/one", "content one" * 20)
        src2 = _make_source_extraction("S2", "https://example.com/two", "content two" * 5)
        return [
            ExtractionResult(source=src1, is_insufficient=False),
            ExtractionResult(source=src2, is_insufficient=False),
        ]

    monkeypatch.setattr(step2_extraction, "extract_sources_from_urls", fake_extract_sources)

    build_log, sources = run_step2_extraction_for_case(
        case_id="test-case-001",
        urls=["https://example.com/one", "https://example.com/two"],
    )

    # Verify sources are propagated
    assert len(sources) == 2
    assert {s.source_id for s in sources} == {"S1", "S2"}

    # Verify BuildLog structure
    assert build_log.case_id == "test-case-001"
    assert build_log.step_2_extraction is not None
    assert len(build_log.step_2_extraction.sources) == 2

    src_logs = build_log.step_2_extraction.sources
    assert {s.source_id for s in src_logs} == {"S1", "S2"}
    assert all(s.raw_file is None and s.text_file is None for s in src_logs)

