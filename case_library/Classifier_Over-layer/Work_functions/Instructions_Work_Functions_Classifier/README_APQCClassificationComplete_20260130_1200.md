# APQC Work Function Classification - Complete Package

**README_APQCClassificationComplete_20260130_1200.md**

---

## Overview

This package provides a complete, battle-tested solution for classifying AI case library claims by work function using the APQC Process Classification Framework. It incorporates lessons learned from fixing **231 misclassifications** (10.74% error rate) in the first build.

### What's Included

| Component | File | Purpose |
|-----------|------|---------|
| **Classification Prompt** | `apqc_classification_prompt.md` | Comprehensive system prompt with decision tree and trap checks |
| **Pydantic Schemas** | `apqc_classification_schemas.py` | Structured output with validation |
| **Validation Script** | `validate_apqc_classification.py` | Post-classification validation using keyword detection |
| **Semantic Audit** | `audit_apqc_semantic.py` | Ongoing monitoring for classification drift |
| **Fix Script** | `fix_apqc_misclassifications.py` | Remediation with dry-run support |
| **Classification Runner** | `classify_claims.py` | Integrated pipeline with API calls + validation |
| **Taxonomy** | `apqc_taxonomy.json` | APQC PCF v7.4 hierarchy (13 categories, 72 process groups) |

---

## The Problem This Solves

### Original Error Rate: 10.74%

The first build of the case library had significant misclassification issues:

| Pattern | Count | Description |
|---------|-------|-------------|
| HR → Finance (7.x → 9.x) | ~80 | Cost savings in HR claims triggered finance codes |
| Product Dev → Manufacturing (2.x → 4.x) | ~60 | Design work tagged as production |
| Manufacturing → Product Dev (4.x → 2.x) | ~40 | Production tagged as design |
| Customer Service → IT (6.x → 8.x) | ~30 | Chatbots tagged as IT, not customer service |
| Risk → Finance (11.x → 9.x) | ~20 | Fraud detection tagged as finance |

### Root Cause

The classifier was tagging based on **keywords** rather than **business function**:
- "Cost savings" → Finance (wrong if HR is doing the work)
- "AI chatbot" → IT (wrong if customer service is the function)
- "Quality inspection" → ambiguous between design and manufacturing

---

## The Solution: Defense in Depth

```
┌─────────────────────────────────────────────────────────────────┐
│                    CLASSIFICATION PIPELINE                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. PROMPT (Prevention)                                          │
│     ├── Decision Tree: Step-by-step classification process       │
│     ├── Trap Checks: Explicit verification of common mistakes    │
│     ├── 8 Worked Examples: Cover all major error patterns        │
│     └── Pattern Warnings: "HR with cost mention ≠ Finance"       │
│                                                                  │
│  2. STRUCTURED OUTPUT (Enforcement)                              │
│     ├── Pydantic schemas with validation                         │
│     ├── trap_check field required in every response              │
│     └── Confidence levels flag uncertain classifications         │
│                                                                  │
│  3. POST-CLASSIFICATION VALIDATION (Detection)                   │
│     ├── Keyword detection cross-checks assigned code             │
│     ├── Known misclassification patterns flagged                 │
│     └── Warnings added to results before saving                  │
│                                                                  │
│  4. SEMANTIC AUDIT (Monitoring)                                  │
│     ├── Regular audits catch drift over time                     │
│     ├── Pattern analysis identifies new error types              │
│     └── Trend comparison shows improvement/degradation           │
│                                                                  │
│  5. FIX SCRIPT (Remediation)                                     │
│     ├── Dry-run mode previews changes                            │
│     ├── Automatic backup before modification                     │
│     └── Audit trail of all fixes applied                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Quick Start

### 1. Basic Classification

```python
from classify_claims import APQCClassifier, ClaimInput

# Initialize
classifier = APQCClassifier()

# Classify a claim
claim = ClaimInput(
    claim_id="CLM-001",
    claim_text="AI-powered recruitment reduced time-to-hire by 40%",
    mechanism="NLP resume screening",
    outcome="Faster hiring, cost savings",
    case_title="HR Transformation",
    organisation_name="Acme Corp"
)

result = classifier.classify_claim(claim)

