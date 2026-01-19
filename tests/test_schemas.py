"""
Tests for AI Case Library schemas.
"""

from datetime import datetime

import pytest

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
    EvidenceType,
    HumanValidationSummary,
    Mechanism,
    OntologyMetadata,
    Outcome,
    Source,
    SourceType,
    ValidationTier,
    ValueClaim,
    VerificationStatus,
    VerificationSummary,
)


class TestEnums:
    """Test enum definitions match spec."""

    def test_mechanism_values(self) -> None:
        assert set(Mechanism) == {
            Mechanism.AUTOMATION,
            Mechanism.AUGMENTATION,
            Mechanism.OPTIMIZATION,
            Mechanism.INNOVATION,
        }

    def test_outcome_values(self) -> None:
        assert set(Outcome) == {
            Outcome.VELOCITY,
            Outcome.EXPERIENCE,
            Outcome.COST_REDUCTION,
            Outcome.REVENUE_LIFT,
            Outcome.RISK_AVOIDANCE,
            Outcome.COST_EROSION,
            Outcome.BUSINESS_GROWTH,
        }

    def test_cognitive_depth_values(self) -> None:
        assert set(CognitiveDepth) == {
            CognitiveDepth.DESCRIPTIVE,
            CognitiveDepth.DIAGNOSTIC,
            CognitiveDepth.PREDICTIVE,
            CognitiveDepth.PRESCRIPTIVE,
            CognitiveDepth.GENERATIVE,
            CognitiveDepth.AUTONOMOUS,
        }

    def test_ai_attribution_values(self) -> None:
        assert set(AIAttribution) == {
            AIAttribution.DIRECT,
            AIAttribution.CONTRIBUTING,
            AIAttribution.CONTEXTUAL,
        }


class TestValueClaim:
    """Test ValueClaim model."""

    def test_valid_value_claim(self) -> None:
        claim = ValueClaim(
            id="VC-001",
            claim_title="40% cost reduction",
            claim_description="AI reduced processing costs by 40%",
            source_ids=["S1"],
            source_quote="Our AI system reduced costs by 40%",
            ai_attribution=AIAttribution.DIRECT,
            attribution_evidence="Quote explicitly states AI caused the reduction",
            verification_status=VerificationStatus.VERIFIED,
            evidence_type=EvidenceType.OUTCOME_VALIDATION,
            evidence_grade=EvidenceGrade.PRIMARY,
            application_type=ApplicationType.CAPABILITY_ENHANCEMENT,
            mechanism=[Mechanism.AUTOMATION],
            outcome=[Outcome.COST_REDUCTION],
            cognitive_depth=CognitiveDepth.AUTONOMOUS,
        )
        assert claim.id == "VC-001"
        assert claim.ai_attribution == AIAttribution.DIRECT

    def test_mechanism_max_two(self) -> None:
        """Mechanism should allow max 2 values."""
        with pytest.raises(ValueError, match="Maximum 2 mechanisms"):
            ValueClaim(
                id="VC-001",
                claim_title="Test",
                claim_description="Test",
                source_ids=["S1"],
                source_quote="Test",
                ai_attribution=AIAttribution.DIRECT,
                attribution_evidence="Test",
                verification_status=VerificationStatus.VERIFIED,
                evidence_type=EvidenceType.OUTCOME_VALIDATION,
                evidence_grade=EvidenceGrade.PRIMARY,
                application_type=ApplicationType.CAPABILITY_ENHANCEMENT,
                mechanism=[Mechanism.AUTOMATION, Mechanism.AUGMENTATION, Mechanism.OPTIMIZATION],
                outcome=[Outcome.COST_REDUCTION],
                cognitive_depth=CognitiveDepth.AUTONOMOUS,
            )

    def test_outcome_max_four(self) -> None:
        """Outcome should allow max 4 values."""
        with pytest.raises(ValueError, match="Maximum 4 outcomes"):
            ValueClaim(
                id="VC-001",
                claim_title="Test",
                claim_description="Test",
                source_ids=["S1"],
                source_quote="Test",
                ai_attribution=AIAttribution.DIRECT,
                attribution_evidence="Test",
                verification_status=VerificationStatus.VERIFIED,
                evidence_type=EvidenceType.OUTCOME_VALIDATION,
                evidence_grade=EvidenceGrade.PRIMARY,
                application_type=ApplicationType.CAPABILITY_ENHANCEMENT,
                mechanism=[Mechanism.AUTOMATION],
                outcome=[
                    Outcome.COST_REDUCTION,
                    Outcome.VELOCITY,
                    Outcome.EXPERIENCE,
                    Outcome.REVENUE_LIFT,
                    Outcome.RISK_AVOIDANCE,
                ],
                cognitive_depth=CognitiveDepth.AUTONOMOUS,
            )


