---
case_id: banco-do-brasil-ai-governance-framework-credit-fraud-compliance
organisation: Banco do Brasil
title: AI Governance Framework for Credit Fraud and Compliance
date_created: '2026-01-29'
date_updated: '2026-01-29'
sources:
- id: S1
  title: https://www.napier.ai/post/case-study-banco-do-brasil-reduces-false-positives-by...
  url: https://www.napier.ai/post/case-study-banco-do-brasil-reduces-false-positives-by-more-than-90
  raw_file: ''
  text_file: sources/text/S1.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S2
  title: https://www.ainvest.com/news/banco-brasil-strategic-resilience-geopolitical-cros...
  url: https://www.ainvest.com/news/banco-brasil-strategic-resilience-geopolitical-crossroads-2508/
  raw_file: ''
  text_file: sources/text/S2.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S3
  title: https://www.bankinfosecurity.com/internet-banking-case-study-banco-do-brasil-a-8...
  url: https://www.bankinfosecurity.com/internet-banking-case-study-banco-do-brasil-a-814
  raw_file: ''
  text_file: sources/text/S3.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
value_claims:
- id: VC-001
  claim_title: 90% reduction in false positive rates for transaction screening
  claim_description: Napier AI's transaction screening module reduced Banco do Brasil's
    false positive rate to just 2%, representing a more than 90% reduction from previous
    levels.
  source_ids:
  - S1
  source_quote: False positive hits reduced by more than 90%... reducing Banco do
    Brasil's False Positive Rate (FPR) to just 2%.
  quote_location: Results section
  ai_attribution: direct
  attribution_evidence: The reduction is explicitly attributed to Napier AI's Transaction
    Screening module implementation, with specific FPR metrics provided.
  verification_status: needs_review
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - optimization
  - automation
  outcome:
  - cost_reduction
  - risk_avoidance
  cognitive_depth: predictive
  metric_raw:
    value: '90'
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
  claim_title: Increased operational efficiency through reduced manual reviews
  claim_description: The 90% reduction in false positives significantly increased
    operational efficiency by reducing the volume of manual reviews required by compliance
    teams.
  source_ids:
  - S1
  source_quote: This significantly increased operational efficiency by reducing manual
    reviews and enhanced risk management which in turn facilitates fewer disruptions
    to customers through faster transaction processing.
  quote_location: Results section
  ai_attribution: direct
  attribution_evidence: Operational efficiency gains are directly linked to the AI-driven
    false positive reduction, which decreased manual review workload.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
  - optimization
  outcome:
  - cost_reduction
  - velocity
  cognitive_depth: predictive
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
- id: VC-003
  claim_title: Enhanced customer experience through faster transaction processing
  claim_description: Reduced false positives facilitated fewer disruptions to customers
    and enabled faster transaction processing, improving overall customer experience.
  source_ids:
  - S1
  source_quote: enhanced risk management which in turn facilitates fewer disruptions
    to customers through faster transaction processing.
  quote_location: Results section
  ai_attribution: direct
  attribution_evidence: Customer experience improvements are directly attributed to
    the AI system's ability to reduce false positives and process transactions more
    efficiently.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
  - experience
  - velocity
  cognitive_depth: predictive
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
- id: VC-004
  claim_title: Multi-geography scalability supporting 300,000 annual transactions
  claim_description: The AI solution provided scalability across multiple geographies
    and business units in a single tenancy environment, supporting up to 300,000 transactions
    screened annually.
  source_ids:
  - S1
  source_quote: This supports up to 300,000 transactions screened annually, while
    segregating and configuring the solution to best fit each business unit's requirements.
  quote_location: Multi-org capability section
  ai_attribution: direct
  attribution_evidence: The multi-org capability and transaction volume capacity are
    direct features of the Napier AI solution implementation.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - automation
  outcome:
  - business_growth
  cognitive_depth: predictive
  metric_raw:
    value: '300000'
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
- id: VC-005
  claim_title: Time and cost savings through autonomous rule configuration
  claim_description: Sandbox environment enabled FCC team to independently change
    and test rules without IT resources or code knowledge, generating significant
    time and cost savings.
  source_ids:
  - S1
  source_quote: This granted the FCC team significant time and cost savings by independently
    changing and testing rules within the user interface, without any need to understand
    the code.
  quote_location: Sandbox environment section
  ai_attribution: direct
  attribution_evidence: Time and cost savings are directly attributed to the AI platform's
    sandbox capability that eliminated IT dependency for rule changes.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_creation
  mechanism:
  - augmentation
  - automation
  outcome:
  - cost_reduction
  - velocity
  cognitive_depth: prescriptive
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
- id: VC-006
  claim_title: 40% reduction in false positives via AI-driven screening
  claim_description: AI-driven tools like Napier AI's transaction screening system
    on Microsoft Azure reduced false positives by 40%, enabling agile responses to
    evolving sanctions.
  source_ids:
  - S2
  source_quote: It has adopted AI-driven tools like Napier AI's transaction screening
    system on Microsoft Azure, which reduces false positives by 40% and enables agile
    responses to evolving sanctions.
  quote_location: Compliance infrastructure section
  ai_attribution: direct
  attribution_evidence: The 40% false positive reduction is explicitly attributed
    to the AI-driven transaction screening system.
  verification_status: needs_review
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - optimization
  - automation
  outcome:
  - cost_reduction
  - risk_avoidance
  cognitive_depth: predictive
  metric_raw:
    value: '40'
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
- id: VC-007
  claim_title: Centralized compliance autonomy across foreign operations
  claim_description: Napier AI solution provided autonomy to centrally calibrate financial
    crime compliance rules and strategies across EMEA operations while maintaining
    customer experience.
  source_ids:
  - S1
  source_quote: Napier AI's solution has given us the autonomy to centrally calibrate
    financial crime compliance rules and strategies and continue providing an industry-leading
    service to our customers
  quote_location: Solution section quote
  ai_attribution: direct
  attribution_evidence: Deputy Head of IT directly attributes the centralized compliance
    autonomy to Napier AI's solution.
  verification_status: verified
  evidence_level: method
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - augmentation
  - automation
  outcome:
  - velocity
  - experience
  cognitive_depth: prescriptive
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
  claim_title: Banco do Brasil is a 200-year-old financial institution
  claim_description: Among the oldest banks in continuous operation in the world,
    playing a crucial role in Brazil's financial system and economy development.
  source_ids:
  - S1
  source_quote: Banco do Brasil is a 200 year old financial services company headquartered
    in Brazil. Among the oldest banks in continuous operation in the world
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
  context_type: scale
  claim_title: Bank manages $200 billion in assets
  claim_description: Banco do Brasil has $200 billion in assets under management as
    of the case study period.
  source_ids:
  - S3
  source_quote: Banco do Brasil, a 200-year-old bank with $200 billion in assets under
    management.
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
- id: CC-003
  context_type: scale
  claim_title: 6 million Internet banking customers
  claim_description: The bank serves 6 million customers through its Internet banking
    platform.
  source_ids:
  - S3
  source_quote: the bank currently has 6 million Internet banking customers
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
  context_type: functional
  claim_title: Financial crime compliance and transaction screening
  claim_description: The AI solution addresses financial crime compliance, specifically
    transaction screening for sanctions and anti-money laundering across foreign operations.
  source_ids:
  - S1
  source_quote: The compliance team realised that the existing legacy solution used
    in conjunction with data vendors wasn't meeting the expectations of changing regulatory
    requirements
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10923'
  apqc_name: Manage compliance
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
  claim_title: Foreign operations across UK, France, Portugal, Austria, and Germany
  claim_description: Banco do Brasil operates foreign branches in multiple European
    countries requiring jurisdiction-specific compliance processes.
  source_ids:
  - S1
  source_quote: compliance needs of foreign branches in the UK, France, Portugal,
    Austria and Germany.
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
  context_type: strategic_intent
  claim_title: Culture of innovation as competitive enabler
  claim_description: Banco do Brasil emphasizes a culture of innovation as the enabler
    of the company's perenniality and competitive edge.
  source_ids:
  - S1
  source_quote: Banco do Brasil upholds its values in which they emphasise a culture
    of innovation as the enabler of the company's perenniality and competitive edge.
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
  context_type: temporal
  claim_title: Internet banking services since 1995
  claim_description: Brazilian Internet banking marketplace has existed since 1995,
    providing context for digital maturity.
  source_ids:
  - S3
  source_quote: the Internet banking marketplace has existed since 1995
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
- id: CC-008
  context_type: scale
  claim_title: 90.7% of transactions conducted electronically
  claim_description: The vast majority of Banco do Brasil's transactions are conducted
    through electronic channels (Internet, mobile, ATM).
  source_ids:
  - S3
  source_quote: 90.7 of the bank's total transactions are conducted electronically
    - either via the Internet, mobile device or ATM.
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
  context_type: sectoral
  claim_title: Banking and financial services sector
  claim_description: Banco do Brasil operates in the banking and financial services
    industry with focus on commercial and consumer banking.
  source_ids:
  - S1
  source_quote: Banco do Brasil is a 200 year old financial services company
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
  context_type: organisational
  claim_title: 'Dual mandate: economic development and international standards'
  claim_description: The bank operates under a dual mandate to advance Brazil's economic
    development while adhering to international financial standards.
  source_ids:
  - S2
  source_quote: 'The bank operates under a dual mandate: to advance Brazil''s economic
    development while adhering to international financial standards.'
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
  context_type: scale
  claim_title: Total assets of $414 billion in 2024
  claim_description: Banco do Brasil's total assets reached $414 billion in 2024,
    with 15.3% year-over-year growth in credit portfolio.
  source_ids:
  - S2
  source_quote: The bank's total assets reached $414 billion in 2024, with a 15.3%
    year-over-year growth in its credit portfolio
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
- id: CC-012
  context_type: temporal
  claim_title: Active fight against cyber threats since 2002
  claim_description: Since 2002, Banco do Brasil has actively fought phishing, pharming,
    Trojans and key-loggers with incident response teams.
  source_ids:
  - S3
  source_quote: Since 2002, Banco do Brasil has actively fought phishing, pharming,
    Trojans and key-loggers
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
    total: 7
    verified: 5
    needs_review: 2
    rejected: 0
    by_attribution:
      direct: 7
  context_claims:
    total: 12
    verified: 12
    unverified: 0
    inferred: 0
  all_value_verified: false
  all_context_verified: true
