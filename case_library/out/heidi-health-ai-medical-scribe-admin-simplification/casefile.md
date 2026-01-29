---
case_id: heidi-health-ai-medical-scribe-admin-simplification
organisation: Heidi Health
title: AI Medical Scribe for Administrative Simplification
date_created: '2026-01-29'
date_updated: '2026-01-29'
sources:
- id: S1
  title: https://www.heidihealth.com/en-gb/blog/ai-tool-halves-time-gps-spend-on-paperwor...
  url: https://www.heidihealth.com/en-gb/blog/ai-tool-halves-time-gps-spend-on-paperwork
  raw_file: ''
  text_file: sources/text/S1.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S2
  title: https://www.mobihealthnews.com/news/heidi-health-raises-65m-expand-global-reach-...
  url: https://www.mobihealthnews.com/news/heidi-health-raises-65m-expand-global-reach-its-ai-medical-scribe-platform
  raw_file: ''
  text_file: sources/text/S2.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S3
  title: https://webflow.heidihealth.com/
  url: https://webflow.heidihealth.com/
  raw_file: ''
  text_file: sources/text/S3.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
value_claims:
- id: VC-001
  claim_title: 51% reduction in documentation time during appointments
  claim_description: Heidi Health's AI medical scribe reduced the time GPs spend on
    clinical documentation during patient appointments by 51% across 47 GPs and over
    2,800 consultations in a 25-day trial.
  source_ids:
  - S1
  source_quote: In the 25-day trial, 47 GPs across more than 2,800 patient consultations
    saw documentation time during appointments reduce by 51%
  quote_location: paragraph 2
  ai_attribution: direct
  attribution_evidence: The reduction in documentation time is directly attributed
    to Heidi Health's ambient AI tool transcribing conversations and automatically
    generating clinical notes.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - velocity
  - cost_reduction
  cognitive_depth: generative
  metric_raw:
    value: '51'
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
  claim_title: 61% reduction in after-hours administrative work
  claim_description: The AI medical scribe reduced after-hours administrative work
    for GPs by 61% during the 25-day trial involving 47 GPs across more than 2,800
    patient consultations.
  source_ids:
  - S1
  source_quote: after-hours admin drop by 61%
  quote_location: paragraph 2
  ai_attribution: direct
  attribution_evidence: The after-hours admin reduction is directly caused by Heidi's
    AI automatically generating clinical notes, referral letters, and care plans.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - velocity
  - cost_reduction
  cognitive_depth: generative
  metric_raw:
    value: '61'
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
- id: VC-003
  claim_title: 78% of GPs reported better patient rapport
  claim_description: With paperwork drastically reduced by the AI scribe, 78% of GPs
    reported building better rapport with patients during the trial.
  source_ids:
  - S1
  source_quote: With paperwork drastically reduced, more than three quarters (78%)
    of GPs said they built better rapport with patients
  quote_location: paragraph 2
  ai_attribution: contributing
  attribution_evidence: Better rapport is enabled by reduced paperwork burden from
    AI, allowing GPs to focus more on patient interaction rather than documentation.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - experience
  cognitive_depth: generative
  metric_raw:
    value: '78'
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
- id: VC-004
  claim_title: 78% of GPs reported lower cognitive load and improved focus
  claim_description: 78% of GPs in the trial reported experiencing lower cognitive
    load and improved focus as a result of using Heidi's AI medical scribe.
  source_ids:
  - S1
  source_quote: 78% reported lower "cognitive load" and improved focus
  quote_location: paragraph 2
  ai_attribution: contributing
  attribution_evidence: Lower cognitive load results from AI automating documentation
    tasks, freeing mental resources for clinical decision-making and patient interaction.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - experience
  cognitive_depth: generative
  metric_raw:
    value: '78'
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
- id: VC-005
  claim_title: 58% reduction in documentation-related stress
  claim_description: The AI medical scribe contributed to a 58% reduction in documentation-related
    stress among clinicians during the trial.
  source_ids:
  - S1
  source_quote: This shift contributed to a 58% reduction in documentation-related
    stress
  quote_location: paragraph 4
  ai_attribution: contributing
  attribution_evidence: Stress reduction is attributed to AI automating transcription
    and clinical note generation, reducing the burden of manual documentation.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - experience
  cognitive_depth: generative
  metric_raw:
    value: '58'
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
- id: VC-006
  claim_title: 18% of clinicians reported greater work enjoyment
  claim_description: Nearly one in five clinicians (18%) reported greater enjoyment
    in their work after using Heidi's AI medical scribe during the trial.
  source_ids:
  - S1
  source_quote: nearly one in five clinicians (18%) reported greater enjoyment in
    their work
  quote_location: paragraph 4
  ai_attribution: contributing
  attribution_evidence: Greater work enjoyment is enabled by AI reducing administrative
    burden and stress, allowing clinicians to focus on patient care.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - experience
  cognitive_depth: generative
  metric_raw:
    value: '18'
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
  claim_title: AI scribe enables 2x faster patient care tasks
  claim_description: Heidi Health's AI medical scribe enables doctors to be 2x faster
    in patient care tasks by automating clinical documentation.
  source_ids:
  - S3
  source_quote: Doctors can be 2x faster and better in patient care tasks.
  quote_location: mid-page section
  ai_attribution: direct
  attribution_evidence: The 2x speed improvement is directly attributed to AI automating
    documentation, allowing doctors to complete patient care tasks more quickly.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_low
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - velocity
  cognitive_depth: generative
  metric_raw:
    value: '2'
    currency: null
    magnitude: null
    timeframe: null
    metric_type: ratio
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
- id: VC-008
  claim_title: Clinicians lose $65,000 annually due to wasted time
  claim_description: Clinicians lose an average of $65,000 every year due to time
    wasted on administrative tasks rather than patient care, which Heidi's AI addresses.
  source_ids:
  - S3
  source_quote: Clinicians lose an average of $65,000 every year due to wasted time.
  quote_location: mid-page section
  ai_attribution: contextual
  attribution_evidence: This is a contextual claim about the problem Heidi addresses.
    The AI's value is in recovering this lost time, but the $65k figure describes
    the baseline problem.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_low
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - cost_reduction
  cognitive_depth: generative
  metric_raw:
    value: '65000'
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
- id: VC-009
  claim_title: AI scribe automates clinical note, referral letter, and care plan generation
  claim_description: Heidi's AI tool transcribes real-time conversations and automatically
    generates clinical notes, referral letters, and care plans, enhancing clinician-patient
    interactions.
  source_ids:
  - S1
  source_quote: transcribing real-time conversations and automatically generating
    clinical notes, referral letters, and care plans
  quote_location: paragraph 4
  ai_attribution: direct
  attribution_evidence: The AI directly performs transcription and document generation,
    which is the core mechanism for time savings and quality improvements.
  verification_status: verified
  evidence_level: method
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  - augmentation
  outcome:
  - velocity
  - experience
  cognitive_depth: generative
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
- id: VC-010
  claim_title: Trial involved 47 GPs across 2,800+ patient consultations
  claim_description: The 25-day trial of Heidi Health's AI medical scribe involved
    47 GPs conducting more than 2,800 patient consultations.
  source_ids:
  - S1
  source_quote: In the 25-day trial, 47 GPs across more than 2,800 patient consultations
  quote_location: paragraph 2
  ai_attribution: direct
  attribution_evidence: This adoption metric demonstrates the scale of AI deployment
    and usage during the trial period.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - velocity
  cognitive_depth: generative
  metric_raw:
    value: '2800'
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
context_claims:
- id: CC-001
  context_type: organisational
  claim_title: Modality Partnership is NHS's largest GP super-partnership
  claim_description: Modality Partnership, which conducted the research trial, is
    identified as the NHS's largest GP super-partnership.
  source_ids:
  - S1
  source_quote: The NHS's largest GP super-partnership
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
  context_type: temporal
  claim_title: Trial conducted over 25 days
  claim_description: The research trial of Heidi Health's AI medical scribe was conducted
    over a 25-day period.
  source_ids:
  - S1
  source_quote: In the 25-day trial
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
  context_type: sectoral
  claim_title: Primary care under extraordinary pressure
  claim_description: Primary care faces extraordinary pressure with GPs experiencing
    rising demand, growing patient complexity, and critical workforce shortages.
  source_ids:
  - S1
  source_quote: Primary care is under extraordinary pressure, with GPs facing rising
    demand, growing patient complexity, and critical workforce shortages.
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
  claim_title: Heidi Health based in Australia
  claim_description: Heidi Health is an Australia-based company developing AI-enabled
    medical scribe software.
  source_ids:
  - S2
  source_quote: Australia-based Heidi Health
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
  context_type: scale
  claim_title: $65M Series B funding at $465M valuation
  claim_description: Heidi Health closed a $65 million Series B funding round, bringing
    company valuation to $465 million and total funding to nearly $100 million.
  source_ids:
  - S2
  source_quote: closed a $65 million Series B funding round. Point72 Private Investments
    led the round... brings the company's valuation to $465 million and its total
    funding to nearly $100 million.
  verification_status: unverified
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
  context_type: organisational
  claim_title: 'New leadership appointments: CRO and CMO'
  claim_description: Heidi Health appointed Paul Williamson as chief revenue officer
    (formerly head of revenue at Plaid) and Dr. Simon Kos as chief medical officer
    (formerly CMO at Microsoft).
  source_ids:
  - S2
  source_quote: Paul Williamson as chief revenue officer and Dr. Simon Kos as chief
    medical officer. Williamson formerly held the position of head of revenue at Plaid,
    and Kos was chief medical officer at Microsoft.
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
  context_type: scale
  claim_title: Global operations across 6 countries
  claim_description: Heidi Health operates globally in the United States, Canada,
    Australia, New Zealand, the United Kingdom, and is expanding to Ireland, France,
    Spain, South Africa, Hong Kong, Germany and Singapore.
  source_ids:
  - S2
  source_quote: The global company works in the United States, Canada, Australia,
    New Zealand and the United Kingdom... expanding clinician adoption in Ireland,
    France, Spain, South Africa, Hong Kong, Germany and Singapore.
  verification_status: unverified
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
  context_type: products_services
  claim_title: AI built on Google's Gemini
  claim_description: Heidi Health utilizes its own AI and builds on top of Google's
    Gemini platform.
  source_ids:
  - S2
  source_quote: The company utilizes its own AI and builds on top of Google's Gemini.
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
  context_type: strategic_intent
  claim_title: Expansion strategy focused on workforce and local support
  claim_description: Heidi will use Series B funds to expand office locations, workforce,
    and provide local support to UK, Canadian and U.S. markets while expanding clinician
    adoption in new countries.
  source_ids:
  - S2
  source_quote: Heidi will use the funds to expand its office locations as well as
    its workforce. It will also provide local support to the UK, Canadian and U.S.
    markets.
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
  context_type: temporal
  claim_title: Partnership with Hendrix Health in March
  claim_description: In March, Heidi Health partnered with healthcare distributor
    Hendrix Health to expand its AI medical scribe to meet requirements of New Zealand
    clinicians.
  source_ids:
  - S2
  source_quote: In March, Heidi Health partnered with healthcare distributor Hendrix
    Health to expand its AI medical scribe to align with and meet the requirements
    of New Zealand clinicians.
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
  context_type: temporal
  claim_title: Previous funding rounds in 2023 and March
  claim_description: Heidi raised A$10 million in Series A in 2023 led by Blackbird
    Ventures, and $17 million additional Series A funding in March for expansion and
    new functionalities.
  source_ids:
  - S2
  source_quote: In 2023, the company raised A$10 million ($6.5 million) in a Series
    A funding round led by Blackbird Ventures... In March... raised $17 million in
    additional Series A funding
  verification_status: unverified
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
  context_type: sectoral
  claim_title: Competitive market with Suki and Commure
  claim_description: Other companies offering AI scribe tools include Suki ($165M
    total funding) and Commure ($200M growth funding from General Catalyst).
  source_ids:
  - S2
  source_quote: Other companies in the U.S. offering AI scribe tools include Suki...
    raised $70 million in Series D funding, bringing its total raise to $165 million...
    Commure... scored $200 million in growth funding
  verification_status: unverified
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
- id: CC-013
  context_type: functional
  claim_title: Clinical documentation and administrative work function
  claim_description: Heidi Health's AI medical scribe automates clinical documentation
    to reduce administrative burden in healthcare delivery.
  source_ids:
  - S3
  source_quote: Heidi is the ambient AI medical scribe that automates clinical documentation
    to reduce administrative burden
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10405'
  apqc_name: Deliver Healthcare Services
  human_validation:
    reviewed: false
    reviewer_verdict: null
    attribution_correct: null
    attribution_override: null
    missed_claim: false
    review_notes: null
    review_date: null
    reviewer_id: null