class TestContextClaim:
    """Test ContextClaim model."""

    def test_valid_context_claim(self) -> None:
        claim = ContextClaim(
            id="CC-001",
            context_type=ContextClaimType.TEMPORAL,
            claim_title="Q2 2024 launch",
            claim_description="Initiative launched in Q2 2024",
            source_ids=["S1"],
            source_quote="We launched in April 2024",
            verification_status=ContextVerificationStatus.VERIFIED,
            verification_confidence="high",
        )
        assert claim.context_type == ContextClaimType.TEMPORAL

    def test_functional_claim_with_apqc(self) -> None:
        claim = ContextClaim(
            id="CC-002",
            context_type=ContextClaimType.FUNCTIONAL,
            claim_title="Customer service function",
            claim_description="Applied to customer service",
            source_ids=["S1"],
            verification_status=ContextVerificationStatus.INFERRED,
            verification_confidence="medium",
            inferred_from="Context suggests customer service application",
            apqc_code="5.3",
            apqc_name="Deliver service to customer",
        )
        assert claim.apqc_code == "5.3"


class TestCase:
    """Test Case model."""

    @pytest.fixture
    def sample_case(self) -> Case:
        """Create a sample case for testing."""
        return Case(
            case_id="test-case-001",
            organisation="Test Corp",
            title="AI Customer Service Transformation",
            date_created=datetime.now(),
            date_updated=datetime.now(),
            sources=[
                Source(
                    id="S1",
                    title="Test Report",
                    url="https://example.com/report",
                    type=SourceType.ORGANISATION_ITSELF,
                    grade=EvidenceGrade.PRIMARY,
                )
            ],
            value_claims=[
                ValueClaim(
                    id="VC-001",
                    claim_title="40% cost reduction",
                    claim_description="AI reduced costs by 40%",
                    source_ids=["S1"],
                    source_quote="Our AI reduced costs by 40%",
                    ai_attribution=AIAttribution.DIRECT,
                    attribution_evidence="Direct causal statement",
                    verification_status=VerificationStatus.VERIFIED,
                    evidence_type=EvidenceType.OUTCOME_VALIDATION,
                    evidence_grade=EvidenceGrade.PRIMARY,
                    application_type=ApplicationType.CAPABILITY_ENHANCEMENT,
                    mechanism=[Mechanism.AUTOMATION],
                    outcome=[Outcome.COST_REDUCTION],
                    cognitive_depth=CognitiveDepth.AUTONOMOUS,
                )
            ],
            context_claims=[],
            verification_summary=VerificationSummary(
                value_claims=VerificationSummary.ValueClaimSummary(
                    total=1,
                    verified=1,
                    needs_review=0,
                    rejected=0,
                    by_attribution={"direct": 1},
                ),
                context_claims=VerificationSummary.ContextClaimSummary(
                    total=0,
                    verified=0,
                    unverified=0,
                    inferred=0,
                ),
                all_value_verified=True,
                all_context_verified=True,
            ),
            status=CaseStatus.COMPLETE,
            confidence="high",
            ontology_metadata=OntologyMetadata(
                version_used="1.0",
                tagged_date=datetime.now(),
                needs_retagging=False,
            ),
        )

    def test_case_creation(self, sample_case: Case) -> None:
        assert sample_case.case_id == "test-case-001"
        assert len(sample_case.value_claims) == 1
        assert sample_case.status == CaseStatus.COMPLETE

    def test_case_with_human_validation(self, sample_case: Case) -> None:
        sample_case.human_validation_summary = HumanValidationSummary(
            reviewed=True,
            review_date=datetime.now(),
            reviewer_id="MB",
            validation_tier=ValidationTier.TIER_1,
            value_claims=HumanValidationSummary.ClaimValidationSummary(
                valid=1,
                invalid=0,
                unclear=0,
                missed=0,
            ),
        )
        assert sample_case.human_validation_summary.reviewed is True
