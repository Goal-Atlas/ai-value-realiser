---
case_id: uchicago-medicine-unified-patient-data-scaling
organisation: UChicago Medicine
title: Unified Patient Data and Scaling
date_created: '2026-01-29'
date_updated: '2026-01-29'
sources:
- id: S1
  title: https://mdclone.com/press-release/uchicago-medicine-and-the-university-of-chicag...
  url: https://mdclone.com/press-release/uchicago-medicine-and-the-university-of-chicago-collaborate-with-mdclone-to-improve-healthcare-data-access-for-clinical-care-insights-and-research/
  raw_file: ''
  text_file: sources/text/S1.txt
  extraction_method: unknown
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S2
  title: https://www.hcinnovationgroup.com/analytics-ai/quality-continuous-performance-im...
  url: https://www.hcinnovationgroup.com/analytics-ai/quality-continuous-performance-improvement/article/55299078/uchicago-medicine-undertaking-data-democratization-effort
  raw_file: ''
  text_file: sources/text/S2.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S3
  title: https://www.salesforce.com/news/press-releases/2025/06/24/university-chicago-age...
  url: https://www.salesforce.com/news/press-releases/2025/06/24/university-chicago-agentforce-patient-support/?bc=HL
  raw_file: ''
  text_file: sources/text/S3.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S4
  title: https://hdsi.uchicago.edu/
  url: https://hdsi.uchicago.edu/
  raw_file: ''
  text_file: sources/text/S4.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