- id: CC-014
  context_type: scale
  claim_title: 50% of clinicians' time not spent on patient care
  claim_description: Clinicians spend more than 2 hours every day on tasks other than
    patient care, representing 50% of their time.
  source_ids:
  - S3
  source_quote: 50% of clinicians' time is not spent on patient care... Clinicians
    spend more than 2 hours every day on tasks other than patient care.
  verification_status: unverified
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
- id: CC-015
  context_type: products_services
  claim_title: Hospital-grade security and privacy standards
  claim_description: Heidi Health implements best-in-class privacy standards and hospital-grade
    security for processing medical encounters.
  source_ids:
  - S3
  source_quote: Processing a medical encounter is just about the most private thing
    an AI can do. So we've wrapped Heidi in best-in-class privacy standards... hospital-grade
    security
  verification_status: unverified
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
    total: 10
    verified: 10
    needs_review: 0
    rejected: 0
    by_attribution:
      direct: 5
      contributing: 4
      contextual: 1
  context_claims:
    total: 15
    verified: 9
    unverified: 6
    inferred: 0
  all_value_verified: true
  all_context_verified: false
human_validation_summary: null
status: complete
confidence: high
review_flags: []
ontology_metadata:
  version_used: '1.0'
  tagged_date: '2026-01-29'
  needs_retagging: false
