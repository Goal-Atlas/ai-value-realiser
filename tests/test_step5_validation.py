"""Tests for Step 5 (Human Validation) recording."""

from __future__ import annotations

from datetime import datetime, timezone

from case_library.pipeline.orchestrator import run_step5_human_validation_for_case
from case_library.pipeline.step5_validation import record_human_validation
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
    ReviewerVerdict,
    ValueClaim,
    ValidationTier,
    VerificationStatus,
)


def _mk_build_log() -> BuildLog:
    return BuildLog(
        case_id="case-1",
        build_started=datetime.now(timezone.utc),
        build_completed=datetime.now(timezone.utc),
    )


def _mk_value_claim(claim_id: str = "VC-001") -> ValueClaim:
    return ValueClaim(
        id=claim_id,
        claim_title="Test",
        claim_description="Test",
        source_ids=["S1"],
        source_quote="Quote",
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


def _mk_context_claim(claim_id: str = "CC-001") -> ContextClaim:
    return ContextClaim(
        id=claim_id,
        context_type=ContextClaimType.TEMPORAL,
        claim_title="Context",
        claim_description=None,
        source_ids=["S1"],
        source_quote="Context quote",
        quote_location="Page 1",
        verification_status=ContextVerificationStatus.VERIFIED,
    )


def test_record_human_validation_updates_claims_and_build_log() -> None:
    log = _mk_build_log()
    vc = _mk_value_claim("VC-001")
    cc = _mk_context_claim("CC-001")
    verdicts = {"VC-001": "valid", "CC-001": "invalid"}
    updated_log, updated_vc, updated_cc = record_human_validation(
        log,
        [vc],
        [cc],
        tier=ValidationTier.TIER_1,
        reviewer_id="reviewer-1",
        verdicts=verdicts,
        time_taken_minutes=10,
        missed_claims_added=0,
    )
    assert updated_log.step_5_human_validation is not None
    assert updated_log.step_5_human_validation.tier == ValidationTier.TIER_1
    assert updated_log.step_5_human_validation.reviewer_id == "reviewer-1"
    assert updated_log.step_5_human_validation.claims_reviewed == 2
    assert updated_log.step_5_human_validation.time_taken_minutes == 10
    assert len(updated_vc) == 1
    assert updated_vc[0].human_validation.reviewed is True
    assert updated_vc[0].human_validation.reviewer_verdict == ReviewerVerdict.VALID
    assert len(updated_cc) == 1
    assert updated_cc[0].human_validation.reviewed is True
    assert updated_cc[0].human_validation.reviewer_verdict == ReviewerVerdict.INVALID


def test_run_step5_human_validation_for_case() -> None:
    log = _mk_build_log()
    vc = _mk_value_claim("VC-001")
    updated_log, updated_vc, _ = run_step5_human_validation_for_case(
        log,
        [vc],
        [],
        tier=ValidationTier.TIER_1,
        reviewer_id="r1",
        verdicts={"VC-001": "valid"},
    )
    assert updated_log.step_5_human_validation is not None
    assert updated_vc[0].human_validation.reviewer_verdict == ReviewerVerdict.VALID
