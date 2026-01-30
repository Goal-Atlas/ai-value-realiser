"""
APQC Work Function Classification Schemas for AI Case Library Claims

Version 2.0 - Enhanced with misclassification prevention

Pydantic models for structured output when classifying claims from AI case studies
by work function using the APQC Process Classification Framework (PCF).

Key enhancements in v2.0:
- trap_check field to verify common misclassification patterns were considered
- Keyword detection for post-classification validation
- Category mismatch detection
- Integration with validation pipeline

Usage:
    from apqc_classification_schemas import APQCClaimClassification
    
    # Use with Claude API structured output
    response = client.messages.create(
        model="claude-sonnet-4-5-20250514",
        max_tokens=1024,
        messages=[...],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "apqc_claim_classification",
                "schema": APQCClaimClassification.model_json_schema()
            }
        }
    )
"""

from enum import Enum
from typing import Optional, Union
from pydantic import BaseModel, Field, model_validator


class ConfidenceLevel(str, Enum):
    """Confidence level for the classification."""
    HIGH = "high"      # Clear function match, no ambiguity
    MEDIUM = "medium"  # Reasonable inference, some interpretation required
    LOW = "low"        # Limited information, best guess - flag for human review


class ClassificationGranularity(str, Enum):
    """Whether process group (Level 2) or only category (Level 1) classification was possible."""
    PROCESS_GROUP = "process_group"  # Full classification to Level 2 (e.g., 8.5)
    CATEGORY = "category"            # Only Level 1 possible (e.g., 8.0)


class TrapCheck(BaseModel):
    """
    Verification that common misclassification traps were considered.
    
    The classifier must explicitly confirm it checked for these patterns.
    """
    verified_not_it: Union[bool, str] = Field(
        ...,
        description="Confirmed this isn't incorrectly tagged as IT (8.x) just because AI is involved. Use string 'N/A - this IS correctly IT' if 8.x is genuinely correct."
    )
    verified_not_finance_trap: Union[bool, str] = Field(
        ...,
        description="Confirmed cost/savings mentions didn't incorrectly trigger finance (9.x) when the function is HR, manufacturing, etc. Use string if N/A."
    )
    verified_correct_dev_vs_mfg: Union[bool, str] = Field(
        ...,
        description="Confirmed correct distinction between product development (2.x) and manufacturing (4.x). Use string 'N/A' if not applicable."
    )


class APQCClaimClassification(BaseModel):
    """
    APQC work function classification for a claim within an AI case study.
    
    The classification follows APQC PCF hierarchy:
    - Category (Level 1): X.0 format (e.g., "8.0"), 13 total
    - Process Group (Level 2): X.Y format (e.g., "8.5"), 72 total
    
    Claims describe specific AI applications, so classification should focus on
    WHICH BUSINESS PROCESS the AI is being applied to, not the AI technology itself.
    """
    
    # Required fields - Category (Level 1)
    category_id: str = Field(
        ...,
        pattern=r"^\d{1,2}\.0$",
        description="APQC category ID (Level 1), format X.0 or XX.0 (e.g., '8.0', '13.0')"
    )
    category_name: str = Field(
        ...,
        description="Full name of the APQC category"
    )
    
    # Process Group fields (Level 2) - optional if only category determinable
    process_group_id: Optional[str] = Field(
        None,
        pattern=r"^\d{1,2}\.\d{1,2}$",
        description="APQC process group ID (Level 2), format X.Y or XX.YY (e.g., '8.5', '13.7'). Null if only category-level classification possible."
    )
    process_group_name: Optional[str] = Field(
        None,
        description="Full name of the APQC process group. Null if only category-level classification possible."
    )
    
    # Metadata
    granularity: ClassificationGranularity = Field(
        ...,
        description="Whether classification reached process group (Level 2) or only category (Level 1)"
    )
    confidence: ConfidenceLevel = Field(
        ...,
        description="Confidence level in the classification"
    )
    rationale: str = Field(
        ...,
        min_length=20,
        max_length=500,
        description="Brief explanation of why this work function was chosen, citing specific evidence from the claim"
    )
    
    # For explainability - what text drove the decision
    key_indicators: list[str] = Field(
        ...,
        min_length=1,
        max_length=5,
        description="1-5 specific phrases or concepts from the claim that informed the classification"
    )
    
    # Trap verification (new in v2.0)
    trap_check: TrapCheck = Field(
        ...,
        description="Verification that common misclassification traps were considered"
    )
    
    @model_validator(mode='after')
    def validate_process_group_matches_category(self):
        """Verify that process group ID's category prefix matches category ID."""
        if self.process_group_id is not None:
            pg_category = self.process_group_id.split('.')[0]
            cat_prefix = self.category_id.split('.')[0]
            if pg_category != cat_prefix:
                raise ValueError(
                    f"Process group {self.process_group_id} doesn't match category {self.category_id}"
                )
        return self
    
    @model_validator(mode='after')
    def validate_granularity_consistency(self):
        """Verify granularity matches presence of process_group_id."""
        if self.granularity == ClassificationGranularity.PROCESS_GROUP and self.process_group_id is None:
            raise ValueError("Granularity is 'process_group' but process_group_id is null")
        if self.granularity == ClassificationGranularity.CATEGORY and self.process_group_id is not None:
            raise ValueError("Granularity is 'category' but process_group_id is provided")
        return self


