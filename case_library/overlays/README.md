# Classification Overlays

Overlay datasets join to the core case library by `case_id` (and optionally `claim_id`). They hold **interpretive classifications** (industry sector, APQC process, client-specific tags) separate from verified case facts.

See `Classifier_Over-layer/CLASSIFICATION_OVERLAY_ARCHITECTURE.md` for full design.

## Directory layout

```
overlays/
  <overlay_name>/           # e.g. industry_sector, apqc_process, client_xyz
    metadata.json           # Required: overlay_id, display_name, version, coverage, etc.
    <data>.json             # Main data file (classifications.json, value_claim_mappings.json, etc.)
    taxonomy.json           # Optional: taxonomy definition for this overlay
```

## Metadata schema

Each overlay must have `metadata.json` with at least:

| Field           | Type   | Description                          |
|----------------|--------|--------------------------------------|
| overlay_id     | string | Unique id (e.g. `industry_sector`)   |
| display_name   | string | Human-readable name                  |
| description    | string | What this overlay contains           |
| version        | string | Semantic version (e.g. `1.0`)       |
| created_date   | string | ISO 8601                             |
| last_updated   | string | ISO 8601                             |
| maintainer     | string | Contact (e.g. email)                 |
| coverage       | object | Optional: total_cases, classified_cases, coverage_percent |

Main data file: any `.json` in the overlay directory except `metadata.json` and `taxonomy.json`. Conventions:

- **Industry sector:** `classifications.json` — list of `{ case_id, primary_sector, secondary_sectors, ... }`
- **APQC process:** `value_claim_mappings.json` — list of `{ case_id, claim_id, apqc_processes, ... }`
- **Client-specific:** `relevance_tags.json` (or similar) — list of `{ case_id, relevance_score, ... }`

## Data safety

- **Back up before long runs.** For any long-running or destructive pipeline (case builds, migrations, overlays), commit or push to version control (or copy the output files) so you can restore if something goes wrong. See **docs/DEVELOPMENT_NOTES_CASE_LIBRARY.md** §1 (Data safety & backups) for the project-wide rule.
- **Overlays:** Classification jobs (e.g. industry sector over 200 cases) can take over an hour. Copy `overlays/<name>/classifications.json` or commit before re-running.
- **Single-case runs merge by default.** When you use `--case-id` with `run_industry_classification`, the script always merges with existing `classifications.json` if it exists, so you never overwrite the full set with one entry. A safety check also refuses to replace many existing entries with fewer unless you pass `--append`.

## Usage

```python
from pathlib import Path
from case_library.overlay_loader import (
    list_overlays,
    load_overlay_metadata,
    load_overlay_data,
    join_overlay_to_cases,
)

overlays_root = Path("case_library/overlays")
names = list_overlays(overlays_root)
meta = load_overlay_metadata(overlays_root, "industry_sector")
data = load_overlay_data(overlays_root, "industry_sector")
# Enrich cases dict (case_id -> case_data) with overlay by case_id
enriched = join_overlay_to_cases(cases, data, case_key="case_id", data_key="classifications")
```
