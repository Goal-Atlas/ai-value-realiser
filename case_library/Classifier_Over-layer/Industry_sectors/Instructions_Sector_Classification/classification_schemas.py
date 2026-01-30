"""
ISIC Industry Classification Schemas

Pydantic models for structured output when classifying AI case studies
by industry using the ISIC Rev 5 taxonomy.

Usage:
    from classification_schemas import ISICClassification
    
    # Use with Claude API structured output
    response = client.messages.create(
        model="claude-sonnet-4-5-20250514",
        max_tokens=1024,
        messages=[...],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "isic_classification",
                "schema": ISICClassification.model_json_schema()
            }
        }
    )
"""

from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class ConfidenceLevel(str, Enum):
    """Confidence level for the classification."""
    HIGH = "high"      # Clear industry match, specific details in case description
    MEDIUM = "medium"  # Reasonable inference, some ambiguity
    LOW = "low"        # Best guess, limited industry information available


class ClassificationGranularity(str, Enum):
    """Whether division-level or only section-level classification was possible."""
    DIVISION = "division"  # Full classification to division level (e.g., C26)
    SECTION = "section"    # Only section-level possible (e.g., C)


class ISICClassification(BaseModel):
    """
    ISIC industry classification for an AI case study.
    
    The classification follows ISIC Rev 5 hierarchy:
    - Section: Single letter (A-V), 22 total
    - Division: Letter + 2 digits (e.g., C26), 87 total
    
    When case description lacks sufficient detail for division-level
    classification, only section is assigned.
    """
    
    # Required fields
    section_code: str = Field(
        ...,
        pattern=r"^[A-V]$",
        description="ISIC section code (single letter A-V)"
    )
    section_name: str = Field(
        ...,
        description="Full name of the ISIC section"
    )
    
    # Division fields (optional - may not be determinable)
    division_code: Optional[str] = Field(
        None,
        pattern=r"^[A-V]\d{2}$",
        description="ISIC division code (letter + 2 digits, e.g., C26). Null if only section-level classification possible."
    )
    division_name: Optional[str] = Field(
        None,
        description="Full name of the ISIC division. Null if only section-level classification possible."
    )
    
    # Metadata
    granularity: ClassificationGranularity = Field(
        ...,
        description="Whether classification reached division or only section level"
    )
    confidence: ConfidenceLevel = Field(
        ...,
        description="Confidence level in the classification"
    )
    rationale: str = Field(
        ...,
        min_length=20,
        max_length=500,
        description="Brief explanation of why this classification was chosen, citing specific evidence from the case description"
    )
    
    # For explainability - what text drove the decision
    key_indicators: list[str] = Field(
        ...,
        min_length=1,
        max_length=5,
        description="1-5 specific phrases or facts from the case description that informed the classification"
    )


class CaseClassificationRequest(BaseModel):
    """Input structure for a case to be classified."""
    case_id: str = Field(..., description="Unique identifier for the case")
    case_title: str = Field(..., description="Title of the AI case study")
    case_description: str = Field(..., description="Full description of the case study")
    organisation_name: Optional[str] = Field(None, description="Name of the organisation in the case (if known)")


class CaseClassificationResult(BaseModel):
    """Complete result combining input case with its classification."""
    case_id: str
    case_title: str
    classification: ISICClassification
    

# For batch processing
class BatchClassificationResult(BaseModel):
    """Results from classifying multiple cases."""
    results: list[CaseClassificationResult]
    total_cases: int
    division_level_count: int = Field(
        ..., 
        description="Number of cases classified to division level"
    )
    section_only_count: int = Field(
        ..., 
        description="Number of cases only classified to section level"
    )


# Validation helper
def validate_division_matches_section(classification: ISICClassification) -> bool:
    """
    Verify that division code's letter matches section code.
    E.g., division C26 must have section C.
    """
    if classification.division_code is None:
        return True
    return classification.division_code[0] == classification.section_code


if __name__ == "__main__":
    # Print the JSON schema for use with Claude API
    import json
    print("=== ISICClassification JSON Schema ===")
    print(json.dumps(ISICClassification.model_json_schema(), indent=2))
