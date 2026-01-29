---
case_id: canon-135-bots-invoice-automation
organisation: Canon USA
title: Invoice Processing Automation
date_created: '2026-01-29'
date_updated: '2026-01-29'
sources:
- id: S1
  title: https://www.greenlightconsulting.com/case-studies/canon-usa-invoice-processing-f...
  url: https://www.greenlightconsulting.com/case-studies/canon-usa-invoice-processing-finance/
  raw_file: ''
  text_file: sources/text/S1.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S2
  title: https://cbps.canon.com/case-studies/accounts-payable-gets-a-makeover
  url: https://cbps.canon.com/case-studies/accounts-payable-gets-a-makeover
  raw_file: ''
  text_file: sources/text/S2.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S3
  title: https://www.canon-europe.com/business/insights/case-studies/digital-transformati...
  url: https://www.canon-europe.com/business/insights/case-studies/digital-transformation-in-document-management/
  raw_file: ''
  text_file: sources/text/S3.txt
  extraction_method: unknown
  extraction_quality: high
  is_multi_page: false
  related_urls: []
value_claims:
- id: VC-001
  claim_title: ML-based invoice processing improved accuracy from 35-40% to high accuracy
  claim_description: Canon USA replaced rigid RPA with custom machine learning models
    for invoice data extraction, dramatically improving accuracy from baseline 35-40%
    to significantly higher rates.
  source_ids:
  - S1
  source_quote: Instead of relying on rigid RegEx rules, we built custom machine learning
    models that could handle the complexity of their data with much higher accuracy.
  quote_location: Main content, paragraph 4
  ai_attribution: direct
  attribution_evidence: ML models directly replaced previous RPA system and are explicitly
    credited with achieving higher accuracy in invoice data extraction.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
  - optimization
  outcome:
  - velocity
  - cost_reduction
  cognitive_depth: predictive
  metric_raw:
    value: 35-40
    currency: null
    magnitude: null
    timeframe: null
    metric_type: percentage
  metric_classification: null
  ontology_version: '1.0'
  ontology_confidence: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: VC-002
  claim_title: Automated invoice processing handles 4,500 invoices monthly
  claim_description: Canon USA deployed UiPath Document Understanding with ML models
    to automatically process 4,500 vendor invoices per month, reducing manual work
    and errors.
  source_ids:
  - S1
  source_quote: Canon's finance team was drowning in paperwork with over 4,500 vendor
    invoices to process every month.
  quote_location: Main content, paragraph 1
  ai_attribution: direct
  attribution_evidence: UiPath Document Understanding with ML models directly automates
    invoice extraction, validation, and updates, handling the full volume of invoices.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - velocity
  - cost_reduction
  cognitive_depth: predictive
  metric_raw:
    value: '4500'
    currency: null
    magnitude: null
    timeframe: null
    metric_type: count
  metric_classification: null
  ontology_version: '1.0'
  ontology_confidence: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: VC-003
  claim_title: OCR-based invoice processing reduced payment time from 45 days to 2
    days
  claim_description: Cosmetics company implemented OCR system for invoice data extraction,
    reducing average payment processing time from 45 days to 2 days.
  source_ids:
  - S2
  source_quote: Instead of 45 days, the company completes payment in an average of
    two days.
  quote_location: Results section
  ai_attribution: direct
  attribution_evidence: OCR system directly automates data extraction from invoices,
    eliminating manual processing bottleneck that caused 45-day delays.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - velocity
  - experience
  cognitive_depth: descriptive
  metric_raw:
    value: 45 to 2
    currency: null
    magnitude: null
    timeframe: null
    metric_type: absolute_value
  metric_classification: null
  ontology_version: '1.0'
  ontology_confidence: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: VC-004
  claim_title: OCR invoice processing achieves 30-second processing time per invoice
  claim_description: Automated OCR system processes invoices in approximately 30 seconds
    when data fields match database, making invoices available within 24 hours.
  source_ids:
  - S2
  source_quote: If an invoice is scanned and all the data fields match with the company's
    database, the process takes about 30 seconds and the invoice is available to the
    cosmetics company within 24 hours.
  quote_location: Results section
  ai_attribution: direct
  attribution_evidence: OCR system directly performs data extraction and matching,
    achieving the 30-second processing time for successful matches.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - velocity
  cognitive_depth: descriptive
  metric_raw:
    value: '30'
    currency: null
    magnitude: null
    timeframe: null
    metric_type: absolute_value
  metric_classification: null
  ontology_version: '1.0'
  ontology_confidence: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: VC-005
  claim_title: Automated invoice processing handles 1,500 daily invoices
  claim_description: Cosmetics company deployed OCR-based digital AP system to process
    1,500 invoices daily that were previously handled manually.
  source_ids:
  - S2
  source_quote: It had 1,500 invoices to manually process each day.
  quote_location: Overwhelmed by Manual Invoice Processing section
  ai_attribution: direct
  attribution_evidence: OCR system directly replaced manual processing, automatically
    extracting and matching invoice data for the full daily volume.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - velocity
  - cost_reduction
  cognitive_depth: descriptive
  metric_raw:
    value: '1500'
    currency: null
    magnitude: null
    timeframe: null
    metric_type: count
  metric_classification: null
  ontology_version: '1.0'
  ontology_confidence: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: VC-006
  claim_title: Automated invoice processing eliminated manual data entry errors
  claim_description: Digital AP system with OCR eliminated human error and manual
    data entry that previously caused delays and compliance issues.
  source_ids:
  - S2
  source_quote: Job complete—without any data entry, human error, or paper piling
    up on the client's end.
  quote_location: Digitizing Accounts Payable section
  ai_attribution: direct
  attribution_evidence: OCR system directly performs data extraction and matching,
    removing the need for manual data entry that caused errors.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - cost_reduction
  - risk_avoidance
  cognitive_depth: descriptive
  metric_raw: null
  metric_classification: null
  ontology_version: '1.0'
  ontology_confidence: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
