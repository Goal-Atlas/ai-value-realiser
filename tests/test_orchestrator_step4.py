from __future__ import annotations

from datetime import datetime

from case_library.pipeline.orchestrator import run_step4_verification_for_case
from case_library.schemas import (
    AIAttribution,
    ApplicationType,
    BuildLog,
    ContextClaim,
    ContextClaimType,
    ContextVerificationStatus,
    EvidenceGrade,
    EvidenceLevel,
    Mechanism,
    Outcome,
    SourceExtraction,
    ValueClaim,
    VerificationStatus,
)


def test_run_step4_verification_for_case_populates_build_log() -> None:
    src = SourceExtraction(
        source_id="S1",
        source_url="https://example.com",
        fetch_timestamp=datetime.utcnow(),
        fetch_status="success",
        extraction_method="trafilatura",
        content_length=100,
        content="Prefix\nThis is a quote.\nSuffix",
    )

    vc = ValueClaim(
        id="VC-001",
        claim_title="Test",
        claim_description="Test",
        source_ids=["S1"],
        source_quote="This is a quote.",
        ai_attribution=AIAttribution.DIRECT,
        attribution_evidence="From source",
        verification_status=VerificationStatus.NEEDS_REVIEW,
        evidence_level=EvidenceLevel.METHOD,
        evidence_grade=EvidenceGrade.PRIMARY,
        application_type=ApplicationType.CAPABILITY_ENHANCEMENT,
        mechanism=[Mechanism.AUTOMATION],
        outcome=[Outcome.VELOCITY],
        cognitive_depth="descriptive",
        metric_raw=None,
    )

    cc = ContextClaim(
        id="CC-001",
        context_type=ContextClaimType.TEMPORAL,
        claim_title="Context",
        claim_description=None,
        source_ids=["S1"],
        source_quote="This is a quote.",
        verification_status=ContextVerificationStatus.UNVERIFIED,
        verification_confidence=None,
        inferred_from=None,
        apqc_code=None,
        apqc_name=None,
    )

    build_log = BuildLog(case_id="case-1", build_started=datetime.utcnow())
    build_log, v_out, c_out = run_step4_verification_for_case(
        build_log,
        value_claims=[vc],
        context_claims=[cc],
        sources=[src],
        model_name=None,
    )

    assert build_log.step_4_verification is not None
    assert build_log.step_4_verification.verification_attempts
    assert v_out[0].verification_status == VerificationStatus.VERIFIED
    assert c_out[0].verification_status == ContextVerificationStatus.VERIFIED

