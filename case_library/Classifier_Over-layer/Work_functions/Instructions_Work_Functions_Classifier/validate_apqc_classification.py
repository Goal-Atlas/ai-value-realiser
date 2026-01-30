#!/usr/bin/env python3
"""
APQC Classification Validation Module

Validates APQC codes against claim content using keyword detection to catch
common misclassification patterns. Can be used:
1. Post-classification to validate API responses
2. As part of enrichment pipeline before saving
3. As standalone audit tool

Version 2.0 - incorporates patterns from 231 misclassification fixes
"""

import json
import re
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, field


# =============================================================================
# KEYWORD DEFINITIONS FOR CATEGORY DETECTION
# =============================================================================

CATEGORY_KEYWORDS = {
    'hr': {
        'keywords': [
            'recruitment', 'recruiting', 'hiring', 'hire', 'hires',
            'employee', 'employees', 'workforce', 'talent', 'talents',
            'hr', 'human resources', 'staffing', 'staff',
            'reskilling', 'upskilling', 'training employees',
            'candidate', 'candidates', 'applicant', 'applicants',
            'onboarding', 'retention', 'turnover',
            'job posting', 'job description', 'resume', 'cv',
            'interview', 'interviewing', 'headcount',
        ],
        'apqc_prefix': '7.',
        'common_wrong_codes': ['9.1', '9.2', '9.3'],  # Often wrongly tagged as finance
    },
    'product_dev': {
        'keywords': [
            'product design', 'product development', 'r&d', 'research and development',
            'generative design', 'design iteration', 'prototype', 'prototyping',
            'new product', 'innovation', 'concept design', 'engineering design',
            'cad', 'computer-aided design', 'design optimization',
            'product lifecycle', 'plm', 'ideation',
        ],
        'apqc_prefix': '2.',
        'common_wrong_codes': ['4.3', '4.1'],  # Often wrongly tagged as manufacturing
    },
    'manufacturing': {
        'keywords': [
            'manufacturing', 'manufacture', 'production', 'production line',
            'assembly', 'assembly line', 'factory', 'plant',
            'quality control', 'quality inspection', 'defect detection',
            'yield', 'scrap', 'throughput', 'oee',
            'cnc', 'machining', 'fabrication',
            'production schedule', 'shop floor',
        ],
        'apqc_prefix': '4.',
        'common_wrong_codes': ['2.3', '2.1'],  # Often wrongly tagged as product dev
    },
    'finance': {
        'keywords': [
            'accounting', 'accounts payable', 'accounts receivable',
            'ap', 'ar', 'invoice', 'invoicing', 'invoice processing',
            'financial reporting', 'financial statements', 'ledger',
            'treasury', 'cash management', 'payroll processing',
            'expense', 'expense management', 'reimbursement',
            'audit', 'auditing', 'compliance reporting',
            'tax', 'taxation', 'budgeting', 'forecasting financial',
        ],
        'apqc_prefix': '9.',
        'common_wrong_codes': ['2.3', '7.2'],  # Sometimes wrongly tagged
    },
    'customer_service': {
        'keywords': [
            'customer service', 'customer support', 'customer inquiry',
            'customer complaint', 'call center', 'call centre', 'contact center',
            'support ticket', 'helpdesk', 'help desk',
            'customer satisfaction', 'csat', 'nps',
            'customer query', 'customer question',
            'service request', 'case management',
        ],
        'apqc_prefix': '6.',
        'common_wrong_codes': ['8.7', '8.1'],  # Often wrongly tagged as IT
    },
    'risk': {
        'keywords': [
            'fraud', 'fraud detection', 'fraudulent',
            'risk', 'risk management', 'risk assessment',
            'compliance', 'regulatory', 'aml', 'anti-money laundering',
            'kyc', 'know your customer', 'security threat',
            'vulnerability', 'threat detection', 'anomaly detection',
            'governance', 'audit trail',
        ],
        'apqc_prefix': '11.',
        'common_wrong_codes': ['9.1', '9.2', '8.3'],  # Often wrongly tagged as finance or IT
    },
    'it_operations': {
        'keywords': [
            'it infrastructure', 'it operations', 'it service',
            'it incident', 'it support', 'service desk',
            'server', 'network', 'system monitoring',
            'aiops', 'devops', 'sre', 'site reliability',
            'uptime', 'availability', 'mttr', 'mttf',
            'it security', 'cybersecurity', 'soc',
            'cloud infrastructure', 'data center',
        ],
        'apqc_prefix': '8.',
        'common_wrong_codes': [],  # 8.x is often INCORRECTLY applied, not incorrectly avoided
    },
    'supply_chain': {
        'keywords': [
            'supply chain', 'logistics', 'warehouse', 'warehousing',
            'inventory', 'stock', 'stockout', 'overstock',
            'distribution', 'fulfillment', 'fulfilment',
            'procurement', 'sourcing', 'supplier',
            'demand forecasting', 'demand planning',
            'transportation', 'shipping', 'freight',
        ],
        'apqc_prefix': '4.',
        'common_wrong_codes': ['3.1', '3.3'],  # Sometimes confused with marketing
    },
    'marketing_sales': {
        'keywords': [
            'marketing', 'advertising', 'campaign',
            'lead generation', 'leads', 'sales pipeline',
            'pricing', 'price optimization', 'dynamic pricing',
            'customer segmentation', 'targeting',
            'conversion', 'churn', 'customer lifetime value', 'clv',
            'crm', 'sales forecast', 'revenue forecast',
        ],
        'apqc_prefix': '3.',
        'common_wrong_codes': ['9.1', '4.1'],  # Sometimes confused
    },
}

