---
case_id: mayo-clinic-ai-scheduling-surgical-throughput
organisation: Mayo Clinic
title: AI-Powered Surgical Scheduling and Throughput Optimization
date_created: '2026-01-29'
date_updated: '2026-01-29'
sources:
- id: S1
  title: https://www.opmed.ai/blog-posts/transforming-cardiac-surgery-scheduling-at-mayo-...
  url: https://www.opmed.ai/blog-posts/transforming-cardiac-surgery-scheduling-at-mayo-clinic-with-opmed-ai
  raw_file: ''
  text_file: sources/text/S1.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S2
  title: https://sloanreview.mit.edu/article/mayo-clinics-healthy-model-for-ai-success/
  url: https://sloanreview.mit.edu/article/mayo-clinics-healthy-model-for-ai-success/
  raw_file: ''
  text_file: sources/text/S2.txt
  extraction_method: unknown
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S3
  title: https://www.cxotalk.com/episode/data-and-ai-improve-patient-outcomes-at-the-mayo...
  url: https://www.cxotalk.com/episode/data-and-ai-improve-patient-outcomes-at-the-mayo-clinic
  raw_file: ''
  text_file: sources/text/S3.txt
  extraction_method: unknown
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S4
  title: https://mayomagazine.mayoclinic.org/2025/04/ai-improves-patient-experience/
  url: https://mayomagazine.mayoclinic.org/2025/04/ai-improves-patient-experience/
  raw_file: ''
  text_file: sources/text/S4.txt
  extraction_method: unknown
  extraction_quality: high
  is_multi_page: false
  related_urls: []