print(f"Category: {result.classification.category_id}")  # 7.0
print(f"Process Group: {result.classification.process_group_id}")  # 7.2
print(f"Confidence: {result.classification.confidence}")  # high
print(f"Validation passed: {result.validation_passed}")  # True
```

### 2. Batch Processing

```python
claims = [ClaimInput(...), ClaimInput(...), ...]

results = classifier.classify_batch(
    claims,
    progress_callback=lambda i, n: print(f"Processing {i}/{n}")
)

print(f"Classified: {results.total_claims}")
print(f"Process group level: {results.process_group_level_count}")
print(f"Needs review: {results.needs_review_count}")
print(f"Cost: {classifier.get_cost_summary()}")
```

### 3. Validation Only (Existing Classifications)

```bash
python validate_apqc_classification.py
```

### 4. Semantic Audit

```bash
python audit_apqc_semantic.py --cases-dir cases_enriched --output audit_report.json
```

### 5. Fix Misclassifications

```bash
# Preview fixes
python fix_apqc_misclassifications.py --dry-run

# Apply fixes
python fix_apqc_misclassifications.py --apply
```

---

## The Five Traps (and How We Prevent Them)

### Trap 1: HR → Finance (Cost Language Trap)

**Pattern:** HR claims mention "cost savings" → incorrectly tagged 9.x

```
❌ "AI recruitment cut hiring costs by $2M" → 9.1 (Finance)
✅ "AI recruitment cut hiring costs by $2M" → 7.2 (HR)
```

**Prevention:**
- Prompt explicitly warns about this pattern
- Keyword detection flags HR keywords + finance codes
- Example in prompt shows correct handling

### Trap 2: Product Dev ↔ Manufacturing

**Pattern:** Confusing design (BEFORE production) with manufacturing (DURING production)

```
❌ "Generative design created 1000 iterations" → 4.3 (Manufacturing)
✅ "Generative design created 1000 iterations" → 2.3 (Product Dev)

❌ "Computer vision inspects parts on assembly line" → 2.3 (Product Dev)
✅ "Computer vision inspects parts on assembly line" → 4.3 (Manufacturing)
```

**Prevention:**
- Decision tree asks "Is this DESIGN or PRODUCTION?"
- Keywords distinguished: "design", "R&D", "prototype" vs "assembly", "factory", "production line"
- trap_check requires explicit verification

### Trap 3: Everything → IT (Technology Trap)

**Pattern:** AI/ML involvement → incorrectly tagged 8.x

```
❌ "NLP chatbot handles customer queries" → 8.7 (IT)
✅ "NLP chatbot handles customer queries" → 6.2 (Customer Service)
```

**Prevention:**
- Prompt emphasizes: "8.0 is for IT-as-the-business, not IT-as-enabler"
- Decision tree asks: "Is the IT department the beneficiary?"
- Validation flags customer service keywords + IT codes

### Trap 4: Risk → Finance (Money Trap)

**Pattern:** Fraud/risk involves money → incorrectly tagged 9.x

```
❌ "ML fraud detection prevented $50M losses" → 9.2 (Revenue Accounting)
✅ "ML fraud detection prevented $50M losses" → 11.1 (Risk)
```

**Prevention:**
- Risk keywords explicitly separated from finance keywords
- Prompt example shows fraud = risk, not finance
- Validation detects risk keywords + finance codes

### Trap 5: Demand Forecasting Confusion

**Pattern:** Demand forecasting could be marketing (3.x) OR supply chain (4.x)

```
For marketing decisions: 3.1 (Market research)
For inventory decisions: 4.1 (Supply chain planning)
```

**Prevention:**
- Prompt provides explicit guidance on distinguishing
- Context clues: "inventory", "stockout" → supply chain
- Context clues: "market sizing", "pricing" → marketing

---

## Integration with Enrichment Pipeline

### Option 1: Inline Integration

```python
from classify_claims import APQCClassifier, integrate_with_enrichment_pipeline

# In your enrichment script:
classifier = APQCClassifier()

# After generating audit data:
audit_data, warnings = integrate_with_enrichment_pipeline(
    audit_data,
    classifier,
    update_existing=False  # Only classify new claims
)

if warnings:
    logger.warning(f"Classification warnings: {warnings}")
