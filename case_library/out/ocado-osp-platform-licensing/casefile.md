---
case_id: ocado-osp-platform-licensing
organisation: Ocado
title: AI-Powered Grocery Fulfillment Platform Licensing
date_created: '2026-01-29'
date_updated: '2026-01-29'
sources:
- id: S1
  title: https://www.reuters.com/article/business/ocado-announces-first-international-cus...
  url: https://www.reuters.com/article/business/ocado-announces-first-international-customer-for-ocado-smart-platform-idUSFWN1J101V/
  raw_file: ''
  text_file: sources/text/S1.txt
  extraction_method: unknown
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S2
  title: https://kubernetes.io/case-studies/ocado/
  url: https://kubernetes.io/case-studies/ocado/
  raw_file: ''
  text_file: sources/text/S2.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S3
  title: https://cloud.google.com/customers/ocado
  url: https://cloud.google.com/customers/ocado
  raw_file: ''
  text_file: sources/text/S3.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S4
  title: https://www.ocadogroup.com/newsroom/stories/smart-scalable-seamless-online-groce...
  url: https://www.ocadogroup.com/newsroom/stories/smart-scalable-seamless-online-grocery-fulfilment-the-ocado-way
  raw_file: ''
  text_file: sources/text/S4.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
value_claims:
- id: VC-001
  claim_title: Deployment speed increased from over a month to under a week
  claim_description: Migration to Kubernetes reduced application deployment time from
    over a month to within a week, enabling faster feature delivery.
  source_ids:
  - S2
  source_quote: I've seen features go from development to production inside of a week
    now. In the old world, a new application deployment could easily take over a month.
  quote_location: Impact section
  ai_attribution: contextual
  attribution_evidence: Kubernetes is infrastructure orchestration, not AI. However,
    it enables the deployment of AI-powered Smart Platform services.
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
    value: 75-87.5
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
  claim_title: Deployment frequency increased from 2 to dozens per week
  claim_description: Kubernetes migration enabled deployment rate to increase from
    as few as 2 per week to dozens per week in warehouse operations.
  source_ids:
  - S2
  source_quote: the rate of deployments has gone from as few as two per week to dozens
    per week
  quote_location: Impact section
  ai_attribution: contextual
  attribution_evidence: Kubernetes enables deployment of AI-powered Smart Platform
    services managing warehouse operations.
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
    value: 10x+
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
- id: VC-003
  claim_title: Hardware resource utilization reduced by 15-25%
  claim_description: Kubernetes migration reduced hardware resource requirements by
    15-25% in test environments through better resource allocation.
  source_ids:
  - S2
  source_quote: I'd estimate that we use about 15-25% less hardware resources to host
    the same applications in Kubernetes in our test environments.
  quote_location: Impact section
  ai_attribution: contextual
  attribution_evidence: Kubernetes optimizes infrastructure for AI-powered Smart Platform
    applications.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
  - cost_reduction
  cognitive_depth: descriptive
  metric_raw:
    value: 15-25
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
  claim_title: Infrastructure consolidation from 10 clusters to 1
  claim_description: Migration to Kubernetes enabled consolidation from approximately
    10 fleet clusters to one Kubernetes cluster.
  source_ids:
  - S2
  source_quote: We have more confidence in the resource allocation/separation features
    of Kubernetes, so we have been able to migrate from around 10 fleet clusters to
    one Kubernetes cluster.
  quote_location: Impact section
  ai_attribution: contextual
  attribution_evidence: Kubernetes provides infrastructure for AI-powered Smart Platform
    operations.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
  - cost_reduction
  cognitive_depth: descriptive
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
- id: VC-005
  claim_title: 700 weekly active users self-serve data insights with Looker
  claim_description: Looker implementation enabled 700 weekly active users to generate
    their own insights through self-serve functionality.
  source_ids:
  - S3
  source_quote: 700 weekly active users generate their own insights with Looker's
    extensive self-serve functionality
  quote_location: Header section
  ai_attribution: contributing
  attribution_evidence: Looker's semantic layer uses ML for data modeling and enables
    AI-driven analytics capabilities.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - augmentation
  outcome:
  - velocity
  - experience
  cognitive_depth: diagnostic
  metric_raw:
    value: '700'
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
  claim_title: External reporting capability delivered in 3 months vs 1+ year
  claim_description: Looker's reusable metric definitions enabled OSP Insights external
    reporting to be built in 3 months instead of over a year.
  source_ids:
  - S3
  source_quote: Being able to reuse these definitions allowed Ocado Technology to
    deliver its OSP Insights capability in just three months, when it would have taken
    more than a year with the third-party BI tool
  quote_location: OSP Insights section
  ai_attribution: contributing
  attribution_evidence: Looker's semantic layer and analytics capabilities accelerated
    development of data products.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  - optimization
  outcome:
  - velocity
  - cost_reduction
  cognitive_depth: descriptive
  metric_raw:
    value: '75'
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
  claim_title: Near-real-time warehouse reporting delivered in days vs months
  claim_description: Looker enabled near-real-time delivery box availability reporting
    to be delivered in days instead of months, achieving highest site productivity.
  source_ids:
  - S3
  source_quote: Before Looker, near-real-time reporting wouldn't have been an option.
    We'd have had to deliver it through a software-development process, and it would
    have taken a couple of months to deliver, instead of the couple of days it took
    with Looker.
  quote_location: Warehouse operations section
  ai_attribution: contributing
  attribution_evidence: Looker's analytics platform enabled real-time data insights
    for warehouse optimization.
  verification_status: needs_review
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - automation
  - optimization
  outcome:
  - velocity
  - business_growth
  cognitive_depth: predictive
  metric_raw:
    value: 95-97
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
- id: VC-008
  claim_title: Coles achieved double the perfect order rate with automated CFCs
  claim_description: Coles reported perfect order rates continuing to track at more
    than double the national home delivery rate after transitioning to OSP-powered
    automated fulfillment.
  source_ids:
  - S4
  source_quote: Perfect order rates continuing to track at more than double the national
    home delivery rate.
  quote_location: Coles case study section
  ai_attribution: direct
  attribution_evidence: OSP's AI-powered automated fulfillment centers directly drive
    perfect order rate improvements.
  verification_status: needs_review
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
  - optimization
  outcome:
  - experience
  - cost_reduction
  cognitive_depth: autonomous
  metric_raw:
    value: '100'
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
- id: VC-009
  claim_title: Ocado Retail achieved 3.3% EBITDA with automated fulfillment network
  claim_description: Ocado Retail achieved 3.3% EBITDA at HY25 using network of automated
    CFCs powered by end-to-end integrated AI software solutions.
  source_ids:
  - S4
  source_quote: At HY25 Ocado Retail achieved a 3.3% EBITDA with a medium term high-mid
    single digit EBITDA trajectory.
  quote_location: Ocado Retail case study section
  ai_attribution: direct
  attribution_evidence: AI-powered robotics, automation, and fulfillment software
    directly enable operational efficiency and profitability.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  - optimization
  outcome:
  - business_growth
  - cost_reduction
  cognitive_depth: autonomous
  metric_raw:
    value: '3.3'
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
- id: VC-010
  claim_title: Ocado manages 200,000+ orders per week at largest facility
  claim_description: Ocado's Erith warehouse delivers more than 200,000 orders per
    week at full capacity, making it the world's largest online grocery facility.
  source_ids:
  - S2
  source_quote: At full capacity, Ocado's latest warehouse in Erith, southeast London,
    will deliver more than 200,000 orders a week, making it the world's largest facility
    for online grocery.
  quote_location: Migration impact section
  ai_attribution: direct
  attribution_evidence: AI-powered Smart Platform with robotics and automation directly
    enables this order volume capacity.
  verification_status: needs_review
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - automation
  - optimization
  outcome:
  - business_growth
  cognitive_depth: autonomous
  metric_raw:
    value: '200000'
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
- id: VC-011
  claim_title: 150 microservices deployed across multiple warehouses
  claim_description: About 150 microservices running on Kubernetes with multiple instances
    deployed across each warehouse facility.
  source_ids:
  - S2
  source_quote: There are about 150 microservices now running on Kubernetes, with
    multiple instances of many of them. We're not just deploying all these microservices
    at once. We're deploying them all for one warehouse, and then they're all being
    deployed again for the next warehouse
  quote_location: Migration details section
  ai_attribution: direct
  attribution_evidence: These microservices comprise the AI-powered Smart Platform
    managing warehouse operations.
  verification_status: needs_review
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - velocity
  cognitive_depth: autonomous
  metric_raw:
    value: '150'
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
- id: VC-012
  claim_title: Bon Preu became highest-rated online grocery service in Spain
  claim_description: Bon Preu was recognized by OCU in 2024 as the highest-rated online
    grocery service in Spain using Ocado's ISF and planned CFC technology.
  source_ids:
  - S4
  source_quote: The business has since grown well ahead of the wider online channel
    in Spain and has become the leading online grocery proposition in Catalonia, recognised
    by the OCU in 2024 as the highest-rated online grocery service in Spain.
  quote_location: Bon Preu case study section
  ai_attribution: direct
  attribution_evidence: Ocado's AI-powered In-Store Fulfilment technology and planned
    automated CFC directly enable service quality.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_creation
  mechanism:
  - automation
  - optimization
  outcome:
  - experience
  - business_growth
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
- id: VC-013
  claim_title: Coles achieved significant NPS uplift with CFC fulfillment
  claim_description: Coles reported a significant uplift in customer Net Promoter
    Scores, particularly for orders fulfilled via AI-powered automated CFCs.
  source_ids:
  - S4
  source_quote: A significant uplift in customer Net Promoter Scores (NPS), particularly
    for those orders fulfilled via CFCs
  quote_location: Coles case study section
  ai_attribution: direct
  attribution_evidence: OSP's AI-powered automated fulfillment centers directly improve
    customer experience and satisfaction.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
  - optimization
  outcome:
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
- id: VC-014
  claim_title: Ocado Retail fastest growing UK grocer with 1M+ active customers
  claim_description: Ocado.com continues to be the fastest growing grocer in UK market
    with more than 1 million active customers using AI-powered platform.
  source_ids:
  - S4
  source_quote: As a result, ocado.com continues to be the fastest growing grocer
    in the UK grocery market, now with more than 1m active customers nationwide.
  quote_location: Ocado Retail case study section
  ai_attribution: direct
  attribution_evidence: AI-powered automated CFCs, robotics, and end-to-end software
    platform directly enable growth and scale.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - automation
  - optimization
  outcome:
  - business_growth
  - revenue_lift
  cognitive_depth: autonomous
  metric_raw:
    value: '1000000'
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
- id: VC-015
  claim_title: 2000+ employees regularly access Looker for data insights
  claim_description: Over 2,000 Ocado Technology employees regularly access Looker,
    with nine analyst teams using it for consistent data insights.
  source_ids:
  - S3
  source_quote: Ocado Technology now has over 2,000 employees regularly accessing
    Looker, with nine analyst teams and 700 active weekly users taking advantage of
    its self-serve functionality
  quote_location: Implementation section
  ai_attribution: contributing
  attribution_evidence: Looker's analytics platform enables widespread data-driven
    decision making across the organization.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - augmentation
  outcome:
  - velocity
  - experience
  cognitive_depth: diagnostic
  metric_raw:
    value: '2000'
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
  claim_title: Ocado Technology has 2,700 technologists developing AI and robotics
  claim_description: Ocado Technology's R&D arm employs 2,700-strong team of technologists
    developing artificial intelligence, robotics, and automation technology.
  source_ids:
  - S3
  source_quote: Today, the company's R&D arm, Ocado Technology, has a 2,700-strong
    team of technologists developing artificial intelligence, robotics, and automation
    technology.
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
  claim_title: Ocado operates in online grocery retail and technology sectors
  claim_description: Ocado is the world's largest online-only grocery retailer and
    also licenses its Smart Platform technology to other retailers globally.
  source_ids:
  - S2
  - S3
  source_quote: The world's largest online-only grocery retailer, Ocado developed
    the Ocado Smart Platform to manage its own operations, from websites to warehouses,
    and is now licensing the technology to other retailers
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
  context_type: products_services
  claim_title: Ocado Smart Platform is end-to-end grocery technology platform
  claim_description: OSP is an end-to-end platform enabling everything from ecommerce
    to fulfillment, logistics, supply chains, and incorporating robotic automation.
  source_ids:
  - S4
  source_quote: At the heart of its offering is the Ocado Smart Platform (OSP), an
    end-to-end platform that enables everything from ecommerce to fulfillment, logistics
    to supply chains, as well as incorporating futuristic fleets of robots
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
  claim_title: Ocado began licensing technology internationally in 2017
  claim_description: Ocado started licensing its Smart Platform technology to international
    retailers in 2017, with Bon Preu as first partner.
  source_ids:
  - S4
  source_quote: Ocado's products have developed significantly since we first started
    licensing our technology internationally in 2017.
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
  claim_title: Ocado has 13 retail partners globally with 1,200+ patents
  claim_description: Ocado Smart Platform is used by 13 retailers worldwide including
    Kroger, AEON, Coles, and Bon Preu, with over 1,200 granted patents.
  source_ids:
  - S3
  source_quote: Used by 13 retailers around the world, from Kroger in the USA to AEON
    in Japan, and with more than 1,200 granted patents, Ocado has become a global
    tech powerhouse.
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
  claim_title: Ocado warehouse generates 75TB of data per day
  claim_description: A single Ocado Technology warehouse generates 75 terabytes of
    semi-structured data per day, stored in Google Cloud BigQuery.
  source_ids:
  - S3
  source_quote: OSP generates vast amounts of data — just one of Ocado Technology's
    warehouses generates 75 TB of semi-structured data per day — which is all stored
    in Google Cloud's enterprise data warehouse, BigQuery.
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
  claim_title: Kubernetes migration began summer 2016, production in 2017
  claim_description: Ocado began migrating from fleet to Kubernetes in summer 2016,
    with first production app deployed summer 2017.
  source_ids:
  - S2
  source_quote: In the summer of 2016, the team began migrating from fleet to Kubernetes
    on Ocado's private cloud. The first app on Kubernetes, a business-critical service
    in the warehouses, went into production a year later.
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
  context_type: temporal
  claim_title: Looker implemented in 2023 for enterprise BI
  claim_description: Ocado Technology implemented Looker in 2023 to provide enterprise-grade
    business intelligence with robust semantic layer.
  source_ids:
  - S3
  source_quote: Impressed with how comprehensive and powerful Looker's semantic layer
    was, it implemented Looker in 2023 and set about migrating its reports to the
    platform.
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
  claim_title: OSP manages warehouse fulfillment operations
  claim_description: Ocado Smart Platform manages warehouse operations including robotic
    picking, packing, and order fulfillment with automated systems.
  source_ids:
  - S2
  - S4
  source_quote: The world's largest online-only grocery retailer, Ocado developed
    the Ocado Smart Platform to manage its own operations, from websites to warehouses
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '4.2'
  apqc_name: Procure Materials and Services
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
  claim_title: OSP manages supply chain and logistics operations
  claim_description: Ocado Smart Platform provides end-to-end supply chain management,
    logistics planning, and last-mile delivery optimization.
  source_ids:
  - S4
  source_quote: an end-to-end platform that enables everything from ecommerce to fulfillment,
    logistics to supply chains
  verification_status: unverified
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
- id: CC-011
  context_type: functional
  claim_title: OSP powers ecommerce webshop and customer experience
  claim_description: Ocado Smart Platform includes customer-facing webshop with search
    functionality and online ordering capabilities.
  source_ids:
  - S3
  - S4
  source_quote: one element of OSP is the customer-facing webshop that shoppers use
    to place their orders. This includes a search functionality to help users find
    goods to fill their baskets.
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
- id: CC-012
  context_type: strategic_intent
  claim_title: Ocado provides flexible fulfillment toolkit for partners
  claim_description: Ocado offers partners flexible fulfillment solutions from in-store
    picking to fully automated CFCs, tailored to local market conditions and growth
    stages.
  source_ids:
  - S4
  source_quote: Our partners can deploy fulfilment networks ranging from AI-powered
    fulfilment software in stores and dark stores, to store automation or a range
    of fully automated CFCs ranging from the micro, to the very large
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
  context_type: temporal
  claim_title: Ocado founded in 2000 as online grocery pioneer
  claim_description: Ocado launched in 2000 with vision to revolutionize online grocery,
    creating proprietary technology to manage perishable item fulfillment.
  source_ids:
  - S3
  source_quote: When Ocado launched in 2000 with a vision to revolutionize the online
    grocery space, people said it couldn't be done.
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
- id: CC-014
  context_type: organisational
  claim_title: Hundreds of engineers deploy on Kubernetes platform
  claim_description: Hundreds of Ocado engineers working on Smart Platform are now
    deploying applications and services on Kubernetes infrastructure.
  source_ids:
  - S2
  source_quote: Hundreds of Ocado engineers working on the Smart Platform are now
    deploying on Kubernetes
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
  context_type: scale
  claim_title: Ocado platform manages tens of thousands of orders weekly
  claim_description: Ocado Smart Platform is live in warehouses managing tens of thousands
    of orders per week across multiple facilities.
  source_ids:
  - S2
  source_quote: the platform is live in Ocado's warehouses, managing tens of thousands
    of orders a week
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
    total: 15
    verified: 11
    needs_review: 4
    rejected: 0
    by_attribution:
      contextual: 4
      contributing: 4
      direct: 7
  context_claims:
    total: 15
    verified: 12
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

