---
case_id: providence-ai-patient-message-routing
organisation: Providence Health System
title: AI-Powered Patient Message Routing and Triage
date_created: '2026-01-29'
date_updated: '2026-01-29'
sources:
- id: S1
  title: https://blog.providence.org/blog/provaria-transforming-care-with-ai-patient-mess...
  url: https://blog.providence.org/blog/provaria-transforming-care-with-ai-patient-message-management
  raw_file: ''
  text_file: sources/text/S1.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S2
  title: https://www.beckershospitalreview.com/healthcare-information-technology/how-prov...
  url: https://www.beckershospitalreview.com/healthcare-information-technology/how-providence-measures-ai-roi/
  raw_file: ''
  text_file: sources/text/S2.txt
  extraction_method: unknown
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S3
  title: https://www.healthcareitnews.com/news/providence-developing-ai-tools-designed-re...
  url: https://www.healthcareitnews.com/news/providence-developing-ai-tools-designed-reduce-clinician-burnout
  raw_file: ''
  text_file: sources/text/S3.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S4
  title: https://blog.providence.org/blog/digital-in-action-improving-patient-navigation-...
  url: https://blog.providence.org/blog/digital-in-action-improving-patient-navigation-with-grace
  raw_file: ''
  text_file: sources/text/S4.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
