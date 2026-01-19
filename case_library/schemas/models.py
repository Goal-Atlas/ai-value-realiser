"""
AI Case Library Data Schemas

Pydantic models for the AI Case Library, implementing the specification
defined in docs/specs/AI_CASE_LIBRARY_SPECIFICATION.md

Version: 0.3 (aligned with spec v0.3)
"""

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


# =============================================================================
# ENUMS
# =============================================================================


class ApplicationType(str, Enum):
    """Axis 1: What kind of change does this represent?"""

    CAPABILITY_ENHANCEMENT = "capability_enhancement"
    CAPABILITY_CREATION = "capability_creation"


class EvidenceType(str, Enum):
    """Axis 2: What kind of proof do we have?"""

    OUTCOME_VALIDATION = "outcome_validation"
    METHOD_VALIDATION = "method_validation"


class AIAttribution(str, Enum):
    """How directly is the outcome attributed to AI?"""

    DIRECT = "direct"  # AI explicitly caused this outcome
    CONTRIBUTING = "contributing"  # AI is one factor among others
    CONTEXTUAL = "contextual"  # Organisational goal, no causal link stated


class VerificationStatus(str, Enum):
    """Verification status for value claims."""

    VERIFIED = "verified"
    NEEDS_REVIEW = "needs_review"
    REJECTED = "rejected"


class ContextVerificationStatus(str, Enum):
    """Verification status for context claims."""

    VERIFIED = "verified"
    UNVERIFIED = "unverified"
    INFERRED = "inferred"


class EvidenceGrade(str, Enum):
    """Source credibility grade."""

    PRIMARY = "primary"
    SECONDARY_HIGH = "secondary_high"
    SECONDARY_LOW = "secondary_low"


class SourceType(str, Enum):
    """Type of primary source."""

    ORGANISATION_ITSELF = "organisation_itself"
    MAJOR_CONSULTANCY = "major_consultancy"
    TECHNOLOGY_PROVIDER = "technology_provider"
    ACADEMIC_GOVERNMENTAL = "academic_governmental"
    SECONDARY = "secondary"


class ContextClaimType(str, Enum):
    """Types of context claims."""

    TEMPORAL = "temporal"
    ORGANISATIONAL = "organisational"
    SECTORAL = "sectoral"
    FUNCTIONAL = "functional"
    SCALE = "scale"
    STRATEGIC_INTENT = "strategic_intent"
    PRODUCTS_SERVICES = "products_services"


class Mechanism(str, Enum):
    """MECHANISM dimension: How does AI create value?"""

    AUTOMATION = "automation"
    AUGMENTATION = "augmentation"
    OPTIMIZATION = "optimization"
    INNOVATION = "innovation"


class Outcome(str, Enum):
    """OUTCOME dimension: What business result?"""

    VELOCITY = "velocity"
    EXPERIENCE = "experience"
    COST_REDUCTION = "cost_reduction"
    REVENUE_LIFT = "revenue_lift"
    RISK_AVOIDANCE = "risk_avoidance"
    COST_EROSION = "cost_erosion"
    BUSINESS_GROWTH = "business_growth"


class CognitiveDepth(str, Enum):
    """COGNITIVE_DEPTH dimension: What AI sophistication level?"""

    DESCRIPTIVE = "descriptive"
    DIAGNOSTIC = "diagnostic"
    PREDICTIVE = "predictive"
    PRESCRIPTIVE = "prescriptive"
    GENERATIVE = "generative"
    AUTONOMOUS = "autonomous"


class ReviewerVerdict(str, Enum):
    """Human validation verdict."""

    VALID = "valid"
    INVALID = "invalid"
    UNCLEAR = "unclear"


class ValidationTier(str, Enum):
    """Human validation tier."""

    TIER_1 = "tier_1"
    TIER_2_BLIND = "tier_2_blind"
    TIER_3_CALIBRATION = "tier_3_calibration"


class CaseStatus(str, Enum):
    """Overall case status."""

    COMPLETE = "complete"
    NEEDS_REVIEW = "needs_review"
    IN_PROGRESS = "in_progress"


