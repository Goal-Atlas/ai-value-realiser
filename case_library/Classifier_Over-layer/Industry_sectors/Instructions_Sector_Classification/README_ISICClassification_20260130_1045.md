# ISIC Industry Classification for AI Case Library

**README_ISICClassification_20260130_1045.md**

---

## Overview

This package provides everything needed to classify AI case studies by industry using the ISIC Rev 5 (International Standard Industrial Classification) taxonomy via Claude API.

The classification follows a two-tier approach:
- **Division-level** (87 categories): When case description provides sufficient detail
- **Section-level** (22 categories): Fallback when industry is mentioned but specifics are unclear

---

## Files Included

| File | Purpose |
|------|---------|
| `isic_taxonomy.json` | Hierarchical JSON taxonomy (22 sections, 87 divisions) |
| `classification_schemas.py` | Pydantic models for structured output validation |
| `classification_prompt.md` | System prompt template with examples |

---

## Quick Start

### 1. Load the Taxonomy

```python
import json

with open('isic_taxonomy.json', 'r') as f:
    taxonomy = json.load(f)

# Taxonomy structure:
# {
#   "C": {
#     "name": "Manufacturing",
#     "divisions": {
#       "C26": {
#         "name": "Manufacture of computer, electronic and optical products",
#         "includes": "Manufacture of electronic components and boards; ..."
#       }
#     }
#   }
# }
```

### 2. Set Up Structured Output

```python
from anthropic import Anthropic
from classification_schemas import ISICClassification

client = Anthropic()

# Build system prompt with taxonomy
system_prompt = f"""You are an industry classification specialist...
## ISIC Rev 5 Taxonomy
{json.dumps(taxonomy, indent=2)}
"""

response = client.messages.create(
    model="claude-sonnet-4-5-20250514",
    max_tokens=1024,
    system=system_prompt,
    messages=[{"role": "user", "content": case_text}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "isic_classification",
            "schema": ISICClassification.model_json_schema()
        }
    }
)

result = ISICClassification.model_validate_json(response.content[0].text)
```

---

## Classification Output Structure

```python
class ISICClassification:
    section_code: str          # "C" (always present)
    section_name: str          # "Manufacturing" (always present)
    division_code: str | None  # "C26" (null if section-only)
    division_name: str | None  # Full name (null if section-only)
    granularity: str           # "division" or "section"
    confidence: str            # "high", "medium", or "low"
    rationale: str             # Explanation citing evidence
    key_indicators: list[str]  # 1-5 phrases that drove decision
```

---

## Design Decisions

### Why Hierarchical JSON?

1. **Natural fallback**: Section → Division structure mirrors classification logic
2. **Grouped context**: All manufacturing divisions together help distinguish C10 vs C26
3. **Single file**: ~12KB, fits easily in system prompt (~3K tokens)

### Why Include `division_includes`?

The "includes" field resolves ambiguous cases. For example:
- "Software company" → Is it J58 (Software publishing) or K62 (Computer programming)?
- Check includes: J58 includes "Software publishing" while K62 includes "Computer programming activities"
- A company that writes custom software = K62; a company that publishes software products = J58

### Why Confidence Levels?

Downstream systems can use confidence to:
- Filter out low-confidence classifications for human review
- Weight recommendations differently based on classification certainty
- Track data quality across the library

---

## Integration with AI Case Library

This classification feeds into the Opportunity Analyser's matching logic:

```
Organisation Profile (ISIC code) 
    → Match against Case Library (ISIC codes)
    → Surface relevant cases from same/similar industries
```

Cases with division-level classification enable tighter matching than section-only.

---

## Cost Estimation

| Metric | Value |
|--------|-------|
| Taxonomy tokens | ~3,000 |
| Per-case tokens | ~3,500-4,000 |
| 200 cases total cost | ~$3 (Sonnet pricing) |

---

## Dependencies

```
anthropic>=0.18.0
pydantic>=2.0.0
```

---

## Limitations

- ISIC is designed for economic statistics, not AI use cases. Some cases (e.g., "AI research lab") don't fit neatly.
- Conglomerates operating across sectors require judgment calls on primary business.
- Newer industries (e.g., "creator economy") may not have precise ISIC mappings.

---

## Version

- **Taxonomy**: ISIC Rev 5 (2023)
- **Package version**: 1.0
- **Created**: 30 January 2026