value_claims:
- id: VC-001
  claim_title: Reduced prediction error for cardiac surgery case duration from 60
    to 34 minutes MAE
  claim_description: AI model reduced Mean Absolute Error in predicting cardiac surgery
    case duration from 60 minutes (traditional methods) to 34 minutes in controlled
    tests.
  source_ids:
  - S1
  source_quote: In controlled tests, our AI model significantly surpassed traditional
    estimation methods, reducing the Mean Absolute Error (MAE) from 60 minutes per
    case to just 34 minutes.
  quote_location: Opmed.ai's Solution section
  ai_attribution: direct
  attribution_evidence: The AI model directly produced the improved predictions, with
    quantified comparison to traditional methods showing 43% reduction in MAE.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - optimization
  - augmentation
  outcome:
  - velocity
  cognitive_depth: predictive
  metric_raw:
    value: '34'
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
- id: VC-002
  claim_title: Saved over 200 operating room hours annually per OR
  claim_description: AI-driven precise case duration predictions minimized wasted
    OR time, saving over 200 operating room hours annually per operating room.
  source_ids:
  - S1
  source_quote: This increased efficiency saves over 200 OR hours annually per operating
    room, boosting the capacity for more life-saving cardiac surgeries.
  quote_location: Results section
  ai_attribution: direct
  attribution_evidence: The time savings are directly attributed to the AI model's
    precise predictions that minimize wasted OR time, as stated in the results section.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
  - velocity
  - cost_reduction
  cognitive_depth: predictive
  metric_raw:
    value: '200'
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
- id: VC-003
  claim_title: Increased surgical capacity for cardiac procedures
  claim_description: Reduced wasted OR time through accurate predictions enabled Mayo
    Clinic to schedule more life-saving cardiac surgeries within existing resources.
  source_ids:
  - S1
  source_quote: This increased efficiency saves over 200 OR hours annually per operating
    room, boosting the capacity for more life-saving cardiac surgeries.
  quote_location: Results section
  ai_attribution: direct
  attribution_evidence: The capacity increase is directly enabled by AI predictions
    that reduce wasted time, allowing more procedures to be scheduled in the same
    timeframe.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
  - business_growth
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
  claim_title: AI model accurately estimates daily workloads for cardiac care providers
  claim_description: The AI model not only predicts individual procedure durations
    but also accurately estimates aggregate daily workloads for specific cardiac care
    providers.
  source_ids:
  - S1
  source_quote: Our AI model not only refines duration predictions for individual
    cardiac procedures but also accurately estimates the daily workloads of specific
    cardiac care providers.
  quote_location: Results section
  ai_attribution: direct
  attribution_evidence: The AI model directly produces workload estimates by aggregating
    individual procedure predictions for specific providers.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - augmentation
  - optimization
  outcome:
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
- id: VC-005
  claim_title: Reduced patient wait times through optimized surgery sequencing
  claim_description: AI and network science analyze and organize surgery sequences
    to maximize OR utilization and reduce patient wait times.
  source_ids:
  - S1
  source_quote: By leveraging AI and network science, we analyze and organize the
    sequence of surgeries to maximize operating room (OR) utilization, reduce patient
    wait times, and minimize potential delays and cancellations.
  quote_location: Project overview section
  ai_attribution: direct
  attribution_evidence: AI and network science directly determine the optimal surgery
    sequence that reduces wait times as a stated outcome.
  verification_status: needs_review
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
  - experience
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
  claim_title: Minimized delays and cancellations through AI-optimized scheduling
  claim_description: AI-driven surgery sequencing minimizes potential delays and cancellations,
    ensuring timely care for more patients.
  source_ids:
  - S1
  source_quote: By leveraging AI and network science, we analyze and organize the
    sequence of surgeries to maximize operating room (OR) utilization, reduce patient
    wait times, and minimize potential delays and cancellations, ensuring timely care
    for more patients.
  quote_location: Project overview section
  ai_attribution: direct
  attribution_evidence: AI directly produces the optimized schedule that minimizes
    delays and cancellations as a stated outcome of the sequencing algorithm.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
  - risk_avoidance
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
  claim_title: Mayo Clinic is the implementing organization
  claim_description: Mayo Clinic is the healthcare organization implementing Opmed.ai's
    AI scheduling solutions for cardiac surgery.
  source_ids:
  - S1
  source_quote: Transforming Cardiac Surgery Scheduling at Mayo Clinic With Opmed.ai
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
  context_type: sectoral
  claim_title: Healthcare sector implementation
  claim_description: The AI solution is implemented in the healthcare sector, specifically
    in hospital surgical operations.
  source_ids:
  - S1
  source_quote: At Mayo Clinic, the complexity of healthcare schedules necessitates
    innovative solutions that optimize resource utilization, reduce costs, and enhance
    patient care.
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
  context_type: functional
  claim_title: Surgical scheduling and resource allocation function
  claim_description: The AI solution addresses surgical case scheduling, operating
    room utilization, and resource allocation for cardiac surgery.
  source_ids:
  - S1
  source_quote: We utilize AI to deliver accurate predictions of the duration for
    each surgical case, significantly enhancing scheduling precision.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10405'
  apqc_name: Manage patient/client scheduling
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
  claim_title: Staff rostering and workforce management
  claim_description: The AI solution includes staff rostering capabilities to navigate
    complex preferences and requirements of staff scheduling.
  source_ids:
  - S1
  source_quote: We develop sophisticated tools to navigate the complex preferences
    and requirements of staff scheduling. This approach ensures that the hospital's
    operational needs are harmoniously aligned with staff well-being.
  verification_status: unverified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10129'
  apqc_name: Manage employee/labor relations
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
  context_type: products_services
  claim_title: Opmed.ai provides AI-driven surgical scheduling platform
  claim_description: Opmed.ai is the technology provider offering AI models and web
    application for surgical case duration prediction and scheduling optimization.
  source_ids:
  - S1
  source_quote: We have developed a user-friendly web application, customized specifically
    for the needs of the cardiac surgery schedulers at Mayo Clinic.
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
  context_type: scale
  claim_title: Focus on cardiac surgery department
  claim_description: The initial implementation focuses specifically on cardiac surgery
    scheduling at Mayo Clinic, with plans to extend to other departments.
  source_ids:
  - S1
  source_quote: This case study will focus specifically on our project aimed at refining
    the prediction of case lengths for cardiac surgeries.
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
  context_type: strategic_intent
  claim_title: Strategic goal to optimize resource utilization and enhance patient
    care
  claim_description: Mayo Clinic's strategic intent is to optimize resource utilization,
    reduce costs, and enhance patient care through innovative scheduling solutions.
  source_ids:
  - S1
  source_quote: At Mayo Clinic, the complexity of healthcare schedules necessitates
    innovative solutions that optimize resource utilization, reduce costs, and enhance
    patient care.
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
  context_type: temporal
  claim_title: Multiple ongoing projects with expansion plans
  claim_description: Opmed.ai engages in multiple pivotal projects with Mayo Clinic,
    with plans to extend technological advancements to other critical areas within
    the hospital.
  source_ids:
  - S1
  source_quote: This initiative is part of a broader effort to extend our technological
    advancements to other critical areas within the hospital, demonstrating our comprehensive
    approach to healthcare optimization.
  verification_status: verified
  verification_confidence: medium
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
    verified: 5
    needs_review: 1
    rejected: 0
    by_attribution:
      direct: 6
  context_claims:
    total: 8
    verified: 7
    unverified: 1
    inferred: 0
  all_value_verified: false
  all_context_verified: false
