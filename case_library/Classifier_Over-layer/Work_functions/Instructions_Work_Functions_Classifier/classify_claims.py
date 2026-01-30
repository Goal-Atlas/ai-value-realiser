#!/usr/bin/env python3
"""
APQC Classification Runner

Integrated classification pipeline that:
1. Calls Claude API with comprehensive prompt
2. Validates response using keyword detection
3. Flags potential misclassifications before saving
4. Supports batch processing with cost tracking

Usage:
    from classify_claims import APQCClassifier
    
    classifier = APQCClassifier()
    result = classifier.classify_claim(claim)
    
    # Or batch:
    results = classifier.classify_batch(claims)
"""

import json
import os
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, field
from datetime import datetime

# Try to import anthropic, but allow module to load without it for schema-only use
try:
    from anthropic import Anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False

from apqc_classification_schemas import (
    APQCClaimClassification,
    ClaimInput,
    ClaimClassificationResult,
    BatchClaimClassificationResult,
    ConfidenceLevel,
)

from validate_apqc_classification import (
    validate_apqc_classification,
    load_apqc_reference,
)


# =============================================================================
# CONFIGURATION
# =============================================================================

@dataclass
class ClassifierConfig:
    """Configuration for the APQC classifier."""
    model: str = "claude-sonnet-4-5-20250514"
    max_tokens: int = 1500
    temperature: float = 0.1  # Low temperature for consistent classification
    taxonomy_file: Path = Path("apqc_taxonomy.json")
    prompt_file: Path = Path("apqc_classification_prompt.md")
    validate_after_classification: bool = True
    flag_low_confidence: bool = True
    cost_tracking: bool = True


@dataclass
class CostTracker:
    """Track API costs."""
    input_tokens: int = 0
    output_tokens: int = 0
    calls: int = 0
    
    # Pricing as of Jan 2025 (Sonnet)
    INPUT_COST_PER_M: float = 3.00
    OUTPUT_COST_PER_M: float = 15.00
    
    def add_call(self, input_tokens: int, output_tokens: int):
        self.input_tokens += input_tokens
        self.output_tokens += output_tokens
        self.calls += 1
    
    @property
    def total_cost(self) -> float:
        return (
            (self.input_tokens / 1_000_000) * self.INPUT_COST_PER_M +
            (self.output_tokens / 1_000_000) * self.OUTPUT_COST_PER_M
        )
    
    def summary(self) -> str:
        return (
            f"API Calls: {self.calls}\n"
            f"Input tokens: {self.input_tokens:,}\n"
            f"Output tokens: {self.output_tokens:,}\n"
            f"Estimated cost: ${self.total_cost:.2f}"
        )


# =============================================================================
# CLASSIFIER
# =============================================================================

