"""
HTTP server that serves the case library from a hardwired path (no user upload).

Case library path: env CASE_LIBRARY_PATH or default case_library/out (relative to cwd).
Endpoints:
  GET  /                              — viewer HTML
  GET  /api/cases                     — list cases (summary per case)
  GET  /api/cases/<case_id>           — full case (value_claims, context_claims, build, sources)
  GET  /api/cases/<case_id>/sources/<source_id> — extracted source text (plain text)
  POST /api/cases/<case_id>/validate   — record human validation verdicts

Run from project root: python -m case_library.viewer.server
"""

from __future__ import annotations

import json
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import unquote

from case_library.pipeline.persistence import read_source_text
from case_library.pipeline.step5_validation import record_human_validation
from case_library.schemas import (
    BuildLog,
    ContextClaim,
    ValidationTier,
    ValueClaim,
)

# Resolve case library root: env or default relative to cwd
CASE_LIBRARY_PATH = os.environ.get("CASE_LIBRARY_PATH", "case_library/out")
# Directory containing this file; static files (viewer) live next to server.py
VIEWER_DIR = Path(__file__).resolve().parent / "static"


def get_case_library_root() -> Path:
    """Return the case library root directory (absolute)."""
    p = Path(CASE_LIBRARY_PATH)
    if not p.is_absolute():
        p = Path.cwd() / p
    return p


def list_case_dirs(root: Path) -> list[Path]:
    """Return subdirs of root that contain build.json or claims.json."""
    if not root.is_dir():
        return []
    out = []
    for child in root.iterdir():
        if child.is_dir() and not child.name.startswith("."):
            if (child / "build.json").is_file() or (child / "claims.json").is_file():
                out.append(child)
    return sorted(out, key=lambda p: p.name)


def load_case_summary(case_dir: Path) -> dict | None:
    """Load summary for one case (for list view). Returns None on error."""
    build_path = case_dir / "build.json"
    claims_path = case_dir / "claims.json"
    case_id = case_dir.name
    summary: dict = {
        "case_id": case_id,
        "title": _humanize_case_id(case_id),
        "value_claims_count": 0,
        "context_claims_count": 0,
        "verified_count": 0,
        "needs_review_count": 0,
        "human_validated_count": 0,
        "evidence_levels": [],
    }
    if build_path.is_file():
        try:
            build = json.loads(build_path.read_text(encoding="utf-8"))
            summary["case_id"] = build.get("case_id", case_id)
            step2 = build.get("step_2_extraction") or {}
            sources = step2.get("sources") or []
            summary["sources"] = [{"source_id": s.get("source_id"), "url": s.get("url")} for s in sources]
            step5 = build.get("step_5_human_validation")
            if step5:
                summary["human_validated"] = True
                summary["human_validated_count"] = step5.get("claims_reviewed", 0)
        except Exception:
            pass
    if claims_path.is_file():
        try:
            data = json.loads(claims_path.read_text(encoding="utf-8"))
            vc = data.get("value_claims") or []
            cc = data.get("context_claims") or []
            summary["value_claims_count"] = len(vc)
            summary["context_claims_count"] = len(cc)
            human_validated = 0
            for c in vc:
                vs = (c.get("verification_status") or "").lower()
                if vs == "verified":
                    summary["verified_count"] += 1
                elif vs == "needs_review" or vs == "rejected":
                    summary["needs_review_count"] += 1
                el = c.get("evidence_level")
                if el and el not in summary["evidence_levels"]:
                    summary["evidence_levels"].append(el)
                hv = c.get("human_validation") or {}
                if hv.get("reviewed"):
                    human_validated += 1
            summary["human_validated_count"] = max(summary.get("human_validated_count", 0), human_validated)
            if vc and summary.get("title") == _humanize_case_id(case_id):
                summary["title"] = (vc[0].get("claim_title") or summary["title"])[:80]
        except Exception:
            pass
    return summary


