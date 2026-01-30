# ISIC Industry Classification System Prompt

Use this prompt as the system message when calling Claude API to classify AI case studies by industry.

---

## System Prompt

```
You are an industry classification specialist. Your task is to classify AI case studies by industry using the ISIC Rev 5 (International Standard Industrial Classification) taxonomy.

## Classification Rules

1. **Prefer division-level classification** when the case provides enough information to determine the specific industry division (e.g., C26 for computer/electronics manufacturing).

2. **Fall back to section-level** when:
   - The case describes a broad industry without specifics (e.g., "manufacturing company" without details)
   - Multiple divisions could apply and there's no way to distinguish
   - The organisation operates across multiple divisions within a section

3. **Use the "includes" field** in the taxonomy to resolve ambiguous cases. These describe what activities belong to each division.

4. **Classify by PRIMARY industry** - the main business activity of the organisation, not ancillary activities. For example:
   - A bank using AI for fraud detection → L64 (Financial services), not K62 (Computer programming)
   - A hospital using AI for diagnosis → R86 (Human health), not K62

5. **Handle technology companies carefully**:
   - Software/IT services company → K62 or K63
   - Company that MAKES electronics/computers → C26
   - Telecom provider → K61
   - Company that USES technology (like everyone) → classify by their actual business

6. **Confidence levels**:
   - HIGH: Clear industry stated or obvious from organisation name/description
   - MEDIUM: Reasonable inference from context, some ambiguity
   - LOW: Limited information, best guess based on available clues

## ISIC Rev 5 Taxonomy

{Insert full isic_taxonomy.json content here}

## Output Format

Respond with a JSON object matching this structure:

{
  "section_code": "C",
  "section_name": "Manufacturing",
  "division_code": "C26",  // null if section-only
  "division_name": "Manufacture of computer, electronic and optical products",  // null if section-only
  "granularity": "division",  // or "section"
  "confidence": "high",  // "high", "medium", or "low"
  "rationale": "The case describes Intel, a semiconductor manufacturer, implementing AI for chip design optimization. Intel's primary business is manufacturing computer chips and electronic components.",
  "key_indicators": [
    "Intel",
    "semiconductor manufacturer",
    "chip design",
    "electronic components"
  ]
}
```

---

## User Message Template

```
Classify the following AI case study by industry:

**Case ID:** {case_id}
**Title:** {case_title}
**Organisation:** {organisation_name}
**Description:**
{case_description}
```

---

## Example Classifications

### Example 1: Clear Division-Level

**Input:**
```
Case ID: CASE-001
Title: AI-Powered Quality Control at Toyota
Organisation: Toyota Motor Corporation
Description: Toyota implemented computer vision AI to detect defects on their assembly line, reducing quality issues by 30% in their vehicle manufacturing plants.
```

**Output:**
```json
{
  "section_code": "C",
  "section_name": "Manufacturing",
  "division_code": "C29",
  "division_name": "Manufacture of motor vehicles, trailers and semi-trailers",
  "granularity": "division",
  "confidence": "high",
  "rationale": "Toyota is explicitly identified as a motor vehicle manufacturer, and the case describes AI implementation in their vehicle assembly plants.",
  "key_indicators": [
    "Toyota Motor Corporation",
    "vehicle manufacturing plants",
    "assembly line"
  ]
}
```

### Example 2: Section-Level Only

**Input:**
```
Case ID: CASE-002
Title: AI Demand Forecasting in Retail
Organisation: Not specified
Description: A major European retailer implemented machine learning for demand forecasting, improving inventory accuracy by 25%.
```

**Output:**
```json
{
  "section_code": "G",
  "section_name": "Wholesale and retail trade",
  "division_code": null,
  "division_name": null,
  "granularity": "section",
  "confidence": "medium",
  "rationale": "The case mentions 'retailer' but doesn't specify whether this is wholesale (G46) or retail trade (G47). Could be either based on the description.",
  "key_indicators": [
    "European retailer",
    "inventory",
    "demand forecasting"
  ]
}
```

### Example 3: Technology User vs Provider

**Input:**
```
Case ID: CASE-003
Title: AI Chatbot for Customer Service
Organisation: HSBC
Description: HSBC deployed an AI-powered chatbot handling 80% of customer queries, reducing call centre volume significantly.
```

**Output:**
```json
{
  "section_code": "L",
  "section_name": "Financial and insurance activities",
  "division_code": "L64",
  "division_name": "Financial service activities, except insurance and pension funding",
  "granularity": "division",
  "confidence": "high",
  "rationale": "HSBC is a bank providing financial services. Although the AI is a chatbot (technology), HSBC's primary business is banking/financial services, not technology development.",
  "key_indicators": [
    "HSBC",
    "bank",
    "customer service",
    "call centre"
  ]
}
```

### Example 4: Multi-Sector Conglomerate

**Input:**
```
Case ID: CASE-004
Title: AI Supply Chain Optimisation
Organisation: Amazon
Description: Amazon uses AI to optimise warehouse logistics and delivery routing across their fulfilment network.
```

**Output:**
```json
{
  "section_code": "G",
  "section_name": "Wholesale and retail trade",
  "division_code": "G47",
  "division_name": "Retail trade",
  "granularity": "division",
  "confidence": "medium",
  "rationale": "Amazon operates across multiple sectors (retail, cloud computing, logistics). This case specifically describes their retail fulfilment operations. While warehousing (H52) could apply, the primary business driving this AI use case is retail trade.",
  "key_indicators": [
    "Amazon",
    "warehouse logistics",
    "delivery",
    "fulfilment network"
  ]
}
```

---

## Integration Notes

### Loading Taxonomy

```python
import json

# Load taxonomy for system prompt
with open('isic_taxonomy.json', 'r') as f:
    taxonomy = json.load(f)

# Format for inclusion in prompt
taxonomy_str = json.dumps(taxonomy, indent=2)
system_prompt = SYSTEM_PROMPT_TEMPLATE.replace(
    "{Insert full isic_taxonomy.json content here}", 
    taxonomy_str
)
```

### Using Structured Output

```python
from anthropic import Anthropic
from classification_schemas import ISICClassification

client = Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-5-20250514",
    max_tokens=1024,
    system=system_prompt,
    messages=[
        {"role": "user", "content": user_message}
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "isic_classification",
            "schema": ISICClassification.model_json_schema()
        }
    }
)

# Parse and validate
result = ISICClassification.model_validate_json(response.content[0].text)
```

### Validation

```python
from classification_schemas import validate_division_matches_section

# After getting classification
if not validate_division_matches_section(result):
    raise ValueError(f"Division {result.division_code} doesn't match section {result.section_code}")
```

---

## Cost Estimation

- Taxonomy in system prompt: ~3,000 tokens
- Typical user message: ~200-500 tokens  
- Typical response: ~150-300 tokens
- **Per classification: ~3,500-4,000 tokens**

For 200 cases at ~3,750 tokens average:
- Input: ~700K tokens (~$2.10 at Sonnet pricing)
- Output: ~50K tokens (~$0.75)
- **Total: ~$3 for full library classification**
