---
case_id: uhcw-nhs-trust-ai-patient-flow-optimization
organisation: University Hospitals Coventry and Warwickshire NHS Trust
title: AI-Powered Patient Flow Optimization and Digital Patient Engagement
date_created: '2026-01-29'
date_updated: '2026-01-29'
sources:
- id: S1
  title: https://aws.amazon.com/blogs/publicsector/university-hospitals-coventry-and-warw...
  url: https://aws.amazon.com/blogs/publicsector/university-hospitals-coventry-and-warwickshire-nhs-trust-digitizes-and-improves-patient-experience-with-aws/
  raw_file: ''
  text_file: sources/text/S1.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S2
  title: https://www.littlejourney.health/news/uhcw-case-study
  url: https://www.littlejourney.health/news/uhcw-case-study
  raw_file: ''
  text_file: sources/text/S2.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
value_claims:
- id: VC-001
  claim_title: 33% reduction in calls to booking centre through AI virtual assistant
  claim_description: Implementation of Amazon Lex-powered virtual assistant handling
    FAQs and appointment queries reduced calls to the booking centre by an estimated
    33 percent over an 8-week pilot period.
  source_ids:
  - S1
  source_quote: During this period, the new solutions dealt with 3,500 patient interactions,
    reducing calls to the booking centre by an estimated 33 percent
  quote_location: Significant progress section
  ai_attribution: direct
  attribution_evidence: The reduction in calls is directly attributed to the AI virtual
    assistant handling patient interactions autonomously using Amazon Lex ASR and
    NLU capabilities.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  - optimization
  outcome:
  - cost_reduction
  - velocity
  cognitive_depth: predictive
  metric_raw:
    value: '33'
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
  claim_title: £270,000 forecasted annual savings from prevented calls
  claim_description: The AI-powered patient engagement solutions delivered forecasted
    annual savings of more than £270,000 from prevented calls alone, based on 8-week
    pilot results.
  source_ids:
  - S1
  source_quote: This translated to forecasted annual savings of more than £270,000
    from prevented calls alone.
  quote_location: Significant progress section
  ai_attribution: direct
  attribution_evidence: Savings directly result from AI virtual assistant and automated
    SMS systems reducing manual call handling workload by the Patient Access Team.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
  - optimization
  outcome:
  - cost_reduction
  cognitive_depth: predictive
  metric_raw:
    value: '270000'
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
  claim_title: 3,500 patient interactions handled by AI solutions in 8 weeks
  claim_description: The virtual assistant and automated SMS solutions handled 3,500
    patient interactions during the 8-week pilot period, demonstrating adoption and
    operational impact.
  source_ids:
  - S1
  source_quote: During this period, the new solutions dealt with 3,500 patient interactions
  quote_location: Significant progress section
  ai_attribution: direct
  attribution_evidence: Patient interactions were directly handled by AI-powered virtual
    assistant and automated messaging systems without human intervention.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - velocity
  - experience
  cognitive_depth: predictive
  metric_raw:
    value: '3500'
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
- id: VC-004
  claim_title: 10,000+ referral text messages sent via automated system
  claim_description: The automated SMS referral confirmation system using Amazon Pinpoint
    sent more than 10,000 referral text messages during the 8-week pilot, improving
    patient communication.
  source_ids:
  - S1
  source_quote: sent more than 10,000 referral text messages
  quote_location: Significant progress section
  ai_attribution: direct
  attribution_evidence: Amazon Pinpoint automated the generation and delivery of personalized
    referral confirmation messages at scale without manual intervention.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - velocity
  - experience
  cognitive_depth: descriptive
  metric_raw:
    value: '10000'
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
  claim_title: Faster patient email response through intelligent categorization
  claim_description: AI-powered email analysis using Amazon Comprehend enabled faster
    response rates by automatically categorizing emails, identifying missing information,
    and sending automated replies.
  source_ids:
  - S1
  source_quote: This system enables the UHCW NHS Trust team to speed up response rates
    by providing intelligent email categorization and automated responses to patient
    emails.
  quote_location: Email responder section
  ai_attribution: direct
  attribution_evidence: Amazon Comprehend NLP capabilities directly analyze, classify,
    and extract information from emails, triggering automated responses and reducing
    manual processing time.
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
  cognitive_depth: diagnostic
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
  claim_title: Reduced follow-up emails through automated information requests
  claim_description: Automated email analysis reduced the number of follow-up emails
    staff needed to send by immediately requesting missing patient information, allowing
    faster processing of requests.
  source_ids:
  - S1
  source_quote: This results in the Patient Access Team having to send fewer follow-up
    emails requesting additional information from patients and allows them to process
    patient requests more quickly.
  quote_location: Email responder section
  ai_attribution: direct
  attribution_evidence: AI system automatically detects missing information and sends
    immediate automated requests, eliminating manual follow-up email cycles by staff.
  verification_status: verified
  evidence_level: method
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  - optimization
  outcome:
  - velocity
  - cost_reduction
  cognitive_depth: diagnostic
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
- id: VC-007
  claim_title: Improved patient satisfaction through convenient appointment management
  claim_description: Automated appointment reminder and change request system improved
    patient satisfaction by enabling convenient self-service appointment management
    via SMS and web interface.
  source_ids:
  - S1
  source_quote: Giving patients the ability to manage their medical appointments more
    conveniently improves their satisfaction with services and clinical outcomes.
  quote_location: Appointment reminder section
  ai_attribution: contributing
  attribution_evidence: AI-powered automation enables the convenient self-service
    capability, but satisfaction improvement also depends on system design and patient
    adoption factors.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_creation
  mechanism:
  - automation
  outcome:
  - experience
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
- id: VC-008
  claim_title: 8-week delivery of virtual assistant and SMS solutions
  claim_description: UHCW NHS Trust and IBM Consulting delivered functional virtual
    assistant and SMS solutions in only 8 weeks using AWS services and design thinking
    methodology.
  source_ids:
  - S1
  source_quote: In only eight weeks, UHCW NHS Trust and IBM Consulting delivered the
    virtual assistant and SMS solutions, which immediately began helping patients.
  quote_location: Significant progress section
  ai_attribution: contributing
  attribution_evidence: AWS AI services enabled rapid development, but delivery speed
    also depended on design thinking approach, partnership collaboration, and serverless
    architecture.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - innovation
  outcome:
  - velocity
  cognitive_depth: descriptive
  metric_raw:
    value: '8'
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
context_claims:
- id: CC-001
  context_type: organisational
  claim_title: UHCW NHS Trust serves population of over 1 million
  claim_description: University Hospitals Coventry and Warwickshire NHS Trust manages
    two major hospitals and serves a population of more than one million people.
  source_ids:
  - S1
  source_quote: University Hospitals Coventry and Warwickshire (UHCW) NHS Trust, which
    manages two major hospitals and serves a population of more than one million
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
  claim_title: Healthcare provider in UK National Health Service
  claim_description: UHCW is one of the UK's largest National Health Service (NHS)
    trusts providing healthcare services.
  source_ids:
  - S1
  source_quote: one of the UK's largest National Health Service (NHS) trusts
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
  claim_title: Patient engagement and appointment management function
  claim_description: The AI solutions target patient engagement, appointment scheduling,
    referral management, and patient access team operations.
  source_ids:
  - S1
  source_quote: UHCW NHS Trust is on its own digitization journey and has recognized
    that it needs to provide more convenient self-service options for patients to
    improve their experience of its services.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10404'
  apqc_name: Manage customer service
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
  context_type: strategic_intent
  claim_title: UHCWi innovation initiative focused on patient-first improvements
  claim_description: UHCW NHS Trust operates UHCWi innovation initiative focusing
    on continuous improvements that put patients first and empower staff to eliminate
    waste and deliver safer care.
  source_ids:
  - S1
  source_quote: This pilot project ties into UHCW NHS Trust's broader innovation initiative,
    UHCWi, which focuses on making continuous improvements that put patients first
    and empowers staff to eliminate waste within their processes and deliver safer
    care.
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
  claim_title: Legacy technology with manual processes
  claim_description: UHCW NHS Trust operated with legacy technology that relied heavily
    on phone calls and manual processes for contacting patients before the digitization
    initiative.
  source_ids:
  - S1
  source_quote: UHCW NHS Trust, which manages two major hospitals and serves a population
    of more than one million, has operated with legacy technology that relies heavily
    on phone calls and manual processes for contacting patients.
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
  context_type: temporal
  claim_title: 8-week pilot project timeframe
  claim_description: The AI patient engagement pilot project was executed over an
    8-week period using design thinking and rapid prototyping approach.
  source_ids:
  - S1
  source_quote: Taking an eight-week approach, IBM Consulting used design thinking
    and the technical knowledge of their Healthcare and Life Sciences team to quickly
    build initial prototypes on AWS.
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
  context_type: organisational
  claim_title: Partnership with IBM Consulting and AWS
  claim_description: UHCW NHS Trust partnered with IBM Consulting for healthcare expertise
    and technical delivery on AWS, with AWS and IBM providing investment and technology
    for the pilot.
  source_ids:
  - S1
  source_quote: It chose IBM Consulting as a partner to help with this, based on their
    healthcare expertise and technical delivery skills on AWS. IBM Consulting and
    AWS provided investment and technology for UHCW NHS Trust to pilot new solutions
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
  context_type: scale
  claim_title: Influx of phone calls and emails created operational challenges
  claim_description: The Trust experienced high volumes of phone calls and emails
    that created challenges for staff responding to patients, motivating the digital
    transformation.
  source_ids:
  - S1
  source_quote: At UHCW NHS Trust, an influx of phone calls and emails created challenges
    for staff responding to a specific sub-set of patients.
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
  context_type: products_services
  claim_title: Four AI-powered patient engagement solutions deployed
  claim_description: 'The pilot deployed four solutions: virtual assistant for FAQs,
    SMS referral confirmation, automated email responder, and automated appointment
    reminder/change system.'
  source_ids:
  - S1
  source_quote: 'The team chose four priority solutions to demonstrate the art of
    the possible and quantify potential benefits: A virtual assistant (VA) on Amazon
    Lex... An SMS text message referral confirmation system... An automated email
    responder... An automated outpatient appointment reminder and change request system'
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
- id: CC-010
  context_type: functional
  claim_title: Patient Access Team operations support
  claim_description: Solutions specifically designed to reduce workload and improve
    efficiency of the Patient Access Team handling appointment bookings and patient
    queries.
  source_ids:
  - S1
  source_quote: User inputs are matched against a knowledge base to provide standard
    responses, or trigger fulfillment code to gather more details, before handing
    off complex requests to a live agent in UHCW NHS Trust's Patient Access Team.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10404'
  apqc_name: Manage customer service
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
    total: 8
    verified: 8
    needs_review: 0
    rejected: 0
    by_attribution:
      direct: 6
      contributing: 2
  context_claims:
    total: 10
    verified: 7
    unverified: 3
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

