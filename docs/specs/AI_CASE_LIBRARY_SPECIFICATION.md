# AI Case Library Specification (Draft)

**Version:** 0.3 (Draft)  
**Date:** 2026-01-19  
**Status:** Ontology finalised; ready for implementation planning

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 0.1 | 2026-01-19 | Initial draft, awaiting ontology discovery results |
| 0.2 | 2026-01-19 | Added: Value Attribution (§3.5), Multi-Page Extraction (§6.3), Human Validation (§7) |
| 0.3 | 2026-01-19 | Finalised ontology v1.0 based on discovery pipeline results (1,440 claims analysed). Added `business_growth` outcome. Split `generative_autonomous` into `generative` + `autonomous`. Removed `innovation` from OUTCOME. Added corpus statistics and co-occurrence patterns. |

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
- Cases that provide either:
  - **Outcome Validation** — quantified evidence of value realised
  - **Method Validation** — qualitative evidence of approach/architecture

### 1.5 Out of Scope

- Cases where AI is incidental (not a key driver)
- Cases with neither outcome nor method validation

---

## 2. Two-Axis Classification Model

Cases and claims are classified on two orthogonal axes:

### 2.1 Axis 1: Application Type

*What kind of change does this represent?*

| Value | Definition | Examples |
|-------|------------|----------|
| **Capability Enhancement** | Optimises existing business functions | Process automation, predictive maintenance, customer service optimisation |
| **Capability Creation** | Creates new capabilities, business models, or revenue streams | New product lines, platform businesses, market entry |

### 2.2 Axis 2: Evidence Type

*What kind of proof do we have?*

| Value | Definition | Examples |
|-------|------------|----------|
| **Outcome Validation** | Quantitative evidence of realised impact | "SGD 1 billion value created", "40% cost reduction" |
| **Method Validation** | Qualitative evidence of approach or operating model | "Three-layer structure", "Bottom-up innovation engine" |

### 2.3 The 2×2 Matrix

|  | **Outcome Validation** | **Method Validation** |
|--|------------------------|----------------------|
| **Capability Enhancement** | Hard proof of optimisation gains | Blueprint for how to optimise |
| **Capability Creation** | Hard proof of new value streams | Blueprint for transformation |

A single case may have claims in multiple quadrants.

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
    evidence_type: "outcome_validation"  # outcome_validation | method_validation
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
| **Strict** | ✅ Include | ⚠️ Include with flag | ❌ Reclassify as Context Claim |
| **Standard** | ✅ Include | ✅ Include | ❌ Reclassify as Context Claim |
| **Exploratory** | ✅ Include | ✅ Include | ✅ Include with `ⓘ contextual` indicator |

**Note:** Claims with `contextual` attribution should be considered for reclassification as Context Claims (type: `strategic_intent`) rather than Value Claims, since they describe organisational direction rather than AI-generated value.

---

## 4. Evidence Grading Standards

### 4.1 Primary Sources

Direct authority on the case:

| Source Type | Examples |
|-------------|----------|
| Organisation itself | Company blog, press release, annual report |
| Major consultancy | McKinsey, BCG, Bain, Deloitte, PwC, Accenture |
| Technology provider | AWS, Microsoft, Google, Nvidia, Anthropic |
| Academic/Governmental | Harvard, MIT, Stanford, World Economic Forum, government reports |

### 4.2 Secondary Sources

No first-hand knowledge, graded by reputation:

| Grade | Indicators |
|-------|------------|
| **secondary_high** | Established consultant, published author, significant LinkedIn/Substack following, recognised analyst |
| **secondary_low** | No obvious reputation markers, aggregator sites, content farms |

---

## 5. File Structure

### 5.1 Case Folder Structure

```
cases/
└── {case-id}/
    ├── casefile.md          # THE PRODUCT — single source of truth
    ├── sources/             # Extracted content (for verification)
    │   ├── S1.md
    │   ├── S2.md
    │   └── ...
    └── build.json           # Pipeline provenance log
```

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
    grade: "organisation_itself"
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

### 5.3 sources/S1.md — Extracted Content