value_claims:
- id: VC-001
  claim_title: 57% reduction in messages to doctors through AI triage
  claim_description: Provaria's AI-powered message categorization and routing reduced
    the number of messages reaching doctors by 57% by enabling nurses and medical
    assistants to handle appropriate messages.
  source_ids:
  - S1
  source_quote: Thanks to its intelligent categorizing and tagging, dedicated nurses
    and medical assistants could quickly respond to messages without waiting for doctors.
    Doctors ended up receiving 57% fewer messages as a result.
  quote_location: How Provaria improves patient care section
  ai_attribution: direct
  attribution_evidence: The reduction is directly attributed to Provaria's AI categorization
    enabling appropriate message routing to non-physician staff
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  - optimization
  outcome:
  - velocity
  - experience
  cognitive_depth: prescriptive
  metric_raw:
    value: '57'
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
  claim_title: 50% reduction in patient response time
  claim_description: Provaria reduced the time patients waited to receive a response
    to their MyChart messages by 50% through intelligent message prioritization and
    routing.
  source_ids:
  - S1
  source_quote: Patients also benefited, with a 50% reduction in the time it took
    to receive a response.
  quote_location: How Provaria improves patient care section
  ai_attribution: direct
  attribution_evidence: The response time improvement is directly attributed to Provaria's
    AI-powered message categorization and prioritization
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  - optimization
  outcome:
  - velocity
  - experience
  cognitive_depth: prescriptive
  metric_raw:
    value: '50'
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
  claim_title: 300,000 messages screened in 10 months across 264 clinics
  claim_description: Within 10 months of release, Provaria processed 300,000 patient
    messages across 264 clinics, demonstrating rapid adoption and scale.
  source_ids:
  - S1
  source_quote: In just 10 months after its release, Provaria screened 300,000 messages
    sent to 264 clinics.
  quote_location: How Provaria improves patient care section
  ai_attribution: direct
  attribution_evidence: The volume of messages screened is directly attributed to
    Provaria's deployment and operation
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - velocity
  cognitive_depth: prescriptive
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
- id: VC-004
  claim_title: 3 million messages processed to date
  claim_description: Providence has processed more than 3 million patient messages
    using Provaria, demonstrating sustained large-scale deployment.
  source_ids:
  - S1
  source_quote: To date, Providence has processed more than three million messages
    with the help of Provaria.
  quote_location: What's on the horizon section
  ai_attribution: direct
  attribution_evidence: The cumulative message volume is directly attributed to Provaria's
    ongoing operation
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - velocity
  cognitive_depth: prescriptive
  metric_raw:
    value: '3000000'
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
  claim_title: Urgent message identified and responded to in under 1 hour
  claim_description: Provaria identified a message describing worsening depression
    symptoms as urgent, enabling response in less than 1 hour versus the previous
    3-day delay, potentially preventing patient self-harm.
  source_ids:
  - S1
  source_quote: In the past, a medical assistant or nurse would have read this message
    in the order it was received. If many patients had sent messages, it might have
    taken three days to reach this message. But thanks to new technology developed
    by Providence, the message was tagged as urgent and read less than an hour after
    it was sent.
  quote_location: Opening case study
  ai_attribution: direct
  attribution_evidence: The rapid identification and response is directly attributed
    to Provaria's AI-powered urgent message tagging
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  - optimization
  outcome:
  - velocity
  - experience
  - risk_avoidance
  cognitive_depth: prescriptive
  metric_raw:
    value: '1'
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
- id: VC-006
  claim_title: Reduction in clinician pajama time through message triage
  claim_description: Provaria helps reduce after-hours work ('pajama time') for clinicians
    by enabling appropriate message routing to support staff, reducing physician workload.
  source_ids:
  - S1
  source_quote: Working through a mountain of messages contributes to caregiver burnout,
    and what people in the health care industry refer to as 'pajama time.' A lot of
    times doctors see patients all day, and they go home, and instead of spending
    time with their family, they log back into Epic and they start working again,
    in their pajamas.
  quote_location: Lots of messages, not enough time section
  ai_attribution: contributing
  attribution_evidence: Provaria contributes to reducing pajama time by routing messages
    appropriately, though specific reduction metrics not provided
  verification_status: needs_review
  evidence_level: method
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
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
- id: VC-007
  claim_title: MedPearl reduces cognitive load through consolidated clinical intelligence
  claim_description: MedPearl platform consolidates clinical knowledge, patient data,
    and suggested next actions into a single interface, reducing cognitive load and
    optimizing clinician workflow.
  source_ids:
  - S3
  source_quote: MedPearl enhances clinical decision-making by consolidating clinical
    knowledge, patient data, and suggested next best actions at the point of care
    into a single interface, thereby optimizing clinicians' workflow and reducing
    the cognitive load.
  quote_location: Q&A section on AI in action
  ai_attribution: direct
  attribution_evidence: The cognitive load reduction is directly attributed to MedPearl's
    AI-enhanced consolidation of clinical information
  verification_status: verified
  evidence_level: method
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - augmentation
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
- id: VC-008
  claim_title: Grace chatbot serves 101,000 active monthly users
  claim_description: Providence's AI-powered chatbot Grace has achieved 101,000 active
    monthly users for patient navigation and self-service tasks.
  source_ids:
  - S4
  source_quote: The Providence app and Grace have already helped thousands of patients
    find answers to their questions, with more than 101,000 active monthly users on
    the app.
  quote_location: Building patient navigation support section
  ai_attribution: direct
  attribution_evidence: The user adoption is directly attributed to Grace's AI-powered
    patient navigation capabilities
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - automation
  - augmentation
  outcome:
  - experience
  - velocity
  cognitive_depth: prescriptive
  metric_raw:
    value: '101000'
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
  context_type: temporal
  claim_title: 10-year shift from phone calls to MyChart messages
  claim_description: Over the past 10 years, patient communication shifted from phone
    calls to MyChart messages, creating operational challenges.
  source_ids:
  - S1
  source_quote: Since COVID, the number of in-basket messages from patients to doctors
    has really taken off. Ten years ago, everyone was making phone calls. But now,
    everything's MyChart messages.
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
- id: CC-002
  context_type: organisational
  claim_title: Providence is a large health system
  claim_description: Providence is characterized as a large health system with complex
    patient navigation needs.
  source_ids:
  - S4
  source_quote: At a basic level, finding and using health care services can feel
    complex, especially in a large health system like Providence.
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
- id: CC-003
  context_type: functional
  claim_title: Patient message management and triage
  claim_description: Provaria operates in the patient communication and triage function,
    managing MyChart messages from patients to providers.
  source_ids:
  - S1
  source_quote: Provaria, Providence's In-Basket Assistant, a groundbreaking technology
    that uses AI to categorize the MyChart messages patients send automatically.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10440'
  apqc_name: Manage Patient/Member Experience
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
  claim_title: In-house AI development over vendor solutions
  claim_description: Providence chose to develop Provaria in-house rather than use
    vendor solutions, citing better understanding of clinical workflows and collaboration
    culture.
  source_ids:
  - S1
  source_quote: First, Dr. Parsons looked at various vendors. It was right around
    the time that large language models, a type of AI, were starting to become popular.
    All the vendors' technology felt outdated, and none truly understood a doctor's
    office workflow. So, Providence chose to develop the technology in-house.
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
- id: CC-005
  context_type: organisational
  claim_title: Collaborative culture between clinical and technical teams
  claim_description: Providence has a culture of collaboration between informatics
    experts, AI experts, and clinical staff in developing AI solutions.
  source_ids:
  - S1
  source_quote: We didn't think of our nurses and medical assistants as customers.
    They were helping build this with us. We had informatics gurus. We had AI gurus.
    And we had clinical gurus all working together and building this thing. I think
    it would be pretty hard to do if we didn't have that culture of collaboration
    here at Providence.
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
  context_type: scale
  claim_title: Deployment across all primary care clinics
  claim_description: Provaria expanded from 4 pilot sites to all primary care clinics
    including family medicine, internal medicine, and pediatrics.
  source_ids:
  - S1
  source_quote: Providence initially launched Provaria in four clinic pilot sites.
    With promising results in turnaround time and quicker care, Providence extended
    Provaria's reach to all its primary care clinics, including family medicine, internal
    medicine and pediatrics.
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
  context_type: sectoral
  claim_title: Healthcare sector addressing clinician burnout
  claim_description: The healthcare industry is experiencing widespread clinician
    burnout, exacerbated by administrative workload including message management.
  source_ids:
  - S1
  - S3
  source_quote: Working through a mountain of messages contributes to caregiver burnout,
    and what people in the health care industry refer to as 'pajama time.'
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
  context_type: organisational
  claim_title: Providence Digital Innovation Group (DIG) leads digital initiatives
  claim_description: Providence has a dedicated Digital Innovation Group responsible
    for developing digital tools including the Providence app and Grace chatbot.
  source_ids:
  - S4
  source_quote: The Providence Digital Innovation Group (DIG) is working to make the
    patient navigation experience simpler for patients through innovative digital
    tools, including the Providence app and its chatbot, Grace.
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
- id: CC-009
  context_type: functional
  claim_title: Patient navigation and self-service
  claim_description: Grace chatbot provides patient navigation including appointment
    scheduling, lab results access, bill payment, and financial assistance eligibility.
  source_ids:
  - S4
  source_quote: Working as a navigation tool, Grace can help with some of the 'admin'
    tasks of managing your health care, including scheduling appointments, finding
    lab and test results, navigating your health record, and paying bills. Grace can
    also support more in-depth tasks like checking eligibility for financial assistance.
  verification_status: unverified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10440'
  apqc_name: Manage Patient/Member Experience
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
  context_type: products_services
  claim_title: MedPearl as AI-enhanced clinical intelligence platform
  claim_description: MedPearl is an AI-enhanced clinical intelligence engine designed
    by and for clinicians, founded by Dr. Eve Cunningham.
  source_ids:
  - S3
  source_quote: Dr. Eve Cunningham is all over this subject. She is group vice president
    and chief of virtual care and digital health at Providence, and founder and chief
    executive of MedPearl. The MedPearl platform is an AI-enhanced clinical intelligence
    engine designed by and for clinicians.
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
  claim_title: Human-in-the-loop AI philosophy
  claim_description: Providence maintains a philosophy that AI should augment rather
    than replace human clinicians, with humans always in control of patient communications.
  source_ids:
  - S1
  source_quote: The AI is helping humans know what order to look at the messages.
    AI is not replying to people. There's always a human, either a medical assistant,
    nurse or doctor, reading the message. We need our nurses. We need our medical
    assistants. AI isn't intended to replace people. It's intended to free them up
    to do the stuff that they're uniquely qualified to do.
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
  context_type: temporal
  claim_title: Planned expansion to specialty clinics and phone triage
  claim_description: Providence plans to expand Provaria to specialty clinics (cardiology,
    OB-GYN, surgery, neurology) and phone message triage.
  source_ids:
  - S1
  source_quote: A lot of the specialty clinics have asked to have this same functionality
    turned on for them, such as cardiology and OB-GYN. People still use the phone.
    And those phone calls are captured and triaged in more or less the same way by
    the same people. Pretty soon after we deployed the in-basket classification, these
    same folks were saying, 'Can you categorize these phone messages as well?'
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
    total: 8
    verified: 7
    needs_review: 1
    rejected: 0
    by_attribution:
      direct: 7
      contributing: 1
  context_claims:
    total: 12
    verified: 3
    unverified: 9
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

