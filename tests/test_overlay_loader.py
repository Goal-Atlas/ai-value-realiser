"""Tests for case_library.overlay_loader."""

from __future__ import annotations

from pathlib import Path

import pytest

from case_library.overlay_loader import (
    get_overlay_for_case,
    join_overlay_to_cases,
    list_overlays,
    load_overlay_data,
    load_overlay_metadata,
)


def test_list_overlays_finds_industry_sector(tmp_path: Path) -> None:
    (tmp_path / "industry_sector").mkdir()
    (tmp_path / "industry_sector" / "metadata.json").write_text("{}")
    (tmp_path / "other").mkdir()
    # No metadata in other -> not listed
    names = list_overlays(tmp_path)
    assert "industry_sector" in names
    assert "other" not in names


def test_load_overlay_metadata(tmp_path: Path) -> None:
    (tmp_path / "industry_sector").mkdir()
    (tmp_path / "industry_sector" / "metadata.json").write_text(
        '{"overlay_id": "industry_sector", "display_name": "Industry", "version": "1.0"}'
    )
    meta = load_overlay_metadata(tmp_path, "industry_sector")
    assert meta is not None
    assert meta["overlay_id"] == "industry_sector"
    assert meta["display_name"] == "Industry"


def test_load_overlay_metadata_missing(tmp_path: Path) -> None:
    assert load_overlay_metadata(tmp_path, "nonexistent") is None


def test_load_overlay_data(tmp_path: Path) -> None:
    (tmp_path / "industry_sector").mkdir()
    (tmp_path / "industry_sector" / "metadata.json").write_text("{}")
    (tmp_path / "industry_sector" / "classifications.json").write_text(
        '{"version": "1.0", "classifications": [{"case_id": "c1", "primary_sector": {"code": "52"}}]}'
    )
    data = load_overlay_data(tmp_path, "industry_sector")
    assert data is not None
    assert data["version"] == "1.0"
    assert len(data["classifications"]) == 1
    assert data["classifications"][0]["case_id"] == "c1"


def test_join_overlay_to_cases() -> None:
    cases = {"c1": {"title": "Case 1"}, "c2": {"title": "Case 2"}}
    overlay_data = {
        "classifications": [
            {"case_id": "c1", "primary_sector": {"code": "52", "name": "Banking"}},
        ]
    }
    enriched = join_overlay_to_cases(cases, overlay_data, data_key="classifications")
    assert enriched["c1"]["classifications"]["primary_sector"]["code"] == "52"
    assert enriched["c2"].get("classifications") is None


def test_join_overlay_to_cases_multi() -> None:
    cases = {"c1": {}}
    overlay_data = {
        "mappings": [
            {"case_id": "c1", "claim_id": "VC-001", "apqc_processes": []},
            {"case_id": "c1", "claim_id": "VC-002", "apqc_processes": []},
        ]
    }
    enriched = join_overlay_to_cases(
        cases, overlay_data, data_key="mappings", overlay_attr="apqc", multi=True
    )
    assert len(enriched["c1"]["apqc"]) == 2


def test_get_overlay_for_case(tmp_path: Path) -> None:
    (tmp_path / "industry_sector").mkdir()
    (tmp_path / "industry_sector" / "metadata.json").write_text("{}")
    (tmp_path / "industry_sector" / "classifications.json").write_text(
        '{"classifications": [{"case_id": "dbs-bank", "primary_sector": {"code": "5221"}}]}'
    )
    out = get_overlay_for_case(tmp_path, "industry_sector", "dbs-bank")
    assert out is not None
    assert out["primary_sector"]["code"] == "5221"
    assert get_overlay_for_case(tmp_path, "industry_sector", "other-case") is None