```

### Option 2: Validation-Only Integration

```python
from validate_apqc_classification import validate_apqc_classification, load_apqc_reference

apqc_lookup = load_apqc_reference()

# After classification (however it's done):
for claim in audit_data['audited_claims']:
    for apqc in claim.get('apqc_functions', []):
        result = validate_apqc_classification(
            apqc_code=apqc['id'],
            apqc_name=apqc['name'],
            claim_text=claim.get('strategic_fit_assessment', ''),
            apqc_lookup=apqc_lookup
        )
        if result.errors:
            logger.error(f"Claim {claim['claim_id']}: {result.errors}")
        if result.warnings:
            logger.warning(f"Claim {claim['claim_id']}: {result.warnings}")
```

---

## Monitoring & Quality Metrics

### Target Metrics

| Metric | Initial | Target | How to Achieve |
|--------|---------|--------|----------------|
| Mismatch rate | 10.74% | <2% | Use this package |
| Needs-review rate | Unknown | <5% | Confidence-based flagging |
| High-confidence rate | Unknown | >80% | Better prompting |

### Regular Audit Schedule

```bash
# After each batch of new cases
python audit_apqc_semantic.py --output audit_$(date +%Y%m%d).json

# Compare with previous
python audit_apqc_semantic.py --compare audit_previous.json
```

### Trend Tracking

The audit script tracks:
- Mismatch rate over time
- New error patterns
- Categories with most issues
- Cases needing attention

---

## Cost Estimation

| Scenario | Input Tokens | Output Tokens | Cost (Sonnet) |
|----------|--------------|---------------|---------------|
| Single claim | ~12,500 | ~300 | ~$0.04 |
| 100 claims | ~1.25M | ~30K | ~$4.20 |
| 1,400 claims | ~17.5M | ~420K | ~$59 |

### Cost Optimization

1. **Prompt Caching**: If available, reduces taxonomy cost (~12K tokens) significantly
2. **Batch Processing**: Process 5-10 claims per call to amortize taxonomy cost
3. **Validation Pre-filter**: Only send ambiguous claims to API, use heuristics for clear cases

---

## File Dependencies

```
apqc-classification-complete/
├── apqc_taxonomy.json                    # Required by all scripts
├── apqc_classification_schemas.py        # Required by classify_claims.py
├── validate_apqc_classification.py       # Required by classify_claims.py, audit, fix
├── apqc_classification_prompt.md         # Required by classify_claims.py
├── classify_claims.py                    # Main classification runner
├── audit_apqc_semantic.py                # Standalone audit tool
├── fix_apqc_misclassifications.py        # Standalone fix tool
└── README_APQCClassificationComplete_*.md
```

### External Dependencies

```
anthropic>=0.18.0   # For API calls (classify_claims.py only)
pydantic>=2.0.0     # For schemas
```

---

## Differences from Previous Implementation

| Aspect | v1 (Original) | v2 (This Package) |
|--------|---------------|-------------------|
| Misclassification prevention | None | Decision tree + trap checks in prompt |
| Post-classification validation | None | Keyword-based validation |
| Structured output | Basic | Full Pydantic with trap_check field |
| Confidence tracking | Implicit | Explicit levels, low flags for review |
| Audit capability | Manual | Automated with pattern detection |
| Fix capability | Manual | Dry-run + automated fix script |
| Cost tracking | None | Built-in cost tracker |
| Documentation | Minimal | 8 worked examples, decision tree |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0 | 2026-01-30 | Complete rewrite incorporating 231 fix learnings |
| 1.0 | 2026-01-xx | Original implementation (10.74% error rate) |

---

## Files in This Package

```
Total: 7 files, ~150KB

apqc_classification_prompt.md       14KB   System prompt with decision tree
apqc_classification_schemas.py       7KB   Pydantic schemas with trap_check
apqc_taxonomy.json                  49KB   APQC PCF v7.4 hierarchy
validate_apqc_classification.py     12KB   Keyword-based validation
audit_apqc_semantic.py              10KB   Semantic audit tool
fix_apqc_misclassifications.py      12KB   Fix script with dry-run
classify_claims.py                  12KB   Integrated classification runner
README_*.md                          9KB   This documentation
```