context_claims:
- id: CC-001
  context_type: organisational
  claim_title: Canon USA is the US unit of global Canon corporation
  claim_description: Canon USA operates as part of the global Canon organization,
    processing vendor invoices for US operations.
  source_ids:
  - S1
  source_quote: Canon's finance team was drowning in paperwork with over 4,500 vendor
    invoices to process every month.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-002
  context_type: functional
  claim_title: Invoice processing function within finance operations
  claim_description: Canon USA's finance team handles accounts payable invoice processing
    for vendor payments.
  source_ids:
  - S1
  source_quote: Canon's finance team was drowning in paperwork with over 4,500 vendor
    invoices to process every month.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10404'
  apqc_name: Process accounts payable
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-003
  context_type: products_services
  claim_title: UiPath Platform with Document Understanding and Action Center
  claim_description: Canon USA deployed UiPath Platform including Document Understanding
    for data extraction and Action Center for exception handling.
  source_ids:
  - S1
  source_quote: Canon transformed the way they handled invoices by choosing the UiPath
    Platform. UiPath Document Understanding took care of pulling out the right data,
    checking it, and updating records automatically.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-004
  context_type: organisational
  claim_title: Greenlight Consulting as implementation partner
  claim_description: Greenlight Consulting served as dedicated implementation partner
    for Canon USA's invoice automation project.
  source_ids:
  - S1
  source_quote: Greenlight Consulting was instrumental in this transformation, providing
    expertise and support throughout the project.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-005
  context_type: organisational
  claim_title: Oracle 11i SAP ERP system integration
  claim_description: Canon USA's invoice automation solution integrated directly with
    Oracle 11i SAP for end-to-end processing.
  source_ids:
  - S1
  source_quote: We connected the solution directly into Oracle 11i SAP so invoices
    could flow through automatically, from extraction to validation to updates.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-006
  context_type: sectoral
  claim_title: Global cosmetics and beauty company
  claim_description: US unit of multibillion-dollar global cosmetics and beauty company
    with seven regional plants.
  source_ids:
  - S2
  source_quote: Our client, the US unit of a global, multibillion-dollar cosmetics
    and beauty company, faced this dilemma and more
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-007
  context_type: functional
  claim_title: Accounts payable processing for multi-plant operations
  claim_description: Company processes AP for seven plants purchasing ingredients,
    packing materials, and paying staff salaries.
  source_ids:
  - S2
  source_quote: Meanwhile, the company's seven plants in the region—which purchase
    cosmetics ingredients and packing materials, as well as pay staff salaries—wanted
    to be reimbursed immediately.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10404'
  apqc_name: Process accounts payable
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-008
  context_type: products_services
  claim_title: Canon Business Process Services with OCR technology
  claim_description: Canon Business Process Services provided document scanning and
    OCR technology for digital AP transformation.
  source_ids:
  - S2
  source_quote: The company needed to transform its invoicing process to save time,
    money, and goodwill. It chose Canon Business Process Services to help complete
    the transformation.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-009
  context_type: scale
  claim_title: Processing volume of 4,500 monthly invoices at Canon USA
  claim_description: Canon USA finance team processes over 4,500 vendor invoices monthly.
  source_ids:
  - S1
  source_quote: Canon's finance team was drowning in paperwork with over 4,500 vendor
    invoices to process every month.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-010
  context_type: scale
  claim_title: Processing volume of 1,500 daily invoices at cosmetics company
  claim_description: Cosmetics company processes 1,500 invoices daily across seven
    regional plants.
  source_ids:
  - S2
  source_quote: It had 1,500 invoices to manually process each day.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-011
  context_type: strategic_intent
  claim_title: Transform invoice processing to save time, money, and goodwill
  claim_description: Cosmetics company sought to transform invoicing process to address
    payment delays, errors, and compliance issues.
  source_ids:
  - S2
  source_quote: The company needed to transform its invoicing process to save time,
    money, and goodwill.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: null
  apqc_name: null
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
verification_summary:
  value_claims:
    total: 6
    verified: 6
    needs_review: 0
    rejected: 0
    by_attribution:
      direct: 6
  context_claims:
    total: 11
    verified: 11
    unverified: 0
    inferred: 0
  all_value_verified: true
  all_context_verified: true
