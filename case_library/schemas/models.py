"""
AI Case Library Data Schemas

Pydantic models for the AI Case Library, implementing the specification
defined in docs/specs/AI_CASE_LIBRARY_SPECIFICATION_v1_5.md

Version: 1.5 (aligned with spec v1.5)
"""

from datetime import datetime
from enum import Enum
from typing import Literal, Optional

from pydantic import BaseModel, Field, field_validator, model_validator


# =============================================================================
# ENUMS
# =============================================================================


class ApplicationType(str, Enum):
    """Axis 1: What kind of change does this represent?"""

    CAPABILITY_ENHANCEMENT = "capability_enhancement"
    CAPABILITY_CREATION = "capability_creation"


class EvidenceLevel(str, Enum):
    """Axis 2: Evidence level hierarchy (outcome > adoption > method)."""

    OUTCOME = "outcome"
    ADOPTION = "adoption"
    METHOD = "method"


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
    """Source type: primary vs secondary (Appendix E.3)."""

    PRIMARY = "primary"
    SECONDARY = "secondary"


class SourceOrigin(str, Enum):
    """Who is making the claim about the initiative (Section 4.1)."""

    FIRST_PARTY = "first_party"
    SECOND_PARTY = "second_party"
    THIRD_PARTY = "third_party"


class SourceGrade(str, Enum):
    """Granular source grade (Section 4)."""

    ORGANISATION_ITSELF = "organisation_itself"
    MAJOR_CONSULTANCY = "major_consultancy"
    TECHNOLOGY_PROVIDER = "technology_provider"
    ACADEMIC_GOVERNMENTAL = "academic_governmental"
    OTHER = "other"


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


class MetricType(str, Enum):
    """Type of metric as extracted from source (Appendix E.1)."""

    ABSOLUTE_VALUE = "absolute_value"
    PERCENTAGE = "percentage"
    RATIO = "ratio"
    COUNT = "count"


# =============================================================================
# COMPONENT SCHEMAS
# =============================================================================


class MetricRaw(BaseModel):
    """Raw metric as extracted from source."""

    value: str = Field(..., description="Original metric string, e.g., 'SGD 1 billion'")
    currency: Optional[str] = Field(None, description="Currency code if applicable")
    magnitude: Optional[float] = Field(None, description="Numeric value if extractable")
    timeframe: Optional[str] = Field(None, description="Time period if specified")
    metric_type: MetricType = Field(
        ...,
        description="Classification of metric: absolute_value | percentage | ratio | count",
    )


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
    type: SourceType  # primary | secondary
    origin: SourceOrigin  # first_party | second_party | third_party
    grade: SourceGrade  # e.g., organisation_itself, major_consultancy
    raw_file: str = Field(..., description="Path to captured source file under sources/raw/")
    text_file: str = Field(..., description="Path to extracted text file under sources/text/")
    extraction_method: str = Field(
        ..., description="pypdf | trafilatura | tesseract_ocr (or other deterministic extractor)"
    )
    extraction_quality: Literal["high", "medium", "low"] = "high"
    is_multi_page: bool = False
    related_urls: list[str] = Field(
        default_factory=list,
        description="Related URLs if multi-page content detected",
    )