```yaml
---
source_id: S1
source_url: https://www.dbs.com/annual-report-2024
fetch_timestamp: "2026-01-19T14:30:00Z"
fetch_status: success
extraction_method: trafilatura
content_length: 4832

# === MULTI-PAGE METADATA ===
is_multi_page: false
multi_page_detection:
  patterns_found: []
  related_urls_detected: []
  related_urls_followed: []
  detection_method: null
---

# Extracted Content

[Full extracted text...]
```

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

---

## 6. Provenance Pipeline

### 6.1 Pipeline Overview

```
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
| **Extraction Chain** | PDF: pypdf / HTML: trafilatura → BeautifulSoup → raw text |
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

**Detection Algorithm:**

```python
def detect_multi_page(content: str, base_url: str) -> MultiPageResult:
    """
    Returns:
      - is_candidate: bool
      - patterns_found: List[str]  # Which pattern types matched
      - related_urls: List[RelatedUrl]  # URLs to potentially follow
    """
    patterns_found = []
    related_urls = []
    
    # 1. Check for pagination indicators
    if has_pagination_pattern(content):
        patterns_found.append("pagination")
        related_urls.extend(extract_pagination_links(content, base_url))
    
    # 2. Check for chapter/part structure
    if has_chapter_pattern(content):
        patterns_found.append("chapter_structure")
        related_urls.extend(extract_chapter_links(content, base_url))
    
    # 3. Check for series indicators
    if has_series_pattern(content):
        patterns_found.append("series")
        related_urls.extend(extract_series_links(content, base_url))
    
    # 4. Check for similar URL patterns (same-domain only)
    similar_links = find_similar_url_patterns(content, base_url)
    if similar_links:
        patterns_found.append("url_structure")
        related_urls.extend(similar_links)
    
    return MultiPageResult(
        is_candidate=len(patterns_found) > 0,
        patterns_found=patterns_found,
        related_urls=deduplicate(related_urls)
    )
```

**Related URL Schema:**

```yaml
related_urls:
  - url: "https://example.com/report/part-2"
    relationship: "continuation"  # continuation | chapter | related | pagination
    pattern_matched: "series"
    confidence: "high"  # high | medium | low
    followed: false  # Updated after human decision
    follow_reason: null  # If followed, why
```

**Processing Options:**

| Approach | When to Use | Implementation |
|----------|-------------|----------------|
| **Flag only** | Default for AI case studies | Mark `is_multi_page: true`, list URLs, continue without following |
| **Auto-follow (depth 1)** | Pagination only, high confidence | Follow paginated links automatically, max 5 additional pages |
| **Human confirm** | Chapter structure, series | Present detected URLs to human, follow only confirmed |

**Default Behaviour:**

1. Run detection on all extracted content
2. If patterns found:
   - Set `is_multi_page: true` in source metadata
   - Log detected URLs and patterns in `build.json`
   - For **pagination** patterns with high confidence: auto-follow (depth 1, max 5 pages)
   - For all other patterns: flag for human review, do not auto-follow
3. Continue pipeline with available content
4. Human reviewer decides whether to trigger re-extraction with additional URLs

**Human Review Interface:**

```
┌─────────────────────────────────────────────────────────────────┐
│ Multi-Page Content Detected                                     │
│ ─────────────────────────────────────────────────────────────── │
│ Source: https://example.com/ai-transformation-report            │
│ Pattern: chapter_structure                                      │
│ ─────────────────────────────────────────────────────────────── │
│ Related URLs detected:                                          │
│                                                                 │
│ ☐ https://example.com/ai-transformation-report/chapter-2        │
│   Relationship: chapter | Confidence: high                      │
│                                                                 │
│ ☐ https://example.com/ai-transformation-report/chapter-3        │
│   Relationship: chapter | Confidence: high                      │
│                                                                 │
│ ☐ https://example.com/related-case-study                        │
│   Relationship: related | Confidence: low                       │
│                                                                 │
│ [Follow Selected]  [Skip All]  [Flag for Later]                 │
└─────────────────────────────────────────────────────────────────┘
```

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

**Claim Extraction Prompt (excerpt):**

```
For each VALUE CLAIM, you must assess the AI attribution level:

- DIRECT: The source explicitly states AI/ML/automation caused this outcome.
  Example: "Our AI chatbot reduced call volume by 40%"
  
- CONTRIBUTING: AI is mentioned as one factor among others, or language hedges causality.
  Example: "AI and process improvements drove efficiency gains"
  
- CONTEXTUAL: An organisational goal or target that AI work relates to, but no causal link is stated.
  Example: "We target 20% margin improvement by 2030"
  
Provide attribution_evidence explaining your reasoning.
```

### 6.5 Step 4: Verification & Categorisation [AI]

| Aspect | Specification |
|--------|---------------|
| **Input** | Claims from Step 3 + Original URLs |
| **Action** | Verify quotes at source, assign ontology categories |
| **Verification** | Fetch original URL, search for quote (±10% fuzzy match) |
| **Categorisation** | Assign application_type, evidence_type, mechanism, outcome, cognitive_depth |
| **Attribution Check** | Verify ai_attribution assignment is consistent with source language |
| **Evidence Grade** | Derive from source metadata (primary/secondary) |
| **Output** | Populated casefile.md with complete YAML frontmatter |
| **Unit Test** | All claims have verification_status, all value claims have ontology tags and ai_attribution |
| **Retry** | URL fetch fail → use .md fallback, mark "verified against extraction only" |
| **Failure** | Zero verified value claims → NEEDS_REVIEW |
| **AI Boundary** | Log: verification attempts, categorisation rationale, confidence, model |

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

**Interface:**

```
┌─────────────────────────────────────────────────────────────────┐
│ Claim Review: DBS Bank AI Customer Service                      │
│ ─────────────────────────────────────────────────────────────── │
│ Source: DBS Annual Report 2024 (Page 23)                        │
│ ─────────────────────────────────────────────────────────────── │
│ "Our AI initiatives have delivered SGD 1 billion in value       │
│ through improved customer service efficiency and reduced        │
│ operational costs across our retail banking division."          │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│ AI Extracted Claim:                                             │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │ "SGD 1 billion value created through AI"                    │ │
│ │ Attribution: DIRECT                                         │ │
│ │ Evidence Type: outcome_validation                           │ │
│ └─────────────────────────────────────────────────────────────┘ │
│                                                                 │
│ Claim accurate?     [✓ Valid]  [✗ Invalid]  [? Unclear]        │
│ Attribution correct? [✓ Yes]   [✗ No → ___________]            │
│                                                                 │
│ Notes: _________________________________________________        │
│                                                                 │
│ ─────────────────────────────────────────────────────────────── │
│ Claim AI missed? [+ Add claim]                                  │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│ [← Previous Claim]  [Next Claim →]  [Complete Review]           │
└─────────────────────────────────────────────────────────────────┘
```

**Output:**

```yaml
human_validation:
  reviewed: true
  reviewer_verdict: "valid"  # valid | invalid | unclear
  attribution_correct: true
  attribution_override: null  # If incorrect, what should it be?
  missed_claim: false
  review_notes: null
  review_date: "2026-01-19"
  reviewer_id: "MB"
