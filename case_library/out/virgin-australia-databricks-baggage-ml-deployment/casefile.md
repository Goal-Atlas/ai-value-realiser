---
case_id: virgin-australia-databricks-baggage-ml-deployment
organisation: Virgin Australia Airlines
title: Data Platform Migration and ML Model Deployment
date_created: '2026-01-29'
date_updated: '2026-01-29'
sources:
- id: S1
  title: https://www.databricks.com/blog/pushing-boundaries-innovation-data-and-ai-announ...
  url: https://www.databricks.com/blog/pushing-boundaries-innovation-data-and-ai-announcing-2024-finalists-databricks-data-team
  raw_file: ''
  text_file: sources/text/S1.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S2
  title: https://www.databricks.com/blog/announcing-winners-2024-databricks-data-team-awa...
  url: https://www.databricks.com/blog/announcing-winners-2024-databricks-data-team-awards
  raw_file: ''
  text_file: sources/text/S2.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S3
  title: https://aws.amazon.com/solutions/case-studies/virgin-australia-case-study/
  url: https://aws.amazon.com/solutions/case-studies/virgin-australia-case-study/
  raw_file: ''
  text_file: sources/text/S3.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
value_claims:
- id: VC-001
  claim_title: 75% increase in real-time data availability
  claim_description: Virgin Australia achieved a 75% increase in real-time data availability
    after transitioning to Databricks Data Intelligence Platform from on-premises
    data warehouse.
  source_ids:
  - S1
  - S2
  source_quote: Databricks adoption facilitated a 75% increase in real-time data availability
  quote_location: Virgin Australia Airlines section
  ai_attribution: direct
  attribution_evidence: The increase in real-time data availability is directly attributed
    to Databricks adoption, which integrated data ingestion, analytics, and data science
    into one cohesive platform.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
  - velocity
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
- id: VC-002
  claim_title: 44% decrease in mishandled baggage
  claim_description: Virgin Australia reduced mishandled baggage by 44% through implementation
    of near-real-time Baggage Reconciliation System on Databricks platform.
  source_ids:
  - S1
  - S2
  source_quote: a 44% decrease in mishandled baggage
  quote_location: Virgin Australia Airlines section
  ai_attribution: direct
  attribution_evidence: The baggage mishandling reduction is directly linked to the
    near-real-time Baggage Reconciliation System implemented using Databricks, enhancing
    operational efficiencies.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_creation
  mechanism:
  - optimization
  - automation
  outcome:
  - experience
  - cost_reduction
  cognitive_depth: predictive
  metric_raw:
    value: '44'
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
  claim_title: 25% revenue boost from analytics insights
  claim_description: Virgin Australia achieved a 25% revenue boost attributed to insights
    drawn from analytics enabled by the Databricks platform.
  source_ids:
  - S1
  - S2
  source_quote: a 25% revenue boost attributed to insights drawn from analytics
  quote_location: Virgin Australia Airlines section
  ai_attribution: contributing
  attribution_evidence: Revenue boost is attributed to insights from analytics, where
    AI/ML and data platform capabilities contributed to better decision-making but
    other business factors may also play a role.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - augmentation
  - optimization
  outcome:
  - revenue_lift
  - business_growth
  cognitive_depth: diagnostic
  metric_raw:
    value: '25'
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
  claim_title: 90% faster deployment of machine learning models
  claim_description: Virgin Australia achieved 90% faster deployment of machine learning
    models after migrating to Databricks Data Intelligence Platform.
  source_ids:
  - S1
  - S2
  source_quote: a 90% faster deployment of machine learning models
  quote_location: Virgin Australia Airlines section
  ai_attribution: direct
  attribution_evidence: The acceleration in ML model deployment is directly attributed
    to Databricks platform capabilities that streamlined data science workflows into
    one cohesive platform.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - optimization
  - automation
  outcome:
  - velocity
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
- id: VC-005
  claim_title: Significant improvements in analytical speed-to-insight
  claim_description: Virgin Australia achieved significant improvements in analytical
    speed-to-insight through optimized data querying and analytics practices on Databricks.
  source_ids:
  - S1
  - S2
  source_quote: significant improvements in analytical speed-to-insight
  quote_location: Virgin Australia Airlines section
  ai_attribution: direct
  attribution_evidence: Speed-to-insight improvements are directly attributed to Databricks
    optimizing data querying and analytics practices, streamlining the entire analytics
    workflow.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_low
  application_type: capability_enhancement
  mechanism:
  - optimization
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
- id: VC-006
  claim_title: Zero security incidents post-AWS EKS migration
  claim_description: Virgin Australia experienced zero security incidents since migrating
    to Amazon EKS Auto Mode, with automatic security patching and updates.
  source_ids:
  - S3
  source_quote: zero security incidents since the migration
  quote_location: Outcome section
  ai_attribution: contributing
  attribution_evidence: While Amazon EKS Auto Mode automates security patching and
    updates, the zero incidents outcome also depends on broader security practices
    and organizational processes.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - risk_avoidance
  cognitive_depth: autonomous
  metric_raw:
    value: '0'
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
  claim_title: 50% reduction in cluster upgrade effort
  claim_description: Virgin Australia reduced cluster upgrade effort from 1 month
    to 2 weeks per team member through Amazon EKS Auto Mode in-place upgrades.
  source_ids:
  - S3
  source_quote: Each cluster upgrade requires approximately 2 weeks of effort per
    team member, compared to at least 1 month per cluster that blue/green migrations
    would have required.
  quote_location: Outcome section
  ai_attribution: direct
  attribution_evidence: The reduction in upgrade effort is directly attributed to
    Amazon EKS Auto Mode's automated upgrade capabilities, replacing manual blue/green
    migration processes.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - velocity
  - cost_reduction
  cognitive_depth: autonomous
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
- id: VC-008
  claim_title: Zero unplanned downtime post-AWS EKS migration
  claim_description: Virgin Australia achieved zero unplanned downtime since migrating
    to Amazon EKS Auto Mode, improving operational reliability.
  source_ids:
  - S3
  source_quote: Virgin Australia has also stated that its operations have run smoothly,
    with no unplanned downtime
  quote_location: Outcome section
  ai_attribution: contributing
  attribution_evidence: While Amazon EKS Auto Mode provides automated management and
    reliability features, zero downtime also depends on application architecture and
    operational practices.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
  - optimization
  outcome:
  - risk_avoidance
  - experience
  cognitive_depth: autonomous
  metric_raw:
    value: '0'
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
  claim_title: Virgin Australia is a major Australian airline
  claim_description: Virgin Australia is one of the largest Australian airlines, operating
    a fleet of more than 90 aircraft serving over 40 domestic and international destinations
    on over 80 routes.
  source_ids:
  - S3
  source_quote: Virgin Australia is one of the largest Australian airlines. It operates
    an extensive domestic network as well as short-haul international services, charter
    and cargo operations
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
  claim_title: Aviation industry
  claim_description: Virgin Australia operates in the aviation/airline industry, providing
    passenger air transport services.
  source_ids:
  - S1
  - S2
  - S3
  source_quote: Virgin Australia Airlines
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
  context_type: temporal
  claim_title: Migration to Databricks completed by 2024
  claim_description: Virgin Australia's transition from on-premises data warehouse
    to Databricks Data Intelligence Platform was completed and recognized as a finalist/winner
    in 2024 Data Team Awards.
  source_ids:
  - S1
  - S2
  source_quote: Below are the finalists for 2024's Data Team Transformation Award
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
  claim_title: AWS EKS migration initiated in early 2024
  claim_description: Virgin Australia began modernizing its container infrastructure
    with Amazon EKS Auto Mode in early 2024 through a 6-month blue/green migration.
  source_ids:
  - S3
  source_quote: In early 2024, Virgin Australia sought to modernize its container
    infrastructure
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
  context_type: strategic_intent
  claim_title: Build trusted, governed central data repository
  claim_description: Virgin Australia's goal was to build a trusted, governed central
    data repository for organizational data, enabling improved collaboration, real-time
    reporting, and data-driven decision-making.
  source_ids:
  - S1
  - S2
  source_quote: The goal was to build a trusted, governed central data repository
    for organizational data, and enable improved collaboration, real-time reporting,
    data-driven decision-making
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
  claim_title: Reduce operational overhead and enable innovation
  claim_description: Virgin Australia aimed to streamline cluster upgrades and maintenance,
    reducing operational overhead so engineering teams could focus on innovation and
    enhanced customer experiences.
  source_ids:
  - S3
  source_quote: With reduced operational overhead, engineering teams can focus on
    innovation, strengthen security, and deliver enhanced customer experiences and
    business outcomes.
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
  claim_title: Baggage handling operations
  claim_description: Virgin Australia implemented a near-real-time Baggage Reconciliation
    System to enhance operational efficiencies in baggage handling.
  source_ids:
  - S1
  - S2
  source_quote: Virgin Australia Airlines implemented new features, like the near-real-time
    Baggage Reconciliation System, enhancing operational efficiencies
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10.0'
  apqc_name: Deliver Physical Product
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
  context_type: functional
  claim_title: Data governance and analytics
  claim_description: Virgin Australia integrated Databricks Unity Catalog for seamless
    data governance, optimizing data querying and analytics practices across the organization.
  source_ids:
  - S1
  - S2
  source_quote: By integrating Databricks' Unity Catalog for seamless data governance,
    Virgin Australia Airlines optimized its data querying and analytics practices
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '11.0'
  apqc_name: Manage Information Technology
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
  claim_title: Over 200 APIs migrated to Amazon EKS
  claim_description: Virgin Australia successfully migrated more than 200 APIs onto
    Amazon EKS Auto Mode, demonstrating enterprise-scale deployment.
  source_ids:
  - S3
  source_quote: More than 200 APIs were successfully migrated onto Amazon EKS Auto
    Mode
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
  context_type: products_services
  claim_title: Velocity Frequent Flyer loyalty program
  claim_description: Virgin Australia operates the Velocity Frequent Flyer loyalty
    program as part of its service offerings.
  source_ids:
  - S3
  source_quote: its loyalty program, Velocity Frequent Flyer
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
  claim_title: Critical digital systems for flight operations
  claim_description: Virgin Australia relies on digital systems for booking, ticketing,
    flight operations, reservations, flight searching, and partner functions - all
    mission-critical infrastructure.
  source_ids:
  - S3
  source_quote: These systems are running critical services that affect airline operations,
    on-time performance, and our ability to service customers through our website,
    retail, ticketing, reservations
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10.0'
  apqc_name: Deliver Physical Product
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
  claim_title: Virgin Australia founded in 2000
  claim_description: Virgin Australia was founded in 2000 and has grown to operate
    a fleet of more than 90 aircraft.
  source_ids:
  - S3
  source_quote: Founded in 2000, Virgin Australia operates a fleet of more than 90
    aircraft
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
    verified: 8
    needs_review: 0
    rejected: 0
    by_attribution:
      direct: 5
      contributing: 3
  context_claims:
    total: 12
    verified: 12
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

