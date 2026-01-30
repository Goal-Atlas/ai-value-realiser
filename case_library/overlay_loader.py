"""
Load and join classification overlays to the core case library.

Overlays are stored under overlays/<name>/ with metadata.json and a main data file.
See case_library/overlays/README.md and Classifier_Over-layer/CLASSIFICATION_OVERLAY_ARCHITECTURE.md.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

# Reserved filenames: not treated as main overlay data
OVERLAY_RESERVED_JSON = {"metadata.json", "taxonomy.json"}


def list_overlays(overlays_root: Path) -> list[str]:
    """
    Return overlay names (subdirs that contain metadata.json).
    """
    root = Path(overlays_root)
    if not root.is_dir():
        return []
    return sorted(
        d.name for d in root.iterdir()
        if d.is_dir() and not d.name.startswith(".") and (d / "metadata.json").is_file()
    )


def load_overlay_metadata(overlays_root: Path, overlay_name: str) -> dict[str, Any] | None:
    """
    Load metadata.json for an overlay. Returns None if missing or invalid.
    """
    path = Path(overlays_root) / overlay_name / "metadata.json"
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def _main_data_file(overlay_dir: Path) -> Path | None:
    """Return path to the main overlay data file (first JSON that is not reserved)."""
    for f in sorted(overlay_dir.glob("*.json")):
        if f.name not in OVERLAY_RESERVED_JSON:
            return f
    return None


def load_overlay_data(overlays_root: Path, overlay_name: str) -> dict[str, Any] | None:
    """
    Load the main overlay data file (e.g. classifications.json, value_claim_mappings.json).
    Returns None if overlay dir or main data file is missing.
    """
    overlay_dir = Path(overlays_root) / overlay_name
    if not overlay_dir.is_dir():
        return None
    path = _main_data_file(overlay_dir)
    if path is None:
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def load_overlay_taxonomy(overlays_root: Path, overlay_name: str) -> dict[str, Any] | None:
    """Load taxonomy.json for an overlay if present."""
    path = Path(overlays_root) / overlay_name / "taxonomy.json"
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def join_overlay_to_cases(
    cases: dict[str, Any],
    overlay_data: dict[str, Any],
    *,
    data_key: str,
    case_key: str = "case_id",
    overlay_attr: str | None = None,
    multi: bool = False,
) -> dict[str, Any]:
    """
    Enrich a cases dict (case_id -> case_data) with overlay data.

    Args:
        cases: Dict mapping case_id to case data (e.g. from load_cases).
        overlay_data: Loaded overlay data dict (e.g. from load_overlay_data).
        data_key: Key in overlay_data that holds the list of items (e.g. "classifications", "mappings", "tags").
        case_key: Key in each item that holds the case_id (default "case_id").
        overlay_attr: Key to set on each case (default: last segment of data_key, e.g. "classifications" -> "classifications").
        multi: If True, attach list of all items per case; if False, attach single item (last wins if duplicates).

    Returns:
        New dict of case_id -> { **case_data, [overlay_attr]: item(s) }. Original cases is not mutated.
    """
    items = overlay_data.get(data_key)
    if not isinstance(items, list):
        return dict(cases)

    attr = overlay_attr or data_key
    if multi:
        lookup: dict[str, list] = {}
        for item in items:
            if not isinstance(item, dict):
                continue
            cid = item.get(case_key)
            if cid is not None:
                lookup.setdefault(cid, []).append(item)
        return {
            cid: {**data, attr: lookup.get(cid, [])}
            for cid, data in cases.items()
        }
    else:
        lookup = {item[case_key]: item for item in items if isinstance(item, dict) and item.get(case_key) is not None}
        return {
            cid: {**data, attr: lookup.get(cid)}
            for cid, data in cases.items()
        }


def get_overlay_for_case(
    overlays_root: Path,
    overlay_name: str,
    case_id: str,
    *,
    data_key: str | None = None,
    case_key: str = "case_id",
) -> Any:
    """
    Return overlay payload for a single case (e.g. for API /api/overlays/<name>/<case_id>).

    If data_key is None, the main data file is scanned for a key that contains a list
    of objects with case_key; the first such key is used (e.g. "classifications", "mappings", "tags").
    Returns single item if one match, list if multiple (e.g. APQC mappings per case).
    """
    data = load_overlay_data(overlays_root, overlay_name)
    if not data:
        return None

    if data_key is None:
        for key in ("classifications", "mappings", "tags", "value_claim_mappings"):
            if key in data and isinstance(data[key], list) and data[key]:
                data_key = key
                break
        if data_key is None:
            return None

    items = data.get(data_key, [])
    matches = [item for item in items if isinstance(item, dict) and item.get(case_key) == case_id]
    if not matches:
        return None
    if len(matches) == 1:
        return matches[0]
    return matches


__all__ = [
    "list_overlays",
    "load_overlay_metadata",
    "load_overlay_data",
    "load_overlay_taxonomy",
    "join_overlay_to_cases",
    "get_overlay_for_case",
]