```

**Workflow:**

1. Pipeline completes Steps 1-4 automatically
2. Case enters human validation queue
3. Reviewer completes Tier 1 review
4. If issues found:
   - Invalid claims → mark `verification_status: rejected`
   - Unclear claims → mark `verification_status: needs_review`
   - Missed claims → add with `extraction_method: human`
   - Attribution errors → update `ai_attribution` field
5. Case status updated to `complete` or `needs_review`

### 7.4 Tier 2: Blind Extraction (10% Sample)

**Purpose:** Measure AI extraction quality without reviewer bias.

**Process:**

1. Randomly select 10% of cases for Tier 2
2. Human extracts claims independently (does NOT see AI output first)
3. Human completes extraction using same schema as AI
4. System compares human vs AI extractions
5. Calculate precision and recall

**Comparison Logic:**

```python
def compare_extractions(ai_claims: List[Claim], human_claims: List[Claim]) -> ExtractionMetrics:
    """
    Match claims using fuzzy title/quote matching (≥80% similarity).
    """
    matched_ai = set()
    matched_human = set()
    
    for ai_claim in ai_claims:
        for human_claim in human_claims:
            if claims_match(ai_claim, human_claim):
                matched_ai.add(ai_claim.id)
                matched_human.add(human_claim.id)
    
    # Precision: What % of AI claims were correct?
    precision = len(matched_ai) / len(ai_claims) if ai_claims else 0
    
    # Recall: What % of human claims did AI find?
    recall = len(matched_human) / len(human_claims) if human_claims else 0
    
    # Missed claims: Human found, AI missed
    missed = [c for c in human_claims if c.id not in matched_human]
    
    # False positives: AI found, human didn't
    false_positives = [c for c in ai_claims if c.id not in matched_ai]
    
    return ExtractionMetrics(
        precision=precision,
        recall=recall,
        missed_claims=missed,
        false_positives=false_positives
    )
```

**Metrics:**

| Metric | Definition | Target |
|--------|------------|--------|
| **AI Precision** | Matched AI claims / Total AI claims | ≥90% |
| **AI Recall** | Matched human claims / Total human claims | ≥85% |
| **Attribution Accuracy** | AI attribution matches human / Total matched | ≥85% |

**Output:**

```yaml
human_validation_summary:
  validation_tier: "tier_2_blind"
  review_date: "2026-01-19"
  reviewer_id: "MB"
  blind_extraction:
    human_claims_count: 6
    ai_claims_count: 5
    matched_count: 4
    precision_score: 0.80  # 4/5
    recall_score: 0.67     # 4/6
    missed_claims: ["Human found claim about implementation timeline"]
    false_positives: ["AI extracted contextual goal as value claim"]
```

### 7.5 Tier 3: Inter-Rater Calibration (Monthly)

**Purpose:** Establish reliable human baseline and calibrate reviewers.

**Process:**

1. Select 3-5 cases for calibration exercise
2. Two humans independently extract claims (both blind)
3. Calculate inter-rater agreement (Cohen's kappa)
4. Discuss disagreements to align on standards
5. Update extraction guidelines based on findings

**Agreement Calculation:**

```python
def cohens_kappa(rater1_claims: List[Claim], rater2_claims: List[Claim]) -> float:
    """
    Calculate inter-rater reliability for claim extraction.
    
    Treats extraction as a classification task:
    - For each potential claim (union of both raters' claims)
    - Did rater agree it should be extracted?
    """
    # ... implementation
    return kappa_score
```

**Targets:**

| Metric | Definition | Target |
|--------|------------|--------|
| **Inter-Rater Kappa** | Agreement beyond chance | ≥0.70 (substantial) |
| **Attribution Agreement** | Same ai_attribution level | ≥0.75 |

**Output:**

Calibration report documenting:
- Cases used
- Per-rater claim counts
- Kappa scores
- Disagreement analysis
- Guidelines updates

### 7.6 Validation Queue Management

**Queue Priorities:**

| Priority | Condition |
|----------|-----------|
| **High** | Cases with 0 verified value claims |
| **Medium** | Cases flagged by pipeline (NEEDS_REVIEW) |
| **Normal** | Standard cases awaiting Tier 1 |
| **Sample** | Cases selected for Tier 2 blind extraction |

**Workflow States:**

```
[Pipeline Complete] 
    → [Awaiting Tier 1] 
    → [Tier 1 In Progress] 
    → [Tier 1 Complete]
    → [Complete] or [Needs Rework]

For 10% sample:
[Tier 1 Complete] 
    → [Awaiting Tier 2] 
    → [Tier 2 In Progress] 
    → [Tier 2 Complete]
