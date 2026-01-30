# Classification Overlay Architecture

Architectural recommendation for adding industry sector, APQC, and client-specific classifications to the AI Case Library.

**Decision:** Use separate overlay datasets that join to the core library, rather than embedding classifications in case files.

---

## Rationale

### Why not embed classifications in cases

1. **Provenance integrity** — The pipeline has a clean chain: source → extraction → claims → verification → human validation. Each step has audit logs. Industry/APQC classifications are *interpretive overlays*, not facts extracted from sources. Embedding them blurs that distinction.

2. **Judgement-call volatility** — APQC codes evolve. Industry classifications are contested (is a fintech a bank or a tech company?). Different stakeholders will disagree. Embedding means constantly patching core case files.

3. **Multi-client reality** — Client A wants cases tagged by their internal capability model. Client B uses a different framework. Embedded classifications force either client-specific forks or a one-size-fits-all taxonomy.

4. **Separation of concerns** — Core cases are *evidence*; classifications are *interpretation*. Different update cycles, different owners, different confidence levels.

---

## Recommended Structure

```
case_library/
  out/                              # Core library (pipeline output)
    <case_id>/
      build.json                    # Provenance log (immutable after pipeline)
      claims.json                   # Extracted facts + verification status
      casefile.md                   # Human-readable summary
      sources/text/*.txt            # Captured source text
  
  overlays/                         # Classification layers (separate)
    industry_sector/
      classifications.json          # case_id → industry codes
      taxonomy.json                 # Defines taxonomy (SIC, NAICS, custom)
      metadata.json                 # Version, last updated, maintainer
      
    apqc_process/
      value_claim_mappings.json     # claim_id → APQC process codes
      taxonomy.json                 # APQC version (7.3, 8.0, etc.)
      metadata.json
    
    # Client-specific overlays
    client_ucas/
      relevance_tags.json           # case_id → UCAS-specific categories
      priority_scores.json          # Which cases matter most to them
      metadata.json
```

---

## Overlay Schema Specifications

### Industry Sector Overlay

**`overlays/industry_sector/classifications.json`**
```json
{
  "version": "1.0",
  "taxonomy_ref": "taxonomy.json",
  "classifications": [
    {
      "case_id": "dbs-bank-ai-transformation",
      "primary_sector": {
        "code": "5221",
        "name": "Depository Credit Intermediation",
        "taxonomy": "NAICS_2022"
      },
      "secondary_sectors": [
        {
          "code": "5182",
          "name": "Data Processing and Hosting",
          "taxonomy": "NAICS_2022"
        }
      ],
      "confidence": "high",
      "tagged_by": "mike",
      "tagged_date": "2026-01-29T10:00:00Z",
      "notes": "Core banking with significant tech investment"
    }
  ]
}
```

**`overlays/industry_sector/taxonomy.json`**
```json
{
  "id": "NAICS_2022",
  "name": "North American Industry Classification System 2022",
  "source_url": "https://www.census.gov/naics/",
  "hierarchical": true,
  "levels": ["sector", "subsector", "industry_group", "industry", "national_industry"]
}
```

### APQC Process Overlay

**`overlays/apqc_process/value_claim_mappings.json`**
```json
{
  "version": "1.0",
  "apqc_version": "7.3.0",
  "mappings": [
    {
      "claim_id": "VC-001",
      "case_id": "dbs-bank-ai-transformation",
      "apqc_processes": [
        {
          "code": "10.2.3",
          "name": "Manage IT customer services",
          "level": 3,
          "primary": true
        },
        {
          "code": "8.2.1",
          "name": "Develop and manage customer service strategy",
          "level": 3,
          "primary": false
        }
      ],
      "confidence": "medium",
      "tagged_by": "system",
      "tagged_date": "2026-01-29T10:00:00Z",
      "method": "llm_assisted"
    }
  ]
}
```

### Client-Specific Overlay

**`overlays/client_ucas/relevance_tags.json`**
```json
{
  "version": "1.0",
  "client": "UCAS",
  "purpose": "AI training programme case selection",
  "tags": [
    {
      "case_id": "dbs-bank-ai-transformation",
      "relevance_score": 0.85,
      "capability_areas": ["customer_service", "process_automation"],
      "maturity_tier": "ai_native",
      "teaching_notes": "Good example of phased rollout",
      "tagged_by": "mike",
      "tagged_date": "2026-01-29T10:00:00Z"
    }
  ]
}
```

### Overlay Metadata