value_claims:
- id: VC-001
  claim_title: Reduced data request fulfillment time from weeks to minutes
  claim_description: MDClone synthetic data platform eliminated long delays in data
    request fulfillment, enabling clinicians to get answers in minutes instead of
    waiting weeks for IT to process iterative data requests.
  source_ids:
  - S2
  source_quote: Previously it would have taken quite a bit of effort and time to even
    find that answer. We had that answer in minutes.
  quote_location: Interview with Tom Spiegel, ED medication usage example
  ai_attribution: direct
  attribution_evidence: MDClone's synthetic data platform directly enabled the speed
    improvement through automated data access and query capabilities
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  - optimization
  outcome:
  - velocity
  cognitive_depth: descriptive
  metric_raw:
    value: minutes vs weeks
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
  claim_title: Identified 586 patients for blood pressure medication optimization
  claim_description: Retired quality chief used MDClone to independently identify
    586 primary care patients with systolic BP over 160 across 3 years, enabling proactive
    medication protocol development with pharmacy team.
  source_ids:
  - S2
  source_quote: There were 586 patients he identified to say that we could be doing
    a better job, and we should be taking an active role in that.
  quote_location: Primary care blood pressure management example
  ai_attribution: direct
  attribution_evidence: MDClone platform directly enabled the physician to query and
    identify the patient cohort independently without IT support
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - augmentation
  - optimization
  outcome:
  - business_growth
  cognitive_depth: diagnostic
  metric_raw:
    value: '586'
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
  claim_title: Projected $50,000+ annual savings from anti-nausea medication optimization
  claim_description: ED team used MDClone to identify overuse of expensive anti-nausea
    medication ($44 vs $0.44 alternatives). Analysis across departments led to removal
    from post-op order list with dramatic decline in weeks.
  source_ids:
  - S2
  source_quote: if we use this three or four times a day over the course of a year,
    that's over $50,000 that we don't need to be spending...we've seen a dramatic
    decline of this already within the first few weeks.
  quote_location: ED medication cost optimization example
  ai_attribution: direct
  attribution_evidence: MDClone enabled rapid identification of usage patterns and
    departmental analysis that directly led to formulary changes
  verification_status: needs_review
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - optimization
  - augmentation
  outcome:
  - cost_reduction
  cognitive_depth: diagnostic
  metric_raw:
    value: '50000'
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
  claim_title: Enabled self-service data access for clinicians without IT dependency
  claim_description: Data democratization initiative eliminated iterative delays where
    clinicians requested data from IT, received it after long delays, then needed
    refinements. Clinicians now query data independently.
  source_ids:
  - S2
  source_quote: There are a lot of time delays from data request to fulfillment, and
    then it's never a one and done...After a long delay, you get your data, and then
    you realize you need six more elements
  quote_location: Data accessibility challenges discussion
  ai_attribution: direct
  attribution_evidence: MDClone synthetic data platform directly enabled self-service
    access, eliminating the IT intermediary requirement
  verification_status: needs_review
  evidence_level: method
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - automation
  - augmentation
  outcome:
  - velocity
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
- id: VC-005
  claim_title: 24/7 patient access to self-service information and support
  claim_description: Agentforce for Health implementation provides patients with round-the-clock
    access to tailored information and support for routine inquiries outside regular
    business hours.
  source_ids:
  - S3
  source_quote: provide patients with 24/7 access to tailored, self-service information
    and support
  quote_location: Agentforce implementation announcement
  ai_attribution: direct
  attribution_evidence: Agentforce AI agents directly provide the 24/7 automated patient
    support capability
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_creation
  mechanism:
  - automation
  outcome:
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
- id: VC-006
  claim_title: Automated routine patient inquiries to free staff for complex needs
  claim_description: Agentforce implementation intended to alleviate staff pressure
    by handling high-volume, non-urgent tasks, allowing staff to focus on complex
    needs requiring personalized attention.
  source_ids:
  - S3
  source_quote: agentic, AI-powered tools is intended to alleviate pressure on staff
    by assisting with high-volume, non-urgent tasks and providing patients with timely
    responses
  quote_location: Implementation rationale
  ai_attribution: direct
  attribution_evidence: Agentforce agents directly automate routine inquiries, creating
    capacity for staff to handle complex cases
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
  - augmentation
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
- id: VC-007
  claim_title: Event-based data organization enables complex temporal queries
  claim_description: MDClone's event-based data structure allows clinicians to query
    time-related clinical events (e.g., aspirin within 1 hour of chest pain arrival)
    that would be cumbersome in relational databases.
  source_ids:
  - S2
  source_quote: you could do time-related events. So I could say, within one hour
    of arriving at the emergency department with chest pain, did you get an aspirin?
  quote_location: Data organization explanation
  ai_attribution: direct
  attribution_evidence: MDClone's event-based architecture directly enables the temporal
    query capabilities
  verification_status: verified
  evidence_level: method
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - augmentation
  outcome:
  - velocity
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
- id: VC-008
  claim_title: Natural language processing enables unstructured data queries
  claim_description: MDClone's NLP application allows querying of unstructured clinical
    notes and radiology reports with few discrete data elements, expanding accessible
    data beyond structured fields.
  source_ids:
  - S2
  source_quote: This system does have a natural natural language processing application
    with it. So we could do notes queries. For instance, our radiology reports have
    very few discrete data elements
  quote_location: Unstructured data access discussion
  ai_attribution: direct
  attribution_evidence: NLP capabilities directly enable access to and querying of
    previously inaccessible unstructured clinical data
  verification_status: verified
  evidence_level: method
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - augmentation
  outcome:
  - velocity
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
- id: VC-009
  claim_title: Autonomous prescription refills and appointment scheduling
  claim_description: Agentforce implementation enables patients to autonomously refill
    prescriptions, schedule and modify appointments, and verify insurance through
    user-friendly chat interface.
  source_ids:
  - S3
  source_quote: Patients will be able to refill prescriptions, schedule and modify
    appointments, and verify insurance ahead of time through a user-friendly chat
    interface.
  quote_location: Planned capabilities description
  ai_attribution: direct
  attribution_evidence: Agentforce agents directly provide autonomous transaction
    capabilities for routine patient administrative tasks
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_creation
  mechanism:
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
- id: VC-010
  claim_title: Real-time logistical support for patient appointments
  claim_description: Agentforce can provide real-time travel support, such as notifying
    patients if parking garage is full and suggesting alternative locations during
    appointment travel.
  source_ids:
  - S3
  source_quote: Patients also could receive real-time logistical support when traveling
    to appointments, such as notifying them if a parking garage is full and suggesting
    an alternative location.
  quote_location: Advanced capabilities description
  ai_attribution: direct
  attribution_evidence: Agentforce agents directly monitor real-time conditions and
    provide proactive guidance to patients
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_creation
  mechanism:
  - automation
  - augmentation
  outcome:
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
  claim_title: UChicago Medicine is an academic medical center
  claim_description: UChicago Medicine operates as an academic health system with
    research, clinical care, and teaching missions
  source_ids:
  - S2
  - S3
  source_quote: The academic health system will soon handle personalized requests
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
  context_type: strategic_intent
  claim_title: Data democratization initiative to enable self-service analytics
  claim_description: Strategic initiative to allow clinicians, researchers, staff,
    and administrators to independently query and analyze data without IT intermediaries
  source_ids:
  - S2
  source_quote: our approach to data democratization really stemmed from a couple
    of different areas. One is research...let's open up the doors to data
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
  context_type: organisational
  claim_title: 'Three executive sponsors: Research Dean, Quality Officer, and IT'
  claim_description: Data democratization initiative has executive sponsorship from
    research, quality/hospital operations, and IT leadership
  source_ids:
  - S2
  source_quote: We have three executive sponsors on the team. One is our dean of research.
    I'm representing the hospital and the quality improvement entities. Our third
    partner is IT.
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
  context_type: temporal
  claim_title: MDClone implementation with early adopters in emergency department
  claim_description: Emergency department physicians were among early adopters of
    MDClone platform, with implementation mature enough for multiple completed projects
  source_ids:
  - S2
  source_quote: I'm an ER doc, and I am a big proponent of this entire approach...So
    I think they were some of the early adopters of this.
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
  context_type: functional
  claim_title: Quality improvement and continuous performance improvement focus
  claim_description: Initiative enables continuous quality improvement approach with
    rapid data access for iterative process changes and outcome tracking
  source_ids:
  - S2
  source_quote: Does this allow for them to think in terms of a continuous quality
    improvement approach, by requesting the data and getting it back rapidly
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10419'
  apqc_name: Manage quality
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
  claim_title: Thousands of primary care patients in data set
  claim_description: UChicago Medicine primary care population includes thousands
    of patients available for analysis
  source_ids:
  - S2
  source_quote: he looked across all of our thousands of primary care patients
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
  claim_title: Agentforce implementation announced June 2025
  claim_description: Salesforce Agentforce for Health implementation announced June
    24, 2025, with deployment in progress
  source_ids:
  - S3
  source_quote: 'SAN FRANCISCO AND CHICAGO – June 24, 2025 – Salesforce, the world''s
    #1 AI CRM, today announced that UChicago Medicine is implementing Agentforce'
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
  context_type: strategic_intent
  claim_title: Focus on non-clinical operational workflows for patient support
  claim_description: Agentforce implementation targets non-clinical, operational workflows
    for routine patient inquiries and administrative tasks
  source_ids:
  - S3
  source_quote: Agentforce, Salesforce's digital labor platform, is being integrated
    into the academic health system's non-clinical, operational workflows
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
  context_type: functional
  claim_title: Patient experience enhancement initiative
  claim_description: Broader organizational effort to enhance patient experience and
    streamline access to information through digital tools
  source_ids:
  - S3
  source_quote: As part of our broader efforts to enhance the patient experience and
    streamline access to information, we're implementing new digital tools
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10424'
  apqc_name: Manage patient/member experience
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
  claim_title: Privacy and policy considerations for synthetic data
  claim_description: Implementation required addressing privacy policies and administrative
    concerns, with synthetic data approach enabling broader access while maintaining
    privacy
  source_ids:
  - S2
  source_quote: From an administrative standpoint, privacy is the big lion's share
    of what we've had to come to terms with...it's not real patients. You can't trace
    any of this back to real patients.
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
- id: CC-011
  context_type: strategic_intent
  claim_title: Parallel self-service toolkit for enacting changes
  claim_description: Developing complementary toolkit to enable frontline providers
    to take action on insights, including changing order sets, care pathways, and
    EHR configurations
  source_ids:
  - S2
  source_quote: we're having a parallel work stream that's basically creating a self-service
    toolkit to enact change. How do you change order sets? How do you change a care
    pathway?
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
  claim_title: Campus-wide rollout planned after champion cohort
  claim_description: Initial implementation with small cohort of champions, with plans
    for campus-wide expansion across medical center and business school
  source_ids:
  - S2
  source_quote: We started off with a small cohort of our champions, who are now out
    talking about it with their colleagues. We're going to be doing this campus-wide.
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
- id: CC-013
  context_type: functional
  claim_title: Healthcare delivery science and innovation focus
  claim_description: HDSI represents overlap between healthcare operations, innovation,
    and research, studying system-level interventions rather than patient-level interventions
  source_ids:
  - S4
  source_quote: Healthcare Delivery Science and Innovation (HDSI) represents the overlap
    between healthcare operations and innovation and research. The healthcare system
    itself is the organism under both evaluation
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10419'
  apqc_name: Manage quality
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
  context_type: sectoral
  claim_title: Academic healthcare delivery with research integration
  claim_description: Organization integrates research-quality methods into real-world
    healthcare delivery operations
  source_ids:
  - S4
  source_quote: Healthcare delivery science integrates research-quality methods into
    what we actually do in the real world.
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
- id: CC-015
  context_type: products_services
  claim_title: MDClone synthetic data platform for healthcare analytics
  claim_description: MDClone provides synthetic data generation that maintains statistical
    properties while preventing patient re-identification
  source_ids:
  - S2
  source_quote: We are working with MDClone and it offers a very unique opportunity
    to create synthetic data sets...The system changes every element just a bit so
    that you can't trace it back
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
- id: CC-016
  context_type: products_services
  claim_title: Salesforce Agentforce for Health and Health Cloud
  claim_description: Salesforce digital labor platform with AI-powered agents integrated
    with Health Cloud for patient support automation
  source_ids:
  - S3
  source_quote: With the integration of Agentforce and Health Cloud, digital, AI-powered
    agents will help UChicago Medicine patients
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
    total: 10
    verified: 8
    needs_review: 2
    rejected: 0
    by_attribution:
      direct: 10
  context_claims:
    total: 16
    verified: 12
    unverified: 4
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

