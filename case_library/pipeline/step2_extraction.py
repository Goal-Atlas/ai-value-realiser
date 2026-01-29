"""
Step 2: Content Extraction (deterministic)

Implements the behaviour described in §6.3 of
`docs/specs/AI_CASE_LIBRARY_SPECIFICATION_v1_5.md`:

- Input: list of URLs (typically from Step 1: Source Discovery)
- Behaviour:
  - HTTP fetch with retries on transient status codes
  - Content extraction for HTML and PDF sources
  - Minimum content length check (200 characters)
  - Basic multi-page detection stub (structure in place, logic can evolve)
- Output: list of `SourceExtraction` records for downstream steps

This module is intentionally **pure** – it does not write to disk. Orchestration
code is responsible for:
- Deciding source IDs (`S1`, `S2`, …)
- Persisting raw responses and extracted text under `cases/{case_id}/sources/*`
- Embedding results into `build.json` (`BuildLog.step_2_extraction`)
"""

from __future__ import annotations

from datetime import datetime
from dataclasses import dataclass
from time import sleep
from typing import Iterable, List, Optional, Tuple

import httpx
from pypdf import PdfReader
import trafilatura

from case_library.schemas import MultiPageDetection, SourceExtraction


RETRY_STATUS_CODES = {429, 500, 502, 503, 504}
MIN_CONTENT_CHARS = 200


@dataclass
class ExtractionResult:
    """Convenience wrapper for extraction outputs."""

    source: SourceExtraction
    is_insufficient: bool


def _fetch_url_with_retries(url: str, timeout: float = 15.0, max_retries: int = 3) -> httpx.Response:
    """
    Fetch a URL with simple retry logic for transient errors.

    Retries on 429 / 5xx (except 501) with exponential backoff: 1s, 2s, 4s.
    Does not retry on 4xx like 401/403/404 – those are treated as final.
    """
    backoff = 1.0
    last_exc: Optional[Exception] = None

    for attempt in range(max_retries + 1):
        try:
            resp = httpx.get(url, timeout=timeout, follow_redirects=True)
            # If status is not in retry set, return immediately
            if resp.status_code not in RETRY_STATUS_CODES:
                return resp
            # Otherwise, fall through to retry logic below
        except Exception as exc:  # Network/transport errors
            last_exc = exc
        else:
            last_exc = None

        if attempt == max_retries:
            if last_exc:
                raise last_exc
            return resp  # type: ignore[UnboundLocalVariable]

        sleep(backoff)
        backoff *= 2

    # Should not reach here
    raise RuntimeError(f"Exhausted retries for URL: {url}")


def _is_pdf_response(resp: httpx.Response) -> bool:
    content_type = resp.headers.get("Content-Type", "").lower()
    if "application/pdf" in content_type:
        return True
    # Fallback: check URL extension
    return resp.url.path.lower().endswith(".pdf")


def _extract_text_from_pdf(content: bytes) -> str:
    """Extract text from PDF bytes using pypdf."""
    try:
        reader = PdfReader.from_bytes(content)
    except Exception:
        return ""

    chunks: list[str] = []
    for page in reader.pages:
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        chunks.append(text)
    return "\n".join(chunks).strip()


def _extract_text_from_html(html: str, url: str) -> str:
    """
    Extract main text from HTML using trafilatura.

    Falls back to raw HTML text if trafilatura returns nothing.
    """
    try:
        extracted = trafilatura.extract(
            html,
            url=url,
            include_comments=False,
            include_tables=False,
            no_fallback=True,
        )
    except Exception:
        extracted = None

    if extracted:
        return extracted.strip()
    return html.strip()


def _basic_multi_page_detection(text: str) -> MultiPageDetection:
    """
    Very lightweight multi-page detection stub.

    The full v1.5 spec defines a richer pattern-based detector. Here we only
    set the structure and leave patterns empty so downstream code can rely
    on the presence of the `MultiPageDetection` object.
    """
    # TODO: Implement full pattern-based detection per §6.3.1 if needed.
    return MultiPageDetection()


def extract_sources_from_urls(
    urls: Iterable[str],
    *,
    starting_source_index: int = 1,
    timeout: float = 15.0,
) -> List[ExtractionResult]:
    """
    Extract content from a list of URLs into `SourceExtraction` records.

    This function is deterministic and side-effect free (no file writes).

    Parameters
    ----------
    urls:
        Iterable of URLs to fetch.
    starting_source_index:
        Index to start numbering source IDs from (S{n}). Defaults to 1.
    timeout:
        Per-request timeout in seconds.

    Returns
    -------
    list[ExtractionResult]
        One result per URL, preserving order. `is_insufficient` is True when
        extracted content has fewer than `MIN_CONTENT_CHARS` characters.
    """
    results: list[ExtractionResult] = []

    for idx, url in enumerate(urls, start=starting_source_index):
        source_id = f"S{idx}"

        try:
            resp = _fetch_url_with_retries(url, timeout=timeout)
        except Exception:
            # Failed fetch – record minimal metadata
            source = SourceExtraction(
                source_id=source_id,
                source_url=url,
                fetch_timestamp=datetime.utcnow(),
                fetch_status="failed",
                extraction_method=None,
                content_length=None,
                content=None,
                is_multi_page=False,
                multi_page_detection=_basic_multi_page_detection(""),
            )
            results.append(ExtractionResult(source=source, is_insufficient=True))
            continue

        status = resp.status_code
        fetch_status = "success" if status == 200 else "inaccessible"

        raw_bytes = resp.content or b""
        text_content = ""
        extraction_method: Optional[str] = None

        if status == 200:
            if _is_pdf_response(resp):
                extraction_method = "pypdf"
                text_content = _extract_text_from_pdf(raw_bytes)

                # OCR fallback stub – we currently only flag the condition;
                # actual OCR integration can be added later.
                if len(text_content) < MIN_CONTENT_CHARS:
                    extraction_method = "tesseract_ocr"
                    # Leave text_content as-is; set low quality to flag for review.
            else:
                extraction_method = "trafilatura"
                text_content = _extract_text_from_html(resp.text, str(resp.url))

        content_length = len(text_content)
        is_insufficient = content_length < MIN_CONTENT_CHARS

        source = SourceExtraction(
            source_id=source_id,
            source_url=str(resp.url),
            fetch_timestamp=datetime.utcnow(),
            fetch_status=fetch_status,
            extraction_method=extraction_method,
            content_length=content_length if text_content else None,
            content=text_content or None,
            is_multi_page=False,
            multi_page_detection=_basic_multi_page_detection(text_content),
        )
        results.append(ExtractionResult(source=source, is_insufficient=is_insufficient))

    return results


__all__ = [
    "ExtractionResult",
    "extract_sources_from_urls",
]