class QuantificationLevel(str, Enum):
    """How the metric is expressed."""

    ABSOLUTE = "absolute"
    RELATIVE = "relative"
    QUALITATIVE = "qualitative"


class MagnitudeBand(str, Enum):
    """Scale of impact."""

    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    TRANSFORMATIONAL = "transformational"


# =============================================================================
# COMPONENT SCHEMAS
# =============================================================================


class MetricRaw(BaseModel):
    """Raw metric as extracted from source."""

    value: str = Field(..., description="Original metric string, e.g., 'SGD 1 billion'")
    currency: Optional[str] = Field(None, description="Currency code if applicable")
    magnitude: Optional[float] = Field(None, description="Numeric value if extractable")
    timeframe: Optional[str] = Field(None, description="Time period if specified")
    metric_type: str = Field(..., description="Type: percentage, currency, count, time, etc.")


class MetricClassification(BaseModel):
    """Standardised metric classification."""

    quantification_level: QuantificationLevel
    magnitude_band: MagnitudeBand


class OntologyConfidence(BaseModel):
    """Confidence scores for ontology assignments."""

    mechanism: float = Field(..., ge=0.0, le=1.0)
    outcome: float = Field(..., ge=0.0, le=1.0)
    cognitive_depth: float = Field(..., ge=0.0, le=1.0)


class HumanValidation(BaseModel):
    """Human validation record for a claim."""

    reviewed: bool = False
    reviewer_verdict: Optional[ReviewerVerdict] = None
    attribution_correct: Optional[bool] = None
    attribution_override: Optional[AIAttribution] = None
    missed_claim: bool = False
    review_notes: Optional[str] = None
    review_date: Optional[datetime] = None
    reviewer_id: Optional[str] = None


class RelatedUrl(BaseModel):
    """URL detected as related to a multi-page source."""

    url: str
    relationship: str = Field(
        ..., description="continuation | chapter | related | pagination"
    )
    pattern_matched: str
    confidence: str = Field(..., description="high | medium | low")
    followed: bool = False
    follow_reason: Optional[str] = None


class MultiPageDetection(BaseModel):
    """Multi-page detection metadata."""

    patterns_found: list[str] = Field(default_factory=list)
    related_urls_detected: list[RelatedUrl] = Field(default_factory=list)
    related_urls_followed: list[str] = Field(default_factory=list)
    detection_method: Optional[str] = None


# =============================================================================
# MAIN SCHEMAS
# =============================================================================


class Source(BaseModel):
    """A source document for a case."""

    id: str = Field(..., description="Source ID, e.g., 'S1'")
    title: str
    url: str
    type: SourceType
    grade: EvidenceGrade
    is_multi_page: bool = False
    related_urls: list[RelatedUrl] = Field(default_factory=list)


class ValueClaim(BaseModel):
    """A claim about how AI created business value."""

    id: str = Field(..., description="Claim ID, e.g., 'VC-001'")

    # Core claim
    claim_title: str
    claim_description: str
    source_ids: list[str]
    source_quote: str
    quote_location: Optional[str] = None

    # Attribution
    ai_attribution: AIAttribution
    attribution_evidence: str

    # Evidence
    verification_status: VerificationStatus
    evidence_type: EvidenceType
    evidence_grade: EvidenceGrade

    # Application
    application_type: ApplicationType

    # Ontology classification
    mechanism: list[Mechanism] = Field(..., min_length=1, max_length=2)
    outcome: list[Outcome] = Field(..., min_length=1, max_length=4)
    cognitive_depth: CognitiveDepth

    # Metrics
    metric_raw: Optional[MetricRaw] = None
    metric_classification: Optional[MetricClassification] = None

    # Ontology metadata
    ontology_version: str = "1.0"
    ontology_confidence: Optional[OntologyConfidence] = None

    # Human validation
    human_validation: HumanValidation = Field(default_factory=HumanValidation)

    @field_validator("mechanism")
    @classmethod
    def validate_mechanism_count(cls, v: list[Mechanism]) -> list[Mechanism]:
        if len(v) > 2:
            raise ValueError("Maximum 2 mechanisms per claim")
        return v

    @field_validator("outcome")
    @classmethod
    def validate_outcome_count(cls, v: list[Outcome]) -> list[Outcome]:
        if len(v) > 4:
            raise ValueError("Maximum 4 outcomes per claim")
        return v