```

### 7.7 Quality Metrics Dashboard

Track aggregate metrics across all cases:

| Metric | Calculation | Target | Alert Threshold |
|--------|-------------|--------|-----------------|
| **Tier 1 Pass Rate** | Cases valid / Cases reviewed | ≥85% | <75% |
| **Tier 2 Precision** | Rolling average | ≥90% | <85% |
| **Tier 2 Recall** | Rolling average | ≥85% | <80% |
| **Review Backlog** | Cases awaiting Tier 1 | <20 | >50 |
| **Time per Review** | Median Tier 1 time | ≤15 min | >25 min |

If metrics fall below alert thresholds:
- Investigate systematic issues
- Consider prompt refinement for AI steps
- Schedule Tier 3 calibration
- Update extraction guidelines

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

### 8.3 UI Indicators

| Location | Verified | Unverified/Unclear | Attribution: Contextual |
|----------|----------|--------------------|-----------------------|
| **Card (list)** | Shown | Not shown | Not shown |
| **Modal (detail)** | Shown | Shown with `⚠ NEEDS REVIEW` | Shown with `ⓘ contextual` |
| **Match results** | Included | Excluded or warned | Excluded (Strict) or flagged |

---

## 9. Evidence Filtering for Matching

### 9.1 Three Evidence Modes

| Mode | Value Claims | Context Claims | Attribution | Use Case |
|------|--------------|----------------|-------------|----------|
| **Strict** | Verified only | Verified only | Direct only | Commit stage — business cases |
| **Standard** (default) | Verified only | Any | Direct + Contributing | Explore stage — understanding options |
| **Exploratory** | Any | Any | All | Scope stage — broad discovery |

### 9.2 Alignment with Value Realisation Stages

| Stage | Recommended Mode | Rationale |
|-------|------------------|-----------|
| **Scope** | Exploratory | Cast wide net |
| **Explore** | Standard | Focus on credible cases |
| **Commit** | Strict | Bulletproof evidence for business case |
| **Adopt** | Standard | Implementation guidance |

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

| Term | Definition | Indicators | Corpus Count | Avg Confidence |
|------|------------|------------|--------------|----------------|
| **automation** | AI performs tasks previously done by humans, reducing manual effort | handles, processes, executes, replaces manual | 377 (28%) | 0.87 |
| **augmentation** | AI enhances human capabilities without replacing the human | assists, supports, helps, enhances, empowers | 360 (26%) | 0.84 |
| **optimization** | AI finds better solutions within existing constraints | improves, optimises, reduces waste, increases efficiency | 429 (31%) | 0.83 |
| **innovation** | AI enables fundamentally new products, services, or business models | new product, new capability, novel approach, first-of-kind | 191 (14%) | 0.81 |

**Usage Notes:**
- Most claims have a single mechanism
- `automation` + `augmentation` rarely co-occur (verify if both claimed)
- `optimization` is most common — be precise about whether it's truly optimisation vs automation

### 10.3 OUTCOME Dimension

*What business result does the AI produce?*

| Term | Definition | Metric Patterns | Corpus Count | Avg Confidence |
|------|------------|-----------------|--------------|----------------|
| **velocity** | Acceleration of time to deliver value | X% faster, reduced from X to Y, X hours saved | 524 (30%) | 0.87 |
| **experience** | Improved quality of interaction for customers/employees | satisfaction score, NPS, engagement rate | 409 (23%) | 0.85 |
| **cost_reduction** | Operational efficiency gains reducing what you spend | X% reduction in costs, £/$/€ X saved | 317 (18%) | 0.86 |
| **revenue_lift** | Direct increase in revenue or monetisation | X% increase in sales, £/$/€ X additional revenue | 304 (17%) | 0.85 |
| **risk_avoidance** | Prevention or mitigation of potential losses | X% reduction in fraud, £/$/€ X losses prevented, X% fewer errors | 141 (8%) | 0.86 |
| **cost_erosion** | Competitive pressure reducing what you can charge (external) | pricing pressure, margin compression, competitive pricing | 47 (3%) | 0.88 |
| **business_growth** | Organisational scale expansion (customers, market share, valuation) | X customers acquired, X% market share, unicorn status | NEW | — |

**Usage Notes:**
- `velocity` is most common outcome — AI frequently speeds things up
- `cost_reduction` (internal efficiency) vs `cost_erosion` (external pricing pressure) are distinct
- `business_growth` captures scale expansion that isn't directly cost/revenue (e.g., "reached 1.6M customers")
- Claims can have multiple outcomes (e.g., `velocity` + `cost_reduction`)

**Removed:** `innovation` was previously listed as an OUTCOME but belongs only in MECHANISM. Claims about "new capabilities" should use `business_growth` or `revenue_lift` for outcome.

### 10.4 COGNITIVE_DEPTH Dimension

*What level of AI sophistication is demonstrated?*

| Term | Definition | Indicators | Corpus Count | Avg Confidence |
|------|------------|------------|--------------|----------------|
| **descriptive** | What happened? Reporting and summarisation | summarises, reports, dashboards, aggregates data, shows trends | 379 (27%) | 0.76 |
| **diagnostic** | Why did it happen? Root cause analysis | root cause analysis, explains why, identifies drivers, anomaly detection | 83 (6%) | 0.83 |
| **predictive** | What will happen? Forecasting and prediction | predicts, forecasts, anticipates, probability, likelihood | 151 (11%) | 0.84 |
| **prescriptive** | What should we do? Recommendations and decision support | recommends, suggests, advises, next best action | 497 (35%) | 0.77 |
| **generative** | Create this. Content generation (text, code, images, designs) | generates, creates, writes, produces, designs | SPLIT | — |
| **autonomous** | Do this. Takes action without per-instance human direction | handles independently, executes, acts, decides | SPLIT | — |

**Usage Notes:**
- `prescriptive` is most common — many AI systems provide recommendations
- `descriptive` has lower confidence (0.76) — often confused with other levels
- `generative` and `autonomous` were split from the previous `generative_autonomous` term:
  - `generative` = Creates new content (LLMs writing, image generation, code generation)
  - `autonomous` = Takes action without human approval per instance (auto-trading, self-driving)
  - A system can be generative but not autonomous (human reviews AI-written content)
  - A system can be autonomous but not generative (rule-based auto-actions)
  - Some systems are both (AI agent that writes and sends emails)

### 10.5 Co-occurrence Patterns

Common mechanism + outcome combinations (from corpus analysis):

| Pattern | Count | Interpretation |
|---------|-------|----------------|
| automation + velocity | 221 | Automating tasks speeds them up |
| augmentation + experience | 180 | Helping humans improves customer/employee experience |
| optimization + cost_reduction | 167 | Finding efficiencies reduces costs |
| augmentation + velocity | 166 | AI assistance speeds up human work |
| optimization + velocity | 139 | Optimisation often means faster |
| automation + cost_reduction | 122 | Removing manual work cuts costs |
| optimization + revenue_lift | 113 | Better targeting/pricing increases revenue |
| innovation + revenue_lift | 97 | New products generate new revenue |

**Suspicious Combinations (require verification):**

| Combination | Concern |
|-------------|---------|
| automation + augmentation | Usually one or the other — verify claim involves both |
| cost_erosion + revenue_lift | Opposite value drivers — verify claim addresses both |

### 10.6 Ontology Versioning

```yaml
ontology_metadata:
  version: "1.0"
  effective_date: "2026-01-19"
  corpus_validated: 1440
  classification_rate: 0.799