class ValueClaim(BaseModel):
    """A claim about how AI created business value."""

    id: str = Field(..., description="Claim ID, e.g., 'VC-001'")

    # Core claim
    claim_title: str
    claim_description: str
    source_ids: list[str]
    source_quote: str
    quote_location: Optional[str] = None
    quote_source_id: Optional[str] = None  # source where source_quote was verified (e.g. S1)

    # Attribution
    ai_attribution: AIAttribution
    attribution_evidence: str

    # Evidence
    verification_status: VerificationStatus
    evidence_level: EvidenceLevel
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

    @model_validator(mode="after")
    def validate_metric_for_evidence_level(self) -> "ValueClaim":
        """
        Enforce metric_raw requirement for outcome/adoption evidence levels.

        By definition (spec §3.2.1), outcome and adoption claims are quantified.
        Therefore, metric_raw (with value and metric_type) must be present
        whenever evidence_level is outcome or adoption.
        """

        if self.evidence_level in {EvidenceLevel.OUTCOME, EvidenceLevel.ADOPTION}:
            if self.metric_raw is None:
                raise ValueError(
                    f"metric_raw required for {self.evidence_level.value}-level claims"
                )
            if not self.metric_raw.value or not self.metric_raw.metric_type:
                raise ValueError(
                    f"metric_raw.value and metric_raw.metric_type required for "
                    f"{self.evidence_level.value}-level claims"
                )
        return self


class ContextClaim(BaseModel):
    """A claim about when/where/who was involved."""

    id: str = Field(..., description="Claim ID, e.g., 'CC-001'")

    context_type: ContextClaimType
    claim_title: str
    claim_description: Optional[str] = None
    source_ids: list[str]
    source_quote: Optional[str] = None

    verification_status: ContextVerificationStatus
    verification_confidence: Optional[str] = Field(
        None,
        description="high | medium | low",
    )
    inferred_from: Optional[str] = None

    # For functional claims
    apqc_code: Optional[str] = None
    apqc_name: Optional[str] = None

    # Human validation
    human_validation: HumanValidation = Field(default_factory=HumanValidation)

    @model_validator(mode="after")
    def validate_source_and_functional_requirements(self) -> "ContextClaim":
        """
        Enforce Appendix E.2:

        - source_ids: at least one, unless verification_status == inferred.
        - If verification_status == inferred, inferred_from must be populated.
        - For functional context_type, apqc_code and apqc_name are required.
        """

        if self.verification_status == ContextVerificationStatus.INFERRED:
            if self.inferred_from is None:
                raise ValueError(
                    "inferred_from must be provided when verification_status is 'inferred'"
                )
            # For inferred claims source_ids may be empty.
        else:
            if not self.source_ids:
                raise ValueError(
                    "At least one source_id is required unless verification_status is 'inferred'"
                )

        if self.context_type == ContextClaimType.FUNCTIONAL:
            if not self.apqc_code or not self.apqc_name:
                raise ValueError(
                    "apqc_code and apqc_name are required for functional context claims"
                )

        return self


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


class Casefile(BaseModel):
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

    # Case-level evidence level (highest among value_claims)
    evidence_level: Optional[EvidenceLevel] = None

    # Summaries
    verification_summary: VerificationSummary
    human_validation_summary: Optional[HumanValidationSummary] = None

    # Status
    status: CaseStatus
    confidence: str = Field(..., description="high | medium | low")
    review_flags: list[str] = Field(default_factory=list)

    # Ontology
    ontology_metadata: OntologyMetadata

    @model_validator(mode="after")
    def derive_case_evidence_level(self) -> "Casefile":
        """
        Derive case-level evidence_level as the highest evidence level
        present among all value_claims, regardless of verification_status.

        Hierarchy: outcome (3) > adoption (2) > method (1).
        """

        if not self.value_claims:
            return self

        if self.evidence_level is None:
            rank = {
                EvidenceLevel.METHOD: 1,
                EvidenceLevel.ADOPTION: 2,
                EvidenceLevel.OUTCOME: 3,
            }
            highest = max(self.value_claims, key=lambda c: rank[c.evidence_level]).evidence_level
            self.evidence_level = highest
        return self


