"""
Step 3: Claim Extraction (AI-assisted)

Implements the behaviour described in §6.4 of
`docs/specs/AI_CASE_LIBRARY_SPECIFICATION_v1_5.md`:

- Input: case_id + extracted sources (Step 2 `SourceExtraction`)
- Behaviour:
  - Build a prompt that instructs an LLM to extract Value Claims and Context Claims
  - Call a pluggable `llm_fn` to obtain a JSON response
  - Parse into `ValueClaim` and `ContextClaim` Pydantic models
  - Enforce schema rules (ai_attribution, evidence_level, metric_raw, etc.)
  - Retry on malformed JSON / zero-claim responses
- Output:
  - `ClaimExtraction` model instance
  - `BuildLog.Step3ClaimsLog` with counts and retry metadata

This module is responsible only for **logic and parsing**. It does not make
real network calls itself; `llm_fn` is injected so tests and callers can
decide which model/backend to use.
"""

from __future__ import annotations

from datetime import datetime
import json
from typing import Callable, Iterable, List, Tuple

from case_library.schemas import (
    BuildLog,
    ClaimExtraction,
    ContextClaim,
    SourceExtraction,
    ValueClaim,
)

LLMFn = Callable[[str], str]


def _coerce_missing_metric_to_method(raw_claim: dict) -> tuple[dict, bool]:
    """
    Enforce spec rule: outcome/adoption claims must be quantified.

    If an LLM returns evidence_level=outcome/adoption but omits metric_raw, we
    downgrade to evidence_level=method so the claim can be retained without
    faking a metric. We also mark verification_status as needs_review (if present)
    to preserve the claim's intent for later human review.
    """
    claim = dict(raw_claim)
    level = claim.get("evidence_level")
    metric = claim.get("metric_raw")

    if level in {"outcome", "adoption"} and not metric:
        claim["evidence_level"] = "method"
        # Keep intent visible for review if pipeline provided a status field
        if claim.get("verification_status") == "verified":
            claim["verification_status"] = "needs_review"
        return claim, True
    return claim, False


def _coerce_context_sources(raw_claim: dict) -> tuple[dict, bool]:
    """
    Enforce Appendix E.2 rules for ContextClaim source_ids.

    If source_ids is empty/missing, the only valid state is verification_status=inferred
    with inferred_from populated. Rather than fail the whole run, we coerce to inferred
    and record a short inferred_from note.
    """
    claim = dict(raw_claim)
    if "context_type" not in claim:
        return claim, False

    source_ids = claim.get("source_ids")
    status = claim.get("verification_status")
    if (not source_ids) and status != "inferred":
        claim["verification_status"] = "inferred"
        if not claim.get("inferred_from"):
            claim["inferred_from"] = "source_ids missing in LLM output"
        return claim, True
    return claim, False


def _repair_json_newlines(raw: str) -> str:
    """
    Repair JSON where the LLM embedded raw newlines inside double-quoted strings.

    Valid JSON requires newlines in strings to be escaped as \\n. This walks the
    string and replaces unescaped \\n and \\r inside quoted strings with \\n / \\r.
    """
    result: List[str] = []
    i = 0
    in_string = False
    escaped = False
    while i < len(raw):
        c = raw[i]
        if escaped:
            result.append(c)
            escaped = False
            i += 1
            continue
        if c == "\\" and in_string:
            result.append(c)
            escaped = True
            i += 1
            continue
        if c == '"':
            result.append(c)
            in_string = not in_string
            i += 1
            continue
        if in_string and c == "\n":
            result.append("\\n")
            i += 1
            continue
        if in_string and c == "\r":
            result.append("\\r")
            i += 1
            continue
        result.append(c)
        i += 1
    return "".join(result)


