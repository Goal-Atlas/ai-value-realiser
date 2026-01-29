"""
Step 1: Source Discovery [AI-assisted]

Spec alignment (v1.5 §6.2, §12.3–12.4):

- Input: `SeedEntry` (organisation + initiative_description + legacy_urls)
- Behaviour:
  - Construct search queries from organisation + initiative description
  - Call a search backend to retrieve candidate URLs
  - Optionally add `legacy_urls` as extra candidates
  - Return a **prioritised** list of URLs (most relevant first)

This module defines a small, testable interface around a pluggable search
backend. It does **not** perform real web requests; callers provide a function
that implements `search_fn(query: str, k: int) -> list[str]`.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable, List, Sequence

from case_library.schemas import SeedEntry


SearchFn = Callable[[str, int], Sequence[str]]


@dataclass
class DiscoveryResult:
    """Result of running source discovery for a single seed."""

    seed: SeedEntry
    search_queries: List[str]
    candidate_urls: List[str]


def build_search_queries(seed: SeedEntry) -> List[str]:
    """
    Build a small set of search queries from a SeedEntry.

    Simple heuristics:
    - Start with "organisation + initiative_description"
    - Add a shorter variant using only key terms from initiative_description
    """
    org = seed.organisation.strip()
    desc = seed.initiative_description.strip()

    queries: list[str] = []
    if org and desc:
        queries.append(f"{org} {desc}")
    elif org:
        queries.append(org)
    elif desc:
        queries.append(desc)

    # Naive shorter variant: first 6 words of description
    if desc:
        parts = desc.split()
        short = " ".join(parts[:6])
        if short and short not in queries:
            queries.append(f"{org} {short}".strip())

    # Ensure at least one query
    if not queries:
        queries.append(seed.original_case_id.replace("-", " "))

    return queries


def discover_sources_for_seed(
    seed: SeedEntry,
    *,
    search_fn: SearchFn,
    max_urls: int = 10,
    per_query: int = 10,
) -> DiscoveryResult:
    """
    Run source discovery for a single SeedEntry.

    Parameters
    ----------
    seed:
        Seed entry describing the organisation and initiative.
    search_fn:
        Callable that executes a web/search query and returns a list of URLs.
        Signature: `search_fn(query: str, k: int) -> Sequence[str]`.
    max_urls:
        Maximum number of candidate URLs to return across all queries
        (excluding any legacy_urls that may be appended).
    per_query:
        Maximum number of URLs to request from the search function per query.

    Returns
    -------
    DiscoveryResult
        Contains the queries used and the final candidate URL list.
    """
    queries = build_search_queries(seed)

    seen: set[str] = set()
    candidates: list[str] = []

    for q in queries:
        if len(candidates) >= max_urls:
            break
        try:
            urls = search_fn(q, per_query) or []
        except Exception:
            urls = []

        for url in urls:
            if url not in seen:
                seen.add(url)
                candidates.append(url)
                if len(candidates) >= max_urls:
                    break

    # Add legacy_urls as extra candidates (without deduping against seen,
    # so we preserve them even if search didn't surface them)
    for url in seed.legacy_urls:
        if url not in candidates:
            candidates.append(url)

    return DiscoveryResult(seed=seed, search_queries=queries, candidate_urls=candidates)


__all__ = [
    "SearchFn",
    "DiscoveryResult",
    "build_search_queries",
    "discover_sources_for_seed",
]