human_validation_summary: null
status: needs_review
confidence: high
review_flags: []
ontology_metadata:
  version_used: '1.0'
  tagged_date: '2026-01-29'
  needs_retagging: false
---

# AI Governance Framework for Credit Fraud and Compliance

## Executive Summary

Banco do Brasil: 90% reduction in false positive rates for transaction screening.

## Key Findings

- **90% reduction in false positive rates for transaction screening** — needs_review (outcome)
  - Quote: "False positive hits reduced by more than 90%... reducing Banco do Brasil's False Positive Rate (FPR) to just 2%."

- **Increased operational efficiency through reduced manual reviews** — verified (method)
  - Quote: "This significantly increased operational efficiency by reducing manual reviews and enhanced risk management which in turn facilitates fewer disruptions to customers through faster transaction processi..."

- **Enhanced customer experience through faster transaction processing** — verified (method)
  - Quote: "enhanced risk management which in turn facilitates fewer disruptions to customers through faster transaction processing."

- **Multi-geography scalability supporting 300,000 annual transactions** — verified (adoption)
  - Quote: "This supports up to 300,000 transactions screened annually, while segregating and configuring the solution to best fit each business unit's requirements."

- **Time and cost savings through autonomous rule configuration** — verified (method)
  - Quote: "This granted the FCC team significant time and cost savings by independently changing and testing rules within the user interface, without any need to understand the code."

- **40% reduction in false positives via AI-driven screening** — needs_review (outcome)
  - Quote: "It has adopted AI-driven tools like Napier AI's transaction screening system on Microsoft Azure, which reduces false positives by 40% and enables agile responses to evolving sanctions."

- **Centralized compliance autonomy across foreign operations** — verified (method)
  - Quote: "Napier AI's solution has given us the autonomy to centrally calibrate financial crime compliance rules and strategies and continue providing an industry-leading service to our customers"

## Sources

- **S1**: https://www.napier.ai/post/case-study-banco-do-brasil-reduces-false-positives-by-more-than-90
- **S2**: https://www.ainvest.com/news/banco-brasil-strategic-resilience-geopolitical-crossroads-2508/
- **S3**: https://www.bankinfosecurity.com/internet-banking-case-study-banco-do-brasil-a-814