def _normalize_common_fields(raw_claim: dict) -> dict:
    """
    Normalize common field name mismatches and enum value mismatches from LLM output.

    Maps common variations to the exact schema field names and enum values:
    - claim_id -> id
    - case_id -> (remove, not a field)
    - evidence_strength -> evidence_level
    - evidence_grade: "high"/"medium"/"low" -> "primary"/"secondary_high"/"secondary_low"
    - application_type: "internal"/"customer_facing"/etc -> "capability_enhancement"/"capability_creation"
    """
    normalized = dict(raw_claim)

    # Field name mappings
    field_mappings = {
        "claim_id": "id",
        "context_claim_id": "id",
        "value_claim_id": "id",
        "evidence_strength": "evidence_level",
    }

    # Apply mappings
    for old_key, new_key in field_mappings.items():
        if old_key in normalized and new_key not in normalized:
            normalized[new_key] = normalized.pop(old_key)

    # Enum value mappings
    # evidence_grade: common incorrect values
    if "evidence_grade" in normalized:
        grade = normalized["evidence_grade"]
        if grade == "high":
            normalized["evidence_grade"] = "primary"
        elif grade == "medium":
            normalized["evidence_grade"] = "secondary_high"
        elif grade == "low":
            normalized["evidence_grade"] = "secondary_low"

    # application_type: common incorrect values
    if "application_type" in normalized:
        app_type = normalized["application_type"]
        # Map common incorrect values to capability_enhancement (most common case)
        if app_type in ("internal", "customer_facing", "product", "research"):
            normalized["application_type"] = "capability_enhancement"
        # If it's already correct, leave it

    # Remove fields that don't belong in the schema
    invalid_fields = ["case_id"]  # This is case-level, not claim-level
    for field in invalid_fields:
        normalized.pop(field, None)

    return normalized


def _normalize_value_claim(raw_claim: dict) -> tuple[dict, bool]:
    normalized = _normalize_common_fields(raw_claim)
    normalized, downgraded = _coerce_missing_metric_to_method(normalized)
    return normalized, downgraded


def _normalize_context_claim(raw_claim: dict) -> tuple[dict, bool]:
    normalized = _normalize_common_fields(raw_claim)
    normalized, coerced = _coerce_context_sources(normalized)
    return normalized, coerced


def build_claim_extraction_prompt(case_id: str, sources: Iterable[SourceExtraction]) -> str:
    """
    Construct a detailed prompt for claim extraction with exact schema specification.

    The prompt includes:
    - Case ID
    - Each source_id + URL + extracted text content
    - Exact field names and structure for ValueClaim and ContextClaim
    """
    lines: List[str] = []
    lines.append(
        "You are an AI assistant that extracts structured claims from source documents "
        "about how organisations create value with AI."
    )
    lines.append(f"Case ID: {case_id}")
    lines.append("")
    lines.append("Extract VALUE CLAIMS and CONTEXT CLAIMS from the sources below.")
    lines.append("")
    lines.append("=== REQUIRED JSON STRUCTURE ===")
    lines.append("")
    lines.append("Return a JSON object with this exact structure:")
    lines.append('{')
    lines.append('  "model": "string (model name)",')
    lines.append('  "extraction_confidence": 0.0-1.0,')
    lines.append('  "value_claims": [ /* array of ValueClaim objects */ ],')
    lines.append('  "context_claims": [ /* array of ContextClaim objects */ ]')
    lines.append('}')
    lines.append("")
    lines.append("=== VALUE CLAIM SCHEMA (exact field names) ===")
    lines.append("Each value_claims item must have these EXACT field names:")
    lines.append('{')
    lines.append('  "id": "string (e.g., VC-001)",')
    lines.append('  "claim_title": "string",')
    lines.append('  "claim_description": "string",')
    lines.append('  "source_ids": ["S1", "S2"],')
    lines.append('  "source_quote": "string (exact quote from source)",')
    lines.append('  "quote_location": "string (optional)",')
    lines.append('  "ai_attribution": "direct" | "contributing" | "contextual",')
    lines.append('  "attribution_evidence": "string (explaining why this attribution)",')
    lines.append('  "verification_status": "verified" | "needs_review" | "rejected",')
    lines.append('  "evidence_level": "outcome" | "adoption" | "method",')
    lines.append('  "evidence_grade": "primary" | "secondary_high" | "secondary_low",')
    lines.append('  "application_type": "capability_enhancement" | "capability_creation",')
    lines.append('  "mechanism": ["automation" | "augmentation" | "optimization" | "innovation"],')
    lines.append('  "outcome": ["velocity" | "experience" | "cost_reduction" | "revenue_lift" | "risk_avoidance" | "cost_erosion" | "business_growth"],')
    lines.append('  "cognitive_depth": "descriptive" | "diagnostic" | "predictive" | "prescriptive" | "generative" | "autonomous",')
    lines.append('  "metric_raw": { /* REQUIRED if evidence_level is "outcome" or "adoption" */')
    lines.append('    "value": "string (the number/metric)",')
    lines.append('    "unit": "string (e.g., %, $, days)",')
    lines.append('    "metric_type": "absolute_value" | "percentage" | "ratio" | "count"')
    lines.append('  } /* null if evidence_level is "method" */,')
    lines.append('  "metric_classification": null,')
    lines.append('  "ontology_version": "1.0",')
    lines.append('  "ontology_confidence": null')
    lines.append('}')
    lines.append("")
    lines.append("IMPORTANT: Use 'id' NOT 'claim_id'. Use 'evidence_level' NOT 'evidence_strength'.")
    lines.append("")
    lines.append("JSON STRING RULES: Every string value MUST be valid JSON: no raw newlines inside quotes.")
    lines.append("Use \\n for newlines. Keep source_quote and claim_description under 400 characters each.")
    lines.append("")
    lines.append("=== CONTEXT CLAIM SCHEMA (exact field names) ===")
    lines.append("Each context_claims item must have these EXACT field names:")
    lines.append('{')
    lines.append('  "id": "string (e.g., CC-001)",')
    lines.append('  "context_type": "temporal" | "organisational" | "sectoral" | "functional" | "scale" | "strategic_intent" | "products_services",')
    lines.append('  "claim_title": "string",')
    lines.append('  "claim_description": "string (optional)",')
    lines.append('  "source_ids": ["S1"],')
    lines.append('  "source_quote": "string (optional)",')
    lines.append('  "verification_status": "verified" | "unverified" | "inferred",')
    lines.append('  "verification_confidence": "high" | "medium" | "low" (optional),')
    lines.append('  "inferred_from": "string (required if verification_status is inferred)",')
    lines.append('  "apqc_code": "string (required if context_type is functional)",')
    lines.append('  "apqc_name": "string (required if context_type is functional)"')
    lines.append('}')
    lines.append("")
    lines.append("=== SOURCES ===")
    lines.append("")

    for src in sources:
        lines.append(f"--- SOURCE {src.source_id} ---")
        lines.append(f"URL: {src.source_url}")
        if src.content:
            # Truncate very long content to avoid token limits
            content = src.content
            if len(content) > 10000:
                content = content[:10000] + "\n\n[... content truncated ...]"
            lines.append(content)
        else:
            lines.append("[No content extracted]")
        lines.append("")  # separator

    return "\n".join(lines)