# Unified Patient Data and Scaling

## Executive Summary

UChicago Medicine: Reduced data request fulfillment time from weeks to minutes.

## Key Findings

- **Reduced data request fulfillment time from weeks to minutes** — verified (outcome)
  - Quote: "Previously it would have taken quite a bit of effort and time to even find that answer. We had that answer in minutes."

- **Identified 586 patients for blood pressure medication optimization** — verified (outcome)
  - Quote: "There were 586 patients he identified to say that we could be doing a better job, and we should be taking an active role in that."

- **Projected $50,000+ annual savings from anti-nausea medication optimization** — needs_review (outcome)
  - Quote: "if we use this three or four times a day over the course of a year, that's over $50,000 that we don't need to be spending...we've seen a dramatic decline of this already within the first few weeks."

- **Enabled self-service data access for clinicians without IT dependency** — needs_review (method)
  - Quote: "There are a lot of time delays from data request to fulfillment, and then it's never a one and done...After a long delay, you get your data, and then you realize you need six more elements"

- **24/7 patient access to self-service information and support** — verified (method)
  - Quote: "provide patients with 24/7 access to tailored, self-service information and support"

- **Automated routine patient inquiries to free staff for complex needs** — verified (method)
  - Quote: "agentic, AI-powered tools is intended to alleviate pressure on staff by assisting with high-volume, non-urgent tasks and providing patients with timely responses"

