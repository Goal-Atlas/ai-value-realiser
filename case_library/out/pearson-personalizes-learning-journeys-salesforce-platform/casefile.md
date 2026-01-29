---
case_id: pearson-personalizes-learning-journeys-salesforce-platform
organisation: Pearson Education
title: AI-Powered Customer Service and Learning Journey Personalization
date_created: '2026-01-29'
date_updated: '2026-01-29'
sources:
- id: S1
  title: https://www.salesforce.com/customer-stories/pearson/?bc=OTH
  url: https://www.salesforce.com/customer-stories/pearson/?bc=OTH
  raw_file: ''
  text_file: sources/text/S1.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S2
  title: https://nucleusresearch.com/research/single/salesforce-roi-case-study-pearson-ed...
  url: https://nucleusresearch.com/research/single/salesforce-roi-case-study-pearson-education/
  raw_file: ''
  text_file: sources/text/S2.txt
  extraction_method: unknown
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S3
  title: https://www.salesforce.com/blog/a-leader-in-online-learning-predicts-the-future-...
  url: https://www.salesforce.com/blog/a-leader-in-online-learning-predicts-the-future-of-education/?bc=HL
  raw_file: ''
  text_file: sources/text/S3.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
value_claims:
- id: VC-001
  claim_title: Agentforce handles 40% of routine customer inquiries
  claim_description: Agentforce automates approximately 40% of routine customer service
    inquiries, enabling the service team to focus on more complex learner needs and
    improving operational efficiency.
  source_ids:
  - S1
  source_quote: Agentforce handles an estimated 40% of routine customer inquiries,
    so the service team can prioritize complex learner needs.
  quote_location: Main content section
  ai_attribution: direct
  attribution_evidence: Agentforce directly handles customer inquiries autonomously,
    performing tasks like answering FAQs, processing returns, tracking orders, and
    generating invoices without human intervention.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  - augmentation
  outcome:
  - velocity
  - cost_reduction
  cognitive_depth: autonomous
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
- id: VC-002
  claim_title: Automated refund processing through integrated systems
  claim_description: Agentforce autonomously processes customer refunds by checking
    order history in Oracle ERP via MuleSoft API, verifying eligibility through knowledge
    base, and initiating refunds, reducing manual processing time.
  source_ids:
  - S1
  source_quote: After Agentforce confirms the purchase is eligible for a refund by
    cross-checking it with Pearson's knowledge base via Data 360, Agentforce initiates
    a refund in Oracle ERP and lets the customer know they're all set.
  quote_location: Agentforce implementation section
  ai_attribution: direct
  attribution_evidence: Agentforce directly executes the entire refund workflow autonomously,
    from verification to processing to customer notification, without human intervention.
  verification_status: verified
  evidence_level: method
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  - optimization
  outcome:
  - velocity
  - experience
  cognitive_depth: autonomous
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
  claim_title: Semantic search improves knowledge base accuracy
  claim_description: Data 360 enables semantic searches that understand query intent
    rather than exact keywords, delivering more accurate answers without manual metadata
    management across thousands of knowledge articles.
  source_ids:
  - S1
  source_quote: With Data 360, Agentforce can perform semantic searches, which means
    it understands the intent behind a query rather than just matching exact keywords.
    This delivers more accurate answers without the need to manually manage keywords,
    tags, or other metadata.
  quote_location: Data 360 capabilities section
  ai_attribution: direct
  attribution_evidence: AI-powered semantic search directly improves answer accuracy
    by understanding intent, eliminating the need for manual keyword management that
    would otherwise be required.
  verification_status: needs_review
  evidence_level: method
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - optimization
  - augmentation
  outcome:
  - velocity
  - experience
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
  claim_title: Improved self-service resolution metrics
  claim_description: Deployment of integrated support community and interactive chatbots
    enabled students to resolve questions faster through self-service while improving
    average handle time and first call resolution metrics.
  source_ids:
  - S3
  source_quote: deployment of an integrated support community and interactive chat
    bots have enabled students to resolve questions and issues faster through self-service
    while improving key metrics like average handle time and first call (contact)
    resolution.
  quote_location: Salesforce Platform usage section
  ai_attribution: direct
  attribution_evidence: Interactive chatbots directly enable self-service resolution,
    reducing handle time and improving first contact resolution through automated
    responses.
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
  - cost_reduction
  cognitive_depth: prescriptive
  metric_raw:
    value: improved
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
  claim_title: Seamless handoff with full context preservation
  claim_description: When Agentforce cannot answer a question, it seamlessly transfers
    customers to human reps with full context. All interactions are saved to Data
    360 for complete customer records across future conversations.
  source_ids:
  - S1
  source_quote: Agentforce seamlessly transfers them to a service rep with full context.
    Every interaction is saved into Data 360, giving Pearson a complete customer record
    so future conversations pick up right where they left off.
  quote_location: Agentforce workflow section
  ai_attribution: contributing
  attribution_evidence: AI contributes to improved service by maintaining context
    and enabling smooth handoffs, but the ultimate resolution may involve human agents
    working with AI-provided information.
  verification_status: needs_review
  evidence_level: method
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - augmentation
  - optimization
  outcome:
  - experience
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
- id: VC-006
  claim_title: Sales development agent for lead qualification
  claim_description: Pearson launched a sales development agent to help prospect and
    qualify leads, with additional marketing agents planned, expanding AI automation
    beyond customer service.
  source_ids:
  - S1
  source_quote: They've launched a sales development agent to help prospect and qualify
    leads, with marketing agents next in line.
  quote_location: Future agents section
  ai_attribution: direct
  attribution_evidence: The sales development agent directly performs prospecting
    and lead qualification tasks, automating sales development activities.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  - augmentation
  outcome:
  - velocity
  - business_growth
  cognitive_depth: prescriptive
  metric_raw:
    value: launched
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
- id: VC-007
  claim_title: Unified customer journey visibility across divisions
  claim_description: Data 360 ingests and unifies knowledge across divisions, providing
    real-time visibility into the complete customer journey including program progression,
    struggle points, and success factors for outcome improvement.
  source_ids:
  - S1
  source_quote: This real-time visibility gives Pearson a full view of the customer
    journey — not just website clicks and email opens, but how they progress through
    programs, where they struggle, and what helps them succeed.
  quote_location: Data 360 expansion section
  ai_attribution: contributing
  attribution_evidence: AI-powered data unification and analytics contribute to visibility
    and insights that enable human decision-makers to improve outcomes, but AI does
    not directly deliver the improvements.
  verification_status: verified
  evidence_level: method
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - optimization
  - augmentation
  outcome:
  - experience
  - business_growth
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
  claim_title: Personalized marketing outreach throughout learner lifecycle
  claim_description: Marketing Cloud enables personalized outreach to learners as
    they progress through coursework and careers, sending relevant updates, event
    invitations, and program reminders to support continuous engagement.
  source_ids:
  - S1
  source_quote: As learners progress through coursework, ace the test, and advance
    in their careers, Pearson keeps them inspired to grow through personalized outreach
    in Marketing Cloud.
  quote_location: Marketing Cloud section
  ai_attribution: contributing
  attribution_evidence: AI contributes to personalization by analyzing learner data
    and enabling targeted communications, but works alongside human-designed marketing
    strategies.
  verification_status: verified
  evidence_level: method
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - optimization
  - augmentation
  outcome:
  - experience
  - business_growth
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
context_claims:
- id: CC-001
  context_type: organisational
  claim_title: Pearson is a global education company with nearly 100 years of history
  claim_description: Pearson has helped people across the globe grow their skills
    and knowledge at every stage of life, from kindergarten through retirement, for
    almost 100 years.
  source_ids:
  - S1
  source_quote: for almost 100 years, they've helped people across the globe grow
    their skills and knowledge at every stage of life, from kindergarten through retirement.
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
  claim_title: Education industry transformation through AI
  claim_description: AI is transforming the education industry by enabling personalized,
    adaptive learning experiences for students and streamlining routine tasks for
    educators to focus more on student engagement.
  source_ids:
  - S1
  source_quote: AI is transforming how students learn through personalized, adaptive
    experiences, while also changing how educators teach by streamlining routine tasks
    and freeing them to focus more on student engagement.
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
  claim_title: Tens of thousands of annual order-related inquiries
  claim_description: Pearson's service team manages tens of thousands of order-related
    inquiries each year, with routine questions coming in quickly and involving multiple
    steps.
  source_ids:
  - S1
  source_quote: Each year, Pearson's service team manages tens of thousands of order-related
    inquiries.
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
  claim_title: Rapid growth through strategic acquisitions
  claim_description: Pearson's rapid growth through acquisitions like Credly, Mondly,
    and eDynamic Learning added multiple tools, platforms, and data sources across
    their portfolio.
  source_ids:
  - S1
  source_quote: The company's rapid growth through acquisitions like Credly, Mondly,
    and eDynamic Learning added even more tools, platforms, and data sources to the
    mix.
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
  context_type: products_services
  claim_title: Multi-brand learner journey across Pearson portfolio
  claim_description: A student might start with Pearson+, certify through Pearson
    VUE, and upskill later with Mondly, representing a lifelong learner relationship
    across multiple Pearson brands.
  source_ids:
  - S1
  source_quote: A student might start with Pearson+, certify through Pearson VUE,
    and upskill later with Mondly.
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
  context_type: functional
  claim_title: Customer service operations with seasonal demand spikes
  claim_description: Pearson's service model needed to accommodate seasonal spikes
    and growing learner demands, requiring scalable automation solutions.
  source_ids:
  - S1
  source_quote: Pearson's service model needed to accommodate seasonal spikes and
    growing learner demands.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10.0'
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
- id: CC-007
  context_type: temporal
  claim_title: 25-year partnership with Salesforce
  claim_description: Pearson has been working with Salesforce for 25 years and continues
    to see tremendous potential to grow the partnership.
  source_ids:
  - S1
  source_quote: We've been with Salesforce for 25 years and still see tremendous potential
    to grow our partnership
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
  claim_title: Becoming an Agentic Enterprise
  claim_description: Pearson is setting out to become an Agentic Enterprise, embedding
    AI agents into daily operations and empowering Agentforce to take on manual tasks.
  source_ids:
  - S1
  source_quote: as Pearson sets out to become an Agentic Enterprise, they're trusting
    Salesforce to help build a roadmap that embeds AI agents into daily operations
    and empowers Agentforce to take on manual tasks.
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
  context_type: organisational
  claim_title: Operations in 70 countries
  claim_description: Pearson provides digital coursework to grade schools, high schools
    and universities in 70 countries globally.
  source_ids:
  - S3
  source_quote: Pearson, a leader in the education space historically known for publishing
    textbooks, shifted its business to provide digital coursework to grade schools,
    high schools and universities in 70 countries.
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
  context_type: sectoral
  claim_title: COVID-19 pandemic accelerated online learning adoption
  claim_description: The COVID-19 pandemic forced the world to take distance learning
    seriously, with 80% of survey respondents believing the pandemic changed education
    forever.
  source_ids:
  - S3
  source_quote: According to a 2020 Pearson consumer survey conducted in seven countries,
    around 80% of respondents believe the pandemic has changed education forever.
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
  context_type: functional
  claim_title: Integrated sales, marketing, and service operations
  claim_description: Pearson uses Sales Cloud, Marketing Cloud, and Service Cloud
    to digitally connect and communicate with students and faculty from initial interest
    through post-enrollment support.
  source_ids:
  - S3
  source_quote: Pearson uses the full Salesforce Platform, including Sales Cloud,
    Marketing Cloud, and Service Cloud, to digitally connect and communicate with
    students and faculty from initial interest through post enrollment support.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '4.0'
  apqc_name: Deliver Products and Services
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
  context_type: products_services
  claim_title: Multiple learning platforms and programs
  claim_description: Pearson operates multiple learning platforms including UK Learns,
    Connections Academy (K-12 virtual schools), and Pearson Pathways (graduate-level
    business education).
  source_ids:
  - S3
  source_quote: This new program joins the already-active Connections Academy, Pearson's
    virtual learning schools for K-12 students. And in September, the company launched
    Pearson Pathways, a digital learning platform with coursework focusing on graduate-level
    business education
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
    total: 8
    verified: 6
    needs_review: 2
    rejected: 0
    by_attribution:
      direct: 5
      contributing: 3
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