# Data Platform Migration and ML Model Deployment

## Executive Summary

Virgin Australia Airlines: 75% increase in real-time data availability.

## Key Findings

- **75% increase in real-time data availability** — verified (outcome)
  - Quote: "Databricks adoption facilitated a 75% increase in real-time data availability"

- **44% decrease in mishandled baggage** — verified (outcome)
  - Quote: "a 44% decrease in mishandled baggage"

- **25% revenue boost from analytics insights** — verified (outcome)
  - Quote: "a 25% revenue boost attributed to insights drawn from analytics"

- **90% faster deployment of machine learning models** — verified (outcome)
  - Quote: "a 90% faster deployment of machine learning models"

- **Significant improvements in analytical speed-to-insight** — verified (method)
  - Quote: "significant improvements in analytical speed-to-insight"

- **Zero security incidents post-AWS EKS migration** — verified (outcome)
  - Quote: "zero security incidents since the migration"

- **50% reduction in cluster upgrade effort** — verified (outcome)
  - Quote: "Each cluster upgrade requires approximately 2 weeks of effort per team member, compared to at least 1 month per cluster that blue/green migrations would have required."

- **Zero unplanned downtime post-AWS EKS migration** — verified (outcome)
  - Quote: "Virgin Australia has also stated that its operations have run smoothly, with no unplanned downtime"

## Sources

- **S1**: https://www.databricks.com/blog/pushing-boundaries-innovation-data-and-ai-announcing-2024-finalists-databricks-data-team
- **S2**: https://www.databricks.com/blog/announcing-winners-2024-databricks-data-team-awards
- **S3**: https://aws.amazon.com/solutions/case-studies/virgin-australia-case-study/