# Keywords that indicate cost/savings but should NOT trigger finance classification
COST_BENEFIT_KEYWORDS = [
    'cost reduction', 'cost savings', 'reduced costs', 'cut costs',
    'savings', 'efficiency', 'roi', 'return on investment',
    'productivity', 'time savings', 'faster', 'reduced time',
]


# =============================================================================
# VALIDATION CLASSES
# =============================================================================

@dataclass
class ValidationResult:
    """Result of validating an APQC classification."""
    is_valid: bool = True
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    detected_category: Optional[str] = None
    assigned_category: Optional[str] = None
    confidence_in_validation: str = "high"  # high, medium, low


def detect_claim_category(claim_text: str, strategic_fit: str = "", outcome: str = "") -> tuple[Optional[str], dict[str, int]]:
    """
    Detect primary category from claim text using keyword matching.
    
    Returns:
        tuple: (detected_category, scores_dict)
    """
    # Combine all text sources
    full_text = f"{claim_text} {strategic_fit} {outcome}".lower()
    
    scores = {}
    for category, config in CATEGORY_KEYWORDS.items():
        score = sum(1 for kw in config['keywords'] if kw.lower() in full_text)
        if score > 0:
            scores[category] = score
    
    if not scores:
        return None, {}
    
    # Get category with highest score
    max_category = max(scores.items(), key=lambda x: x[1])[0]
    return max_category, scores


def has_cost_benefit_language(text: str) -> bool:
    """Check if text contains cost/benefit language that might trigger false finance classification."""
    text_lower = text.lower()
    return any(kw in text_lower for kw in COST_BENEFIT_KEYWORDS)


def get_category_from_code(code: str) -> Optional[str]:
    """Get semantic category from APQC code prefix."""
    for category, config in CATEGORY_KEYWORDS.items():
        if code.startswith(config['apqc_prefix']):
            return category
    return None