# AI-Powered Customer Service and Learning Journey Personalization

## Executive Summary

Pearson Education: Agentforce handles 40% of routine customer inquiries.

## Key Findings

- **Agentforce handles 40% of routine customer inquiries** — verified (outcome)
  - Quote: "Agentforce handles an estimated 40% of routine customer inquiries, so the service team can prioritize complex learner needs."

- **Automated refund processing through integrated systems** — verified (method)
  - Quote: "After Agentforce confirms the purchase is eligible for a refund by cross-checking it with Pearson's knowledge base via Data 360, Agentforce initiates a refund in Oracle ERP and lets the customer know ..."

- **Semantic search improves knowledge base accuracy** — needs_review (method)
  - Quote: "With Data 360, Agentforce can perform semantic searches, which means it understands the intent behind a query rather than just matching exact keywords. This delivers more accurate answers without the ..."

- **Improved self-service resolution metrics** — verified (outcome)
  - Quote: "deployment of an integrated support community and interactive chat bots have enabled students to resolve questions and issues faster through self-service while improving key metrics like average handl..."

- **Seamless handoff with full context preservation** — needs_review (method)
  - Quote: "Agentforce seamlessly transfers them to a service rep with full context. Every interaction is saved into Data 360, giving Pearson a complete customer record so future conversations pick up right where..."

- **Sales development agent for lead qualification** — verified (adoption)
  - Quote: "They've launched a sales development agent to help prospect and qualify leads, with marketing agents next in line."

- **Unified customer journey visibility across divisions** — verified (method)
  - Quote: "This real-time visibility gives Pearson a full view of the customer journey — not just website clicks and email opens, but how they progress through programs, where they struggle, and what helps them ..."

- **Personalized marketing outreach throughout learner lifecycle** — verified (method)
  - Quote: "As learners progress through coursework, ace the test, and advance in their careers, Pearson keeps them inspired to grow through personalized outreach in Marketing Cloud."

## Sources

- **S1**: https://www.salesforce.com/customer-stories/pearson/?bc=OTH
- **S2**: https://nucleusresearch.com/research/single/salesforce-roi-case-study-pearson-education/
- **S3**: https://www.salesforce.com/blog/a-leader-in-online-learning-predicts-the-future-of-education/?bc=HL
