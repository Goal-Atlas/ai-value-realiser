"""
Tests for Step 2: Content Extraction pipeline.
"""

from datetime import datetime
from typing import Any

from case_library.pipeline.step2_extraction import (
    ExtractionResult,
    extract_sources_from_urls,
)


class DummyResponse:
    """Simple stand-in for httpx.Response for testing."""

    def __init__(self, url: str, status_code: int, content: bytes, content_type: str):
        self.status_code = status_code
        self.content = content
        self._text = content.decode("utf-8", errors="ignore")
        self.headers = {"Content-Type": content_type}

        class _URL:
            def __init__(self, raw: str) -> None:
                self._raw = raw

            @property
            def path(self) -> str:
                return self._raw

            def __str__(self) -> str:
                return self._raw

        self.url = _URL(url)

    @property
    def text(self) -> str:  # type: ignore[override]
        return self._text


def test_extract_html_success(monkeypatch: Any) -> None:
    """HTML pages should be extracted with trafilatura and marked sufficient when long enough."""

    from case_library.pipeline import step2_extraction

    html = "<html><body>" + ("hello " * 50) + "</body></html>"

    def fake_fetch(url: str, timeout: float = 15.0) -> DummyResponse:  # type: ignore[override]
        return DummyResponse(url=url, status_code=200, content=html.encode("utf-8"), content_type="text/html")

    monkeypatch.setattr(step2_extraction, "_fetch_url_with_retries", fake_fetch)

    results = extract_sources_from_urls(["https://example.com/article"])
    assert len(results) == 1

    res: ExtractionResult = results[0]
    src = res.source

    assert src.source_id == "S1"
    assert src.fetch_status == "success"
    assert src.extraction_method == "trafilatura"
    assert src.content is not None
    assert isinstance(src.fetch_timestamp, datetime)
    assert src.content_length is not None and src.content_length >= 200
    assert res.is_insufficient is False


def test_extract_pdf_with_low_content_triggers_ocr_stub(monkeypatch: Any) -> None:
    """PDF responses with very low text yield should switch extraction_method to tesseract_ocr."""

    from case_library.pipeline import step2_extraction

    # This is *not* a real PDF; the test only checks that we fall through to the low-length branch.
    # We simulate a PDF by content-type and URL extension; _extract_text_from_pdf will likely return empty.
    fake_pdf_bytes = b"%PDF-1.4\n%"  # minimal header, no actual pages

    def fake_fetch(url: str, timeout: float = 15.0) -> DummyResponse:  # type: ignore[override]
        return DummyResponse(
            url="/test.pdf",
            status_code=200,
            content=fake_pdf_bytes,
            content_type="application/pdf",
        )

    # Monkeypatch the network fetch and force _extract_text_from_pdf to return a very short string.
    def fake_extract_pdf(content: bytes) -> str:  # noqa: ARG001
        return "short"

    monkeypatch.setattr(step2_extraction, "_fetch_url_with_retries", fake_fetch)
    monkeypatch.setattr(step2_extraction, "_extract_text_from_pdf", fake_extract_pdf)

    results = extract_sources_from_urls(["https://example.com/test.pdf"])
    assert len(results) == 1

    res = results[0]
    src = res.source

    assert src.extraction_method == "tesseract_ocr"
    # Content is too short, so is_insufficient should be True
    assert res.is_insufficient is True


def test_extract_failed_url(monkeypatch: Any) -> None:
    """Failed fetches should produce SourceExtraction with fetch_status='failed' and no content."""

    from case_library.pipeline import step2_extraction

    def fake_fetch(url: str, timeout: float = 15.0) -> DummyResponse:  # noqa: ARG001
        raise RuntimeError("network failure")

    monkeypatch.setattr(step2_extraction, "_fetch_url_with_retries", fake_fetch)

    results = extract_sources_from_urls(["https://example.com/broken"])
    assert len(results) == 1

    res = results[0]
    src = res.source

    assert src.fetch_status == "failed"
    assert src.content is None
    assert src.content_length is None
    assert res.is_insufficient is True

