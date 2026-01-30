"""Unit tests for case_library.pipeline.deduplication."""

from __future__ import annotations

import pytest

from case_library.pipeline.deduplication import (
    content_similarity,
    dedupe_by_content,
    dedupe_sources_pipeline,
    dedupe_urls,
    get_url_signature,
    normalise_url,
)


class TestUrlNormalisation:
    def test_locale_normalisation(self) -> None:
        assert normalise_url("https://example.com/gb-en/page") == normalise_url(
            "https://example.com/us-en/page"
        )

    def test_strips_tracking_params(self) -> None:
        url = "https://example.com/page?utm_source=google&id=123"
        norm = normalise_url(url)
        assert "utm_source" not in norm
        assert "id=123" in norm

    def test_trailing_slash(self) -> None:
        assert normalise_url("https://example.com/page/") == normalise_url(
            "https://example.com/page"
        )

    def test_case_insensitive_host(self) -> None:
        assert normalise_url("https://Example.COM/page") == normalise_url(
            "https://example.com/page"
        )


class TestUrlSignature:
    def test_removes_www(self) -> None:
        assert get_url_signature("https://www.example.com/page") == get_url_signature(
            "https://example.com/page"
        )

    def test_locale_variants_same_signature(self) -> None:
        sig1 = get_url_signature("https://accenture.com/gb-en/services/ai")
        sig2 = get_url_signature("https://accenture.com/mu-en/services/ai")
        assert sig1 == sig2


class TestDedupeUrls:
    def test_removes_duplicates(self) -> None:
        urls = [
            "https://example.com/gb-en/page",
            "https://example.com/us-en/page",
            "https://other.com/page",
        ]
        result = dedupe_urls(urls)
        assert len(result) == 2
        assert "https://example.com/gb-en/page" in result
        assert "https://other.com/page" in result

    def test_preserves_order(self) -> None:
        urls = ["https://a.com", "https://b.com", "https://c.com"]
        assert dedupe_urls(urls) == urls


class TestContentSimilarity:
    def test_identical_content(self) -> None:
        assert content_similarity("hello world", "hello world") == 1.0

    def test_different_content(self) -> None:
        assert content_similarity("hello", "goodbye") < 0.5

    def test_empty_content(self) -> None:
        assert content_similarity("", "hello") == 0.0
        assert content_similarity("", "") == 0.0

    def test_similar_content(self) -> None:
        text1 = "The quick brown fox jumps over the lazy dog."
        text2 = "The quick brown fox leaps over the lazy dog."
        sim = content_similarity(text1, text2)
        assert 0.8 < sim < 1.0


class TestDedupeByContent:
    def test_removes_similar_content(self) -> None:
        sources = [
            {"source_id": "S1", "content": "Hello world, this is a test."},
            {"source_id": "S2", "content": "Hello world, this is a test."},
            {"source_id": "S3", "content": "Completely different content here."},
        ]
        kept, dropped = dedupe_by_content(
            sources,
            get_content=lambda s: s["content"],
            threshold=0.9,
        )
        assert len(kept) == 2
        assert len(dropped) == 1
        assert dropped[0][0] == "S2"
        assert dropped[0][1] == "S1"


class TestDedupeSourcesPipeline:
    def test_url_dedupe_then_content(self) -> None:
        sources = [
            {"source_id": "S1", "url": "https://accenture.com/gb-en/ai", "content": "Same text."},
            {"source_id": "S2", "url": "https://accenture.com/mu-en/ai", "content": "Same text."},
            {"source_id": "S3", "url": "https://other.com/page", "content": "Different."},
        ]
        result = dedupe_sources_pipeline(
            sources,
            get_url=lambda s: s["url"],
            get_content=lambda s: s["content"],
            get_id=lambda s: s["source_id"],
        )
        assert len(result.kept) == 2
        assert len(result.dropped_url) == 1
        assert result.total_dropped == 1

    def test_to_log_dict(self) -> None:
        sources = [
            {"source_id": "S1", "url": "https://a.com/gb-en/p", "content": "x" * 100},
            {"source_id": "S2", "url": "https://a.com/mu-en/p", "content": "x" * 100},
        ]
        result = dedupe_sources_pipeline(
            sources,
            get_url=lambda s: s["url"],
            get_content=lambda s: s["content"],
            get_id=lambda s: s["source_id"],
        )
        log = result.to_log_dict()
        assert "kept_count" in log
        assert "url_duplicates" in log
