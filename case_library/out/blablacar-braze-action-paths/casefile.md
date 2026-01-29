---
case_id: blablacar-braze-action-paths
organisation: BlaBlaCar
title: AI-Powered Marketing Automation and Personalization
date_created: '2026-01-29'
date_updated: '2026-01-29'
sources:
- id: S1
  title: https://www.braze.com/customers/blablacar-case-study-abandoned-cart
  url: https://www.braze.com/customers/blablacar-case-study-abandoned-cart
  raw_file: ''
  text_file: sources/text/S1.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S2
  title: https://www.braze.com/customers/blablacar-case-study
  url: https://www.braze.com/customers/blablacar-case-study
  raw_file: ''
  text_file: sources/text/S2.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S3
  title: https://aws.amazon.com/blogs/apn/transforming-the-customer-experience-at-speed-a...
  url: https://aws.amazon.com/blogs/apn/transforming-the-customer-experience-at-speed-and-scale-with-aws-and-braze/
  raw_file: ''
  text_file: sources/text/S3.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S4
  title: https://www.linkedin.com/posts/braze_blablacar-x-braze-activity-7093267183174066...
  url: https://www.linkedin.com/posts/braze_blablacar-x-braze-activity-7093267183174066178-rBnV
  raw_file: ''
  text_file: sources/text/S4.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
value_claims:
- id: VC-002
  claim_title: 48% uplift in click rate through personalized messaging
  claim_description: BlaBlaCar achieved a 48% increase in message click rates by using
    Connected Content dynamic personalization to populate messages with customized
    content based on user behavior and search parameters.
  source_ids:
  - S1
  source_quote: BlaBlaCar saw up to a 48% uplift in their message click rate and up
    to a 30% uplift in conversions (bookings) in connection with the enriched version
    of the emails.
  quote_location: S1, Results section
  ai_attribution: direct
  attribution_evidence: Canvas Flow's personalization features and Connected Content
    directly enabled the enriched messaging that drove the 48% click rate improvement.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - augmentation
  - optimization
  outcome:
  - experience
  - velocity
  cognitive_depth: prescriptive
  metric_raw:
    value: '48'
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
  claim_title: 24% increase in email open rates through sender name optimization
  claim_description: BlaBlaCar increased email open rates by up to 24% by testing
    and implementing personalized sender names (real person names) instead of the
    brand name 'BlaBlaCar' across multiple markets.
  source_ids:
  - S2
  source_quote: In fact, the brand discovered that sending emails with the first names
    of real people resulted in 20+% higher open rates for their messages, compared
    to emails sent from 'BlaBlaCar.'
  quote_location: S2, Step Four section
  ai_attribution: direct
  attribution_evidence: Braze Canvas automation enabled systematic A/B testing across
    markets to identify optimal sender names, directly driving the 24% open rate improvement.
  verification_status: needs_review
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - optimization
  - automation
  outcome:
  - experience
  - velocity
  cognitive_depth: predictive
  metric_raw:
    value: '24'
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
  claim_title: Reduced manual testing and QA time through action paths
  claim_description: BlaBlaCar reduced time spent on manual testing and QA by leveraging
    Canvas Flow's action paths and audience evaluation features, eliminating need
    for workarounds and manual user verification.
  source_ids:
  - S1
  source_quote: Action paths and audience evaluation allows the team to be more confident,
    and spend less time on manual testing and QAing. They also don't have to waste
    time on finding workarounds or checking random users.
  quote_location: S1, Building strategy section, point 11
  ai_attribution: direct
  attribution_evidence: Canvas Flow's automated action paths and audience evaluation
    directly replaced manual testing processes, reducing time spent on QA activities.
  verification_status: needs_review
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - velocity
  - cost_reduction
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
- id: VC-005
  claim_title: Faster creation of complex customer journeys
  claim_description: Canvas Flow enabled BlaBlaCar to create more complex customer
    journey Canvases in less time and iterate more easily and frequently, with granular
    control over specific components.
  source_ids:
  - S1
  source_quote: Using Canvas Flow, it's possible to create more complex Canvases in
    less time and to iterate more easily and frequently. Now, when BlaBlaCar creates
    a Canvas, they know they can control specific components with more granularity.
  quote_location: S1, Building strategy section, point 9
  ai_attribution: direct
  attribution_evidence: Canvas Flow's drag-and-drop interface and automation features
    directly enabled faster creation and iteration of complex customer journeys.
  verification_status: needs_review
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
  - augmentation
  outcome:
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
  claim_title: Increased team productivity through reduced engineering dependencies
  claim_description: Canvas Flow's advanced automation helped BlaBlaCar cut back on
    coordination with engineering and data teams, leading to more iterative and impactful
    campaigns and increased team productivity.
  source_ids:
  - S1
  source_quote: Braze Canvas Flow has enabled BlaBlaCar to reach more of their customers
    at scale and increase team productivity. This feature can help drive financial
    KPIs, and its advanced automation can help teams cut back on back and forth with
    engineering and data teams.
  quote_location: S1, Introduction section
  ai_attribution: direct
  attribution_evidence: Canvas Flow's automation directly reduced need for engineering
    team involvement, enabling marketing team to work more independently and productively.
  verification_status: needs_review
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - velocity
  - cost_reduction
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
  claim_title: BlaBlaCar operates community-based travel platform with 100M+ members
  claim_description: BlaBlaCar is a community-based travel network enabling over 100
    million members to rideshare across 22 global markets, facilitating 120 million
    human connections annually.
  source_ids:
  - S1
  source_quote: BlaBlaCar is leading the way in community-based travel, with a network
    that enables over 100 million members to rideshare across 22 global markets.
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
  claim_title: BlaBlaCar operates in on-demand transportation industry
  claim_description: BlaBlaCar operates in the on-demand transportation and travel
    sector, providing ridesharing and bus travel services.
  source_ids:
  - S1
  - S2
  source_quote: 'INDUSTRY: On-Demand'
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
  context_type: temporal
  claim_title: BlaBlaCar adopted Braze platform in 2017
  claim_description: BlaBlaCar migrated to Braze customer engagement platform in 2017
    from an internal email-focused tool to support cross-channel campaigns and app-first
    strategy.
  source_ids:
  - S1
  source_quote: Finding a partner for their customer engagement led them to Braze
    in 2017. Before adopting Braze, BlaBlaCar used an internal tool focused on email
    that couldn't send push.
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
- id: CC-004
  context_type: temporal
  claim_title: Canvas Flow feature released in 2022
  claim_description: Braze Canvas Flow, the customer journey orchestration tool used
    by BlaBlaCar, was released in 2022, enabling creation of previously impossible
    customer journeys.
  source_ids:
  - S1
  source_quote: Canvas Flow, which was released in 2022, enabled BlaBlaCar to create
    Canvases they couldn't have created before.
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
  context_type: functional
  claim_title: Marketing and customer engagement function
  claim_description: BlaBlaCar's marketing team focuses on customer engagement across
    lifecycle stages including activation, onboarding, and retention to build lasting
    customer relationships.
  source_ids:
  - S1
  source_quote: By actively accompanying users at every step of the lifecycle, BlaBlaCar's
    marketing team works to build lasting customer relationships that lead to increased
    brand loyalty and repeat business.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '3.0'
  apqc_name: Market and Sell Products and Services
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
  claim_title: App-first strategy adoption
  claim_description: BlaBlaCar adopted an app-first strategy, necessitating migration
    to Braze platform to support cross-channel campaigns including push notifications.
  source_ids:
  - S1
  source_quote: As the company adopted an app-first strategy, these limitations necessitated
    the migration to Braze.
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
  claim_title: Operations across 22 countries with 87M members
  claim_description: BlaBlaCar operates a carpooling app across 22 countries with
    87 million members as of the sender name testing campaign period.
  source_ids:
  - S3
  source_quote: For BlaBlaCar, a carpooling app that operates in 22 countries with
    87 million members, the ability to test marketing hypotheses at scale has made
    a huge impact.
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
  context_type: products_services
  claim_title: Ridesharing and bus travel services
  claim_description: BlaBlaCar provides both carpooling/ridesharing services and bus
    travel booking services to connect travelers.
  source_ids:
  - S1
  source_quote: the technology they leverage is as practical as it is visionary, connecting
    members looking to sync up a carpool or travel by bus.
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
  claim_title: Environmental sustainability focus
  claim_description: BlaBlaCar's environmentally friendly ridesharing approach saves
    1.6 million tons of CO2 annually, demonstrating commitment to sustainable transportation.
  source_ids:
  - S1
  source_quote: BlaBlaCar's environmentally friendly approach saves 1.6 million tons
    of CO2 annually and drives 120 million human connections annually.
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
  claim_title: Abandoned cart recovery program
  claim_description: BlaBlaCar identified users abandoning booking process before
    completion and implemented abandoned cart recovery program to address conversion
    funnel leakage.
  source_ids:
  - S1
  source_quote: Passengers come to BlaBlaCar to plan their next trip, but the company
    noticed there were places in the customer journey where some users were dropping
    off.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '3.5'
  apqc_name: Manage Customer Service
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
    total: 5
    verified: 1
    needs_review: 4
    rejected: 0
    by_attribution:
      direct: 5
  context_claims:
    total: 10
    verified: 7
    unverified: 3
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

