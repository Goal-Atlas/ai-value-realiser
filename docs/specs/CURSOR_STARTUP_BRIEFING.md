# Cursor Startup Briefing: AI Value Realiser

**Project:** AI Case Library  
**Owner:** Mike Parsons (Goal Atlas)  
**Date:** 2026-01-28  
**Handoff from:** Claude.ai conversation

---

## 1. Project Context

You are implementing the **AI Case Library** — a structured repository of AI business value cases with full provenance and explainability. This is a component of the larger **Value Realiser Architecture**.

**The core question it answers:** "What value can be realised by organisations through their use of AI?"

**What exists:**
- Specification v1.5 (attached: `AI_CASE_LIBRARY_SPECIFICATION_v1_5.md`)
- An `ai-value-realiser/` folder with `case_library/` subfolder (local)
- A GitHub repo that may already exist: `github.com/goalatlas/ai-value-realiser`
- A legacy case library with 202 cases (metadata only, no captured source content)

**What needs building (all inside `case_library/`):**
- Pydantic schemas matching the spec
- Provenance pipeline (5 steps: Discovery → Extraction → Claims → Verification → Validation)
- Case storage structure with raw + extracted sources
- Rebuild of the case library with proper source capture

---

## 2. First Task: Specification Validation Reviews

Before implementation, run these reviews against `AI_CASE_LIBRARY_SPECIFICATION_v1_5.md`:

### Review A: Trace the Data (30 mins)

Pick an **outcome claim with a metric** (e.g., "40% cost reduction") and trace it through the entire system:

1. **Source capture** — What files get created? Check §5.1 folder structure, §5.3 text file schema, §12.5 storage paths. Are they consistent?
2. **Claim extraction** — What fields must the AI populate? Check §3.2 Value Claim Schema, §6.4 Step 3 requirements.
3. **Verification** — How is the quote verified? Check §6.5.1 verification method. Does build.json (§5.4) log everything described?
4. **Casefile output** — Check §5.2. Does the sources example include all fields from Appendix E.3?
5. **Analyser query** — §11 says the Analyser queries by `value_claims.outcome`. Is `outcome` guaranteed present? Check Appendix E.1.

**Deliverable:** List any field mismatches, missing definitions, or ambiguous paths.

### Review B: Interface Contract Check (15 mins)

Compare §11.1 (Required Query Patterns) against Appendix E (Field Requirements):

| Query | Field Used | Is it Required in E.1/E.2? |
|-------|------------|---------------------------|
| By Sector | context_claims[sectoral] | ? |
| By Function | context_claims[functional].apqc_code | ? |
| By Value Driver | value_claims.outcome | ? |
| ... | ... | ... |

**Deliverable:** Confirm every queryable field is either (a) required, or (b) has defined fallback behaviour.

### Review C: Build.json Completeness (10 mins)

The example in §5.4 is abbreviated. Check that it could log:
- All Step 2 fields (§6.3): multi-page detection, extraction method, OCR fallback
- All Step 4 fields (§6.5.1): verification attempts with char offsets
- All Step 5 fields (§6.6/§7): validation tier, reviewer verdicts

**Deliverable:** Expanded build.json schema if gaps found.

---

## 3. Git Repository Setup

### Existing Structure

Mike already has an `ai-value-realiser/` folder containing `case_library/`. The repo may already exist on GitHub at `goalatlas/ai-value-realiser`.

### Step 1: Check GitHub repo status

```bash
cd ai-value-realiser
git remote -v                    # Check if connected to GitHub
gh repo view goalatlas/ai-value-realiser   # Check if repo exists
```

If not connected to GitHub:

```bash
gh repo create goalatlas/ai-value-realiser --private --source=. --push
```

### Step 2: Confirm folder structure

**All v1.5 spec implementation happens inside `case_library/`:**

```text
ai-value-realiser/                      # Value Realiser system (repo root)
├── case_library/                       # ← ALL v1.5 WORK GOES HERE
│   ├── schemas/
│   │   └── models.py                   # Pydantic models
│   ├── ontology/
│   │   └── ontology_v1.0.yaml
│   ├── pipeline/
│   │   ├── step1_discovery.py
│   │   ├── step2_extraction.py
│   │   ├── step3_claims.py
│   │   ├── step4_verification.py
│   │   └── step5_validation.py
│   ├── cases/                          # Populated cases go here
│   │   └── {case-id}/
│   │       ├── casefile.md
│   │       ├── build.json
│   │       └── sources/
│   │           ├── raw/
│   │           └── text/
│   └── tests/
├── opportunity_analyser/               # Future component (not v1.5 scope)
├── profiler/                           # Future component (not v1.5 scope)
├── docs/
│   └── specs/
│       ├── AI_CASE_LIBRARY_SPECIFICATION_v1_5.md
│       └── VALUE_REALISER_ARCHITECTURE_BRIEF.md
├── archive/
│   └── legacy_cases_pre_rebuild/       # Old 202 cases for seed list
└── README.md
```

