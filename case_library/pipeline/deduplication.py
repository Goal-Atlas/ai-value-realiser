"""
Source deduplication utilities for the AI Case Library pipeline.

Provides:
- URL normalisation to canonical forms
- URL-based duplicate detection
- Content-based duplicate detection
- Combined deduplication pipeline
"""

from __future__ import annotations

import re
from collections import defaultdict
from difflib import SequenceMatcher
from typing import Any, Callable, Optional
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse


# =============================================================================
# CONFIGURATION
# =============================================================================

# Locale patterns to normalise (path segment like /gb-en/ or /en_GB/ -> /en-us/)
LOCALE_PATTERNS = [
    (re.compile(r"/[a-z]{2}-[a-z]{2}/", re.IGNORECASE), "/en-us/"),
    (re.compile(r"/[a-z]{2}_[A-Z]{2}/", re.IGNORECASE), "/en-us/"),
]

# Query params to strip (tracking, session, locale)
STRIP_QUERY_PARAMS = {
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_term",
    "utm_content",
    "fbclid",
    "gclid",
    "msclkid",
    "locale",
    "lang",
    "language",
    "hl",
    "ref",
    "source",
    "from",
    "_ga",
    "_gid",
}

# Default content similarity threshold
DEFAULT_SIMILARITY_THRESHOLD = 0.85

# Sample size for content comparison (characters)
CONTENT_SAMPLE_SIZE = 5000


# =============================================================================
# URL NORMALISATION
# =============================================================================


def normalise_url(url: str) -> str:
    """
    Normalise a URL to a canonical form for duplicate detection.

    Operations:
    - Lowercase scheme and host
    - Remove trailing slashes
    - Normalise locale path segments to preferred locale
    - Strip tracking/session query parameters
    - Sort remaining query parameters
    """
    try:
        parsed = urlparse(url)
    except Exception:
        return url

    scheme = parsed.scheme.lower()
    netloc = parsed.netloc.lower()

    path = parsed.path
    for pattern, replacement in LOCALE_PATTERNS:
        path = pattern.sub(replacement, path)

    if path != "/":
        path = path.rstrip("/")

    if parsed.query:
        params = parse_qs(parsed.query, keep_blank_values=True)
        filtered = {
            k: v for k, v in params.items() if k.lower() not in STRIP_QUERY_PARAMS
        }
        query = urlencode(sorted(filtered.items()), doseq=True)
    else:
        query = ""

    return urlunparse((scheme, netloc, path, "", query, ""))


def get_url_signature(url: str) -> str:
    """
    Extract a signature for grouping potential duplicates (e.g. locale variants).
    Domain + normalised path, no query.
    """
    try:
        parsed = urlparse(url)
    except Exception:
        return url.lower()

    netloc = parsed.netloc.lower()
    if netloc.startswith("www."):
        netloc = netloc[4:]

    path = parsed.path.lower()
    for pattern, _ in LOCALE_PATTERNS:
        path = pattern.sub("/", path)
    path = path.rstrip("/") or "/"

    return f"{netloc}{path}"


# =============================================================================
# URL-BASED DEDUPLICATION
# =============================================================================


def dedupe_urls(urls: list[str]) -> list[str]:
    """
    Deduplicate a list of URLs based on normalised form.
    Preserves order, keeping the first occurrence of each normalised URL.
    """
    seen_normalised: set[str] = set()
    result: list[str] = []

    for url in urls:
        norm = normalise_url(url)
        if norm not in seen_normalised:
            seen_normalised.add(norm)
            result.append(url)

    return result


def find_url_duplicates(urls: list[str]) -> list[tuple[int, int, str]]:
    """
    Find duplicate URL pairs based on signature matching.
    Returns list of (index1, index2, shared_signature) tuples.
    """
    by_signature: dict[str, list[int]] = defaultdict(list)
    for i, url in enumerate(urls):
        sig = get_url_signature(url)
        by_signature[sig].append(i)

    duplicates = []
    for sig, indices in by_signature.items():
        if len(indices) > 1:
            for i, idx1 in enumerate(indices):
                for idx2 in indices[i + 1 :]:
                    duplicates.append((idx1, idx2, sig))
    return duplicates


# =============================================================================
# CONTENT-BASED DEDUPLICATION
# =============================================================================


def content_similarity(text1: str, text2: str) -> float:
    """
    Calculate similarity ratio between two text contents.
    Uses SequenceMatcher on truncated texts for performance.
    """
    if not text1 or not text2:
        return 0.0
    t1 = text1[:CONTENT_SAMPLE_SIZE]
    t2 = text2[:CONTENT_SAMPLE_SIZE]
    return SequenceMatcher(None, t1, t2).ratio()


def _get_id(source: Any, get_id: Optional[Callable[[Any], str]], index: int) -> str:
    """Get source id from object or dict."""
    if get_id is not None:
        return get_id(source) or str(index)
    if isinstance(source, dict):
        return source.get("source_id", str(index))
    return getattr(source, "source_id", str(index))