- **Event-based data organization enables complex temporal queries** — verified (method)
  - Quote: "you could do time-related events. So I could say, within one hour of arriving at the emergency department with chest pain, did you get an aspirin?"

- **Natural language processing enables unstructured data queries** — verified (method)
  - Quote: "This system does have a natural natural language processing application with it. So we could do notes queries. For instance, our radiology reports have very few discrete data elements"

- **Autonomous prescription refills and appointment scheduling** — verified (method)
  - Quote: "Patients will be able to refill prescriptions, schedule and modify appointments, and verify insurance ahead of time through a user-friendly chat interface."

- **Real-time logistical support for patient appointments** — verified (method)
  - Quote: "Patients also could receive real-time logistical support when traveling to appointments, such as notifying them if a parking garage is full and suggesting an alternative location."

## Sources

- **S1**: https://mdclone.com/press-release/uchicago-medicine-and-the-university-of-chicago-collaborate-with-mdclone-to-improve-healthcare-data-access-for-clinical-care-insights-and-research/
- **S2**: https://www.hcinnovationgroup.com/analytics-ai/quality-continuous-performance-improvement/article/55299078/uchicago-medicine-undertaking-data-democratization-effort
- **S3**: https://www.salesforce.com/news/press-releases/2025/06/24/university-chicago-agentforce-patient-support/?bc=HL
- **S4**: https://hdsi.uchicago.edu/