# AI-Powered Patient Flow Optimization and Digital Patient Engagement

## Executive Summary

University Hospitals Coventry and Warwickshire NHS Trust: 33% reduction in calls to booking centre through AI virtual assistant.

## Key Findings

- **33% reduction in calls to booking centre through AI virtual assistant** — verified (outcome)
  - Quote: "During this period, the new solutions dealt with 3,500 patient interactions, reducing calls to the booking centre by an estimated 33 percent"

- **£270,000 forecasted annual savings from prevented calls** — verified (outcome)
  - Quote: "This translated to forecasted annual savings of more than £270,000 from prevented calls alone."

- **3,500 patient interactions handled by AI solutions in 8 weeks** — verified (adoption)
  - Quote: "During this period, the new solutions dealt with 3,500 patient interactions"

- **10,000+ referral text messages sent via automated system** — verified (adoption)
  - Quote: "sent more than 10,000 referral text messages"

- **Faster patient email response through intelligent categorization** — verified (method)
  - Quote: "This system enables the UHCW NHS Trust team to speed up response rates by providing intelligent email categorization and automated responses to patient emails."

- **Reduced follow-up emails through automated information requests** — verified (method)
  - Quote: "This results in the Patient Access Team having to send fewer follow-up emails requesting additional information from patients and allows them to process patient requests more quickly."

- **Improved patient satisfaction through convenient appointment management** — verified (method)
  - Quote: "Giving patients the ability to manage their medical appointments more conveniently improves their satisfaction with services and clinical outcomes."

- **8-week delivery of virtual assistant and SMS solutions** — verified (adoption)
  - Quote: "In only eight weeks, UHCW NHS Trust and IBM Consulting delivered the virtual assistant and SMS solutions, which immediately began helping patients."

## Sources

- **S1**: https://aws.amazon.com/blogs/publicsector/university-hospitals-coventry-and-warwickshire-nhs-trust-digitizes-and-improves-patient-experience-with-aws/
- **S2**: https://www.littlejourney.health/news/uhcw-case-study