```

**Evolution Rules:**
- Minor version (1.1, 1.2): New examples, clarified definitions, no term changes
- Major version (2.0): New terms added, terms removed, or definitions changed materially
- Claims track which ontology version was used
- When ontology advances, older claims marked `needs_retagging: true`
- Re-tagging is AI-assisted, human-reviewed

### 10.7 Terms Considered But Rejected

| Proposed Term | Dimension | Evidence | Decision | Rationale |
|---------------|-----------|----------|----------|-----------|
| strategic_positioning | outcome | 8 claims | REJECT | Overlaps with `business_growth` and `experience`; many are contextual attribution claims |
| engagement_improvement | outcome | 4 claims | REJECT | Subset of `experience`; insufficient distinct evidence |
| platform_enablement | mechanism | 6 claims | REJECT | Describes architecture, not AI action; use method_validation evidence_type instead |
| contextual | cognitive_depth | 3 claims | REJECT | Feature of many AI systems, not a distinct level; subsume under `prescriptive` |

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
| By Organisation Similarity | context_claims (sector, scale, geography) |

### 11.2 Matching Input (from Profiler)

The Opportunity Analyser receives:
- Sector(s)
- Work functions (APQC codes)
- Products/services
- Strategic priorities
- Size/geography

And matches against Case Library fields to surface relevant cases.

### 11.3 Filtering by Evidence Mode

```python
def filter_cases(cases: List[Case], mode: EvidenceMode) -> List[Case]:
    """
    Filter cases based on evidence mode for matching.
    """
    filtered = []
    for case in cases:
        eligible_claims = []
        
        for claim in case.value_claims:
            # Check verification status
            if mode == "strict" and claim.verification_status != "verified":
                continue
            if mode in ["strict", "standard"] and claim.verification_status == "rejected":
                continue
                
            # Check attribution level
            if mode == "strict" and claim.ai_attribution not in ["direct"]:
                continue
            if mode == "standard" and claim.ai_attribution == "contextual":
                continue
            
            eligible_claims.append(claim)
        
        if eligible_claims:
            filtered.append(case.with_claims(eligible_claims))
    
    return filtered
