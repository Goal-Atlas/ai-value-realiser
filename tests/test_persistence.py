"""Tests for pipeline persistence (build.json, sources/text, claims.json)."""

from __future__ import annotations

import tempfile
from datetime import datetime, timezone
from pathlib import Path

from case_library.pipeline.persistence import (
    read_build_log,
    read_claims,
    read_source_text,
    write_build_log,
    write_claims,
    write_sources_text,
)
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


def test_write_and_read_build_log() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        case_dir = Path(tmp)
        log = BuildLog(
            case_id="case-1",
            build_started=datetime.now(timezone.utc),
            build_completed=datetime.now(timezone.utc),
        )
        write_build_log(case_dir, log)
        read_log = read_build_log(case_dir)
        assert read_log is not None
        assert read_log.case_id == log.case_id


def test_write_and_read_claims() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        case_dir = Path(tmp)
        vc = _mk_value_claim()
        cc = _mk_context_claim()
        write_claims(case_dir, [vc], [cc])
        v_list, c_list = read_claims(case_dir)
        assert len(v_list) == 1
        assert len(c_list) == 1
        assert v_list[0].id == vc.id
        assert c_list[0].id == cc.id


def test_write_and_read_sources_text() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        case_dir = Path(tmp)
        src = SourceExtraction(
            source_id="S1",
            source_url="https://example.com",
            fetch_timestamp=datetime.now(timezone.utc),
            fetch_status="success",
            extraction_method="trafilatura",
            content_length=5,
            content="hello",
        )
        write_sources_text(case_dir, [src])
        text = read_source_text(case_dir, "S1")
        assert text == "hello"