# AI-Powered Grocery Fulfillment Platform Licensing

## Executive Summary

Ocado: Deployment speed increased from over a month to under a week.

## Key Findings

- **Deployment speed increased from over a month to under a week** — verified (outcome)
  - Quote: "I've seen features go from development to production inside of a week now. In the old world, a new application deployment could easily take over a month."

- **Deployment frequency increased from 2 to dozens per week** — verified (outcome)
  - Quote: "the rate of deployments has gone from as few as two per week to dozens per week"

- **Hardware resource utilization reduced by 15-25%** — verified (outcome)
  - Quote: "I'd estimate that we use about 15-25% less hardware resources to host the same applications in Kubernetes in our test environments."

- **Infrastructure consolidation from 10 clusters to 1** — verified (outcome)
  - Quote: "We have more confidence in the resource allocation/separation features of Kubernetes, so we have been able to migrate from around 10 fleet clusters to one Kubernetes cluster."

- **700 weekly active users self-serve data insights with Looker** — verified (adoption)
  - Quote: "700 weekly active users generate their own insights with Looker's extensive self-serve functionality"

- **External reporting capability delivered in 3 months vs 1+ year** — verified (outcome)
  - Quote: "Being able to reuse these definitions allowed Ocado Technology to deliver its OSP Insights capability in just three months, when it would have taken more than a year with the third-party BI tool"

