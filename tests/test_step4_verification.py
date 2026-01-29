from __future__ import annotations

from datetime import datetime

from case_library.pipeline.step4_verification import find_quote_in_text, run_step4_verification
from case_library.schemas import (
    AIAttribution,
    ApplicationType,
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


def _mk_source(source_id: str, text: str) -> SourceExtraction:
    return SourceExtraction(
        source_id=source_id,
        source_url=f"https://example.com/{source_id}",
        fetch_timestamp=datetime.utcnow(),
        fetch_status="success",
        extraction_method="trafilatura",
        content_length=len(text),
        content=text,
    )


def _mk_value_claim(*, quote: str, source_ids: list[str]) -> ValueClaim:
    return ValueClaim(
        id="VC-001",
        claim_title="Test claim",
        claim_description="Test description",
        source_ids=source_ids,
        source_quote=quote,
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


def _mk_context_claim(*, quote: str | None, source_ids: list[str], status: ContextVerificationStatus) -> ContextClaim:
    return ContextClaim(
        id="CC-001",
        context_type=ContextClaimType.TEMPORAL,
        claim_title="Context",
        claim_description=None,
        source_ids=source_ids,
        source_quote=quote,
        verification_status=status,
        verification_confidence=None,
        inferred_from=None if status != ContextVerificationStatus.INFERRED else "inferred test",
        apqc_code=None,
        apqc_name=None,
    )


def test_find_quote_exact() -> None:
    text = "Hello world. This is a quote."
    quote = "This is a quote."
    m = find_quote_in_text(text, quote)
    assert m.matched is True
    assert m.method == "exact"
    assert m.start == text.find(quote)
    assert m.end == m.start + len(quote)


def test_find_quote_regex_whitespace() -> None:
    text = "Hello world.\nThis   is a quote.\nDone."
    quote = "This is a quote."
    m = find_quote_in_text(text, quote)
    assert m.matched is True
    assert m.method in {"regex_normalized", "exact"}
    assert m.start is not None and m.end is not None


def test_step4_updates_value_claim_status() -> None:
    src = _mk_source("S1", "Prefix\nThis is a quote.\nSuffix")
    claim = _mk_value_claim(quote="This is a quote.", source_ids=["S1"])

    v_out, c_out, log = run_step4_verification(
        value_claims=[claim], context_claims=[], sources=[src], model_name=None
    )
    assert len(v_out) == 1
    assert v_out[0].verification_status == VerificationStatus.VERIFIED
    assert log.verification_attempts
    assert log.verification_attempts[0].claim_id == "VC-001"
    assert log.verification_attempts[0].source_id == "S1"
    assert log.verification_attempts[0].result == "matched"
    assert log.verification_attempts[0].char_offset_start is not None


def test_step4_skips_inferred_context_claim() -> None:
    src = _mk_source("S1", "Some text")
    cc = _mk_context_claim(quote=None, source_ids=[], status=ContextVerificationStatus.INFERRED)

    v_out, c_out, log = run_step4_verification(
        value_claims=[], context_claims=[cc], sources=[src], model_name=None
    )
    assert len(c_out) == 1
    assert c_out[0].verification_status == ContextVerificationStatus.INFERRED
    # No attempts should be recorded for inferred context claims
    assert log.verification_attempts == []


def test_step4_marks_value_claim_needs_review_if_not_found() -> None:
    src = _mk_source("S1", "No matching quote here.")
    claim = _mk_value_claim(quote="This is missing.", source_ids=["S1"])

    v_out, _, log = run_step4_verification(value_claims=[claim], context_claims=[], sources=[src])
    assert v_out[0].verification_status == VerificationStatus.NEEDS_REVIEW
    assert log.verification_attempts
    assert log.verification_attempts[0].result == "not_found"