def validate_apqc_classification(
    apqc_code: str,
    apqc_name: str,
    claim_text: str,
    strategic_fit: str = "",
    outcome: str = "",
    apqc_lookup: Optional[dict] = None
) -> ValidationResult:
    """
    Validate an APQC classification against claim content.
    
    Args:
        apqc_code: The assigned APQC code (e.g., "7.2")
        apqc_name: The assigned APQC name
        claim_text: The claim being classified
        strategic_fit: Additional context
        outcome: Outcome description
        apqc_lookup: Optional dict mapping codes to names for validation
    
    Returns:
        ValidationResult with errors and warnings
    """
    result = ValidationResult()
    
    # 1. Validate code format
    if not re.match(r'^\d{1,2}\.\d{1,2}$', apqc_code) and not re.match(r'^\d{1,2}\.0$', apqc_code):
        result.errors.append(f"Invalid APQC code format: {apqc_code}")
        result.is_valid = False
        return result
    
    # 2. Validate against lookup if provided
    if apqc_lookup and apqc_code not in apqc_lookup:
        result.errors.append(f"Unknown APQC code: {apqc_code}")
        result.is_valid = False
        return result
    
    if apqc_lookup and apqc_name != apqc_lookup.get(apqc_code):
        result.warnings.append(f"Name mismatch for {apqc_code}: expected '{apqc_lookup.get(apqc_code)}', got '{apqc_name}'")
    
    # 3. Semantic validation - detect what category the claim is about
    detected_category, scores = detect_claim_category(claim_text, strategic_fit, outcome)
    assigned_category = get_category_from_code(apqc_code)
    
    result.detected_category = detected_category
    result.assigned_category = assigned_category
    
    if detected_category and assigned_category:
        # Check for mismatch
        if detected_category != assigned_category:
            # Check if this is a known misclassification pattern
            config = CATEGORY_KEYWORDS.get(detected_category, {})
            
            if apqc_code in config.get('common_wrong_codes', []):
                # This is a KNOWN misclassification pattern
                result.errors.append(
                    f"LIKELY MISCLASSIFICATION: Claim appears to be {detected_category} "
                    f"(keywords: {scores}) but tagged with {assigned_category} code {apqc_code}. "
                    f"This is a known error pattern."
                )
                result.is_valid = False
            else:
                # Potential mismatch, but not a known pattern
                result.warnings.append(
                    f"Potential category mismatch: Claim keywords suggest {detected_category} "
                    f"(score: {scores.get(detected_category, 0)}) but assigned {assigned_category} ({apqc_code})"
                )
                result.confidence_in_validation = "medium"
    
    # 4. Check for finance trap (cost language triggering 9.x)
    if assigned_category == 'finance' and detected_category and detected_category != 'finance':
        if has_cost_benefit_language(f"{claim_text} {strategic_fit} {outcome}"):
            result.warnings.append(
                f"FINANCE TRAP: Code {apqc_code} assigned, but claim contains cost/benefit language "
                f"that may have incorrectly triggered finance classification. "
                f"Claim appears to be about {detected_category}."
            )
    
    # 5. Check for IT trap (everything tagged as 8.x)
    if assigned_category == 'it_operations' and detected_category and detected_category != 'it_operations':
        result.warnings.append(
            f"IT TRAP: Code {apqc_code} assigned, but claim appears to be about {detected_category}, "
            f"not IT operations. AI/technology involvement doesn't make it an IT function."
        )
    
    # 6. Check for product dev vs manufacturing confusion
    if (detected_category == 'product_dev' and assigned_category == 'manufacturing') or \
       (detected_category == 'manufacturing' and assigned_category == 'product_dev'):
        result.errors.append(
            f"DEV/MFG CONFUSION: Claim appears to be {detected_category} but tagged as {assigned_category}. "
            f"Product development (2.x) is DESIGN; Manufacturing (4.x) is PRODUCTION."
        )
        result.is_valid = False
    
    return result


def validate_classification_batch(
    classifications: list[dict],
    apqc_lookup: Optional[dict] = None
) -> tuple[list[ValidationResult], dict]:
    """
    Validate a batch of classifications.
    
    Args:
        classifications: List of dicts with 'apqc_code', 'apqc_name', 'claim_text', etc.
        apqc_lookup: Optional APQC reference lookup
    
    Returns:
        tuple: (list of ValidationResults, summary stats)
    """
    results = []
    
    for item in classifications:
        result = validate_apqc_classification(
            apqc_code=item.get('apqc_code') or item.get('process_group_id') or item.get('category_id', ''),
            apqc_name=item.get('apqc_name') or item.get('process_group_name') or item.get('category_name', ''),
            claim_text=item.get('claim_text', ''),
            strategic_fit=item.get('strategic_fit', ''),
            outcome=item.get('outcome', ''),
            apqc_lookup=apqc_lookup
        )
        results.append(result)
    
    # Calculate summary
    summary = {
        'total': len(results),
        'valid': sum(1 for r in results if r.is_valid),
        'invalid': sum(1 for r in results if not r.is_valid),
        'with_warnings': sum(1 for r in results if r.warnings),
        'error_types': {},
        'warning_types': {},
    }
    
    for r in results:
        for err in r.errors:
            error_type = err.split(':')[0] if ':' in err else 'OTHER'
            summary['error_types'][error_type] = summary['error_types'].get(error_type, 0) + 1
        for warn in r.warnings:
            warn_type = warn.split(':')[0] if ':' in warn else 'OTHER'
            summary['warning_types'][warn_type] = summary['warning_types'].get(warn_type, 0) + 1
    
    return results, summary