human_validation_summary: null
status: complete
confidence: high
review_flags: []
ontology_metadata:
  version_used: '1.0'
  tagged_date: '2026-01-29'
  needs_retagging: false
---

# Invoice Processing Automation

## Executive Summary

Canon USA: ML-based invoice processing improved accuracy from 35-40% to high accuracy.

## Key Findings

- **ML-based invoice processing improved accuracy from 35-40% to high accuracy** — verified (outcome)
  - Quote: "Instead of relying on rigid RegEx rules, we built custom machine learning models that could handle the complexity of their data with much higher accuracy."

- **Automated invoice processing handles 4,500 invoices monthly** — verified (adoption)
  - Quote: "Canon's finance team was drowning in paperwork with over 4,500 vendor invoices to process every month."

- **OCR-based invoice processing reduced payment time from 45 days to 2 days** — verified (outcome)
  - Quote: "Instead of 45 days, the company completes payment in an average of two days."

- **OCR invoice processing achieves 30-second processing time per invoice** — verified (outcome)
  - Quote: "If an invoice is scanned and all the data fields match with the company's database, the process takes about 30 seconds and the invoice is available to the cosmetics company within 24 hours."

- **Automated invoice processing handles 1,500 daily invoices** — verified (adoption)
  - Quote: "It had 1,500 invoices to manually process each day."

- **Automated invoice processing eliminated manual data entry errors** — verified (method)
  - Quote: "Job complete—without any data entry, human error, or paper piling up on the client's end."

## Sources

- **S1**: https://www.greenlightconsulting.com/case-studies/canon-usa-invoice-processing-finance/
- **S2**: https://cbps.canon.com/case-studies/accounts-payable-gets-a-makeover
- **S3**: https://www.canon-europe.com/business/insights/case-studies/digital-transformation-in-document-management/
