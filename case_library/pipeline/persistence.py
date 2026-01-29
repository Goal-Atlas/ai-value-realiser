"""
Persistence for pipeline outputs (build.json, sources/text/*.txt, claims).

Implements the case directory layout from §5.1 of the AI Case Library spec:
  case_id/
    build.json
    sources/
      text/
        S1.txt, S2.txt, ...
    claims.json   # value_claims + context_claims for round-trip (Step 5)

This module does not create casefile.md; that can be generated from
BuildLog + claims + sources in a separate export step.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, List, Tuple

from case_library.schemas import (
    BuildLog,
    ContextClaim,
    SourceExtraction,
    ValueClaim,
)

BUILD_JSON = "build.json"
CLAIMS_JSON = "claims.json"
SOURCES_TEXT_DIR = "sources/text"


def write_build_log(case_dir: Path, build_log: BuildLog) -> None:
    """Write BuildLog to case_dir/build.json."""
    case_dir = Path(case_dir)
    case_dir.mkdir(parents=True, exist_ok=True)
    path = case_dir / BUILD_JSON
    data = build_log.model_dump(mode="json")
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def read_build_log(case_dir: Path) -> BuildLog | None:
    """Read BuildLog from case_dir/build.json. Returns None if file missing."""
    path = Path(case_dir) / BUILD_JSON
    if not path.is_file():
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    return BuildLog.model_validate(data)


def write_sources_text(case_dir: Path, sources: Iterable[SourceExtraction]) -> None:
    """Write extracted text for each source to case_dir/sources/text/{source_id}.txt."""
    case_dir = Path(case_dir)
    text_dir = case_dir / SOURCES_TEXT_DIR
    text_dir.mkdir(parents=True, exist_ok=True)
    for src in sources:
        if src.content is None:
            continue
        # Safe filename: source_id is typically S1, S2, ...
        name = _safe_source_filename(src.source_id)
        (text_dir / f"{name}.txt").write_text(src.content, encoding="utf-8")


def _safe_source_filename(source_id: str) -> str:
    """Return a safe filename stem from source_id (e.g. S1 -> S1)."""
    return "".join(c for c in source_id if c.isalnum() or c in "-_") or "unknown"


def read_source_text(case_dir: Path, source_id: str) -> str | None:
    """Read extracted text for one source. Returns None if file missing."""
    path = Path(case_dir) / SOURCES_TEXT_DIR / f"{_safe_source_filename(source_id)}.txt"
    if not path.is_file():
        return None
    return path.read_text(encoding="utf-8")


def list_source_ids_in_dir(case_dir: Path) -> List[str]:
    """List source IDs present in sources/text (by stripping .txt)."""
    text_dir = Path(case_dir) / SOURCES_TEXT_DIR
    if not text_dir.is_dir():
        return []
    return [p.stem for p in text_dir.glob("*.txt")]


def write_claims(
    case_dir: Path,
    value_claims: List[ValueClaim],
    context_claims: List[ContextClaim],
) -> None:
    """Write value_claims and context_claims to case_dir/claims.json."""
    case_dir = Path(case_dir)
    case_dir.mkdir(parents=True, exist_ok=True)
    path = case_dir / CLAIMS_JSON
    data = {
        "value_claims": [c.model_dump(mode="json") for c in value_claims],
        "context_claims": [c.model_dump(mode="json") for c in context_claims],
    }
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def read_claims(
    case_dir: Path,
) -> Tuple[List[ValueClaim], List[ContextClaim]]:
    """Read value_claims and context_claims from case_dir/claims.json."""
    path = Path(case_dir) / CLAIMS_JSON
    if not path.is_file():
        return [], []
    data = json.loads(path.read_text(encoding="utf-8"))
    value_claims = [ValueClaim.model_validate(c) for c in data.get("value_claims", [])]
    context_claims = [
        ContextClaim.model_validate(c) for c in data.get("context_claims", [])
    ]
    return value_claims, context_claims
