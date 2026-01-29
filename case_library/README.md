# Case Library (v1.5)

This package implements the **AI Case Library** component of the AI Value Realiser.

## Structure

- `schemas/` — Pydantic models for cases, claims, sources, build logs, and seed entries (v1.5 spec).
- `pipeline/` — Five-step provenance pipeline (discovery → extraction → claims → verification → human validation), persistence, casefile export, migration progress.
- `viewer/` — Browse UI: HTTP server that serves the library from a hardwired path (no upload).
- `ontology/` — Ontology v1.0 (`ontology_v1.0.yaml`) for mechanism/outcome/cognitive_depth.
- `OLD_cases_enriched/` — **Legacy reference only.** Seeds (organisation, initiative, legacy URLs) for the rebuild; no legacy claims or audits reused.
- `out/` — **Rebuilt library** (default path). After migration: one directory per case with `build.json`, `claims.json`, `sources/text/*.txt`, `casefile.md`. Progress: `out/migration_progress.json`.

## Running the pipeline

**Migrate legacy cases (202 seeds):**
```bash
# From repo root
python -m case_library.run_legacy_cases --out case_library/out --limit 9999
# Resume after a stop:
python -m case_library.run_legacy_cases --out case_library/out --resume
```

**Browse the rebuilt library:**
```bash
python -m case_library.viewer.server   # then open http://127.0.0.1:8765/
```
Library path: env `CASE_LIBRARY_PATH` or default `case_library/out`.

## Specifications & Briefing

Authoritative documents live under `docs/specs/` at the repo root:

- `AI_CASE_LIBRARY_SPECIFICATION_v1_5.md` — full v1.5 specification.
- `CURSOR_STARTUP_BRIEFING.md` — implementation briefing for Cursor/AI agents.

The v1.5 specification is the **source of truth** for schemas and pipeline behaviour; `schemas/models.py` is aligned with it.

