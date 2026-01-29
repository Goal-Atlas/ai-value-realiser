"""
HTTP server that serves the case library from a hardwired path (no user upload).

Case library path: env CASE_LIBRARY_PATH or default case_library/out (relative to cwd).
Endpoints:
  GET /         — viewer HTML
  GET /api/cases — list cases (summary per case)
  GET /api/cases/<case_id> — full case (value_claims, context_claims, build summary, sources)

Run from project root: python -m case_library.viewer.server
"""

from __future__ import annotations

import json
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import unquote

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
        "evidence_levels": [],
    }
    if build_path.is_file():
        try:
            build = json.loads(build_path.read_text(encoding="utf-8"))
            summary["case_id"] = build.get("case_id", case_id)
            step2 = build.get("step_2_extraction") or {}
            sources = step2.get("sources") or []
            summary["sources"] = [{"source_id": s.get("source_id"), "url": s.get("url")} for s in sources]
        except Exception:
            pass
    if claims_path.is_file():
        try:
            data = json.loads(claims_path.read_text(encoding="utf-8"))
            vc = data.get("value_claims") or []
            cc = data.get("context_claims") or []
            summary["value_claims_count"] = len(vc)
            summary["context_claims_count"] = len(cc)
            for c in vc:
                vs = (c.get("verification_status") or "").lower()
                if vs == "verified":
                    summary["verified_count"] += 1
                elif vs == "needs_review" or vs == "rejected":
                    summary["needs_review_count"] += 1
                el = c.get("evidence_level")
                if el and el not in summary["evidence_levels"]:
                    summary["evidence_levels"].append(el)
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
    return {
        "case_id": case_dir.name,
        "build": build_data,
        "value_claims": claims_data.get("value_claims", []),
        "context_claims": claims_data.get("context_claims", []),
        "sources": sources,
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
            case_id = path[len("/api/cases/"):].strip("/")
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

    def log_message(self, format: str, *args: object) -> None:
        # Quiet logs unless needed
        pass


def main() -> None:
    port = int(os.environ.get("PORT", "8765"))
    root = get_case_library_root()
    print(f"Case library root: {root.resolve()}")
    print(f"Viewer: http://127.0.0.1:{port}/")
    print(f"API:    http://127.0.0.1:{port}/api/cases")
    if not root.is_dir():
        print(f"Warning: {root} does not exist. Create it and run the pipeline with --out {root}.")
    server = HTTPServer(("127.0.0.1", port), CaseLibraryHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