# =============================================================================
# APQC REFERENCE LOADING
# =============================================================================

def load_apqc_reference(apqc_file: Optional[Path] = None) -> dict[str, str]:
    """
    Load APQC reference file and create code -> name lookup.
    
    Args:
        apqc_file: Path to APQC JSON file. If None, tries common locations.
    
    Returns:
        dict mapping hierarchy_id to name
    """
    # Try common locations
    possible_paths = [
        apqc_file,
        Path("apqc_taxonomy.json"),
        Path("WorkFunctionsProcessor/apqc_level_1_to_3_enhanced.json"),
        Path("data/apqc_taxonomy.json"),
    ]
    
    for path in possible_paths:
        if path and path.exists():
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Handle different formats
            if isinstance(data, list):
                # Format: [{"hierarchy_id": "7.2", "name": "...", ...}, ...]
                return {r['hierarchy_id']: r['name'] for r in data if 'hierarchy_id' in r}
            elif isinstance(data, dict):
                # Format: {"7.0": {"name": "...", "process_groups": {...}}, ...}
                lookup = {}
                for cat_id, cat_data in data.items():
                    lookup[cat_id] = cat_data.get('name', '')
                    for pg_id, pg_data in cat_data.get('process_groups', {}).items():
                        lookup[pg_id] = pg_data.get('name', '')
                return lookup
    
    return {}


# =============================================================================
# STANDALONE EXECUTION
# =============================================================================

def validate_audit_files(cases_dir: Path, apqc_lookup: dict) -> None:
    """Validate all audit files in cases_enriched directory."""
    print("=== APQC Classification Validation ===\n")
    
    case_dirs = [d for d in cases_dir.iterdir() if d.is_dir()]
    
    total_claims = 0
    total_errors = 0
    total_warnings = 0
    cases_with_issues = 0
    
    for case_dir in sorted(case_dirs):
        audit_file = case_dir / "3_audit.json"
        if not audit_file.exists():
            continue
        
        with open(audit_file, 'r', encoding='utf-8') as f:
            audit_data = json.load(f)
        
        case_issues = []
        
        for claim in audit_data.get('audited_claims', []):
            claim_id = claim.get('claim_id', 'unknown')
            apqc_functions = claim.get('apqc_functions', []) or claim.get('apqc_work_functions', [])
            claim_text = claim.get('strategic_fit_assessment', '')
            
            for apqc in apqc_functions:
                code = apqc.get('id') or apqc.get('code', '')
                name = apqc.get('name', '')
                
                if not code:
                    continue
                
                result = validate_apqc_classification(
                    apqc_code=code,
                    apqc_name=name,
                    claim_text=claim_text,
                    apqc_lookup=apqc_lookup
                )
                
                total_claims += 1
                
                if result.errors:
                    total_errors += len(result.errors)
                    case_issues.append((claim_id, 'ERROR', result.errors))
                
                if result.warnings:
                    total_warnings += len(result.warnings)
                    case_issues.append((claim_id, 'WARNING', result.warnings))
        
        if case_issues:
            cases_with_issues += 1
            print(f"⚠️  {case_dir.name}:")
            for claim_id, level, messages in case_issues:
                for msg in messages:
                    icon = "❌" if level == 'ERROR' else "⚠️"
                    print(f"    {icon} {claim_id}: {msg}")
            print()
    
    print("=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    print(f"Total claims validated: {total_claims}")
    print(f"Cases with issues: {cases_with_issues}")
    print(f"Total errors: {total_errors}")
    print(f"Total warnings: {total_warnings}")
    print("=" * 60)


if __name__ == "__main__":
    # Load APQC reference
    apqc_lookup = load_apqc_reference()
    print(f"Loaded {len(apqc_lookup)} APQC codes\n")
    
    # Run validation on cases_enriched
    cases_dir = Path("cases_enriched")
    if cases_dir.exists():
        validate_audit_files(cases_dir, apqc_lookup)
    else:
        print(f"Directory not found: {cases_dir}")
        print("Run this script from the ai-case-library directory, or specify the path.")
