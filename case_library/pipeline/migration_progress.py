"""
Migration progress tracking: persist and report how much of the rebuild is complete.

Progress file: <out_root>/migration_progress.json
  { "case_id": { "status": "done"|"failed"|"skipped", "completed_at": "ISO", "error": "..." }, ... }

Supports --resume: skip cases already marked "done".
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PROGRESS_FILENAME = "migration_progress.json"


def progress_path(out_root: Path) -> Path:
    return Path(out_root) / PROGRESS_FILENAME


def load_progress(out_root: Path) -> dict[str, dict[str, Any]]:
    path = progress_path(out_root)
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def save_progress(out_root: Path, progress: dict[str, dict[str, Any]]) -> None:
    path = progress_path(out_root)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(progress, indent=2), encoding="utf-8")


def mark_done(out_root: Path, case_id: str) -> None:
    progress = load_progress(out_root)
    progress[case_id] = {
        "status": "done",
        "completed_at": datetime.now(timezone.utc).isoformat(),
    }
    save_progress(out_root, progress)


def mark_failed(out_root: Path, case_id: str, error: str) -> None:
    progress = load_progress(out_root)
    progress[case_id] = {
        "status": "failed",
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "error": error[:500],
    }
    save_progress(out_root, progress)


def migration_report(
    out_root: Path,
    total_seeds: int,
    seed_ids: list[str],
) -> tuple[int, int, list[str]]:
    """
    Return (done_count, to_process_count, list of case_ids still to process).

    to_process = seed_ids not yet in progress with status "done".
    """
    progress = load_progress(out_root)
    done = sum(1 for cid in seed_ids if progress.get(cid, {}).get("status") == "done")
    to_process = [cid for cid in seed_ids if progress.get(cid, {}).get("status") != "done"]
    return done, len(to_process), to_process