# AI-Powered Patient Message Routing and Triage

## Executive Summary

Providence Health System: 57% reduction in messages to doctors through AI triage.

## Key Findings

- **57% reduction in messages to doctors through AI triage** — verified (outcome)
  - Quote: "Thanks to its intelligent categorizing and tagging, dedicated nurses and medical assistants could quickly respond to messages without waiting for doctors. Doctors ended up receiving 57% fewer messages..."

- **50% reduction in patient response time** — verified (outcome)
  - Quote: "Patients also benefited, with a 50% reduction in the time it took to receive a response."

- **300,000 messages screened in 10 months across 264 clinics** — verified (adoption)
  - Quote: "In just 10 months after its release, Provaria screened 300,000 messages sent to 264 clinics."

- **3 million messages processed to date** — verified (adoption)
  - Quote: "To date, Providence has processed more than three million messages with the help of Provaria."

- **Urgent message identified and responded to in under 1 hour** — verified (outcome)
  - Quote: "In the past, a medical assistant or nurse would have read this message in the order it was received. If many patients had sent messages, it might have taken three days to reach this message. But thank..."

- **Reduction in clinician pajama time through message triage** — needs_review (method)
  - Quote: "Working through a mountain of messages contributes to caregiver burnout, and what people in the health care industry refer to as 'pajama time.' A lot of times doctors see patients all day, and they go..."

- **MedPearl reduces cognitive load through consolidated clinical intelligence** — verified (method)
  - Quote: "MedPearl enhances clinical decision-making by consolidating clinical knowledge, patient data, and suggested next best actions at the point of care into a single interface, thereby optimizing clinician..."

- **Grace chatbot serves 101,000 active monthly users** — verified (adoption)
  - Quote: "The Providence app and Grace have already helped thousands of patients find answers to their questions, with more than 101,000 active monthly users on the app."

## Sources

- **S1**: https://blog.providence.org/blog/provaria-transforming-care-with-ai-patient-message-management
- **S2**: https://www.beckershospitalreview.com/healthcare-information-technology/how-providence-measures-ai-roi/
- **S3**: https://www.healthcareitnews.com/news/providence-developing-ai-tools-designed-reduce-clinician-burnout
- **S4**: https://blog.providence.org/blog/digital-in-action-improving-patient-navigation-with-grace