human_validation_summary: null
status: needs_review
confidence: high
review_flags: []
ontology_metadata:
  version_used: '1.0'
  tagged_date: '2026-01-29'
  needs_retagging: false
---

# AI-Powered Surgical Scheduling and Throughput Optimization

## Executive Summary

Mayo Clinic: Reduced prediction error for cardiac surgery case duration from 60 to 34 minutes MAE.

## Key Findings

- **Reduced prediction error for cardiac surgery case duration from 60 to 34 minutes MAE** — verified (outcome)
  - Quote: "In controlled tests, our AI model significantly surpassed traditional estimation methods, reducing the Mean Absolute Error (MAE) from 60 minutes per case to just 34 minutes."

- **Saved over 200 operating room hours annually per OR** — verified (outcome)
  - Quote: "This increased efficiency saves over 200 OR hours annually per operating room, boosting the capacity for more life-saving cardiac surgeries."

- **Increased surgical capacity for cardiac procedures** — verified (method)
  - Quote: "This increased efficiency saves over 200 OR hours annually per operating room, boosting the capacity for more life-saving cardiac surgeries."

- **AI model accurately estimates daily workloads for cardiac care providers** — verified (method)
  - Quote: "Our AI model not only refines duration predictions for individual cardiac procedures but also accurately estimates the daily workloads of specific cardiac care providers."

- **Reduced patient wait times through optimized surgery sequencing** — needs_review (method)
  - Quote: "By leveraging AI and network science, we analyze and organize the sequence of surgeries to maximize operating room (OR) utilization, reduce patient wait times, and minimize potential delays and cancel..."

- **Minimized delays and cancellations through AI-optimized scheduling** — verified (method)
  - Quote: "By leveraging AI and network science, we analyze and organize the sequence of surgeries to maximize operating room (OR) utilization, reduce patient wait times, and minimize potential delays and cancel..."

## Sources

- **S1**: https://www.opmed.ai/blog-posts/transforming-cardiac-surgery-scheduling-at-mayo-clinic-with-opmed-ai
- **S2**: https://sloanreview.mit.edu/article/mayo-clinics-healthy-model-for-ai-success/
- **S3**: https://www.cxotalk.com/episode/data-and-ai-improve-patient-outcomes-at-the-mayo-clinic
- **S4**: https://mayomagazine.mayoclinic.org/2025/04/ai-improves-patient-experience/
