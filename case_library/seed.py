"""
Seed list extraction from legacy enriched cases.

The legacy library in `OLD_cases_enriched/` is **reference-only**. We use it
to derive seed entries (organisation + initiative description + legacy URLs)
for the new provenance pipeline, but do not reuse any legacy claims, audits,
or ontology tags.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, List

import yaml

from case_library.schemas import SeedEntry


def _load_yaml_frontmatter(md_path: Path) -> dict:
    """
    Load YAML frontmatter from a legacy casefile markdown.

    Legacy `4_casefile.md` files start with a `---` YAML header. We read until
    the closing `---` and parse that as YAML. If anything goes wrong, we
    return an empty dict and let the caller fall back to folder-based defaults.
    """
    text = md_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}

    # Split on the second '---'
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}

    frontmatter = parts[1]
    try:
        data = yaml.safe_load(frontmatter) or {}
        if not isinstance(data, dict):
            return {}
        return data
    except yaml.YAMLError:
        return {}


def _load_legacy_sources(json_path: Path) -> list[str]:
    """
    Load legacy source URLs from `1_sources.json`.

    The legacy schema is:
    {
      "case_id": "...",
      "sources": [
        { "source_id": "S1", "title": "...", "url": "...", "doc_type": "..." },
        ...
      ]
    }
    """
    import json

    data = json.loads(json_path.read_text(encoding="utf-8"))
    sources = data.get("sources", []) or []
    urls: list[str] = []
    for src in sources:
        url = src.get("url")
        if isinstance(url, str) and url:
            urls.append(url)
    return urls


def extract_seed_list(legacy_root: Path | str) -> List[SeedEntry]:
    """
    Extract a seed list from the legacy enriched cases.

    Parameters
    ----------
    legacy_root:
        Path to the legacy cases root, typically
        `case_library/OLD_cases_enriched`.

    Returns
    -------
    list[SeedEntry]
        One entry per legacy case folder with:
        - organisation
        - initiative_description
        - original_case_id
        - legacy_urls
        - research_priority (default "medium")
    """
    root = Path(legacy_root)
    if not root.exists():
        return []

    entries: list[SeedEntry] = []

    for case_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        original_case_id = case_dir.name
        sources_path = case_dir / "1_sources.json"
        casefile_path = case_dir / "4_casefile.md"

        if not sources_path.exists() or not casefile_path.exists():
            # Skip incomplete legacy cases
            continue

        frontmatter = _load_yaml_frontmatter(casefile_path)
        organisation = str(frontmatter.get("org") or frontmatter.get("organisation") or "").strip()
        initiative_description = str(
            frontmatter.get("use_case") or frontmatter.get("title") or ""
        ).strip()

        # Fallbacks if frontmatter is missing or incomplete
        if not organisation:
            # Use a simple transformation of the folder name as last resort
            organisation = original_case_id.split("-")[0].replace("_", " ").title()
        if not initiative_description:
            initiative_description = original_case_id.replace("-", " ")

        legacy_urls = _load_legacy_sources(sources_path)

        entry = SeedEntry(
            organisation=organisation,
            initiative_description=initiative_description,
            original_case_id=original_case_id,
            legacy_urls=legacy_urls,
        )
        entries.append(entry)

    return entries


def iter_seed_entries(legacy_root: Path | str) -> Iterable[SeedEntry]:
    """
    Convenience generator version of `extract_seed_list`.

    Useful when streaming or progressively processing seeds.
    """
    for entry in extract_seed_list(legacy_root):
        yield entry