# Backwards-compatibility alias (older code may import Case)
Case = Casefile


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

    class Step1DiscoveryLog(BaseModel):
        model: Optional[str] = None
        search_queries: list[str] = Field(default_factory=list)
        results_considered: Optional[int] = None
        urls_ranked: list[dict] = Field(default_factory=list)
        urls_selected: list[str] = Field(default_factory=list)
        retries: int = 0

    class Step2ExtractionSourceLog(BaseModel):
        source_id: str
        url: str
        http_status: Optional[int] = None
        retries: int = 0
        raw_file: Optional[str] = None
        text_file: Optional[str] = None
        extraction_method: Optional[str] = None
        extraction_quality: Optional[str] = None
        content_length: Optional[int] = None
        ocr_fallback_used: bool = False
        is_multi_page: bool = False
        multi_page_detection: MultiPageDetection = Field(
            default_factory=MultiPageDetection
        )

    class Step2ExtractionLog(BaseModel):
        sources: list["BuildLog.Step2ExtractionSourceLog"] = Field(default_factory=list)
        multi_page_candidates: list[str] = Field(default_factory=list)
        multi_page_followed: list[str] = Field(default_factory=list)
        deduplication: Optional[dict] = Field(
            default=None,
            description="Deduplication results: kept_count, dropped sources with reasons",
        )

    class Step3ClaimsLog(BaseModel):
        model: Optional[str] = None
        prompt_version: Optional[str] = None
        raw_response_file: Optional[str] = None
        claims_file: Optional[str] = None
        value_claims_count: int = 0
        context_claims_count: int = 0
        retries_malformed_json: int = 0
        retries_zero_claims: int = 0
        skipped_no_sources: bool = False
        claims_downgraded_metric_missing: int = 0
        context_claims_coerced_inferred: int = 0
        value_claims_dropped_invalid: int = 0
        context_claims_dropped_invalid: int = 0

    class VerificationAttempt(BaseModel):
        claim_id: str
        source_id: str
        method: str
        result: str
        char_offset_start: Optional[int] = None
        char_offset_end: Optional[int] = None
        match_confidence: Optional[float] = None
        ai_explanation: Optional[str] = None

    class Step4VerificationLog(BaseModel):
        model: Optional[str] = None
        verification_attempts: list["BuildLog.VerificationAttempt"] = Field(
            default_factory=list
        )
        verification_summary: Optional[VerificationSummary] = None

    class Step5HumanValidationLog(BaseModel):
        tier: ValidationTier
        reviewer_id: Optional[str] = None
        review_date: Optional[datetime] = None
        time_taken_minutes: Optional[int] = None
        claims_reviewed: Optional[int] = None
        verdicts: dict = Field(default_factory=dict)
        missed_claims_added: int = 0
        precision_score: Optional[float] = None
        recall_score: Optional[float] = None

    step_1_discovery: Optional[Step1DiscoveryLog] = None
    step_2_extraction: Optional[Step2ExtractionLog] = None
    step_3_claims: Optional[Step3ClaimsLog] = None
    step_4_verification: Optional[Step4VerificationLog] = None
    step_5_human_validation: Optional[Step5HumanValidationLog] = None


class SeedEntry(BaseModel):
    """
    Seed list entry derived from legacy cases (OLD_cases_enriched).

    Used only for input to the new provenance pipeline; does not carry over
    any legacy claims or ontology tags.
    """

    organisation: str
    initiative_description: str
    original_case_id: str
    legacy_urls: list[str] = Field(default_factory=list)
    research_priority: Literal["high", "medium", "low"] = "medium"
    notes: Optional[str] = None


# =============================================================================
# OVERLAY METADATA (classification overlays)
# =============================================================================


class OverlayCoverage(BaseModel):
    """Coverage stats for an overlay."""

    total_cases: Optional[int] = None
    classified_cases: Optional[int] = None
    coverage_percent: Optional[float] = None


class OverlayMetadata(BaseModel):
    """
    Metadata for a classification overlay (overlays/<name>/metadata.json).
    """

    overlay_id: str
    display_name: str
    description: str = ""
    version: str = "1.0"
    created_date: Optional[str] = None
    last_updated: Optional[str] = None
    maintainer: Optional[str] = None
    coverage: Optional[OverlayCoverage] = None
