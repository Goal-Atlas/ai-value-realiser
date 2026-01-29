"""
Tests for Step 3: Claim Extraction.
"""

from typing import Any, Iterable, List

from case_library.pipeline.step3_claims import (
    LLMFn,
    build_claim_extraction_prompt,
    run_claim_extraction,
)
from case_library.schemas import (
    AIAttribution,
    ApplicationType,
    Case,
    CaseStatus,
    CognitiveDepth,
    ContextClaim,
    ContextClaimType,
    ContextVerificationStatus,
    EvidenceGrade,
    EvidenceLevel,
    Mechanism,
    MetricRaw,
    MetricType,
    Outcome,
    Source,
    SourceExtraction,
)


def _make_source_extraction() -> SourceExtraction:
    from datetime import datetime

    return SourceExtraction(
        source_id="S1",
        source_url="https://example.com/source",
        fetch_timestamp=datetime.utcnow(),
        fetch_status="success",
        extraction_method="trafilatura",
        content_length=300,
        content="This is a test source describing a 40% cost reduction from an AI system.",
    )


def test_build_claim_extraction_prompt_includes_case_id_and_sources() -> None:
    src = _make_source_extraction()
    prompt = build_claim_extraction_prompt("test-case-123", [src])
    assert "test-case-123" in prompt
    assert "S1" in prompt
    assert "https://example.com/source" in prompt


def test_run_claim_extraction_parses_value_and_context_claims(monkeypatch: Any) -> None:
    src = _make_source_extraction()

    def fake_llm(prompt: str) -> str:  # type: ignore[override]
        # Return a minimal JSON payload that conforms to the ValueClaim/ContextClaim schemas.
        return """
        {
          "model": "test-model",
          "extraction_confidence": 0.9,
          "value_claims": [
            {
              "id": "VC-001",
              "claim_title": "40% cost reduction",
              "claim_description": "AI reduced costs by 40%",
              "source_ids": ["S1"],
              "source_quote": "Our AI system reduced costs by 40%",
              "quote_location": "Section 3, paragraph 2",
              "ai_attribution": "direct",
              "attribution_evidence": "Quote explicitly attributes reduction to AI",
              "verification_status": "verified",
              "evidence_level": "outcome",
              "evidence_grade": "primary",
              "application_type": "capability_enhancement",
              "mechanism": ["automation"],
              "outcome": ["cost_reduction"],
              "cognitive_depth": "autonomous",
              "metric_raw": {
                "value": "40%",
                "metric_type": "percentage"
              },
              "metric_classification": {
                "quantification_level": "relative",
                "magnitude_band": "medium"
              },
              "ontology_version": "1.0",
              "ontology_confidence": {
                "mechanism": 0.9,
                "outcome": 0.9,
                "cognitive_depth": 0.9
              },
              "human_validation": {
                "reviewed": false
              }
            }
          ],
          "context_claims": [
            {
              "id": "CC-001",
              "context_type": "temporal",
              "claim_title": "2024",
              "claim_description": "The initiative launched in 2024",
              "source_ids": ["S1"],
              "source_quote": "In 2024, we launched our AI initiative",
              "verification_status": "verified",
              "verification_confidence": "high",
              "inferred_from": null,
              "apqc_code": null,
              "apqc_name": null,
              "human_validation": {
                "reviewed": false
              }
            }
          ]
        }
        """

    extraction, log = run_claim_extraction(
        case_id="test-case-123",
        sources=[src],
        llm_fn=fake_llm,  # type: ignore[arg-type]
        model_name="test-model",
        prompt_version="test-v1",
    )

    # Check extraction model
    assert extraction.case_id == "test-case-123"
    assert extraction.model_used == "test-model"
    assert extraction.extraction_confidence == 0.9
    assert len(extraction.value_claims) == 1
    assert len(extraction.context_claims) == 1

    vc = extraction.value_claims[0]
    assert vc.evidence_level == EvidenceLevel.OUTCOME
    assert vc.metric_raw is not None
    assert vc.metric_raw.value == "40%"
    assert vc.metric_raw.metric_type == MetricType.PERCENTAGE

    cc = extraction.context_claims[0]
    assert cc.context_type == ContextClaimType.TEMPORAL
    assert cc.verification_status == ContextVerificationStatus.VERIFIED

    # Check log
    assert log.model == "test-model"
    assert log.prompt_version == "test-v1"
    assert log.value_claims_count == 1
    assert log.context_claims_count == 1
    assert log.retries_malformed_json == 0
    assert log.retries_zero_claims == 0

