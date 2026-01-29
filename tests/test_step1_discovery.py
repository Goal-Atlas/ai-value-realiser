"""
Tests for Step 1: Source Discovery.
"""

from typing import List

from case_library.pipeline.step1_discovery import (
    DiscoveryResult,
    build_search_queries,
    discover_sources_for_seed,
)
from case_library.schemas import SeedEntry


def test_build_search_queries_uses_org_and_description() -> None:
    seed = SeedEntry(
        organisation="BMW Group",
        initiative_description="Generative design for vehicle components",
        original_case_id="bmw-generative-design",
    )
    queries = build_search_queries(seed)
    assert any("BMW Group" in q and "Generative design" in q for q in queries)


def test_discover_sources_for_seed_uses_search_fn_and_legacy_urls() -> None:
    seed = SeedEntry(
        organisation="DBS Bank",
        initiative_description="AI transformation programme creating SGD 1B value",
        original_case_id="dbs-ai-transformation",
        legacy_urls=["https://legacy.example.com/dbs-old"],
    )

    # Simple fake search function that returns deterministic URLs per query
    def fake_search_fn(query: str, k: int) -> List[str]:  # noqa: ARG001
        return [
            f"https://search.example.com/{query.replace(' ', '-').lower()}-1",
            f"https://search.example.com/{query.replace(' ', '-').lower()}-2",
        ]

    result: DiscoveryResult = discover_sources_for_seed(
        seed,
        search_fn=fake_search_fn,
        max_urls=3,
        per_query=5,
    )

    # We should have at most 3 discovered URLs plus the legacy URL (if unique)
    assert len(result.candidate_urls) <= 4

    # All discovered URLs should come from the fake search or legacy list
    assert any(url.startswith("https://search.example.com/") for url in result.candidate_urls)
    assert "https://legacy.example.com/dbs-old" in result.candidate_urls

