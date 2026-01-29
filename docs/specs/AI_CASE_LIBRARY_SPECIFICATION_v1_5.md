# AI Case Library Specification

**Version:** 1.5  
**Date:** 2026-01-28  
**Status:** Finalised — implemented in [ai-value-realiser](https://github.com/goalatlas/ai-value-realiser) repository

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 0.1 | 2026-01-19 | Initial draft, awaiting ontology discovery results |
| 0.2 | 2026-01-19 | Added: Value Attribution (§3.5), Multi-Page Extraction (§6.3), Human Validation (§7) |
| 0.3 | 2026-01-19 | Finalised ontology v1.0 based on discovery pipeline results (1,440 claims analysed). Added `business_growth` outcome. Split `generative_autonomous` into `generative` + `autonomous`. Removed `innovation` from OUTCOME. Added corpus statistics and co-occurrence patterns. |
| 1.0 | 2026-01-19 | Specification finalised. Pydantic schemas implemented. Repository created at github.com/goalatlas/ai-value-realiser. |
| 1.1 | 2026-01-19 | Replaced Section 12 (Migration Path) with Population Strategy. Documents rebuild-from-scratch approach required because existing library lacks captured source content, making XAI impossible. |
| 1.2 | 2026-01-27 | Added Document Context section establishing relationship to parent architecture. No functional changes. |
| 1.3 | 2026-01-27 | Added implementation-critical details: Case ID conventions (§5.5), Quote Verification Method (§6.5.1), Field Requirements (Appendix E). |
| 1.4 | 2026-01-27 | **Evidence Level Hierarchy:** Replaced binary Evidence Type (outcome/method) with three-tier Evidence Level (outcome/adoption/method). Adoption level captures scale and reach metrics without business outcome attribution. Updated §2.2, §2.3, §3.2, §9, Appendix E. |
| 1.5 | 2026-01-28 | **Consistency fixes:** Resolved Strict mode attribution conflict (§3.5 now Direct only, aligned with §9.1). Harmonised source storage format (§5 now matches §12.5: raw + extracted files). Added source_origin classification to §4 (first_party/second_party/third_party). Added OCR fallback note to §6.3. |

---

## Document Context

**Parent System:** Value Realiser Architecture  
**Parent Document:** `VALUE_REALISER_ARCHITECTURE_BRIEF.md` (v2026-01-27)  
**Interface Contract:** `INTERFACE_CASE_LIBRARY.md` (pending)

This specification implements the **Case Library** component of the AI Value Realiser, as defined in the parent architecture document.

**What this document defines:**
- AI Case Library schemas, ontology, and data structures
- Provenance pipeline for case population
- Human validation framework
- Evidence filtering modes

**What this document references (without redefining):**
- Value Realisation Process stages (Scope → Explore → Commit → Adopt) — see parent document §2
- XAI/Provenance requirements — see parent document §1.4 and §3
- Component relationships — see parent document §1.6

When this specification references process stages (e.g., "Strict mode for Commit stage"), the stage definitions are authoritative in the parent document.

---

## 1. Purpose & Scope

### 1.1 The Question It Answers

> **"What value can be realised by organisations through their use of AI?"**

### 1.2 Target Organisations

- Businesses (private sector)
- Government organisations (departments, local authorities)
- Third sector organisations (charities, non-profits)

### 1.3 Two Core Purposes

| Purpose | Description |
|---------|-------------|
| **Feed Opportunity Analysis** | Enable systematic matching of organisational profiles to relevant cases |
| **Support Value Realisation Process** | Provide evidence at each stage (Scope, Explore, Commit, Adopt) |

### 1.4 In Scope

- Cases where AI is a **key driver** of value
- Cases that provide at least one of:
  - **Outcome Evidence** — quantified business results with attributed value
  - **Adoption Evidence** — quantified scale, reach, or activity metrics
  - **Method Evidence** — qualitative evidence of approach/architecture

### 1.5 Out of Scope

- Cases where AI is incidental (not a key driver)
- Cases with no evidence at any level (no outcomes, adoption metrics, or method detail)

---

## 2. Two-Axis Classification Model

Cases and claims are classified on two orthogonal axes:

### 2.1 Axis 1: Application Type

*What kind of change does this represent?*

| Value | Definition | Examples |
|-------|------------|----------|
| **Capability Enhancement** | Optimises existing business functions | Process automation, predictive maintenance, customer service optimisation |
| **Capability Creation** | Creates new capabilities, business models, or revenue streams | New product lines, platform businesses, market entry |

### 2.2 Axis 2: Evidence Level

*What strength of proof do we have?*

Evidence levels form a hierarchy. Higher levels implicitly contain lower-level information (an outcome case necessarily describes adoption and method; an adoption case necessarily describes method).

| Level | Name | Definition | Examples |
|-------|------|------------|----------|
| **3** | **Outcome** | Quantified business results with attributed value (revenue, cost, time, risk metrics) | "SGD 1 billion value created", "40% cost reduction", "$50M new revenue" |
| **2** | **Adoption** | Quantified scale, reach, or activity metrics *without* business outcome attribution | "Used by 80% of marketing staff", "10,000 hours of AI-assisted work", "Deployed across 12 departments" |
| **1** | **Method** | Qualitative description of approach, architecture, or operating model | "RAG pipeline with human review", "Three-layer governance structure" |

**Hierarchy principle:** A case's overall evidence level is the **highest** level present among its claims. A Level 3 case has outcome evidence and (implicitly) adoption/method information. A Level 2 case has adoption evidence and method information, but no quantified business outcomes.

**Why three levels?**

The previous binary (outcome vs method) forced awkward choices:
- "AI used by 500 employees" is quantified but not a business outcome
- "Pilot reached 80% of target users" proves scale but not value
- These "adoption metrics" are stronger than pure method descriptions but weaker than P&L impact

The three-tier model captures this real distinction.

### 2.3 The 2×3 Matrix

|  | **Outcome Evidence** | **Adoption Evidence** | **Method Evidence** |
|--|----------------------|----------------------|---------------------|
| **Capability Enhancement** | Hard proof of optimisation gains | Proof of scaled adoption for optimisation | Blueprint for how to optimise |
| **Capability Creation** | Hard proof of new value streams | Proof of new capability deployed at scale | Blueprint for transformation |

A single case may have claims across multiple cells. The case's overall classification uses the highest evidence level present.

---

## 3. Claim Categories

### 3.1 Two Categories of Claims

| Category | Purpose | Examples |
|----------|---------|----------|
| **Value Claims** | How AI created business value | "SGD 1 billion value created", "40% reduction in call handling time" |
| **Context Claims** | When/where/who was involved | "Q2 2024", "Retail Banking division", "Financial services sector" |

Both categories follow identical provenance patterns — sourced and audited.

### 3.2 Value Claim Schema

```yaml
value_claims:
  - id: "VC-001"
    # === CORE CLAIM ===
    claim_title: "SGD 1 billion value created"
    claim_description: "DBS reports AI initiatives have generated..."
    source_ids: ["S1"]
    source_quote: "Our AI initiatives have delivered SGD 1 billion..."
    quote_location: "Page 23, paragraph 2"
    
    # === ATTRIBUTION ===
    ai_attribution: "direct"  # direct | contributing | contextual
    attribution_evidence: "Quote explicitly states AI system achieved this result"
    
    # === EVIDENCE ===
    verification_status: "verified"  # verified | needs_review | rejected
    evidence_level: "outcome"  # outcome | adoption | method
    evidence_grade: "primary"  # primary | secondary_high | secondary_low
    
    # === APPLICATION ===
    application_type: "capability_enhancement"  # enhancement | creation
    
    # === ONTOLOGY CLASSIFICATION ===
    mechanism: ["automation"]  # From ontology v1.0
    outcome: ["cost_reduction", "velocity"]  # Can be multiple
    cognitive_depth: "autonomous"  # Single value
    
    # === RAW METRIC ===
    metric_raw:
      value: "SGD 1 billion"
      currency: "SGD"
      magnitude: 1000000000
      timeframe: null
      metric_type: "absolute_value"
      
    # === STANDARDISED METRIC ===
    metric_classification:
      quantification_level: "absolute"  # absolute | relative | qualitative
      magnitude_band: "transformational"  # small | medium | large | transformational
      
    # === ONTOLOGY METADATA ===
    ontology_version: "1.0"
    ontology_confidence:
      mechanism: 0.85
      outcome: 0.80
      cognitive_depth: 0.90
      
    # === HUMAN VALIDATION ===
    human_validation:
      reviewed: true
      reviewer_verdict: "valid"  # valid | invalid | unclear
      missed_claim: false
      review_notes: null
      review_date: "2026-01-19"
```

#### 3.2.1 Evidence Level Assignment

| Level | Assign when... | Examples |
|-------|----------------|----------|
| **outcome** | Claim states quantified business impact (revenue, cost savings, time reduction, risk mitigation) with AI attribution | "40% reduction in processing time", "$50M new revenue", "Risk incidents reduced by 60%" |
| **adoption** | Claim states quantified scale, reach, or activity but *not* business outcome | "Used by 500 employees", "10,000 hours logged", "Deployed in 12 regions", "80% adoption rate" |
| **method** | Claim describes approach, architecture, or process without quantified metrics | "Uses RAG architecture", "Three-stage approval workflow", "Human-in-the-loop review" |

**Decision rule:** If the claim contains a number, ask: "Is this measuring business value or measuring scale/activity?" Business value → `outcome`. Scale/activity → `adoption`. No number → `method`.

### 3.3 Context Claim Types

| Type | What it establishes | Required? | Likely Availability |
|------|---------------------|-----------|---------------------|
| **Temporal** | When did this happen? | Yes | High |
| **Organisational** | Division/brand/territory | No | Medium |
| **Sectoral** | Industry sector | Yes | High |
| **Functional** | APQC work function | Yes | High (derivable) |
| **Scale** | Organisation size | No | Low |
| **Strategic Intent** | Cost/growth/risk/CX | No | Medium |
| **Products/Services** | What AI was applied to | No | Medium |

### 3.4 Context Claim Schema

```yaml
context_claims:
  - id: "CC-001"
    context_type: "temporal"  # temporal | organisational | sectoral | functional | scale | strategic_intent | products_services
    claim_title: "Initiative launched Q2 2024"
    claim_description: "The AI transformation programme began in April 2024"
    source_ids: ["S1"]
    source_quote: "We launched our AI-first strategy in April 2024..."
    
    verification_status: "verified"  # verified | unverified | inferred
    verification_confidence: "high"  # high | medium | low
    inferred_from: null  # If inferred, what was it based on?
    
    # For functional claims:
    apqc_code: "5.3"
    apqc_name: "Deliver service to customer"
    
    # === HUMAN VALIDATION ===
    human_validation:
      reviewed: true
      reviewer_verdict: "valid"  # valid | invalid | unclear
      review_date: "2026-01-19"
```

### 3.5 Value Attribution

Value claims must indicate how directly the stated outcome is attributed to AI:

| Attribution Level | Definition | Example |
|-------------------|------------|---------|
| **Direct** | AI explicitly caused this outcome; causal link stated | "AI reduced call handling time by 40%" |
| **Contributing** | AI is a stated factor among others; partial attribution | "AI is one of several initiatives driving our efficiency gains" |
| **Contextual** | Organisational goal that AI work relates to, but no causal link stated | "Company targets 20% margins by 2030" |

#### Attribution Evidence

The `attribution_evidence` field must explain why the chosen attribution level was assigned:

| Attribution | Evidence Required |
|-------------|-------------------|
| **Direct** | Quote explicitly names AI/ML/automation as the cause |
| **Contributing** | Quote lists AI alongside other factors, or uses hedging language |
| **Contextual** | Quote describes organisational goals without AI causal connection |

#### Attribution Filtering by Evidence Mode

| Mode | Direct | Contributing | Contextual |
|------|--------|--------------|------------|
| **Strict** | ✅ Include | ❌ Exclude | ❌ Reclassify as Context Claim |
| **Standard** | ✅ Include | ✅ Include | ❌ Reclassify as Context Claim |
| **Exploratory** | ✅ Include | ✅ Include | ✅ Include with `ⓘ contextual` indicator |

**Note:** Strict mode requires direct AI attribution to ensure claims are defensible for Commit-stage business cases. Contributing claims may have value but their partial attribution makes them unsuitable for investment justification.

---

## 4. Evidence Grading Standards

### 4.1 Source Origin

Source origin distinguishes *who* is making claims about the AI initiative:

| Origin | Definition | Examples |
|--------|------------|----------|
| **first_party** | The organisation itself describing its own initiative | DBS Bank blog about DBS AI programme |
| **second_party** | A vendor, partner, or consultant describing a customer's initiative | Microsoft case study about a customer; McKinsey report on client engagement |
| **third_party** | Independent observer with no commercial relationship to the initiative | Reuters article; academic paper; government report |

**Why this matters:** A vendor case study (second_party) may be "primary" in the sense of originating the information, but has different authority than the organisation's own disclosure (first_party) or independent verification (third_party).

### 4.2 Primary vs Secondary Sources

| Type | Definition |
|------|------------|
| **Primary** | Direct authority on the case — originates or has first-hand knowledge of the information |
| **Secondary** | No first-hand knowledge — reports, aggregates, or comments on primary sources |

**Primary source examples:**

| Source Type | Examples |
|-------------|----------|
| Organisation itself | Company blog, press release, annual report |
| Major consultancy | McKinsey, BCG, Bain, Deloitte, PwC, Accenture |
| Technology provider | AWS, Microsoft, Google, Nvidia, Anthropic |
| Academic/Governmental | Harvard, MIT, Stanford, government reports |

**Note:** World Economic Forum and similar organisations are closer to "convener/aggregator" than "direct authority" — classify as primary only when they conducted original research, otherwise secondary_high.

### 4.3 Secondary Source Grading

| Grade | Indicators |
|-------|------------|
| **secondary_high** | Established consultant, published author, significant LinkedIn/Substack following, recognised analyst |
| **secondary_low** | No obvious reputation markers, aggregator sites, content farms |

### 4.4 Evidence Strength

A claim's overall evidence strength is derived from multiple factors:

| Factor | Contribution |
|--------|--------------|
| Source origin | first_party > third_party > second_party (for outcome claims) |
| Source type | primary > secondary_high > secondary_low |
| AI attribution | direct > contributing > contextual |
| Verification | verified > needs_review |
| Metric presence | quantified > qualitative |

The viewer applies these factors according to the selected evidence mode (§9).

---

## 5. File Structure

### 5.1 Case Folder Structure

```text
cases/
└── {case-id}/
    ├── casefile.md          # THE PRODUCT — single source of truth
    ├── sources/             # Captured sources (for verification)
    │   ├── raw/             # Original files as captured
    │   │   ├── S1_dbs_annual_report_2024.pdf
    │   │   └── S2_mckinsey_case_study.html
    │   └── text/            # Extracted text for verification
    │       ├── S1_dbs_annual_report_2024.txt
    │       └── S2_mckinsey_case_study.txt
    └── build.json           # Pipeline provenance log
```

**Storage principle:** Preserve both raw source files (PDF, HTML) and extracted text. This ensures the provenance chain is complete and self-contained — verification never depends on external URLs remaining available.

### 5.2 casefile.md — Single Source of Truth

The viewer and matcher only need to read this one file per case.

```yaml
---
# === IDENTITY ===
case_id: "dbs-bank-ai-customer-service"
organisation: "DBS Bank"
title: "AI-Powered Customer Service Transformation"
date_created: "2026-01-19"
date_updated: "2026-01-19"

# === SOURCES ===
sources:
  - id: "S1"
    title: "DBS Annual Report 2024"
    url: "https://..."
    type: "primary"
    origin: "first_party"
    grade: "organisation_itself"
    raw_file: "sources/raw/S1_dbs_annual_report_2024.pdf"
    text_file: "sources/text/S1_dbs_annual_report_2024.txt"
    extraction_method: "pypdf"
    extraction_quality: "high"
    is_multi_page: false
    related_urls: []

# === VALUE CLAIMS ===
value_claims:
  - id: "VC-001"
    # ... (full schema as above)

# === CONTEXT CLAIMS ===
context_claims:
  - id: "CC-001"
    # ... (full schema as above)

# === VERIFICATION SUMMARY ===
verification_summary:
  value_claims:
    total: 5
    verified: 4
    needs_review: 1
    by_attribution:
      direct: 3
      contributing: 1
      contextual: 1
  context_claims:
    total: 8
    verified: 5
    unverified: 2
    inferred: 1
  all_value_verified: false
  all_context_verified: false

# === HUMAN VALIDATION SUMMARY ===
human_validation_summary:
  reviewed: true
  review_date: "2026-01-19"
  reviewer_id: "MB"
  validation_tier: "tier_1"  # tier_1 | tier_2_blind | tier_3_calibration
  value_claims:
    valid: 4
    invalid: 0
    unclear: 1
    missed: 0
  context_claims:
    valid: 7
    invalid: 0
    unclear: 1
  precision_score: null  # Only populated for Tier 2
  recall_score: null     # Only populated for Tier 2

# === STATUS ===
status: "complete"  # complete | needs_review | in_progress
confidence: "high"
review_flags: []

# === ONTOLOGY METADATA ===
ontology_metadata:
  version_used: "1.0"
  tagged_date: "2026-01-19"
  needs_retagging: false
---

# DBS Bank: AI-Powered Customer Service Transformation

## Executive Summary
...

## Key Findings
...

## Sources
...
```

### 5.3 sources/text/S1_*.txt — Extracted Text

```yaml
---
source_id: S1
source_url: https://www.dbs.com/annual-report-2024
raw_file: sources/raw/S1_dbs_annual_report_2024.pdf
fetch_timestamp: "2026-01-19T14:30:00Z"
fetch_status: success
extraction_method: pypdf  # pypdf | trafilatura | tesseract_ocr
extraction_quality: high  # high | medium | low (low indicates OCR or degraded extraction)
content_length: 4832

# === MULTI-PAGE METADATA ===
is_multi_page: false
multi_page_detection:
  patterns_found: []
  related_urls_detected: []
  related_urls_followed: []
  detection_method: null
---

[Full extracted text...]
```

**File naming convention:** `S{n}_{org_slug}_{doc_type}.{ext}`

| Component | Example |
|-----------|---------|
| Source ID | `S1`, `S2` |
| Org slug | `dbs`, `mckinsey`, `nhs_england` |
| Doc type | `annual_report_2024`, `case_study`, `press_release` |
| Extension | `.pdf`, `.html` (raw) / `.txt` (extracted) |

### 5.4 build.json — Pipeline Provenance Log

```json
{
  "case_id": "dbs-bank-ai-customer-service",
  "build_started": "2026-01-19T14:25:00Z",
  "build_completed": "2026-01-19T14:35:00Z",
  
  "step_1_discovery": { ... },
  "step_2_extraction": { 
    "multi_page_candidates": [],
    "multi_page_followed": []
  },
  "step_3_claims": { ... },
  "step_4_verification": { ... },
  "step_5_human_validation": {
    "tier": "tier_1",
    "reviewer_id": "MB",
    "review_date": "2026-01-19",
    "time_taken_minutes": 12,
    "claims_reviewed": 13,
    "verdicts": {
      "valid": 11,
      "invalid": 0,
      "unclear": 2
    },
    "missed_claims_added": 0
  }
}
```

### 5.5 Case ID Conventions

Case IDs must be unique and stable. They serve as folder names, internal references, and URL slugs.

**Format:** `{org-slug}-{initiative-slug}-{disambiguator}`

| Component | Rules | Example |
|-----------|-------|---------|
| `org-slug` | Lowercase, hyphenated, recognisable short name | `dbs-bank`, `rolls-royce`, `nhs-england` |
| `initiative-slug` | 2-4 words describing the AI initiative | `ai-customer-service`, `predictive-maintenance` |
| `disambiguator` | Optional. Year or qualifier if org has multiple similar initiatives | `2024`, `phase-2`, `apac` |

**Examples:**

| Organisation | Initiative | Case ID |
|--------------|------------|---------|
| DBS Bank | AI-powered customer service | `dbs-bank-ai-customer-service` |
| DBS Bank | Fraud detection system | `dbs-bank-fraud-detection` |
| Rolls-Royce | Predictive engine maintenance | `rolls-royce-predictive-maintenance` |
| NHS England | AI triage pilot (2024) | `nhs-england-ai-triage-2024` |
| NHS England | AI triage national rollout | `nhs-england-ai-triage-national` |

**Collision handling:**

1. Before creating a case, check if `{org-slug}-{initiative-slug}` already exists
2. If collision, add disambiguator (year, region, phase)
3. If still ambiguous, use more specific initiative description

**Immutability:** Once assigned, case IDs never change. If an initiative evolves significantly, create a new case and link to the original via a context claim.

---

## 6. Provenance Pipeline

### 6.1 Pipeline Overview

```text
INPUT: (Organisation, Topic Description)
    │
    ▼
┌─────────────────────────────────────────┐
│ STEP 1: Source Discovery          [AI] │
│ Web search → Select 5-10 URLs           │
└─────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────┐
│ STEP 2: Content Extraction    [DETERM.] │
│ Fetch URLs → Extract to .md files       │
│ Detect multi-page → Flag for review     │
└─────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────┐
│ STEP 3: Claim Extraction          [AI] │
│ Analyse .md → Extract claims            │
│ Assign ai_attribution level             │
└─────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────┐
│ STEP 4: Verification & Categorisation  │
│ Verify quotes, assign ontology    [AI] │
└─────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────┐
│ STEP 5: Human Validation        [HUMAN] │
│ Review claims, mark valid/invalid       │
│ Add missed claims                       │
└─────────────────────────────────────────┘
    │
    ▼
OUTPUT: casefile.md + sources/*.md + build.json
```

### 6.2 Step 1: Source Discovery [AI]

| Aspect | Specification |
|--------|---------------|
| **Input** | Organisation name + Topic description |
| **Action** | Web search → AI selects most relevant, authoritative sources |
| **Output** | Prioritised list of 5-10 URLs |
| **Unit Test** | ≥1 valid URL |
| **Retry** | 3× on failure, refine search terms |
| **Failure** | After 3 fails → Flag case as NEEDS_REVIEW |
| **AI Boundary** | Log: search query, results, selection rationale, model |

### 6.3 Step 2: Content Extraction [DETERMINISTIC]

| Aspect | Specification |
|--------|---------------|
| **Input** | First 5 URLs from Step 1 |
| **HTTP Retry** | 3× on [429, 500, 502, 503, 504] with exponential backoff (1s, 2s, 4s) |
| **No Retry** | On [401, 403, 404] — log as inaccessible |
| **Extraction Chain** | PDF: pypdf → (if low text yield) tesseract OCR / HTML: trafilatura → BeautifulSoup → raw text |
| **OCR Fallback** | If pypdf yields <200 chars from PDF, assume scanned document and route to OCR. Set `extraction_quality: low` and log `extraction_method: tesseract_ocr` |
| **Min Content** | 200 characters (below = "insufficient content") |
| **Multi-Page Detection** | After extraction, scan for continuation patterns (see §6.3.1) |
| **Output** | .md file per URL with source_url, fetch_status, extraction_method, content, multi_page_metadata |
| **Unit Test** | Count(.md files) = Count(URLs requested), ≥1 success |
| **Failure** | Failed URLs don't block; if ALL fail → NEEDS_REVIEW |
| **AI Boundary** | None — deterministic |

#### 6.3.1 Multi-Page Detection

After initial content extraction, scan for patterns indicating content spans multiple pages:

**Detection Patterns:**

| Pattern Type | Indicators | Examples |
|--------------|------------|----------|
| **Pagination** | "Page X of Y", "Next", "Previous", numbered page links | `<a href="?page=2">`, "Continue reading →" |
| **Chapter Structure** | "Part X", "Chapter X", Table of Contents with internal links | "Part 2: Implementation", ToC linking to `/report/chapter-2` |
| **Series** | "Read part 2", "Continued in...", "See also" with same-domain links | "This is part 1 of 3" |
| **URL Structure** | Same-domain links with similar path patterns | `/blog/ai-strategy-1`, `/blog/ai-strategy-2` |

**Default Behaviour:**

1. Run detection on all extracted content
2. If patterns found:
   - Set `is_multi_page: true` in source metadata
   - Log detected URLs and patterns in `build.json`
   - For **pagination** patterns with high confidence: auto-follow (depth 1, max 5 pages)
   - For all other patterns: flag for human review, do not auto-follow
3. Continue pipeline with available content
4. Human reviewer decides whether to trigger re-extraction with additional URLs

### 6.4 Step 3: Claim Extraction [AI]

| Aspect | Specification |
|--------|---------------|
| **Input** | Set of .md files from Step 2 |
| **Action** | AI extracts Value Claims + Context Claims |
| **Attribution** | AI assigns `ai_attribution` level (direct/contributing/contextual) for each value claim |
| **Output** | claims_extracted.json |
| **Unit Test** | ≥1 value claim, all claims have required fields, valid source_ids, all value claims have ai_attribution |
| **Retry** | 2× on malformed JSON, 1× on zero claims |
| **Failure** | After retries → NEEDS_REVIEW, continue with empty claims |
| **AI Boundary** | Log: prompt, raw response, parsed claims, retries, model |

### 6.5 Step 4: Verification & Categorisation [AI]

| Aspect | Specification |
|--------|---------------|
| **Input** | Claims from Step 3 + Original URLs |
| **Action** | Verify quotes at source, assign ontology categories |
| **Verification** | Fetch original URL, search for quote (see §6.5.1) |
| **Categorisation** | Assign application_type, evidence_type, mechanism, outcome, cognitive_depth |
| **Attribution Check** | Verify ai_attribution assignment is consistent with source language |
| **Evidence Grade** | Derive from source metadata (primary/secondary) |
| **Output** | Populated casefile.md with complete YAML frontmatter |
| **Unit Test** | All claims have verification_status, all value claims have ontology tags and ai_attribution |
| **Retry** | URL fetch fail → use .md fallback, mark "verified against extraction only" |
| **Failure** | Zero verified value claims → NEEDS_REVIEW |
| **AI Boundary** | Log: verification attempts, categorisation rationale, confidence, model |

#### 6.5.1 Quote Verification Method

Quote verification establishes the provenance chain from claim to source. This is the foundation of XAI compliance.

**Verification approach:**

| Method | When Used | Process |
|--------|-----------|---------|
| **Exact match** | First attempt | Search captured source text for exact `source_quote` string |
| **Normalised match** | If exact fails | Normalise whitespace, punctuation, and case; retry match |
| **Substring match** | If normalised fails | Search for longest matching substring (minimum 60% of quote length) |
| **AI-assisted match** | If substring fails | AI compares quote against source, explains any discrepancy |
| **Manual verification** | If AI-assisted fails | Human reviewer locates quote or marks claim `needs_review` |

**Verification outcomes:**

| Outcome | Criteria | `verification_status` |
|---------|----------|----------------------|
| **Verified (exact)** | Exact or normalised match found | `verified` |
| **Verified (partial)** | Substring match ≥60% with AI confirmation of semantic equivalence | `verified` + flag `partial_match` |
| **Verified (source updated)** | Quote found in captured source but not current URL (source has changed) | `verified` + flag `source_diverged` |
| **Unverifiable** | Quote not in captured source; likely extraction or AI error | `needs_review` |

**Quote location recording:**

The `quote_location` field uses a practical format based on source type:

```yaml
# For captured web pages / HTML
quote_location: "Section: 'AI Strategy', paragraph 3"

# For PDFs with stable page numbers  
quote_location: "Page 23, paragraph 2"

# For long documents — character offset as fallback
quote_location: "chars 12450-12680 in S1.txt"
```

The priority is human-navigability. Character offsets are recorded in `build.json` for programmatic access but the `quote_location` field in the casefile should be human-readable.

**What gets logged (in build.json):**

```json
"verification_attempts": [
  {
    "claim_id": "VC-001",
    "method": "normalised_match",
    "result": "found",
    "char_offset_start": 12450,
    "char_offset_end": 12680,
    "match_confidence": 1.0
  },
  {
    "claim_id": "VC-002", 
    "method": "ai_assisted",
    "result": "found_paraphrased",
    "ai_explanation": "Source uses 'approximately $1B' vs quote '~$1 billion' — semantically equivalent",
    "match_confidence": 0.9
  }
]
```

**Verification against captured source vs live URL:**

Primary verification is always against the **captured source** (the `.md` or `.txt` file in `sources/`). This ensures reproducibility — the source we verified against is preserved.

Secondary verification against the live URL is optional and informational only. If the live URL differs from the captured source, flag `source_diverged` is set but the claim remains verified against the captured content.

### 6.6 Step 5: Human Validation [HUMAN]

Human validation is **mandatory** for all cases. Three tiers exist with different depth/coverage trade-offs.

| Aspect | Specification |
|--------|---------------|
| **Input** | casefile.md from Step 4 + source .md files |
| **Action** | Human reviews AI-extracted claims against source material |
| **Output** | Updated casefile.md with human_validation fields populated |
| **Mandatory** | Every case must complete at least Tier 1 validation |
| **Frequency** | Tier 1: all cases / Tier 2: 10% sample / Tier 3: monthly calibration |

See §7 for full Human Validation specification.

---

## 7. Human Validation Framework

### 7.1 Purpose

Human validation ensures the AI extraction pipeline produces accurate, complete claims. It is **core to quality** and non-optional.

### 7.2 Three-Tier Validation Model

| Tier | Name | Coverage | Purpose | Time per Case |
|------|------|----------|---------|---------------|
| **Tier 1** | Review Validation | 100% of cases | Catch errors and gaps | ~10-15 min |
| **Tier 2** | Blind Extraction | 10% sample | Measure AI precision/recall | ~30-45 min |
| **Tier 3** | Calibration | Monthly | Establish human baseline | ~45-60 min |

### 7.3 Tier 1: Review Validation (Every Case)

**Process:**

1. Human sees source material alongside AI-extracted claims
2. For each claim, human marks: ✓ Valid | ✗ Invalid | ? Unclear
3. Human adds any claims AI missed
4. Human flags any attribution disagreements

**Metrics:**

| Metric | Calculation | Target | Alert Threshold |
|--------|-------------|--------|-----------------|
| **Tier 1 Pass Rate** | Cases valid / Cases reviewed | ≥85% | <75% |
| **Tier 2 Precision** | Rolling average | ≥90% | <85% |
| **Tier 2 Recall** | Rolling average | ≥85% | <80% |
| **Review Backlog** | Cases awaiting Tier 1 | <20 | >50 |
| **Time per Review** | Median Tier 1 time | ≤15 min | >25 min |

---

## 8. Two-Tier Review Model (Viewer Behaviour)

### 8.1 Separation of Concerns

| Claim Category | Viewer | NEEDS_REVIEW Impact |
|----------------|--------|---------------------|
| **Value Claims** | Main viewer | Visible to users — quality matters |
| **Context Claims** | Curation viewer | Hidden from main viewer — improves matching |

### 8.2 Verification Status by Category

**Value Claims:**
- `verified` — Quote found at source
- `needs_review` — Quote not found, or other issue
- `rejected` — Claim invalid (after human review)

**Context Claims:**
- `verified` — Quote found at source
- `unverified` — Quote not found / source unavailable
- `inferred` — Derived from other information (no direct quote)

---

## 9. Evidence Filtering for Matching

### 9.1 Three Evidence Modes

| Mode | Evidence Level | Value Claims | Context Claims | Attribution | Use Case |
|------|----------------|--------------|----------------|-------------|----------|
| **Strict** | Outcome only | Verified only | Verified only | Direct only | Commit stage — business cases |
| **Standard** (default) | Outcome + Adoption | Verified only | Any | Direct + Contributing | Explore stage — understanding options |
| **Exploratory** | All levels | Any | Any | All | Scope stage — broad discovery |

### 9.2 Evidence Level Filtering

The evidence level filter controls which cases are surfaced based on their highest evidence level:

| Filter Setting | Cases Included | Rationale |
|----------------|----------------|-----------|
| **Outcome only** | Only cases with ≥1 outcome-level claim | Need hard numbers for investment decisions |
| **Adoption+** | Cases with outcome OR adoption claims | Need proof of real-world deployment |
| **All** | All cases including method-only | Maximise discovery, accept lower evidence strength |

### 9.3 Alignment with Value Realisation Stages

*Stage definitions are authoritative in the parent architecture document.*

| Stage | Recommended Mode | Evidence Level | Rationale |
|-------|------------------|----------------|-----------|
| **Scope** | Exploratory | All | Cast wide net, find relevant patterns |
| **Explore** | Standard | Adoption+ | Focus on cases proven at scale |
| **Commit** | Strict | Outcome only | Bulletproof evidence for business case |
| **Adopt** | Standard | Adoption+ | Implementation guidance from proven deployments |

---

## 10. Ontology v1.0 (Finalised)

### 10.1 Overview

The ontology was validated against 1,440 claims from 202 cases. Classification success rate: **79.9%**.

| Dimension | Question | Cardinality | Confidence |
|-----------|----------|-------------|------------|
| **MECHANISM** | How does AI create value? | 1-2 tags | Avg 0.84 |
| **OUTCOME** | What business result? | 1-4 tags | Avg 0.86 |
| **COGNITIVE_DEPTH** | What AI sophistication level? | 1 tag | Avg 0.80 |

### 10.2 MECHANISM Dimension

*How does the AI create value?*

| Term | Definition | Corpus Count | Avg Confidence |
|------|------------|--------------|----------------|
| **automation** | AI performs tasks previously done by humans, reducing manual effort | 377 (28%) | 0.87 |
| **augmentation** | AI enhances human capabilities without replacing the human | 360 (26%) | 0.84 |
| **optimization** | AI finds better solutions within existing constraints | 429 (31%) | 0.83 |
| **innovation** | AI enables fundamentally new products, services, or business models | 191 (14%) | 0.81 |

### 10.3 OUTCOME Dimension

*What business result does the AI produce?*

| Term | Definition | Corpus Count | Avg Confidence |
|------|------------|--------------|----------------|
| **velocity** | Acceleration of time to deliver value | 524 (30%) | 0.87 |
| **experience** | Improved quality of interaction for customers/employees | 409 (23%) | 0.85 |
| **cost_reduction** | Operational efficiency gains reducing what you spend | 317 (18%) | 0.86 |
| **revenue_lift** | Direct increase in revenue or monetisation | 304 (17%) | 0.85 |
| **risk_avoidance** | Prevention or mitigation of potential losses | 141 (8%) | 0.86 |
| **cost_erosion** | Competitive pressure reducing what you can charge (external) | 47 (3%) | 0.88 |
| **business_growth** | Organisational scale expansion (customers, market share, valuation) | NEW | — |

**Removed:** `innovation` was previously listed as an OUTCOME but belongs only in MECHANISM.

### 10.4 COGNITIVE_DEPTH Dimension

*What level of AI sophistication is demonstrated?*

| Term | Definition | Corpus Count | Avg Confidence |
|------|------------|--------------|----------------|
| **descriptive** | What happened? Reporting and summarisation | 379 (27%) | 0.76 |
| **diagnostic** | Why did it happen? Root cause analysis | 83 (6%) | 0.83 |
| **predictive** | What will happen? Forecasting and prediction | 151 (11%) | 0.84 |
| **prescriptive** | What should we do? Recommendations and decision support | 497 (35%) | 0.77 |
| **generative** | Create this. Content generation (text, code, images, designs) | SPLIT | — |
| **autonomous** | Do this. Takes action without per-instance human direction | SPLIT | — |

**Note:** `generative` and `autonomous` were split from the previous `generative_autonomous` term.

### 10.5 Co-occurrence Patterns

Common mechanism + outcome combinations (from corpus analysis):

| Pattern | Count | Interpretation |
|---------|-------|----------------|
| automation + velocity | 221 | Automating tasks speeds them up |
| augmentation + experience | 180 | Helping humans improves customer/employee experience |
| optimization + cost_reduction | 167 | Finding efficiencies reduces costs |
| augmentation + velocity | 166 | AI assistance speeds up human work |
| optimization + velocity | 139 | Optimisation often means faster |

### 10.6 Terms Considered But Rejected

| Proposed Term | Dimension | Decision | Rationale |
|---------------|-----------|----------|-----------|
| strategic_positioning | outcome | REJECT | Overlaps with `business_growth`; many are contextual attribution claims |
| engagement_improvement | outcome | REJECT | Subset of `experience`; insufficient distinct evidence |
| platform_enablement | mechanism | REJECT | Describes architecture, not AI action |
| contextual | cognitive_depth | REJECT | Feature of many AI systems, not a distinct level |

---

## 11. Interface Contract (for Opportunity Analyser)

### 11.1 Required Query Patterns

| Query Type | Fields Used |
|------------|-------------|
| By Sector | context_claims[sectoral] |
| By Function | context_claims[functional].apqc_code |
| By Value Driver | value_claims.outcome |
| By Application Type | value_claims.application_type |
| By Mechanism | value_claims.mechanism |
| By Cognitive Depth | value_claims.cognitive_depth |
| By Attribution Strength | value_claims.ai_attribution |
| By Recency | context_claims[temporal] |
| By Evidence Strength | value_claims.evidence_grade, verification_summary |

### 11.2 Matching Input (from Profiler)

The Opportunity Analyser receives:
- Sector(s)
- Work functions (APQC codes)
- Products/services
- Strategic priorities
- Size/geography

And matches against Case Library fields to surface relevant cases.

---

## 12. Population Strategy

### 12.1 Why Rebuild From Scratch

The existing 202-case library **cannot be migrated** because it lacks captured source content.

**The Problem:**

The current `sources.json` files contain metadata (URL, title, doc_type) but **no downloaded content**. The actual text from those URLs was never captured and stored.

| What XAI Requires | What Exists | Gap |
|-------------------|-------------|-----|
| Source content captured at extraction time | URLs pointing to external pages | No content |
| Verifiable quotes with location references | Claims referencing URLs | Cannot verify |
| Traceable provenance chain | Metadata only | Chain broken at first link |

**The Consequence:**

Without source content, the validator cannot function. Claims cannot be checked against original text. The `quote_location` field cannot be populated. The entire explainability architecture — which requires every claim to trace back to a verified passage in a captured source — is impossible to satisfy.

**The Decision:**

Rebuild the library from scratch, capturing source content at extraction time. The existing library serves only as a **seed list** — providing organisation names and initiative descriptions to guide source discovery.

### 12.2 What the Existing Library Provides

| Asset | Usable? | How Used |
|-------|---------|----------|
| Organisation names | ✅ | Research targets |
| Initiative descriptions | ✅ | Search queries for source discovery |
| Source URLs | ⚠️ | Starting points (may be stale/dead) |
| Extracted claims | ❌ | Cannot be trusted without source verification |
| Audit data | ❌ | Audited against non-existent content |
| Ontology tags | ❌ | Must be reapplied to verified claims |

### 12.3 Population Pipeline Overview

| Phase | Input | Process | Output |
|-------|-------|---------|--------|
| **1. Seed Extraction** | Existing case library | Extract org names + initiative descriptions | Research target list |
| **2. Source Discovery** | Research target list | AI-assisted search for current sources | Source candidates per case |
| **3. Content Extraction** | Source URLs | Web scraping / PDF extraction | **Captured source content** |
| **4. Claim Extraction** | Captured content | AI-assisted claim identification with quotes | Extracted claims with source references |
| **5. Validation & Categorisation** | Extracted claims | Attribution, ontology tagging, verification | Validated claims |
| **6. Archiving** | Validated claims + sources | Generate casefile.md + build.json | Complete case with full provenance |

**Critical difference from migration:** Phase 3 captures and stores source content, establishing the provenance chain that makes all subsequent steps possible.

### 12.4 Seed List Schema

The seed list extracted from the existing library:

```yaml
seed_list:
  - organisation: "DBS Bank"
    initiative_description: "AI transformation programme creating SGD 1B value"
    original_case_id: "dbs-ai-transformation"  # Reference only
    legacy_urls:  # Starting points for source discovery
      - "https://www.dbs.com/ai-report-2024"
      - "https://www.mckinsey.com/dbs-case-study"
    research_priority: "high"  # high | medium | low
    notes: "Major case, likely well-documented"
```

### 12.5 Source Content Storage

Captured source content is stored alongside the case:

```text
cases/
  dbs-ai-transformation/
    casefile.md           # Case with YAML frontmatter
    build.json            # Pipeline provenance
    sources/
      S1_dbs_annual_report_2024.pdf      # Captured source
      S1_dbs_annual_report_2024.txt      # Extracted text
      S2_mckinsey_case_study.html        # Captured source
      S2_mckinsey_case_study.txt         # Extracted text
```

This ensures the provenance chain is complete and self-contained — verification never depends on external URLs remaining available.

### 12.6 Legacy Archive

The existing 4-file structure will be archived (not deleted):

```text
archive/
  legacy_cases_pre_rebuild/
    dbs-ai-transformation/
      1_sources.json
      2_claims.json
      3_audit.json
      4_casefile.md
    [... all 202 cases ...]
```

This preserves the original work for reference while establishing clean provenance for the rebuilt library.

### 12.7 Rebuild vs Migration Summary

| Aspect | Migration (rejected) | Rebuild (chosen) |
|--------|---------------------|------------------|
| Source content | Assume URLs still valid | Capture at extraction time |
| Claims | Inherit and retrofit | Extract fresh with attribution |
| Provenance | Reconstruct from metadata | Built natively in pipeline |
| Validation | Cannot verify quotes | Full verification possible |
| XAI compliance | ❌ Impossible | ✅ By design |

---

## 13. Open Items

### 13.1 Decisions Deferred

| Decision | Options | Notes |
|----------|---------|-------|
| APQC classification | Deterministic lookup vs AI-assisted | Schemas support both approaches |
| Casefile markdown body | AI-generated narrative vs templated | Current schema has placeholder |
| Build.json structure | Single file vs separate step logs | Current design uses single file |

### 13.2 Not Yet Implemented

- Batch processing / orchestration
- Manual case creation workflow
- Viewer implementation details
- Curation viewer for context claims
- Human validation interface implementation
- Seed list extraction tooling

---

## Appendix A: AI Boundary Summary

| Step | AI? | What Gets Logged |
|------|-----|------------------|
| 1. Source Discovery | ✅ | Search queries, results, selection rationale, model |
| 2. Content Extraction | ❌ | URL, HTTP status, extraction method, content length, multi-page detection |
| 3. Claim Extraction | ✅ | Prompt, raw response, parsed claims, attribution assignments, retries, model |
| 4. Verification | ✅ | Verification attempts, categorisation rationale, confidence, model |
| 5. Human Validation | ❌ | Reviewer ID, verdicts, missed claims, time taken |

---

## Appendix B: Glossary

| Term | Definition |
|------|------------|
| **Value Claim** | A claim about how AI created business value |
| **Context Claim** | A claim about when/where/who was involved |
| **AI Attribution** | How directly a stated outcome is attributed to AI (direct/contributing/contextual) |
| **Application Type** | Enhancement (optimise existing) vs Creation (new capability) |
| **Evidence Level** | Three-tier hierarchy: Outcome (quantified business results), Adoption (quantified scale/activity), Method (qualitative approach). Higher levels implicitly contain lower levels. |
| **Source Origin** | Who is making the claim: first_party (org itself), second_party (vendor/partner), third_party (independent observer) |
| **Mechanism** | How AI creates value (automation, augmentation, optimization, innovation) |
| **Outcome** | Business result (velocity, experience, cost_reduction, revenue_lift, risk_avoidance, cost_erosion, business_growth) |
| **Cognitive Depth** | AI sophistication level (descriptive, diagnostic, predictive, prescriptive, generative, autonomous) |
| **Primary Source** | Direct authority — originates or has first-hand knowledge of the information |
| **Secondary Source** | No first-hand knowledge, graded by reputation (secondary_high, secondary_low) |
| **Tier 1 Validation** | Human review of AI-extracted claims (every case) |
| **Tier 2 Validation** | Blind human extraction for precision/recall measurement (10% sample) |
| **Tier 3 Validation** | Inter-rater calibration for baseline reliability (monthly) |
| **Seed List** | Organisation names and initiative descriptions extracted from legacy library to guide source discovery |

---

## Appendix C: Ontology Discovery Statistics

**Corpus:** 1,440 claims from 202 cases  
**Analysis Date:** 2026-01-19

### Classification Results

| Status | Count | Percentage |
|--------|-------|------------|
| Fit well | 1,150 | 79.9% |
| Uncertain | 144 | 10.0% |
| No fit | 146 | 10.1% |

### Confidence Distribution

| Level | Count | Percentage |
|-------|-------|------------|
| High (≥0.8) | 976 | 67.8% |
| Medium (0.5-0.8) | 341 | 23.7% |
| Low (<0.5) | 123 | 8.5% |

### Metrics Extraction

- **Claims with metrics:** 868 (60.3%)
- **Most common metric types:** percentage (466), count (201), time (161), currency (154)
- **Currencies detected:** USD (127), EUR (7), GBP (5), SGD (4), others (8)

---

## Appendix D: Implementation Reference

### Repository

**GitHub:** `https://github.com/goalatlas/ai-value-realiser`

### Key Files

| File | Purpose |
|------|---------|
| `case_library/schemas/models.py` | Pydantic models implementing this spec |
| `case_library/ontology/ontology_v1.0.yaml` | Ontology definition with corpus statistics |
| `docs/specs/AI_CASE_LIBRARY_SPECIFICATION_v1_5.md` | This document |

---

## Appendix E: Field Requirements

This appendix defines which fields are required vs optional for each schema. **Required** fields must be present for a case to pass validation. **Optional** fields improve matching quality but their absence doesn't block processing.

### E.1 Value Claim Fields

| Field | Required | Default | Notes |
|-------|----------|---------|-------|
| `id` | ✅ Yes | — | Auto-generated: `VC-{NNN}` |
| `claim_title` | ✅ Yes | — | Short description, ≤100 chars |
| `claim_description` | ✅ Yes | — | Full description |
| `source_ids` | ✅ Yes | — | At least one source reference |
| `source_quote` | ✅ Yes | — | Verbatim or near-verbatim from source |
| `quote_location` | ✅ Yes | — | Human-readable location in source |
| `ai_attribution` | ✅ Yes | — | `direct` \| `contributing` \| `contextual` |
| `attribution_evidence` | ✅ Yes | — | Explanation of attribution assignment |
| `verification_status` | ✅ Yes | `needs_review` | Set by verification step |
| `evidence_level` | ✅ Yes | — | `outcome` \| `adoption` \| `method` (see §3.2.1) |
| `evidence_grade` | ✅ Yes | — | `primary` \| `secondary_high` \| `secondary_low` |
| `application_type` | ✅ Yes | — | `capability_enhancement` \| `capability_creation` |
| `mechanism` | ✅ Yes | — | 1-2 values from ontology |
| `outcome` | ✅ Yes | — | 1-4 values from ontology |
| `cognitive_depth` | ✅ Yes | — | Single value from ontology |
| `metric_raw` | ❌ No | `null` | Required for `outcome` and `adoption` level claims |
| `metric_raw.value` | If parent | — | Original string from source |
| `metric_raw.magnitude` | ❌ No | `null` | Parsed numeric value |
| `metric_raw.currency` | ❌ No | `null` | If monetary |
| `metric_raw.timeframe` | ❌ No | `null` | If time-bounded |
| `metric_raw.metric_type` | If parent | — | `absolute_value` \| `percentage` \| `ratio` \| `count` |
| `metric_classification` | ❌ No | `null` | Derived from metric_raw if present |
| `ontology_version` | ✅ Yes | `"1.0"` | Version used for tagging |
| `ontology_confidence` | ❌ No | `null` | AI confidence scores if AI-tagged |
| `human_validation` | ❌ No | `null` | Populated during Tier 1 review |
| `human_validation.reviewed` | If parent | `false` | — |
| `human_validation.reviewer_verdict` | If reviewed | — | `valid` \| `invalid` \| `unclear` |

### E.2 Context Claim Fields

| Field | Required | Default | Notes |
|-------|----------|---------|-------|
| `id` | ✅ Yes | — | Auto-generated: `CC-{NNN}` |
| `context_type` | ✅ Yes | — | See §3.3 for valid types |
| `claim_title` | ✅ Yes | — | Short description |
| `claim_description` | ❌ No | `null` | Extended description if needed |
| `source_ids` | ✅ Yes | — | At least one, unless `inferred` |
| `source_quote` | ❌ No | `null` | Not required for inferred claims |
| `verification_status` | ✅ Yes | `unverified` | `verified` \| `unverified` \| `inferred` |
| `verification_confidence` | ❌ No | `null` | `high` \| `medium` \| `low` |
| `inferred_from` | If inferred | — | Explanation of inference |
| `apqc_code` | If functional | — | Required for `functional` type |
| `apqc_name` | If functional | — | Required for `functional` type |
| `human_validation` | ❌ No | `null` | Populated during review |

### E.3 Source Fields

| Field | Required | Default | Notes |
|-------|----------|---------|-------|
| `id` | ✅ Yes | — | `S1`, `S2`, etc. |
| `title` | ✅ Yes | — | Document/page title |
| `url` | ✅ Yes | — | Original URL |
| `type` | ✅ Yes | — | `primary` \| `secondary` |
| `origin` | ✅ Yes | — | `first_party` \| `second_party` \| `third_party` (see §4.1) |
| `grade` | ✅ Yes | — | See §4 for grading |
| `raw_file` | ✅ Yes | — | Path to captured source: `sources/raw/S1_*.pdf` |
| `text_file` | ✅ Yes | — | Path to extracted text: `sources/text/S1_*.txt` |
| `extraction_method` | ✅ Yes | — | `pypdf` \| `trafilatura` \| `tesseract_ocr` |
| `extraction_quality` | ✅ Yes | `high` | `high` \| `medium` \| `low` |
| `is_multi_page` | ✅ Yes | `false` | Set by extraction |
| `related_urls` | ❌ No | `[]` | If multi-page detected |

### E.4 Casefile Top-Level Fields

| Field | Required | Default | Notes |
|-------|----------|---------|-------|
| `case_id` | ✅ Yes | — | See §5.5 for conventions |
| `organisation` | ✅ Yes | — | Full organisation name |
| `title` | ✅ Yes | — | Case title |
| `date_created` | ✅ Yes | — | ISO date |
| `date_updated` | ✅ Yes | — | ISO date |
| `sources` | ✅ Yes | — | At least one source |
| `value_claims` | ✅ Yes | — | At least one value claim |
| `context_claims` | ❌ No | `[]` | May be empty |
| `evidence_level` | ✅ Yes | — | Highest level among claims: `outcome` \| `adoption` \| `method` |
| `verification_summary` | ✅ Yes | — | Auto-generated from claims |
| `human_validation_summary` | ❌ No | `null` | Populated after Tier 1 |
| `status` | ✅ Yes | `in_progress` | `complete` \| `needs_review` \| `in_progress` |
| `confidence` | ❌ No | `null` | Overall case confidence |
| `review_flags` | ❌ No | `[]` | Issues requiring attention |
| `ontology_metadata` | ✅ Yes | — | Version tracking |

**Note:** The case-level `evidence_level` is automatically derived as the highest evidence level present among verified value claims. It determines which filtering modes surface this case.

### E.5 Minimum Viable Case

A case passes validation with:

1. **One source** — captured content available in `sources/`
2. **One value claim** — with all required fields populated
3. **Verification complete** — at least one `verified` value claim
4. **Status set** — even if `needs_review`

Context claims, metrics, human validation, and confidence scores improve quality but are not required for a case to exist in the library.

---

*This specification is finalised and implemented. Changes should follow semantic versioning.*