### Step 3: Commit the spec

```bash
mkdir -p docs/specs
cp AI_CASE_LIBRARY_SPECIFICATION_v1_5.md docs/specs/
git add docs/specs/AI_CASE_LIBRARY_SPECIFICATION_v1_5.md
git commit -m "Add specification v1.5"
git push origin main
```

---

## 4. Legacy Cases: Pull for Validation

**Yes, pull the legacy cases.** They serve two purposes:

1. **Seed list extraction** — Organisation names and initiative descriptions become search inputs for source discovery (see §12.2-12.4)
2. **Schema validation** — Test Pydantic models against real-ish data structure (even though the claims themselves can't be trusted without source verification)

### Where to put them

Place legacy cases in `archive/legacy_cases_pre_rebuild/` at the repo root (not inside `case_library/` — they're reference material, not part of the rebuilt library):

```text
ai-value-realiser/
├── archive/
│   └── legacy_cases_pre_rebuild/
│       └── {case-id}/
│           ├── 1_sources.json
│           ├── 2_claims.json
│           ├── 3_audit.json
│           └── 4_casefile.md
└── case_library/
    └── cases/                  # NEW cases go here (rebuilt with provenance)
```

### What to extract

Create a seed list per §12.4:

```python
# Extract from legacy cases
seed_entry = {
    "organisation": "...",           # From casefile
    "initiative_description": "...", # From casefile title/summary
    "original_case_id": "...",       # For reference
    "legacy_urls": [...],            # From 1_sources.json
    "research_priority": "high|medium|low",
}
```

---

## 5. Implementation Priorities

**All implementation work for v1.5 occurs inside `case_library/`.**

### Phase 1: Schema + Storage (do first)
1. Implement Pydantic models matching Appendix E → `case_library/schemas/models.py`
2. Create folder structure for `case_library/cases/`
3. Write schema validation tests → `case_library/tests/`

### Phase 2: Extraction Pipeline
1. Step 2 (Content Extraction) — deterministic, test first → `case_library/pipeline/step2_extraction.py`
2. Step 1 (Source Discovery) — AI-assisted → `case_library/pipeline/step1_discovery.py`
3. Step 3 (Claim Extraction) — AI-assisted → `case_library/pipeline/step3_claims.py`

### Phase 3: Verification + Validation
1. Step 4 (Quote Verification) — critical for XAI compliance → `case_library/pipeline/step4_verification.py`
2. Step 5 (Human Validation) — interface TBD → `case_library/pipeline/step5_validation.py`

### Phase 4: Population
1. Extract seed list from legacy cases
2. Run pipeline on high-priority seeds
3. Build up `case_library/cases/` with proper provenance

---

## 6. Key Technical Decisions Already Made

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Source storage | Raw + extracted text | Provenance requires both; can't depend on URLs staying live |
| Quote verification | Against captured source, not live URL | Reproducibility |
| OCR fallback | Tesseract if pypdf yields <200 chars | Handle scanned PDFs |
| Strict mode attribution | Direct only (no Contributing) | Defensibility for Commit stage |
| Evidence hierarchy | Outcome > Adoption > Method | Three tiers, not binary |

---

## 7. Questions for Mike

Before starting implementation, confirm:

1. **Legacy case location** — Where are the 202 cases currently stored? (So we can copy them to `archive/legacy_cases_pre_rebuild/`)
2. **Existing code** — Is there any existing code in `case_library/` from your earlier work? Should it be preserved, archived, or replaced?
3. **GitHub status** — Is the repo already connected to GitHub, or does it need setup?
4. **Python environment** — Any preferences? (venv, conda, poetry)
5. **API keys** — Will this use Claude API for Steps 1/3/4? If so, where should keys be stored?
6. **Priority cases** — Any specific organisations/cases to rebuild first for validation?

---

## 8. Files to Provide to Cursor

- [x] `AI_CASE_LIBRARY_SPECIFICATION_v1_5.md` (attached to this briefing)
- [ ] Legacy cases folder (202 cases) → copy to `archive/legacy_cases_pre_rebuild/`
- [ ] `VALUE_REALISER_ARCHITECTURE_BRIEF.md` (parent document, for context) → `docs/specs/`
- [ ] `ontology_v1.0.yaml` (if it exists separately) → `case_library/ontology/`
- [ ] Any existing code in `case_library/` that should be preserved

---

*This briefing was generated from a Claude.ai session on 2026-01-28. The spec has been reviewed against a critical review document; four inconsistencies were identified and fixed in v1.5.*

