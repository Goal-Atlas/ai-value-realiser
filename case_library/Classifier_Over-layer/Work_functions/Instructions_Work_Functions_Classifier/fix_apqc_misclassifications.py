#!/usr/bin/env python3
"""
APQC Misclassification Fix Script

Automatically fixes mis-categorized APQC codes based on semantic audit results.
Supports dry-run mode to preview changes before applying.

Usage:
    # Preview changes (dry-run)
    python fix_apqc_misclassifications.py --dry-run
    
    # Apply fixes
    python fix_apqc_misclassifications.py --apply
    
    # Fix specific patterns only
    python fix_apqc_misclassifications.py --apply --pattern hr_tagged_as_finance
"""

import json
import argparse
from pathlib import Path
from collections import defaultdict
from datetime import datetime
from typing import Optional
import shutil

from validate_apqc_classification import (
    detect_claim_category,
    load_apqc_reference,
    CATEGORY_KEYWORDS,
)


# =============================================================================
# FIX MAPPINGS - Which code to use for each detected category
# =============================================================================

CATEGORY_FIX_MAPPINGS = {
    'hr': {
        'default_code': '7.2',
        'default_name': 'Recruit, source, and select employees',
        'alternatives': {
            'training': ('7.3', 'Manage employee onboarding, training, and development'),
            'retention': ('7.5', 'Reward and retain employees'),
            'workforce_planning': ('7.1', 'Develop and manage human resources planning, policies, and strategies'),
        }
    },
    'product_dev': {
        'default_code': '2.3',
        'default_name': 'Develop products and services',
        'alternatives': {
            'portfolio': ('2.1', 'Govern and manage product/service development program'),
            'ideation': ('2.2', 'Generate and define new product/service ideas'),
        }
    },
    'manufacturing': {
        'default_code': '4.3',
        'default_name': 'Produce/Assemble/Test product',
        'alternatives': {
            'planning': ('4.1', 'Plan for and align supply chain resources'),
            'procurement': ('4.2', 'Procure materials and services'),
            'logistics': ('4.4', 'Manage logistics and warehousing'),
        }
    },
    'finance': {
        'default_code': '9.1',
        'default_name': 'Perform planning and management accounting',
        'alternatives': {
            'accounts_payable': ('9.6', 'Process accounts payable and expense reimbursements'),
            'accounts_receivable': ('9.2', 'Perform revenue accounting'),
            'payroll': ('9.5', 'Process payroll'),
            'treasury': ('9.7', 'Manage treasury operations'),
        }
    },
    'customer_service': {
        'default_code': '6.2',
        'default_name': 'Plan and manage customer service contacts',
        'alternatives': {
            'strategy': ('6.1', 'Develop customer service strategy'),
            'after_sales': ('6.3', 'Service products after sales'),
        }
    },
    'risk': {
        'default_code': '11.1',
        'default_name': 'Manage enterprise risk',
        'alternatives': {
            'compliance': ('11.2', 'Manage compliance'),
            'resiliency': ('11.4', 'Manage business resiliency'),
        }
    },
    'it_operations': {
        'default_code': '8.7',
        'default_name': 'Create and manage support services/solutions',
        'alternatives': {
            'security': ('8.3', 'Develop and manage IT resilience and risk'),
            'strategy': ('8.2', 'Develop and manage IT business strategy'),
        }
    },
    'supply_chain': {
        'default_code': '4.1',
        'default_name': 'Plan for and align supply chain resources',
        'alternatives': {
            'logistics': ('4.4', 'Manage logistics and warehousing'),
            'procurement': ('4.2', 'Procure materials and services'),
        }
    },
    'marketing_sales': {
        'default_code': '3.3',
        'default_name': 'Develop and manage marketing plans',
        'alternatives': {
            'strategy': ('3.2', 'Develop marketing strategy'),
            'sales': ('3.5', 'Develop and manage sales plans'),
            'market_research': ('3.1', 'Understand markets, customers, and capabilities'),
        }
    },
}


def suggest_correct_code(detected_category: str, claim_text: str) -> tuple[str, str]:
    """
    Suggest the correct APQC code based on detected category and claim content.
    
    Returns:
        tuple: (code, name)
    """
    if detected_category not in CATEGORY_FIX_MAPPINGS:
        return ('', '')
    
    config = CATEGORY_FIX_MAPPINGS[detected_category]
    text_lower = claim_text.lower()
    
    # Check for alternative mappings based on keywords
    for keyword, (code, name) in config.get('alternatives', {}).items():
        if keyword.replace('_', ' ') in text_lower:
            return (code, name)
    
    # Return default
    return (config['default_code'], config['default_name'])