def load_case_detail(case_dir: Path) -> dict | None:
    """Load full case for detail view. Returns None on error."""
    build_path = case_dir / "build.json"
    claims_path = case_dir / "claims.json"
    if not claims_path.is_file():
        return None
    try:
        claims_data = json.loads(claims_path.read_text(encoding="utf-8"))
    except Exception:
        return None
    build_data = None
    if build_path.is_file():
        try:
            build_data = json.loads(build_path.read_text(encoding="utf-8"))
        except Exception:
            pass
    sources = []
    if build_data:
        step2 = build_data.get("step_2_extraction") or {}
        for s in step2.get("sources") or []:
            sources.append({"source_id": s.get("source_id"), "url": s.get("url")})

    value_claims_raw = claims_data.get("value_claims", [])
    step4 = (build_data or {}).get("step_4_verification") or {}
    attempts = step4.get("verification_attempts") or []
    # Build map: claim_id -> first source_id that matched (for enriching quote_source_id)
    matched_source_by_claim: dict[str, str] = {}
    for att in attempts:
        if att.get("result") != "matched":
            continue
        cid = att.get("claim_id")
        if cid and cid not in matched_source_by_claim:
            matched_source_by_claim[cid] = att.get("source_id") or ""
    value_claims = []
    for vc in value_claims_raw:
        vc = dict(vc)
        if not vc.get("quote_source_id") and vc.get("id") in matched_source_by_claim:
            vc["quote_source_id"] = matched_source_by_claim[vc["id"]]
        value_claims.append(vc)

    return {
        "case_id": case_dir.name,
        "build": build_data,
        "value_claims": value_claims,
        "context_claims": claims_data.get("context_claims", []),
        "sources": sources,
    }


def save_validation(case_dir: Path, validation_data: dict) -> dict:
    """
    Apply human validation to a case and persist results.

    validation_data: verdicts (claim_id -> valid|invalid|unclear), reviewer_id, tier, time_taken_minutes.
    Returns {"success": True, ...} or {"error": "message"}.
    """
    build_path = case_dir / "build.json"
    claims_path = case_dir / "claims.json"
    if not claims_path.is_file():
        return {"error": "claims.json not found"}
    if not build_path.is_file():
        return {"error": "build.json not found"}
    try:
        claims_data = json.loads(claims_path.read_text(encoding="utf-8"))
        build_data = json.loads(build_path.read_text(encoding="utf-8"))
    except Exception as e:
        return {"error": f"Failed to read case files: {e}"}
    try:
        value_claims = [ValueClaim.model_validate(vc) for vc in claims_data.get("value_claims", [])]
        context_claims = [ContextClaim.model_validate(cc) for cc in claims_data.get("context_claims", [])]
        build_log = BuildLog.model_validate(build_data)
    except Exception as e:
        return {"error": f"Failed to parse case data: {e}"}
    verdicts = validation_data.get("verdicts", {})
    reviewer_id = validation_data.get("reviewer_id")
    tier_str = validation_data.get("tier", "tier_1")
    time_taken = validation_data.get("time_taken_minutes")
    tier_map = {
        "tier_1": ValidationTier.TIER_1,
        "tier_2_blind": ValidationTier.TIER_2_BLIND,
        "tier_3_calibration": ValidationTier.TIER_3_CALIBRATION,
    }
    tier = tier_map.get(tier_str, ValidationTier.TIER_1)
    try:
        updated_log, updated_vc, updated_cc = record_human_validation(
            build_log=build_log,
            value_claims=value_claims,
            context_claims=context_claims,
            tier=tier,
            reviewer_id=reviewer_id,
            verdicts=verdicts,
            time_taken_minutes=time_taken,
        )
    except Exception as e:
        return {"error": f"Validation failed: {e}"}
    try:
        build_path.write_text(
            json.dumps(updated_log.model_dump(mode="json"), indent=2, default=str),
            encoding="utf-8",
        )
        updated_claims = {
            "value_claims": [vc.model_dump(mode="json") for vc in updated_vc],
            "context_claims": [cc.model_dump(mode="json") for cc in updated_cc],
        }
        claims_path.write_text(
            json.dumps(updated_claims, indent=2, default=str),
            encoding="utf-8",
        )
    except Exception as e:
        return {"error": f"Failed to save: {e}"}
    return {
        "success": True,
        "claims_validated": len(verdicts),
        "reviewer_id": reviewer_id,
    }


