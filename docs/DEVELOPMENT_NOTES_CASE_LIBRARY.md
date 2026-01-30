# Development Notes – AI Case Library (v1.5)

Working notes and “gotchas” for implementing and evolving the **Case Library** component.  
Audience: future maintainers and anyone building the *next* library.

---

## 0. Current status (as of 2026-01)

- **Migration complete:** Legacy cases have been rebuilt via the pipeline and written to `case_library/out/<case_id>/`. Progress is recorded in `case_library/out/migration_progress.json`. Library has 200 cases.
- **Pipeline:** Steps 1–5 implemented. Steps 1–4 run in the legacy runner (`run_legacy_cases.py` with `--out`); Step 5 is data-only (record verdicts via API, no UI yet).
- **Output per case:** `build.json`, `claims.json`, `sources/text/*.txt`, `casefile.md` (YAML frontmatter + markdown body).
- **Viewer:** `python -m case_library.viewer.server` serves the library from the hardwired path (`case_library/out` by default). No upload; cards + filters + modal.
- **Industry sector overlay:** ISIC Rev 5 classifications for all 200 cases in `case_library/overlays/industry_sector/`. Run via `python -m case_library.run_industry_classification`; join to cases with `case_library.overlay_loader`. See §1 (Data safety) and `case_library/overlays/README.md`.
- **Next:** Human validation UI (Step 5) and/or value-claim APQC post-step if desired.

---

## 1. Data safety & backups

**Rule: before any long-running or destructive pipeline, commit or push to version control (or copy outputs elsewhere) so you can restore if something goes wrong.**

This applies to **all** created files, not just overlays:

- **Case library output** — `case_library/out/<case_id>/` (build.json, claims.json, casefile.md, sources). Full rebuilds and migrations can take a long time; a bad run or accidental overwrite can wipe hours of work.
- **Overlays** — e.g. `case_library/overlays/industry_sector/classifications.json`. Classification batches (e.g. 200 cases) can take over an hour.
- **Progress / state files** — e.g. `migration_progress.json`, or any script that writes a single file summarizing many items.

**Script-level safeguards:** Where a script writes a file that aggregates many entries (e.g. one JSON with 200 classifications), it should:

1. **Merge when running a subset** — If the user passes something like `--case-id foo`, load existing data and merge the new result(s) instead of replacing the whole file.
2. **Refuse to shrink without explicit consent** — If the run would replace N existing entries with M &lt; N, refuse unless the user passes something like `--append` (or equivalent).

The industry classification script (`run_industry_classification.py`) implements both; see `case_library/overlays/README.md` for overlay-specific notes. When adding or changing other writers (build pipeline, other overlays), apply the same pattern where it fits.

---

## 2. Environment & Tooling

- **Shell (zsh) vs pip extras**
  - In `zsh`, `pip install -e ".[dev]"` can be misinterpreted if `extendedglob` is enabled.
  - Symptom: `zsh: unknown file attribute: i`.
  - Fix: disable globbing for that command:
    ```bash
    noglob pip install -e '.[dev]'
    ```

- **Editable install & license field**
  - Build backend: `hatchling`.
  - `hatchling` does **not** accept `license = "Proprietary"` as a valid SPDX identifier.
  - Fix in `pyproject.toml`:
    ```toml
    [project]
    license = { text = "Proprietary" }
    ```
  - With this change, `pip install -e ".[dev]"` works as expected.

