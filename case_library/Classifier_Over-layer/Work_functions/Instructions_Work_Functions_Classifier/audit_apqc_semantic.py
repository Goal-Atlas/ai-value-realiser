#!/usr/bin/env python3
"""
APQC Semantic Audit - Monitoring Tool

Performs comprehensive semantic audit of APQC classifications to identify:
1. Mismatches between claim content and assigned codes
2. Patterns in misclassification errors
3. Quality metrics over time

Run periodically to monitor classification quality and identify drift.

Usage:
    python audit_apqc_semantic.py [--cases-dir PATH] [--output FILE]
"""

import json
import argparse
from pathlib import Path
from collections import defaultdict
from datetime import datetime
from typing import Optional

from validate_apqc_classification import (
    detect_claim_category,
    get_category_from_code,
    has_cost_benefit_language,
    load_apqc_reference,
    CATEGORY_KEYWORDS,
)


def audit_case_file(
    audit_file: Path,
    apqc_lookup: dict
) -> dict:
    """Audit a single case's audit file for semantic mismatches."""
    with open(audit_file, 'r', encoding='utf-8') as f:
        audit_data = json.load(f)
    
    case_id = audit_data.get('case_id', audit_file.parent.name)
    results = {
        'case_id': case_id,
        'total_claims': 0,
        'total_tags': 0,
        'mismatches': [],
        'warnings': [],
    }
    
    for claim in audit_data.get('audited_claims', []):
        claim_id = claim.get('claim_id', 'unknown')
        results['total_claims'] += 1
        
        # Build claim text from all relevant fields
        claim_text = ' '.join(filter(None, [
            claim.get('strategic_fit_assessment', ''),
            claim.get('evidence_quality_assessment', ''),
            claim.get('notes', ''),
            claim.get('claim_text', ''),
        ]))
        
        # Detect what category the claim appears to be about
        detected_category, scores = detect_claim_category(claim_text)
        
        # Check each APQC tag
        apqc_functions = claim.get('apqc_functions', []) or claim.get('apqc_work_functions', [])
        
        for apqc_tag in apqc_functions:
            results['total_tags'] += 1
            
            code = apqc_tag.get('id') or apqc_tag.get('code') or apqc_tag.get('hierarchy_id', '')
            name = apqc_tag.get('name', '')
            confidence = apqc_tag.get('confidence', 'unknown')
            
            if not code:
                continue
            
            assigned_category = get_category_from_code(code)
            
            # Check for semantic mismatch
            if detected_category and assigned_category and detected_category != assigned_category:
                mismatch = {
                    'claim_id': claim_id,
                    'code': code,
                    'code_name': name,
                    'assigned_category': assigned_category,
                    'detected_category': detected_category,
                    'detection_scores': scores,
                    'confidence': confidence,
                    'claim_excerpt': claim_text[:300],
                }
                
                # Classify severity
                config = CATEGORY_KEYWORDS.get(detected_category, {})
                if code in config.get('common_wrong_codes', []):
                    mismatch['severity'] = 'HIGH'
                    mismatch['pattern'] = f"{detected_category}_tagged_as_{assigned_category}"
                    results['mismatches'].append(mismatch)
                else:
                    mismatch['severity'] = 'MEDIUM'
                    results['warnings'].append(mismatch)
            
            # Check for finance trap
            if assigned_category == 'finance' and detected_category and detected_category != 'finance':
                if has_cost_benefit_language(claim_text):
                    if not any(m['claim_id'] == claim_id and m['code'] == code for m in results['mismatches']):
                        results['warnings'].append({
                            'claim_id': claim_id,
                            'code': code,
                            'issue': 'FINANCE_TRAP',
                            'message': f"Finance code assigned but claim appears to be {detected_category} with cost/benefit language",
                        })
    
    return results