---

# AI Medical Scribe for Administrative Simplification

## Executive Summary

Heidi Health: 51% reduction in documentation time during appointments.

## Key Findings

- **51% reduction in documentation time during appointments** — verified (outcome)
  - Quote: "In the 25-day trial, 47 GPs across more than 2,800 patient consultations saw documentation time during appointments reduce by 51%"

- **61% reduction in after-hours administrative work** — verified (outcome)
  - Quote: "after-hours admin drop by 61%"

- **78% of GPs reported better patient rapport** — verified (outcome)
  - Quote: "With paperwork drastically reduced, more than three quarters (78%) of GPs said they built better rapport with patients"

- **78% of GPs reported lower cognitive load and improved focus** — verified (outcome)
  - Quote: "78% reported lower "cognitive load" and improved focus"

- **58% reduction in documentation-related stress** — verified (outcome)
  - Quote: "This shift contributed to a 58% reduction in documentation-related stress"

- **18% of clinicians reported greater work enjoyment** — verified (outcome)
  - Quote: "nearly one in five clinicians (18%) reported greater enjoyment in their work"

- **AI scribe enables 2x faster patient care tasks** — verified (outcome)
  - Quote: "Doctors can be 2x faster and better in patient care tasks."

- **Clinicians lose $65,000 annually due to wasted time** — verified (outcome)
  - Quote: "Clinicians lose an average of $65,000 every year due to wasted time."

- **AI scribe automates clinical note, referral letter, and care plan generation** — verified (method)
  - Quote: "transcribing real-time conversations and automatically generating clinical notes, referral letters, and care plans"

- **Trial involved 47 GPs across 2,800+ patient consultations** — verified (adoption)
  - Quote: "In the 25-day trial, 47 GPs across more than 2,800 patient consultations"

## Sources

- **S1**: https://www.heidihealth.com/en-gb/blog/ai-tool-halves-time-gps-spend-on-paperwork
- **S2**: https://www.mobihealthnews.com/news/heidi-health-raises-65m-expand-global-reach-its-ai-medical-scribe-platform
- **S3**: https://webflow.heidihealth.com/