- **Minimal dev setup for schemas/tests**
  - When you only need to run schema tests:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate

    # Core deps for schemas/tests
    pip install pytest "pydantic>=2.0" "pyyaml>=6.0"

    pytest tests/test_schemas.py
    ```

---

## 3. Spec ↔ Code Alignment

- **Single authoritative spec**
  - Old draft: `docs/specs/AI_CASE_LIBRARY_SPECIFICATION.md` (v0.3) has been removed.
  - **Authoritative spec:** `docs/specs/AI_CASE_LIBRARY_SPECIFICATION_v1_5.md`.
  - Rule: any future spec changes must be reflected in:
    - `case_library/schemas/models.py`
    - Tests in `tests/test_schemas.py`
    - This notes file (for breaking changes / tricky bits).

- **Key schema decisions from v1.5**
  - `EvidenceType` → **`EvidenceLevel`** (`outcome` / `adoption` / `method`).
  - `metric_raw`:
    - Optional overall, but **required** for `evidence_level in {outcome, adoption}`.
    - Enforced via a Pydantic `model_validator` on `ValueClaim`.
  - `Casefile.evidence_level`:
    - Derived as **highest** evidence level among all `value_claims` (ignores verification status).
    - Stored on the case for filtering; verification status + `status` determine whether a case is usable in Strict/Standard modes.
  - `ContextClaim`:
    - `source_ids` may be empty **only** when `verification_status == "inferred"` and `inferred_from` is populated.
    - For `context_type == "functional"`, both `apqc_code` and `apqc_name` are required.
  - `Source`:
    - Now uses `type`, `origin`, `grade`, `raw_file`, `text_file`, `extraction_method`, `extraction_quality`, `is_multi_page`, `related_urls: list[str]`.

---

## 4. Testing Pattern

- **Schema-first approach**
  - Implement and stabilise:
    - Enums (ontology + attribution)
    - `MetricRaw`, `ValueClaim`, `ContextClaim`
    - `Source`, `Casefile`, `BuildLog`, `SeedEntry`
  - Then add focused tests in `tests/test_schemas.py`:
    - Enum value sets match the ontology spec.
    - `metric_raw` required for outcome/adoption claims.
    - Context `inferred` behaviour.
    - Case-level `evidence_level` derivation.

- **Pydantic v2 nuances**
  - Use `@model_validator(mode="after")` for cross-field rules.
  - Error messages come from Pydantic core; tests **should not** assert on exact text.
    - We now only assert that an exception is raised, not its message string.

---

## 5. Legacy Library Strategy

- **Location & purpose**
  - Legacy enriched cases live in `case_library/OLD_cases_enriched/`.
  - They are **reference-only**:
    - **Do use**:
      - Organisation name (`org` / `organisation` in YAML frontmatter of `4_casefile.md`).
      - Initiative / use-case description (`use_case` or `title`).
      - Legacy `1_sources.json` URLs as **hints** (optional additional candidates).
    - **Do not reuse**:
      - Legacy `2_claims.json` value/context claims.
      - Legacy ontology tags.
      - Legacy audit data.

- **Fresh source discovery (important)**
  - Step 1 (Source Discovery) must always:
    - Construct **new web search queries** from `SeedEntry.organisation` + `SeedEntry.initiative_description`.
    - Treat `legacy_urls` as **also-check** candidates, not the only list of sources.
  - Implementation rule:
    - For each seed:
      1. Run web search from organisation + initiative description to build a fresh candidate URL set.
      2. Optionally add `legacy_urls` into this candidate set (if still reachable).
      3. Select top N URLs from the **union** of new + legacy candidates for Step 2.
  - Rationale:
    - Legacy URLs may be stale or incomplete.
    - The rebuilt library should reflect the current, best available public evidence, not be limited to previously found links.

- **Seed extraction**
  - Implemented in `case_library/seed.py`.
  - API:
    ```python
    from case_library.seed import extract_seed_list

    seeds = extract_seed_list(Path("case_library/OLD_cases_enriched"))
    ```
  - Each `SeedEntry` includes:
    - `organisation`
    - `initiative_description`
    - `original_case_id` (legacy folder name)
    - `legacy_urls` (from `1_sources.json`)
    - `research_priority` (default `"medium"`)

---

## 6. Pipeline Implementation Order

- **Phase 1 – Schemas & storage**
  - Done:
    - v1.5 schemas (`models.py`) + tests (`test_schemas.py`).
    - Seed extraction (`seed.py`).
  - Next:
    - Create `case_library/cases/` structure as needed by Step 2.

- **Phase 2 – Pipeline (all implemented)**
  1. **Step 2 – Content Extraction** — `step2_extraction.py`; HTTP fetch, trafilatura/pypdf, truncation, multi-page stub.
  2. **Step 1 – Source Discovery** — `step1_discovery.py`; search queries from seed; default `search_fn` returns no extra URLs (relies on `legacy_urls`).
  3. **Step 3 – Claim Extraction** — `step3_claims.py`; LLM (Anthropic) extracts value + context claims; normalisation, retries, logging.
  4. **Step 4 – Verification** — `step4_verification.py`; quote matching against captured source text (exact + regex); no LLM; updates verification_status.
  5. **Step 5 – Human Validation** — `step5_validation.py`; data recording only (`record_human_validation`, `run_step5_human_validation_for_case`). No UI; callers supply verdicts dict.
  6. **Persistence** — `pipeline/persistence.py`: write/read `build.json`, `sources/text/*.txt`, `claims.json`. Runner: `--out DIR` writes under `DIR/<case_id>/`.
  7. **casefile.md** — `pipeline/casefile_export.write_casefile_md()`: YAML frontmatter + markdown body per case; written automatically with `--out`.
  8. **Migration progress** — `pipeline/migration_progress.py`: `<out>/migration_progress.json`; “Migration: X/Y complete, Z to process”; `--resume` skips done cases.
  9. **Browse viewer** — `case_library/viewer/`: server from hardwired path (`CASE_LIBRARY_PATH` or `case_library/out`); cards + filters + modal; `python -m case_library.viewer.server`.
  10. **APQC** — Context claims (functional): `apqc_code` / `apqc_name` in schema and Step 3 prompt. Value-claim APQC: not in spec; optional post-step if needed.

---

## 7. General Lessons

- Always update **spec, schemas, and tests together**.
- Keep a **single** spec version in `docs/specs/`, and delete or clearly archive older drafts.
- Treat legacy data strictly as **input hints**, not as truth.
- Prefer small, focused tests around each invariant rather than end-to-end tests early on.