def run_claim_extraction(
    case_id: str,
    sources: Iterable[SourceExtraction],
    *,
    llm_fn: LLMFn,
    model_name: str = "unknown-model",
    prompt_version: str = "v1.0",
    max_malformed_retries: int = 2,
    max_zero_claim_retries: int = 1,
) -> Tuple[ClaimExtraction, BuildLog.Step3ClaimsLog]:
    """
    Run Step 3 (Claim Extraction) and return:

    - A `ClaimExtraction` Pydantic model
    - A `BuildLog.Step3ClaimsLog` capturing metadata about the run
    """
    sources_list = list(sources)

    skipped_no_sources = False
    claims_downgraded_metric_missing = 0
    context_claims_coerced_inferred = 0
    value_claims_dropped_invalid = 0
    context_claims_dropped_invalid = 0

    # Robustness: if Step 2 produced no usable sources, don't call the LLM.
    if not sources_list or not any((s.content or "").strip() for s in sources_list):
        skipped_no_sources = True
        extraction = ClaimExtraction(
            case_id=case_id,
            extraction_timestamp=datetime.utcnow(),
            model_used=model_name,
            value_claims=[],
            context_claims=[],
            extraction_confidence=0.0,
        )
        log = BuildLog.Step3ClaimsLog(
            model=model_name,
            prompt_version=prompt_version,
            raw_response_file=None,
            claims_file=None,
            value_claims_count=0,
            context_claims_count=0,
            retries_malformed_json=0,
            retries_zero_claims=0,
            skipped_no_sources=skipped_no_sources,
            claims_downgraded_metric_missing=0,
            context_claims_coerced_inferred=0,
            value_claims_dropped_invalid=0,
            context_claims_dropped_invalid=0,
        )
        return extraction, log

    prompt = build_claim_extraction_prompt(case_id, sources_list)

    malformed_retries = 0
    zero_claim_retries = 0
    last_raw_response: str | None = None

    value_claims: List[ValueClaim] = []
    context_claims: List[ContextClaim] = []
    model_used = model_name
    extraction_confidence = 1.0

    while True:
        raw = llm_fn(prompt)
        last_raw_response = raw

        try:
            data = json.loads(raw)
        except json.JSONDecodeError as e:
            # Try repairing common LLM mistakes: raw newlines inside strings
            repaired = _repair_json_newlines(raw)
            try:
                data = json.loads(repaired)
            except json.JSONDecodeError:
                malformed_retries += 1
                if malformed_retries <= max_malformed_retries:
                    continue
                error_snippet = (
                    raw[max(0, e.pos - 100) : e.pos + 100] if hasattr(e, "pos") else raw[:200]
                )
                raise ValueError(
                    f"Invalid JSON from LLM (after {malformed_retries} retries). "
                    f"Error: {e}. "
                    f"JSON snippet around error: ...{error_snippet}..."
                ) from e

        # We have data (from initial parse or repaired parse)

        # Extract fields from parsed JSON
        model_used = str(data.get("model", model_name))
        extraction_confidence = float(data.get("extraction_confidence", 1.0))

        raw_value_claims = data.get("value_claims", []) or []
        raw_context_claims = data.get("context_claims", []) or []

        if not raw_value_claims and zero_claim_retries < max_zero_claim_retries:
            zero_claim_retries += 1
            continue

        # Normalize field names/values before parsing (and track coercions)
        normalized_value_claims: List[dict] = []
        for vc in raw_value_claims:
            n, downgraded = _normalize_value_claim(vc)
            if downgraded:
                claims_downgraded_metric_missing += 1
            normalized_value_claims.append(n)

        normalized_context_claims: List[dict] = []
        for cc in raw_context_claims:
            n, coerced = _normalize_context_claim(cc)
            if coerced:
                context_claims_coerced_inferred += 1
            normalized_context_claims.append(n)

        # Parse into Pydantic models (enforces all schema rules).
        # Robustness: parse per-claim; skip invalid claims instead of failing the whole run.
        parsed_value: List[ValueClaim] = []
        parsed_context: List[ContextClaim] = []
        value_errors: List[str] = []
        context_errors: List[str] = []

        for vc in normalized_value_claims:
            try:
                parsed_value.append(ValueClaim(**vc))
            except Exception as e:  # noqa: BLE001
                value_errors.append(str(e))
                value_claims_dropped_invalid += 1

        for cc in normalized_context_claims:
            try:
                parsed_context.append(ContextClaim(**cc))
            except Exception as e:  # noqa: BLE001
                context_errors.append(str(e))
                context_claims_dropped_invalid += 1

        if not parsed_value and zero_claim_retries < max_zero_claim_retries:
            zero_claim_retries += 1
            continue

        # If everything was invalid, retry a couple of times to give the LLM a chance to comply.
        if (value_errors or context_errors) and malformed_retries < max_malformed_retries and not parsed_value:
            malformed_retries += 1
            continue

        value_claims = parsed_value
        context_claims = parsed_context
        break

    extraction = ClaimExtraction(
        case_id=case_id,
        extraction_timestamp=datetime.utcnow(),
        model_used=model_used,
        value_claims=value_claims,
        context_claims=context_claims,
        extraction_confidence=extraction_confidence,
    )

    log = BuildLog.Step3ClaimsLog(
        model=model_used,
        prompt_version=prompt_version,
        raw_response_file=None,
        claims_file=None,
        value_claims_count=len(value_claims),
        context_claims_count=len(context_claims),
        retries_malformed_json=malformed_retries,
        retries_zero_claims=zero_claim_retries,
        skipped_no_sources=skipped_no_sources,
        claims_downgraded_metric_missing=claims_downgraded_metric_missing,
        context_claims_coerced_inferred=context_claims_coerced_inferred,
        value_claims_dropped_invalid=value_claims_dropped_invalid,
        context_claims_dropped_invalid=context_claims_dropped_invalid,
    )

    return extraction, log


__all__ = ["LLMFn", "build_claim_extraction_prompt", "run_claim_extraction"]