```

---

## 12. Migration Path

### 12.1 From Current 4-File Structure

| Old File | New Location |
|----------|--------------|
| `1_sources.json` | `casefile.md` YAML + `build.json` |
| `2_claims.json` | `casefile.md` YAML |
| `3_audit.json` | `casefile.md` YAML + `build.json` |
| `4_casefile.md` | Enhanced `casefile.md` |

### 12.2 Migration Steps

1. Parse existing files
2. Map to new schema
3. **Infer ai_attribution** from claim language (AI-assisted, mark as needs_review)
4. **Re-tag ontology** with v1.0 terms (split `generative_autonomous` → `generative` or `autonomous`)
5. Generate `casefile.md` with complete YAML frontmatter
6. Archive original files to `sources/` or `archive/`
7. Generate `build.json` provenance (where possible)
8. Queue all migrated cases for Tier 1 human validation

### 12.3 Attribution Inference for Legacy Cases

For the 202 existing cases, AI will infer attribution level:

```python
def infer_attribution(claim: LegacyClaim) -> Tuple[str, str]:
    """
    Returns (attribution_level, inference_rationale)
    """
    # Check for explicit AI causal language
    if has_direct_ai_causation(claim.quote):
        return ("direct", "Quote explicitly attributes outcome to AI")
    
    # Check for hedged/multi-factor language
    if has_contributing_language(claim.quote):
        return ("contributing", "Quote mentions AI among other factors")
    
    # Check for goal/target language without AI link
    if has_target_language(claim.quote) and not mentions_ai(claim.quote):
        return ("contextual", "Quote describes organisational goal without AI causation")
    
    # Default to needs_review
    return ("needs_review", "Could not confidently determine attribution")
```

### 12.4 Ontology Re-tagging for Legacy Cases

Claims previously tagged with `generative_autonomous` must be re-tagged:

```python
def retag_cognitive_depth(claim: LegacyClaim) -> str:
    """
    Split generative_autonomous into generative or autonomous.
    """
    if claim.cognitive_depth != "generative_autonomous":
        return claim.cognitive_depth
    
    # Check for content generation indicators
    if any(ind in claim.text.lower() for ind in ["generates", "creates", "writes", "produces", "designs"]):
        if any(ind in claim.text.lower() for ind in ["automatically", "without human", "independently"]):
            return "autonomous"  # Both, but autonomous is the primary action
        return "generative"
    
    # Check for autonomous action indicators
    if any(ind in claim.text.lower() for ind in ["handles", "executes", "acts", "decides", "automates"]):
        return "autonomous"
    
    # Default to generative if LLM/content-focused
    return "generative"
