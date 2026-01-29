# AI Case Library Viewer (v1.5)

Browse the case library from a **hardwired path** — no folder upload. Cards + filters + modal detail, aligned with the v1.5 spec (value claims, context claims, verification status, evidence level).

## Setup

1. **Case library path** (hardwired):
   - Default: `case_library/out` (relative to the directory you run the server from). This is where the migration writes; after the full migration, 202 cases are available.
   - Override: set env `CASE_LIBRARY_PATH` to an absolute or relative path.

2. **Populate the library** (if starting fresh):
   ```bash
   python -m case_library.run_legacy_cases --out case_library/out --limit 2
   ```

## Run

From the **project root** (ai-value-realiser):

```bash
python -m case_library.viewer.server
```

- Viewer: http://127.0.0.1:8765/
- API: http://127.0.0.1:8765/api/cases

Port: env `PORT` (default `8765`).

## Behaviour

- **Load:** On load, the app fetches `/api/cases`; no user-selected folder.
- **Cards:** Each case is a card (title, case_id, value-claim counts, verified / needs-review badges, evidence levels). Click → modal.
- **Filters:** Search (title / case ID), verification (all / has verified / has needs review), evidence level (all / outcome / adoption / method).
- **Modal:** Value claims (main viewer) with verification_status, evidence_level, quote, human_validation; context claims (collapsible); sources.