class ClaimInput(BaseModel):
    """Structure of a claim to be classified."""
    claim_id: str = Field(..., description="Unique identifier for the claim")
    claim_text: str = Field(..., description="The claim statement text")
    mechanism: Optional[str] = Field(None, description="How the AI achieves the outcome (if available)")
    outcome: Optional[str] = Field(None, description="The business outcome achieved (if available)")
    case_id: Optional[str] = Field(None, description="Parent case ID for context")
    case_title: Optional[str] = Field(None, description="Parent case title for context")
    organisation_name: Optional[str] = Field(None, description="Organisation name for context")
    
    def to_prompt_text(self) -> str:
        """Format claim for inclusion in API prompt."""
        return f"""**Claim ID:** {self.claim_id}
**Claim Text:** {self.claim_text}
**Mechanism:** {self.mechanism or 'Not specified'}
**Outcome:** {self.outcome or 'Not specified'}
**Case Context:** {self.case_title or 'Unknown'} ({self.organisation_name or 'Unknown'})"""


class ClaimClassificationResult(BaseModel):
    """Complete result combining input claim with its classification."""
    claim_id: str
    case_id: Optional[str] = None
    classification: APQCClaimClassification
    
    # Validation flags (populated by post-classification validation)
    validation_passed: Optional[bool] = Field(None, description="Whether post-classification validation passed")
    validation_warnings: Optional[list[str]] = Field(None, description="Any validation warnings")
    validation_errors: Optional[list[str]] = Field(None, description="Any validation errors")


class BatchClaimClassificationResult(BaseModel):
    """Results from classifying multiple claims."""
    results: list[ClaimClassificationResult]
    total_claims: int
    process_group_level_count: int = Field(
        ..., 
        description="Number of claims classified to process group level"
    )
    category_only_count: int = Field(
        ..., 
        description="Number of claims only classified to category level"
    )
    high_confidence_count: int = Field(
        default=0,
        description="Number of claims with high confidence"
    )
    needs_review_count: int = Field(
        default=0,
        description="Number of claims with low confidence or validation warnings"
    )
    
    # Distribution summary
    category_distribution: dict[str, int] = Field(
        default_factory=dict,
        description="Count of claims per category (Level 1)"
    )


# Quick reference for valid IDs
VALID_CATEGORY_IDS = [
    "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", 
    "8.0", "9.0", "10.0", "11.0", "12.0", "13.0"
]

CATEGORY_NAMES = {
    "1.0": "Develop Vision and Strategy",
    "2.0": "Develop and Manage Products and Services",
    "3.0": "Market and Sell Products and Services",
    "4.0": "Manage Supply Chain for Physical Products",
    "5.0": "Deliver Services",
    "6.0": "Manage Customer Service",
    "7.0": "Develop and Manage Human Capital",
    "8.0": "Manage Information Technology (IT)",
    "9.0": "Manage Financial Resources",
    "10.0": "Acquire, Construct, and Manage Assets",
    "11.0": "Manage Enterprise Risk, Compliance, Remediation, and Resiliency",
    "12.0": "Manage External Relationships",
    "13.0": "Develop and Manage Business Capabilities",
}


def get_category_from_process_group(process_group_id: str) -> str:
    """
    Extract category ID from process group ID.
    E.g., "8.5" -> "8.0", "13.7" -> "13.0"
    """
    category_num = process_group_id.split('.')[0]
    return f"{category_num}.0"


if __name__ == "__main__":
    # Print the JSON schema for use with Claude API
    import json
    print("=== APQCClaimClassification JSON Schema ===")
    print(json.dumps(APQCClaimClassification.model_json_schema(), indent=2))