def dedupe_by_content(
    sources: list[Any],
    get_content: Callable[[Any], str],
    threshold: float = DEFAULT_SIMILARITY_THRESHOLD,
    get_id: Optional[Callable[[Any], str]] = None,
) -> tuple[list[Any], list[tuple[str, str, float]]]:
    """
    Deduplicate sources by content similarity.

    Args:
        sources: List of source objects (dict or object with source_id and content).
        get_content: Function(source) -> str that retrieves content.
        threshold: Similarity threshold (0.0-1.0) above which sources are duplicates.
        get_id: Optional function(source) -> str for source id; default uses source_id attr/key.

    Returns:
        (kept_sources, dropped_duplicates) where dropped_duplicates is
        list of (dropped_id, kept_id, similarity).
    """
    kept: list[Any] = []
    kept_contents: list[str] = []
    dropped: list[tuple[str, str, float]] = []

    for idx, source in enumerate(sources):
        content = get_content(source)
        source_id = _get_id(source, get_id, idx)

        is_duplicate = False
        duplicate_of: Optional[str] = None
        duplicate_sim = 0.0

        for i, existing_content in enumerate(kept_contents):
            sim = content_similarity(content, existing_content)
            if sim >= threshold:
                is_duplicate = True
                duplicate_of = _get_id(kept[i], get_id, i)
                duplicate_sim = sim
                break

        if is_duplicate and duplicate_of is not None:
            dropped.append((source_id, duplicate_of, duplicate_sim))
        else:
            kept.append(source)
            kept_contents.append(content)

    return kept, dropped


# =============================================================================
# COMBINED PIPELINE
# =============================================================================


class DeduplicationResult:
    """Result of deduplication process."""

    def __init__(
        self,
        kept: list[Any],
        dropped_url: list[tuple[Any, Any, str]],
        dropped_content: list[tuple[Any, Any, float]],
    ):
        self.kept = kept
        self.dropped_url = dropped_url  # (dropped_source, kept_source, signature)
        self.dropped_content = dropped_content  # (dropped_source, kept_source, similarity)

    @property
    def total_dropped(self) -> int:
        return len(self.dropped_url) + len(self.dropped_content)

    def to_log_dict(self) -> dict:
        """Format for build log."""
        get_id = lambda s: (
            s.get("source_id") if isinstance(s, dict) else getattr(s, "source_id", "")
        )
        return {
            "kept_count": len(self.kept),
            "dropped_url_pattern": len(self.dropped_url),
            "dropped_content_similarity": len(self.dropped_content),
            "url_duplicates": [
                {"dropped": get_id(d[0]), "duplicate_of": get_id(d[1]), "signature": d[2]}
                for d in self.dropped_url
            ],
            "content_duplicates": [
                {
                    "dropped": get_id(d[0]),
                    "duplicate_of": get_id(d[1]),
                    "similarity": round(d[2], 4),
                }
                for d in self.dropped_content
            ],
        }


def dedupe_sources_pipeline(
    sources: list[Any],
    get_url: Callable[[Any], str],
    get_content: Callable[[Any], str],
    content_threshold: float = DEFAULT_SIMILARITY_THRESHOLD,
    get_id: Optional[Callable[[Any], str]] = None,
) -> DeduplicationResult:
    """
    Full deduplication pipeline: URL normalisation then content similarity.

    Args:
        sources: List of source objects.
        get_url: Function(source) -> str to get URL.
        get_content: Function(source) -> str to get content.
        content_threshold: Similarity threshold for content deduplication.
        get_id: Optional function(source) -> str for source id.
    """
    if len(sources) < 2:
        return DeduplicationResult(sources, [], [])

    # Stage 1: URL-based deduplication
    url_seen: dict[str, Any] = {}
    url_kept: list[Any] = []
    url_dropped: list[tuple[Any, Any, str]] = []

    for source in sources:
        url = get_url(source)
        norm = normalise_url(url)
        if norm in url_seen:
            url_dropped.append((source, url_seen[norm], get_url_signature(url)))
        else:
            url_seen[norm] = source
            url_kept.append(source)

    # Stage 2: Content-based deduplication on remaining
    content_kept, content_dropped_raw = dedupe_by_content(
        url_kept, get_content, content_threshold, get_id=get_id
    )

    # Map ids back to full source references for log
    id_to_source = {}
    for s in url_kept:
        sid = _get_id(s, get_id, -1)
        id_to_source[sid] = s
    content_dropped = [
        (id_to_source.get(d[0]), id_to_source.get(d[1]), d[2])
        for d in content_dropped_raw
        if d[0] in id_to_source and d[1] in id_to_source
    ]

    return DeduplicationResult(content_kept, url_dropped, content_dropped)