```

All inferred attributions and re-tagged ontology terms should be marked for human validation.

---

## 13. Open Items

### 13.1 Decisions Deferred

- APQC classification: Deterministic lookup or AI-assisted?
- Casefile markdown body: AI-generated narrative or templated?
- Build.json structure: Single file or separate step logs?

### 13.2 Not Yet Specified

- Batch processing / orchestration
- Manual case creation workflow
- Viewer implementation details
- Curation viewer for context claims
- Human validation interface implementation

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
| **Evidence Type** | Outcome (quantified) vs Method (qualitative approach) |
| **Mechanism** | How AI creates value (automation, augmentation, optimization, innovation) |
| **Outcome** | Business result (velocity, experience, cost_reduction, revenue_lift, risk_avoidance, cost_erosion, business_growth) |
| **Cognitive Depth** | AI sophistication level (descriptive, diagnostic, predictive, prescriptive, generative, autonomous) |
| **Primary Source** | Direct authority (org itself, major consultancy, etc.) |
| **Secondary Source** | No first-hand knowledge, graded by reputation |
| **Multi-Page Content** | Source material spanning multiple linked web pages |
| **Tier 1 Validation** | Human review of AI-extracted claims (every case) |
| **Tier 2 Validation** | Blind human extraction for precision/recall measurement (10% sample) |
| **Tier 3 Validation** | Inter-rater calibration for baseline reliability (monthly) |

---

## Appendix C: Multi-Page Detection Patterns

### C.1 Pagination Patterns

```regex
# Numeric pagination
Page\s+\d+\s+(of|/)\s+\d+
\bpage[=-]\d+\b

# Navigation text
(Next|Previous|Continue)\s+(page|reading|→|>>)
(Read|See)\s+more\s*→?

# HTML patterns
<a[^>]+href=["'][^"']*[?&]page=\d+
<a[^>]+class=["'][^"']*pagination
```

### C.2 Chapter/Part Patterns

```regex
# Part/Chapter headers
(Part|Chapter|Section)\s+\d+
(Part|Chapter|Section)\s+(One|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten)

# Table of Contents
(Table of Contents|Contents|Index)
^\s*\d+\.\s+[A-Z]

# Navigation
(Previous|Next)\s+(chapter|section|part)
```

### C.3 Series Patterns

```regex
# Explicit series
(Part|Post)\s+\d+\s+of\s+\d+
This is (part|post) \d+
(Read|See|Continue in)\s+part\s+\d+

# Related links
(Related|See also|Continue):?\s*$
(In this series|Series):
```

---

## Appendix D: Ontology Discovery Statistics

**Corpus:** 1,440 claims from 202 cases  
**Analysis Date:** 2026-01-19

### D.1 Classification Results

| Status | Count | Percentage |
|--------|-------|------------|
| Fit well | 1,150 | 79.9% |
| Uncertain | 144 | 10.0% |
| No fit | 146 | 10.1% |
| Error | 0 | 0.0% |

### D.2 Confidence Distribution

| Level | Count | Percentage |
|-------|-------|------------|
| High (≥0.8) | 976 | 67.8% |
| Medium (0.5-0.8) | 341 | 23.7% |
| Low (<0.5) | 123 | 8.5% |

### D.3 Metrics Extraction

- **Claims with metrics:** 868 (60.3%)
- **Most common metric types:** percentage (466), count (201), time (161), currency (154)
- **Currencies detected:** USD (127), EUR (7), GBP (5), SGD (4), others (8)

### D.4 No-Fit Claim Patterns

Common reasons claims didn't fit the ontology:

| Pattern | Example | Recommendation |
|---------|---------|----------------|
| Fundraising claims | "Raised $80M in funding" | Exclude — not AI value |
| Market context | "$400B market opportunity" | Reclassify as Context Claim |
| Environmental facts | "Soil erosion causes $3B losses" | Exclude — problem statement |
| Service discontinuation | "Stopped the AI service" | Exclude — negative outcome |
| Vague strategy | "Enables sustainable practices" | Mark needs_review |

---

*This specification is ready for implementation planning. Ontology v1.0 is finalised.*