- **Near-real-time warehouse reporting delivered in days vs months** — needs_review (outcome)
  - Quote: "Before Looker, near-real-time reporting wouldn't have been an option. We'd have had to deliver it through a software-development process, and it would have taken a couple of months to deliver, instead..."

- **Coles achieved double the perfect order rate with automated CFCs** — needs_review (outcome)
  - Quote: "Perfect order rates continuing to track at more than double the national home delivery rate."

- **Ocado Retail achieved 3.3% EBITDA with automated fulfillment network** — verified (outcome)
  - Quote: "At HY25 Ocado Retail achieved a 3.3% EBITDA with a medium term high-mid single digit EBITDA trajectory."

- **Ocado manages 200,000+ orders per week at largest facility** — needs_review (outcome)
  - Quote: "At full capacity, Ocado's latest warehouse in Erith, southeast London, will deliver more than 200,000 orders a week, making it the world's largest facility for online grocery."

- **150 microservices deployed across multiple warehouses** — needs_review (adoption)
  - Quote: "There are about 150 microservices now running on Kubernetes, with multiple instances of many of them. We're not just deploying all these microservices at once. We're deploying them all for one warehou..."

- **Bon Preu became highest-rated online grocery service in Spain** — verified (method)
  - Quote: "The business has since grown well ahead of the wider online channel in Spain and has become the leading online grocery proposition in Catalonia, recognised by the OCU in 2024 as the highest-rated onli..."

- **Coles achieved significant NPS uplift with CFC fulfillment** — verified (method)
  - Quote: "A significant uplift in customer Net Promoter Scores (NPS), particularly for those orders fulfilled via CFCs"

- **Ocado Retail fastest growing UK grocer with 1M+ active customers** — verified (outcome)
  - Quote: "As a result, ocado.com continues to be the fastest growing grocer in the UK grocery market, now with more than 1m active customers nationwide."

- **2000+ employees regularly access Looker for data insights** — verified (adoption)
  - Quote: "Ocado Technology now has over 2,000 employees regularly accessing Looker, with nine analyst teams and 700 active weekly users taking advantage of its self-serve functionality"

## Sources

- **S1**: https://www.reuters.com/article/business/ocado-announces-first-international-customer-for-ocado-smart-platform-idUSFWN1J101V/
- **S2**: https://kubernetes.io/case-studies/ocado/
- **S3**: https://cloud.google.com/customers/ocado
- **S4**: https://www.ocadogroup.com/newsroom/stories/smart-scalable-seamless-online-grocery-fulfilment-the-ocado-way