class ContextClaim(BaseModel):
    """A claim about when/where/who was involved."""

    id: str = Field(..., description="Claim ID, e.g., 'CC-001'")

    context_type: ContextClaimType
    claim_title: str
    claim_description: str
    source_ids: list[str]
    source_quote: Optional[str] = None

    verification_status: ContextVerificationStatus
    verification_confidence: str = Field(..., description="high | medium | low")
    inferred_from: Optional[str] = None

    # For functional claims
    apqc_code: Optional[str] = None
    apqc_name: Optional[str] = None

    # Human validation
    human_validation: HumanValidation = Field(default_factory=HumanValidation)


class VerificationSummary(BaseModel):
    """Summary of verification status across claims."""

    class ValueClaimSummary(BaseModel):
        total: int
        verified: int
        needs_review: int
        rejected: int = 0
        by_attribution: dict[str, int] = Field(default_factory=dict)

    class ContextClaimSummary(BaseModel):
        total: int
        verified: int
        unverified: int
        inferred: int

    value_claims: ValueClaimSummary
    context_claims: ContextClaimSummary
    all_value_verified: bool
    all_context_verified: bool


class HumanValidationSummary(BaseModel):
    """Summary of human validation for a case."""

    reviewed: bool
    review_date: Optional[datetime] = None
    reviewer_id: Optional[str] = None
    validation_tier: ValidationTier

    class ClaimValidationSummary(BaseModel):
        valid: int
        invalid: int
        unclear: int
        missed: int = 0

    value_claims: ClaimValidationSummary
    context_claims: Optional[ClaimValidationSummary] = None

    # Only for Tier 2
    precision_score: Optional[float] = None
    recall_score: Optional[float] = None


class OntologyMetadata(BaseModel):
    """Ontology version tracking."""

    version_used: str = "1.0"
    tagged_date: datetime
    needs_retagging: bool = False


class Case(BaseModel):
    """Complete case file representing an AI value creation case."""

    # Identity
    case_id: str
    organisation: str
    title: str
    date_created: datetime
    date_updated: datetime

    # Sources
    sources: list[Source]

    # Claims
    value_claims: list[ValueClaim]
    context_claims: list[ContextClaim] = Field(default_factory=list)

    # Summaries
    verification_summary: VerificationSummary
    human_validation_summary: Optional[HumanValidationSummary] = None

    # Status
    status: CaseStatus
    confidence: str = Field(..., description="high | medium | low")
    review_flags: list[str] = Field(default_factory=list)

    # Ontology
    ontology_metadata: OntologyMetadata


# =============================================================================
# PIPELINE SCHEMAS
# =============================================================================


class SourceExtraction(BaseModel):
    """Extracted content from a source URL."""

    source_id: str
    source_url: str
    fetch_timestamp: datetime
    fetch_status: str  # success | failed | inaccessible
    extraction_method: Optional[str] = None  # trafilatura | beautifulsoup | pypdf
    content_length: Optional[int] = None
    content: Optional[str] = None

    # Multi-page
    is_multi_page: bool = False
    multi_page_detection: MultiPageDetection = Field(default_factory=MultiPageDetection)


class ClaimExtraction(BaseModel):
    """Output of the claim extraction step."""

    case_id: str
    extraction_timestamp: datetime
    model_used: str
    value_claims: list[ValueClaim]
    context_claims: list[ContextClaim]
    extraction_confidence: float


class BuildLog(BaseModel):
    """Pipeline provenance log (build.json)."""

    case_id: str
    build_started: datetime
    build_completed: Optional[datetime] = None

    class StepLog(BaseModel):
        started: datetime
        completed: Optional[datetime] = None
        status: str  # success | failed | skipped
        details: dict = Field(default_factory=dict)

    step_1_discovery: Optional[StepLog] = None
    step_2_extraction: Optional[StepLog] = None
    step_3_claims: Optional[StepLog] = None
    step_4_verification: Optional[StepLog] = None
    step_5_human_validation: Optional[StepLog] = None