def generate_audit_report(
    cases_dir: Path,
    apqc_lookup: dict,
    output_file: Optional[Path] = None
) -> dict:
    """Generate comprehensive audit report for all cases."""
    print("=== APQC Semantic Audit ===\n")
    
    case_dirs = [d for d in cases_dir.iterdir() if d.is_dir()]
    
    # Aggregate results
    all_results = []
    totals = {
        'cases_scanned': 0,
        'claims_scanned': 0,
        'tags_scanned': 0,
        'high_severity_mismatches': 0,
        'medium_severity_warnings': 0,
    }
    pattern_counts = defaultdict(int)
    cases_with_issues = []
    
    for case_dir in sorted(case_dirs):
        audit_file = case_dir / "3_audit.json"
        if not audit_file.exists():
            continue
        
        result = audit_case_file(audit_file, apqc_lookup)
        all_results.append(result)
        
        totals['cases_scanned'] += 1
        totals['claims_scanned'] += result['total_claims']
        totals['tags_scanned'] += result['total_tags']
        totals['high_severity_mismatches'] += len(result['mismatches'])
        totals['medium_severity_warnings'] += len(result['warnings'])
        
        # Count patterns
        for mismatch in result['mismatches']:
            pattern = mismatch.get('pattern', 'unknown')
            pattern_counts[pattern] += 1
        
        if result['mismatches'] or result['warnings']:
            cases_with_issues.append(result['case_id'])
    
    # Calculate metrics
    mismatch_rate = (totals['high_severity_mismatches'] / totals['tags_scanned'] * 100) if totals['tags_scanned'] > 0 else 0
    warning_rate = (totals['medium_severity_warnings'] / totals['tags_scanned'] * 100) if totals['tags_scanned'] > 0 else 0
    
    # Build report
    report = {
        'audit_timestamp': datetime.now().isoformat(),
        'summary': {
            'cases_scanned': totals['cases_scanned'],
            'claims_scanned': totals['claims_scanned'],
            'tags_scanned': totals['tags_scanned'],
            'high_severity_mismatches': totals['high_severity_mismatches'],
            'medium_severity_warnings': totals['medium_severity_warnings'],
            'mismatch_rate_percent': round(mismatch_rate, 2),
            'warning_rate_percent': round(warning_rate, 2),
            'cases_with_issues': len(cases_with_issues),
        },
        'pattern_analysis': dict(sorted(pattern_counts.items(), key=lambda x: x[1], reverse=True)),
        'cases_with_issues': cases_with_issues,
        'detailed_mismatches': [],
    }
    
    # Collect detailed mismatches (limit for readability)
    for result in all_results:
        for mismatch in result['mismatches'][:10]:  # Limit per case
            mismatch['case_id'] = result['case_id']
            report['detailed_mismatches'].append(mismatch)
    
    report['detailed_mismatches'] = report['detailed_mismatches'][:100]  # Overall limit
    
    # Print summary
    print("=" * 60)
    print("SEMANTIC AUDIT SUMMARY")
    print("=" * 60)
    print(f"Cases scanned:           {totals['cases_scanned']}")
    print(f"Claims scanned:          {totals['claims_scanned']}")
    print(f"APQC tags scanned:       {totals['tags_scanned']}")
    print()
    print(f"HIGH severity mismatches: {totals['high_severity_mismatches']} ({mismatch_rate:.2f}%)")
    print(f"MEDIUM severity warnings: {totals['medium_severity_warnings']} ({warning_rate:.2f}%)")
    print(f"Cases with issues:        {len(cases_with_issues)}")
    print()
    
    if pattern_counts:
        print("MISCLASSIFICATION PATTERNS:")
        for pattern, count in sorted(pattern_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"  {pattern}: {count}")
        print()
    
    if report['detailed_mismatches']:
        print("SAMPLE MISMATCHES:")
        for m in report['detailed_mismatches'][:5]:
            print(f"  Case: {m['case_id']}, Claim: {m['claim_id']}")
            print(f"    Detected: {m['detected_category']} (scores: {m['detection_scores']})")
            print(f"    Assigned: {m['assigned_category']} via {m['code']}")
            print(f"    Excerpt: {m['claim_excerpt'][:100]}...")
            print()
    
    # Save report
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"Full report saved to: {output_file}")
    
    return report


def compare_audits(current_report: dict, previous_report_file: Path) -> None:
    """Compare current audit with previous to show trends."""
    if not previous_report_file.exists():
        print("No previous report to compare against.")
        return
    
    with open(previous_report_file, 'r') as f:
        previous = json.load(f)
    
    current = current_report['summary']
    prev = previous['summary']
    
    print("\n" + "=" * 60)
    print("TREND COMPARISON")
    print("=" * 60)
    
    # Calculate deltas
    mismatch_delta = current['mismatch_rate_percent'] - prev['mismatch_rate_percent']
    warning_delta = current['warning_rate_percent'] - prev['warning_rate_percent']
    
    trend_icon = lambda d: "📉" if d < 0 else ("📈" if d > 0 else "➡️")
    
    print(f"Mismatch rate: {prev['mismatch_rate_percent']:.2f}% → {current['mismatch_rate_percent']:.2f}% {trend_icon(mismatch_delta)} ({mismatch_delta:+.2f}%)")
    print(f"Warning rate:  {prev['warning_rate_percent']:.2f}% → {current['warning_rate_percent']:.2f}% {trend_icon(warning_delta)} ({warning_delta:+.2f}%)")
    
    if mismatch_delta < 0:
        print("\n✅ Classification quality is IMPROVING")
    elif mismatch_delta > 0:
        print("\n⚠️ Classification quality is DEGRADING - review recent changes")
    else:
        print("\n➡️ Classification quality is STABLE")


def main():
    parser = argparse.ArgumentParser(description='APQC Semantic Audit')
    parser.add_argument('--cases-dir', type=Path, default=Path('cases_enriched'),
                        help='Directory containing case folders')
    parser.add_argument('--output', type=Path, default=Path('apqc_semantic_audit_report.json'),
                        help='Output file for audit report')
    parser.add_argument('--compare', type=Path, default=None,
                        help='Previous report to compare against')
    parser.add_argument('--apqc-file', type=Path, default=None,
                        help='Path to APQC taxonomy JSON')
    
    args = parser.parse_args()
    
    # Load APQC reference
    apqc_lookup = load_apqc_reference(args.apqc_file)
    if apqc_lookup:
        print(f"Loaded {len(apqc_lookup)} APQC codes\n")
    else:
        print("Warning: Could not load APQC reference - name validation disabled\n")
    
    # Generate report
    if not args.cases_dir.exists():
        print(f"Error: Cases directory not found: {args.cases_dir}")
        return
    
    report = generate_audit_report(args.cases_dir, apqc_lookup, args.output)
    
    # Compare with previous if requested
    if args.compare:
        compare_audits(report, args.compare)


if __name__ == "__main__":
    main()