def _humanize_case_id(case_id: str) -> str:
    """Turn case-id-slug into a readable title."""
    return case_id.replace("-", " ").replace("_", " ").title()


class CaseLibraryHandler(SimpleHTTPRequestHandler):
    """Serves viewer static files and /api/cases JSON."""

    def __init__(self, *args, **kwargs):  # type: ignore[no-untyped-def]
        super().__init__(*args, directory=str(VIEWER_DIR), **kwargs)

    def do_GET(self) -> None:
        path = unquote(self.path).split("?")[0]
        if path == "/" or path == "":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            index = VIEWER_DIR / "index.html"
            if index.is_file():
                self.wfile.write(index.read_bytes())
            else:
                self.wfile.write(b"<h1>Viewer not found</h1><p>Place index.html in case_library/viewer/static/</p>")
            return
        if path == "/api/cases":
            self._serve_cases_list()
            return
        if path.startswith("/api/cases/") and path != "/api/cases/":
            remaining = path[len("/api/cases/"):].strip("/")
            if "/sources/" in remaining:
                case_id, _, source_id = remaining.partition("/sources/")
                case_id = case_id.strip("/")
                source_id = source_id.strip("/")
                if case_id and source_id:
                    self._serve_source_text(case_id, source_id)
                    return
            case_id = remaining.split("/")[0] if remaining else ""
            if case_id and "/sources/" not in path:
                self._serve_case_detail(case_id)
                return
        # Fallback: try file under static (e.g. /index.html)
        if path.startswith("/"):
            path = path[1:]
        super().do_GET()

    def _serve_cases_list(self) -> None:
        root = get_case_library_root()
        case_dirs = list_case_dirs(root)
        payload = []
        for case_dir in case_dirs:
            s = load_case_summary(case_dir)
            if s:
                payload.append(s)
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(payload, indent=2).encode("utf-8"))

    def _serve_case_detail(self, case_id: str) -> None:
        root = get_case_library_root()
        case_dir = root / case_id
        if not case_dir.is_dir():
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "case not found"}).encode("utf-8"))
            return
        detail = load_case_detail(case_dir)
        if detail is None:
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "case data unreadable"}).encode("utf-8"))
            return
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(detail, indent=2).encode("utf-8"))

    def _serve_source_text(self, case_id: str, source_id: str) -> None:
        """Serve extracted source text as plain text (GET /api/cases/<case_id>/sources/<source_id>)."""
        root = get_case_library_root()
        case_dir = root / case_id
        if not case_dir.is_dir():
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Case not found")
            return
        text = read_source_text(case_dir, source_id)
        if text is None:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Source text not found")
            return
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(text.encode("utf-8"))

    def do_POST(self) -> None:
        path = unquote(self.path).split("?")[0]
        if path.startswith("/api/cases/") and path.endswith("/validate"):
            case_id = path[len("/api/cases/"): -len("/validate")].strip("/")
            self._handle_validation(case_id)
            return
        self.send_response(404)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"error": "not found"}).encode("utf-8"))

    def do_OPTIONS(self) -> None:
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def _handle_validation(self, case_id: str) -> None:
        root = get_case_library_root()
        case_dir = root / case_id
        if not case_dir.is_dir():
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "case not found"}).encode("utf-8"))
            return
        try:
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)
            validation_data = json.loads(body.decode("utf-8"))
        except Exception as e:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
            return
        result = save_validation(case_dir, validation_data)
        self.send_response(200 if "success" in result else 500)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(result).encode("utf-8"))

    def log_message(self, format: str, *args: object) -> None:
        # Quiet logs unless needed
        pass


def main() -> None:
    port = int(os.environ.get("PORT", "8765"))
    root = get_case_library_root()
    print(f"Case library root: {root.resolve()}")
    print(f"Viewer: http://127.0.0.1:{port}/")
    print(f"API:    http://127.0.0.1:{port}/api/cases")
    print(f"Source text: GET /api/cases/<id>/sources/<source_id>")
    print(f"Validate:    POST /api/cases/<id>/validate")
    if not root.is_dir():
        print(f"Warning: {root} does not exist. Create it and run the pipeline with --out {root}.")
    server = HTTPServer(("127.0.0.1", port), CaseLibraryHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