def load_audit_report(report_file: Path) -> dict:
    """Load semantic audit report."""
    if not report_file.exists():
        raise FileNotFoundError(f"Audit report not found: {report_file}")
    
    with open(report_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def fix_case_audit_file(
    audit_file: Path,
    mismatches_for_case: list[dict],
    apqc_lookup: dict,
    dry_run: bool = True
) -> list[dict]:
    """
    Fix APQC codes in a single audit file.
    
    Returns:
        list of fix records
    """
    with open(audit_file, 'r', encoding='utf-8') as f:
        audit_data = json.load(f)
    
    fixes = []
    modified = False
    
    for claim in audit_data.get('audited_claims', []):
        claim_id = claim.get('claim_id', 'unknown')
        
        # Find mismatches for this claim
        claim_mismatches = [m for m in mismatches_for_case if m['claim_id'] == claim_id]
        if not claim_mismatches:
            continue
        
        # Get current APQC functions
        apqc_key = 'apqc_functions' if 'apqc_functions' in claim else 'apqc_work_functions'
        apqc_functions = claim.get(apqc_key, [])
        
        # Build claim text for context
        claim_text = ' '.join(filter(None, [
            claim.get('strategic_fit_assessment', ''),
            claim.get('claim_text', ''),
        ]))
        
        # Process each mismatch
        new_functions = []
        removed = []
        added = []
        
        for apqc in apqc_functions:
            code = apqc.get('id') or apqc.get('code', '')
            
            # Check if this code needs fixing
            mismatch = next((m for m in claim_mismatches if m['code'] == code), None)
            
            if mismatch:
                # Remove the wrong code
                removed.append({
                    'code': code,
                    'name': apqc.get('name', ''),
                    'was_category': mismatch['assigned_category'],
                })
                
                # Suggest correct code
                correct_code, correct_name = suggest_correct_code(
                    mismatch['detected_category'],
                    claim_text
                )
                
                if correct_code:
                    # Check we don't already have this code
                    if not any((f.get('id') or f.get('code')) == correct_code for f in new_functions):
                        new_apqc = {
                            'id': correct_code,
                            'name': correct_name,
                            'confidence': 'medium',  # Auto-fixed = medium confidence
                            'auto_fixed': True,
                            'original_code': code,
                            'fix_timestamp': datetime.now().isoformat(),
                        }
                        new_functions.append(new_apqc)
                        added.append({
                            'code': correct_code,
                            'name': correct_name,
                            'for_category': mismatch['detected_category'],
                        })
            else:
                # Keep this code unchanged
                new_functions.append(apqc)
        
        if removed or added:
            modified = True
            claim[apqc_key] = new_functions
            
            fixes.append({
                'claim_id': claim_id,
                'removed': removed,
                'added': added,
            })
    
    # Write back if not dry-run and changes were made
    if modified and not dry_run:
        # Backup original
        backup_file = audit_file.with_suffix('.json.bak')
        shutil.copy(audit_file, backup_file)
        
        # Write fixed version
        with open(audit_file, 'w', encoding='utf-8') as f:
            json.dump(audit_data, f, indent=2, ensure_ascii=False)
    
    return fixes


def run_fixes(
    cases_dir: Path,
    audit_report: dict,
    apqc_lookup: dict,
    dry_run: bool = True,
    pattern_filter: Optional[str] = None
) -> dict:
    """
    Run fixes based on audit report.
    
    Args:
        cases_dir: Directory containing case folders
        audit_report: Semantic audit report
        apqc_lookup: APQC reference lookup
        dry_run: If True, preview changes without applying
        pattern_filter: If set, only fix this specific pattern
    
    Returns:
        Summary of fixes applied/previewed
    """
    print("=" * 60)
    print("APQC MISCLASSIFICATION FIX SCRIPT")
    print("=" * 60)
    print(f"Mode: {'DRY-RUN (preview only)' if dry_run else 'APPLY FIXES'}")
    print()
    
    # Group mismatches by case
    mismatches_by_case = defaultdict(list)
    for mismatch in audit_report.get('detailed_mismatches', []):
        # Apply pattern filter if specified
        if pattern_filter and mismatch.get('pattern') != pattern_filter:
            continue
        mismatches_by_case[mismatch['case_id']].append(mismatch)
    
    print(f"Cases to process: {len(mismatches_by_case)}")
    print(f"Total mismatches: {sum(len(v) for v in mismatches_by_case.values())}")
    if pattern_filter:
        print(f"Pattern filter: {pattern_filter}")
    print()
    
    # Process each case
    all_fixes = []
    cases_fixed = 0
    
    for case_id, mismatches in sorted(mismatches_by_case.items()):
        case_dir = cases_dir / case_id
        audit_file = case_dir / "3_audit.json"
        
        if not audit_file.exists():
            print(f"⚠️  {case_id}: Audit file not found")
            continue
        
        fixes = fix_case_audit_file(
            audit_file,
            mismatches,
            apqc_lookup,
            dry_run=dry_run
        )
        
        if fixes:
            cases_fixed += 1
            all_fixes.extend(fixes)
            
            icon = "🔍" if dry_run else "✅"
            print(f"{icon} {case_id}: {len(fixes)} claim(s)")
            
            for fix in fixes:
                print(f"    Claim {fix['claim_id']}:")
                for r in fix['removed']:
                    print(f"      ❌ Remove: {r['code']} ({r['name']}) [{r['was_category']}]")
                for a in fix['added']:
                    print(f"      ✅ Add: {a['code']} ({a['name']}) [{a['for_category']}]")
            print()
    
    # Summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Cases processed: {len(mismatches_by_case)}")
    print(f"Cases {'would be ' if dry_run else ''}fixed: {cases_fixed}")
    print(f"Total claims {'would be ' if dry_run else ''}modified: {len(all_fixes)}")
    
    if dry_run:
        print()
        print("This was a DRY-RUN. No files were modified.")
        print("To apply fixes, run with --apply flag.")
    else:
        print()
        print("✅ Fixes applied. Backup files created with .bak extension.")
    
    return {
        'cases_processed': len(mismatches_by_case),
        'cases_fixed': cases_fixed,
        'claims_fixed': len(all_fixes),
        'dry_run': dry_run,
        'fixes': all_fixes,
    }


def main():
    parser = argparse.ArgumentParser(description='Fix APQC misclassifications')
    parser.add_argument('--cases-dir', type=Path, default=Path('cases_enriched'),
                        help='Directory containing case folders')
    parser.add_argument('--audit-report', type=Path, default=Path('apqc_semantic_audit_report.json'),
                        help='Semantic audit report file')
    parser.add_argument('--dry-run', action='store_true', default=True,
                        help='Preview changes without applying (default)')
    parser.add_argument('--apply', action='store_true',
                        help='Actually apply the fixes')
    parser.add_argument('--pattern', type=str, default=None,
                        help='Only fix specific pattern (e.g., hr_tagged_as_finance)')
    parser.add_argument('--apqc-file', type=Path, default=None,
                        help='Path to APQC taxonomy JSON')
    
    args = parser.parse_args()
    
    # Determine mode
    dry_run = not args.apply
    
    # Safety confirmation for apply mode
    if not dry_run:
        print("⚠️  You are about to MODIFY files.")
        confirm = input("Type 'yes' to proceed: ").strip().lower()
        if confirm != 'yes':
            print("Aborted.")
            return
    
    # Load APQC reference
    apqc_lookup = load_apqc_reference(args.apqc_file)
    print(f"Loaded {len(apqc_lookup)} APQC codes\n")
    
    # Load audit report
    try:
        audit_report = load_audit_report(args.audit_report)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Run audit_apqc_semantic.py first to generate the report.")
        return
    
    # Check cases directory
    if not args.cases_dir.exists():
        print(f"Error: Cases directory not found: {args.cases_dir}")
        return
    
    # Run fixes
    result = run_fixes(
        args.cases_dir,
        audit_report,
        apqc_lookup,
        dry_run=dry_run,
        pattern_filter=args.pattern
    )
    
    # Save fix report
    if result['fixes']:
        report_file = Path(f"apqc_fix_report_{'preview' if dry_run else 'applied'}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"\nFix report saved to: {report_file}")


if __name__ == "__main__":
    main()