**`overlays/<overlay_name>/metadata.json`**
```json
{
  "overlay_id": "industry_sector",
  "display_name": "Industry Sector Classifications",
  "description": "Maps cases to NAICS industry codes",
  "version": "1.0",
  "created_date": "2026-01-29T10:00:00Z",
  "last_updated": "2026-01-29T10:00:00Z",
  "maintainer": "mike@goalatlas.com",
  "coverage": {
    "total_cases": 202,
    "classified_cases": 45,
    "coverage_percent": 22.3
  }
}
```

---

## What Stays in Core Cases vs Overlays

### Core case files (facts, verified)

- `organisation` — name of the company
- `context_claims` with `context_type: "sectoral"` — if source explicitly states the sector
- `context_claims` with `context_type: "functional"` — if APQC is stated in source (rare)

### Overlay files (interpreted, mutable)

- Industry classification codes (NAICS, SIC, custom)
- APQC process mappings for claims
- Client-specific relevance tags
- Custom taxonomies
- Confidence scores for interpretive judgements

**Rule of thumb:** If it came from a source and was verified → core case. If it's our interpretation or classification → overlay.

---

## Query Patterns

### Python examples

```python
from pathlib import Path
import json

def load_cases(library_path: Path) -> dict:
    """Load core case library."""
    cases = {}
    for case_dir in library_path.iterdir():
        if case_dir.is_dir() and (case_dir / "claims.json").exists():
            claims = json.loads((case_dir / "claims.json").read_text())
            build = json.loads((case_dir / "build.json").read_text())
            cases[case_dir.name] = {"claims": claims, "build": build}
    return cases

def load_overlay(overlay_path: Path) -> dict:
    """Load an overlay dataset."""
    # Find the main data file (classifications.json, mappings.json, etc.)
    for f in overlay_path.glob("*.json"):
        if f.name not in ("taxonomy.json", "metadata.json"):
            return json.loads(f.read_text())
    return {}

def join_industry(cases: dict, industry_overlay: dict) -> dict:
    """Enrich cases with industry classifications."""
    lookup = {c["case_id"]: c for c in industry_overlay.get("classifications", [])}
    for case_id, case_data in cases.items():
        case_data["industry"] = lookup.get(case_id)
    return cases

# Usage
cases = load_cases(Path("case_library/out"))
industry = load_overlay(Path("case_library/overlays/industry_sector"))
enriched = join_industry(cases, industry)

# Filter by sector
banking_cases = {
    cid: c for cid, c in enriched.items()
    if c.get("industry", {}).get("primary_sector", {}).get("code", "").startswith("52")
}
```

### Viewer integration

The viewer can optionally load overlays and display them as additional metadata:

```javascript
// Fetch core case
const caseDetail = await fetch(`/api/cases/${caseId}`).then(r => r.json());

// Fetch overlays (if available)
const industry = await fetch(`/api/overlays/industry_sector/${caseId}`).then(r => r.json()).catch(() => null);
const apqc = await fetch(`/api/overlays/apqc_process/${caseId}`).then(r => r.json()).catch(() => null);

// Compose view
const enrichedCase = { ...caseDetail, industry, apqc };
```

---

## Implementation Phases

### Phase 1: Infrastructure
- Create `overlays/` directory structure
- Define overlay metadata schema
- Add overlay loading utilities to `case_library/`

### Phase 2: Industry Sector
- Choose taxonomy (NAICS recommended for breadth)
- Create `industry_sector` overlay with initial classifications
- Add industry filter to viewer

### Phase 3: APQC Process
- Implement claim-level APQC mapping schema
- Consider LLM-assisted tagging with human review
- Add APQC faceted search to viewer

### Phase 4: Client Overlays
- Template for client-specific overlay creation
- Documentation for client onboarding
- Access control considerations (if overlays contain client-specific notes)

---

## Benefits of This Approach

1. **Core library stays clean** — 202 cases with verified provenance, no interpretive baggage
2. **Taxonomies can evolve** — Update APQC 7.3 → 8.0 without touching cases
3. **Client flexibility** — Each client gets their own overlay without forking the library
4. **Auditability** — Each classification has its own `tagged_by`, `confidence`, `method`
5. **Selective loading** — Only join what you need for a given use case
6. **Parallel development** — Core library and overlays can be maintained independently

---

## Open Questions

1. **Overlay API endpoints** — Should the server expose `/api/overlays/<name>/<case_id>` or bundle overlays into case detail response?

2. **Overlay editing UI** — Separate tool, or extend the validation viewer to support classification tagging?

3. **LLM-assisted classification** — For APQC especially, could run a classification pass similar to claim extraction. Store method="llm_assisted" and require human review.

4. **Overlay storage** — Flat JSON files work for 202 cases. At scale, consider SQLite or a proper database with overlay tables.