class APQCClassifier:
    """
    APQC Work Function Classifier with integrated validation.
    """
    
    def __init__(self, config: Optional[ClassifierConfig] = None):
        self.config = config or ClassifierConfig()
        self.cost_tracker = CostTracker() if self.config.cost_tracking else None
        
        # Load taxonomy
        self.taxonomy = self._load_taxonomy()
        
        # Load APQC lookup for validation
        self.apqc_lookup = load_apqc_reference(self.config.taxonomy_file)
        
        # Build system prompt
        self.system_prompt = self._build_system_prompt()
        
        # Initialize API client
        if ANTHROPIC_AVAILABLE:
            self.client = Anthropic()
        else:
            self.client = None
    
    def _load_taxonomy(self) -> dict:
        """Load APQC taxonomy from JSON file."""
        if self.config.taxonomy_file.exists():
            with open(self.config.taxonomy_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            raise FileNotFoundError(f"Taxonomy file not found: {self.config.taxonomy_file}")
    
    def _build_system_prompt(self) -> str:
        """Build the system prompt with embedded taxonomy."""
        # Load prompt template
        if self.config.prompt_file.exists():
            with open(self.config.prompt_file, 'r', encoding='utf-8') as f:
                template = f.read()
        else:
            # Use inline minimal prompt if file not found
            template = self._get_minimal_prompt()
        
        # Insert taxonomy
        taxonomy_json = json.dumps(self.taxonomy, indent=2)
        prompt = template.replace("{INSERT_TAXONOMY_HERE}", taxonomy_json)
        
        return prompt
    
    def _get_minimal_prompt(self) -> str:
        """Minimal prompt if full template not available."""
        return """You are a business process classification specialist. Classify claims by BUSINESS WORK FUNCTION using APQC PCF.

CRITICAL: Classify the BUSINESS PROCESS being improved, NOT the AI technology.

## APQC PCF Taxonomy
{INSERT_TAXONOMY_HERE}

## Output Format
Return JSON with: category_id, category_name, process_group_id, process_group_name, granularity, confidence, rationale, key_indicators, trap_check
"""
    
    def classify_claim(self, claim: ClaimInput) -> ClaimClassificationResult:
        """
        Classify a single claim.
        
        Args:
            claim: ClaimInput object with claim details
        
        Returns:
            ClaimClassificationResult with classification and validation
        """
        if not ANTHROPIC_AVAILABLE or not self.client:
            raise RuntimeError("Anthropic client not available. Install anthropic package.")
        
        # Build user message
        user_message = f"""Classify the following claim by work function:

{claim.to_prompt_text()}

Remember:
1. Follow the Decision Tree
2. Check for the 5 common traps
3. Include trap_check in your response"""
        
        # Call API
        response = self.client.messages.create(
            model=self.config.model,
            max_tokens=self.config.max_tokens,
            temperature=self.config.temperature,
            system=self.system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )
        
        # Track costs
        if self.cost_tracker:
            self.cost_tracker.add_call(
                response.usage.input_tokens,
                response.usage.output_tokens
            )
        
        # Parse response
        try:
            response_text = response.content[0].text
            
            # Extract JSON from response (handle markdown code blocks)
            if "```json" in response_text:
                json_str = response_text.split("```json")[1].split("```")[0].strip()
            elif "```" in response_text:
                json_str = response_text.split("```")[1].split("```")[0].strip()
            else:
                json_str = response_text.strip()
            
            classification = APQCClaimClassification.model_validate_json(json_str)
        except Exception as e:
            # Return error result
            return ClaimClassificationResult(
                claim_id=claim.claim_id,
                case_id=claim.case_id,
                classification=None,
                validation_passed=False,
                validation_errors=[f"Failed to parse API response: {str(e)}"],
            )
        
        # Build result
        result = ClaimClassificationResult(
            claim_id=claim.claim_id,
            case_id=claim.case_id,
            classification=classification,
        )
        
        # Validate if enabled
        if self.config.validate_after_classification:
            validation = validate_apqc_classification(
                apqc_code=classification.process_group_id or classification.category_id,
                apqc_name=classification.process_group_name or classification.category_name,
                claim_text=claim.claim_text,
                strategic_fit=claim.mechanism or "",
                outcome=claim.outcome or "",
                apqc_lookup=self.apqc_lookup
            )
            
            result.validation_passed = validation.is_valid
            result.validation_warnings = validation.warnings if validation.warnings else None
            result.validation_errors = validation.errors if validation.errors else None
            
            # Flag low confidence
            if self.config.flag_low_confidence and classification.confidence == ConfidenceLevel.LOW:
                if result.validation_warnings is None:
                    result.validation_warnings = []
                result.validation_warnings.append("LOW_CONFIDENCE: Classification marked for human review")
        
        return result
    
    def classify_batch(
        self,
        claims: list[ClaimInput],
        progress_callback: Optional[callable] = None
    ) -> BatchClaimClassificationResult:
        """
        Classify multiple claims.
        
        Args:
            claims: List of ClaimInput objects
            progress_callback: Optional function called with (current, total) for progress updates
        
        Returns:
            BatchClaimClassificationResult with all results and summary
        """
        results = []
        category_dist = {}
        pg_count = 0
        cat_count = 0
        high_conf_count = 0
        needs_review_count = 0
        
        for i, claim in enumerate(claims):
            if progress_callback:
                progress_callback(i + 1, len(claims))
            
            result = self.classify_claim(claim)
            results.append(result)
            
            if result.classification:
                # Update stats
                cat_id = result.classification.category_id
                category_dist[cat_id] = category_dist.get(cat_id, 0) + 1
                
                if result.classification.granularity.value == "process_group":
                    pg_count += 1
                else:
                    cat_count += 1
                
                if result.classification.confidence == ConfidenceLevel.HIGH:
                    high_conf_count += 1
                
                if (result.classification.confidence == ConfidenceLevel.LOW or
                    result.validation_warnings or result.validation_errors):
                    needs_review_count += 1
        
        return BatchClaimClassificationResult(
            results=results,
            total_claims=len(claims),
            process_group_level_count=pg_count,
            category_only_count=cat_count,
            high_confidence_count=high_conf_count,
            needs_review_count=needs_review_count,
            category_distribution=category_dist,
        )
    
    def get_cost_summary(self) -> str:
        """Get cost tracking summary."""
        if self.cost_tracker:
            return self.cost_tracker.summary()
        return "Cost tracking disabled"


# =============================================================================
# PIPELINE INTEGRATION HELPERS
# =============================================================================

def integrate_with_enrichment_pipeline(
    audit_data: dict,
    classifier: APQCClassifier,
    update_existing: bool = False
) -> tuple[dict, list[str]]:
    """
    Integrate APQC classification into existing enrichment pipeline.
    
    Args:
        audit_data: Audit data dict with 'audited_claims'
        classifier: APQCClassifier instance
        update_existing: If True, reclassify claims that already have APQC codes
    
    Returns:
        tuple: (updated_audit_data, list of warnings)
    """
    warnings = []
    
    for claim in audit_data.get('audited_claims', []):
        claim_id = claim.get('claim_id', 'unknown')
        
        # Check if already classified
        apqc_key = 'apqc_functions' if 'apqc_functions' in claim else 'apqc_work_functions'
        existing = claim.get(apqc_key, [])
        
        if existing and not update_existing:
            continue
        
        # Build ClaimInput
        claim_input = ClaimInput(
            claim_id=claim_id,
            claim_text=claim.get('strategic_fit_assessment', '') or claim.get('claim_text', ''),
            mechanism=claim.get('mechanism', ''),
            outcome=claim.get('outcome', ''),
            case_id=audit_data.get('case_id'),
            case_title=audit_data.get('case_title'),
        )
        
        # Classify
        result = classifier.classify_claim(claim_input)
        
        if result.classification:
            # Convert to storage format
            apqc_entry = {
                'id': result.classification.process_group_id or result.classification.category_id,
                'name': result.classification.process_group_name or result.classification.category_name,
                'confidence': result.classification.confidence.value,
                'granularity': result.classification.granularity.value,
                'rationale': result.classification.rationale,
            }
            
            claim[apqc_key] = [apqc_entry]
            
            # Track warnings
            if result.validation_warnings:
                for w in result.validation_warnings:
                    warnings.append(f"{claim_id}: {w}")
            if result.validation_errors:
                for e in result.validation_errors:
                    warnings.append(f"{claim_id}: ERROR - {e}")
    
    return audit_data, warnings


# =============================================================================
# STANDALONE EXECUTION
# =============================================================================

def main():
    """Demo/test the classifier."""
    print("=== APQC Classifier Demo ===\n")
    
    # Check for API key
    if not os.environ.get('ANTHROPIC_API_KEY'):
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        return
    
    # Check for required files
    config = ClassifierConfig()
    if not config.taxonomy_file.exists():
        print(f"Error: Taxonomy file not found: {config.taxonomy_file}")
        print("Run this from the directory containing apqc_taxonomy.json")
        return
    
    # Initialize classifier
    classifier = APQCClassifier(config)
    print(f"Loaded taxonomy with {len(classifier.taxonomy)} categories")
    print(f"System prompt: {len(classifier.system_prompt):,} characters\n")
    
    # Test claim
    test_claim = ClaimInput(
        claim_id="TEST-001",
        claim_text="AI-powered recruitment screening reduced time-to-hire by 40% and cut hiring costs by $2M annually",
        mechanism="NLP analysis of resumes matched against job requirements",
        outcome="Faster hiring, cost savings",
        case_id="TEST-CASE",
        case_title="HR Transformation",
        organisation_name="Test Corp"
    )
    
    print("Test claim:")
    print(test_claim.to_prompt_text())
    print()
    
    print("Classifying...")
    result = classifier.classify_claim(test_claim)
    
    print("\nResult:")
    if result.classification:
        c = result.classification
        print(f"  Category: {c.category_id} - {c.category_name}")
        print(f"  Process Group: {c.process_group_id} - {c.process_group_name}")
        print(f"  Granularity: {c.granularity.value}")
        print(f"  Confidence: {c.confidence.value}")
        print(f"  Rationale: {c.rationale}")
        print(f"  Key indicators: {c.key_indicators}")
        print(f"  Trap check: {c.trap_check}")
    
    print(f"\nValidation passed: {result.validation_passed}")
    if result.validation_warnings:
        print(f"Warnings: {result.validation_warnings}")
    if result.validation_errors:
        print(f"Errors: {result.validation_errors}")
    
    print(f"\n{classifier.get_cost_summary()}")


if __name__ == "__main__":
    main()