# AI-Powered Marketing Automation and Personalization

## Executive Summary

BlaBlaCar: 48% uplift in click rate through personalized messaging.

## Key Findings

- **48% uplift in click rate through personalized messaging** — verified (outcome)
  - Quote: "BlaBlaCar saw up to a 48% uplift in their message click rate and up to a 30% uplift in conversions (bookings) in connection with the enriched version of the emails."

- **24% increase in email open rates through sender name optimization** — needs_review (outcome)
  - Quote: "In fact, the brand discovered that sending emails with the first names of real people resulted in 20+% higher open rates for their messages, compared to emails sent from 'BlaBlaCar.'"

- **Reduced manual testing and QA time through action paths** — needs_review (method)
  - Quote: "Action paths and audience evaluation allows the team to be more confident, and spend less time on manual testing and QAing. They also don't have to waste time on finding workarounds or checking random..."

- **Faster creation of complex customer journeys** — needs_review (method)
  - Quote: "Using Canvas Flow, it's possible to create more complex Canvases in less time and to iterate more easily and frequently. Now, when BlaBlaCar creates a Canvas, they know they can control specific compo..."

- **Increased team productivity through reduced engineering dependencies** — needs_review (method)
  - Quote: "Braze Canvas Flow has enabled BlaBlaCar to reach more of their customers at scale and increase team productivity. This feature can help drive financial KPIs, and its advanced automation can help teams..."

## Sources

- **S1**: https://www.braze.com/customers/blablacar-case-study-abandoned-cart
- **S2**: https://www.braze.com/customers/blablacar-case-study
- **S3**: https://aws.amazon.com/blogs/apn/transforming-the-customer-experience-at-speed-and-scale-with-aws-and-braze/
- **S4**: https://www.linkedin.com/posts/braze_blablacar-x-braze-activity-7093267183174066178-rBnV
