---
case_id: airbus-skywise-platform
organisation: Airbus
title: Aviation Data Platform and Predictive Analytics
date_created: '2026-01-29'
date_updated: '2026-01-29'
sources:
- id: S1
  title: https://www.airbus.com/en/newsroom/press-releases/2019-06-airbus-opens-skywise-t...
  url: https://www.airbus.com/en/newsroom/press-releases/2019-06-airbus-opens-skywise-to-global-it-services-leaders
  raw_file: ''
  text_file: sources/text/S1.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S2
  title: https://www.airbus.com/en/newsroom/news/2018-03-airbus-skywise-data-platform-gai...
  url: https://www.airbus.com/en/newsroom/news/2018-03-airbus-skywise-data-platform-gains-momentum
  raw_file: ''
  text_file: sources/text/S2.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S3
  title: https://theaircurrent.com/aviation-safety/skywise-big-data-airbus-catastrophic-a...
  url: https://theaircurrent.com/aviation-safety/skywise-big-data-airbus-catastrophic-accident-a330neo/
  raw_file: ''
  text_file: sources/text/S3.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S4
  title: https://www.mulesoft.com/case-studies/api/integration-airbus
  url: https://www.mulesoft.com/case-studies/api/integration-airbus
  raw_file: ''
  text_file: sources/text/S4.txt
  extraction_method: unknown
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S5
  title: https://runwaygirlnetwork.com/2018/02/press-release-airbus-open-aviation-data-pl...
  url: https://runwaygirlnetwork.com/2018/02/press-release-airbus-open-aviation-data-platform-skywise-continues-to-gain-market-traction/
  raw_file: ''
  text_file: sources/text/S5.txt
  extraction_method: unknown
  extraction_quality: high
  is_multi_page: false
  related_urls: []
value_claims:
- id: VC-001
  claim_title: Over 80 airlines connected to Skywise platform by 2019
  claim_description: By 2019, over 80 airlines globally had connected their Airbus
    and non-Airbus fleets to the Skywise platform, demonstrating significant market
    adoption of the data analytics platform.
  source_ids:
  - S1
  source_quote: Today over 80 airlines around the world have connected their Airbus
    and non-Airbus fleet to Skywise.
  quote_location: Body paragraph 3
  ai_attribution: direct
  attribution_evidence: The claim directly relates to adoption of the AI-powered Skywise
    platform which uses Palantir's Foundry technology for data analytics.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - optimization
  outcome:
  - business_growth
  cognitive_depth: predictive
  metric_raw:
    value: '80'
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
- id: VC-002
  claim_title: 60x increase in data collection with FOMAX system
  claim_description: Airbus' FOMAX (flight operations and maintenance exchanger) collects
    60 times more data than existing systems, enabling enhanced predictive maintenance
    capabilities through Skywise.
  source_ids:
  - S2
  source_quote: Skywise is able to analyse data from other components on easyJet's
    aircraft thanks to the installation of Airbus' new flight operations and maintenance
    exchanger, called FOMAX – which collects 60-times more data than existing systems.
  quote_location: easyJet section, paragraph 2
  ai_attribution: direct
  attribution_evidence: The increased data collection directly enables AI-powered
    predictive analytics through the Skywise platform.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
  - velocity
  cognitive_depth: predictive
  metric_raw:
    value: '60'
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
  claim_title: easyJet engineers removed components before faults occurred
  claim_description: Using Skywise predictive maintenance technology, easyJet engineers
    were able to proactively remove aircraft components before faults occurred, limiting
    delays and cancellations.
  source_ids:
  - S2
  source_quote: This activity builds on extensive trials with the platform that allowed
    easyJet engineers to remove components before faults occurred, limiting delays
    and cancellations as a result.
  quote_location: easyJet section, paragraph 1
  ai_attribution: direct
  attribution_evidence: The predictive capability is directly enabled by Skywise's
    AI-powered data analytics, allowing proactive maintenance decisions.
  verification_status: verified
  evidence_level: method
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - optimization
  - augmentation
  outcome:
  - risk_avoidance
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
  claim_title: Skywise prevented catastrophic A330neo accident
  claim_description: Airbus engineers used Skywise to analyze operational and sensor
    data, discovering a hidden flaw in the A330neo pneumatic system before it resulted
    in a catastrophic accident.
  source_ids:
  - S3
  source_quote: Seeking an explanation for the leaking valves, Airbus engineers turned
    to the company's big data platform, Skywise, in search of clues. By comparing
    operational and sensor data, they were ultimately able to determine that in certain
    take-off configurations, the software in the bleed monitoring computer did not
    correctly control the high-pressure valve.
  quote_location: Main investigation section
  ai_attribution: direct
  attribution_evidence: Skywise's big data analytics directly enabled the discovery
    of the hidden failure mode through pattern analysis across operational data.
  verification_status: needs_review
  evidence_level: method
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - innovation
  outcome:
  - risk_avoidance
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
- id: VC-005
  claim_title: 11,900 aircraft connected to Skywise platform
  claim_description: Airbus reports that more than 11,900 aircraft are connected to
    the Skywise platform, representing significant scale and adoption across the aviation
    industry.
  source_ids:
  - S3
  source_quote: Today, Airbus reports that more than 11,900 aircraft are connected
    to the platform (some users analyze data from other manufacturers' aircraft with
    the help of Skywise as well).
  quote_location: Seeing the big picture section
  ai_attribution: direct
  attribution_evidence: The adoption metric directly reflects usage of the AI-powered
    Skywise analytics platform.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - optimization
  outcome:
  - business_growth
  cognitive_depth: predictive
  metric_raw:
    value: '11900'
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
  claim_title: 500GB to 1TB daily data collection per aircraft
  claim_description: Modern Airbus aircraft generate 500 gigabytes per day for A330neo
    and up to 1 terabyte per day for latest generation aircraft like A350, enabling
    comprehensive predictive analytics.
  source_ids:
  - S3
  source_quote: Skywise integrates data from many different sources, including the
    wealth of flight and health-and-usage data that is collected onboard modern aircraft,
    which is around 500 gigabytes per day for the A330neo and up to 1 terabyte per
    day for latest generation aircraft like the A350.
  quote_location: Seeing the big picture section
  ai_attribution: contributing
  attribution_evidence: The data volume enables AI analytics but represents the input
    rather than the AI capability itself.
  verification_status: verified
  evidence_level: method
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
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
- id: VC-007
  claim_title: Skywise enables prioritization of safety risks
  claim_description: With aggregated data from multiple aircraft, Skywise enables
    Airbus to identify, assess exposure, and prioritize safety risks across operations,
    focusing on critical issues like loss of control and runway excursions.
  source_ids:
  - S3
  source_quote: With more data, we can have a look at a bigger picture. We can prioritize,
    and prioritization in operations and safety is very important. So if we get an
    issue that's identified, we can identify what the safety risk is, we can identify
    what the exposure is, then we can prioritize on the key issues.
  quote_location: Seeing the big picture section, Goodwin quote
  ai_attribution: direct
  attribution_evidence: The prioritization capability is enabled by AI-powered analytics
    that process large-scale data to identify patterns and assess risk levels.
  verification_status: needs_review
  evidence_level: method
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - augmentation
  - optimization
  outcome:
  - risk_avoidance
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
  claim_title: Skywise supports formal safety investigations
  claim_description: Skywise has been used to support formal investigations into serious
    incidents, such as the TAP Air Portugal A320 thrust reverser incident, enabling
    root cause analysis through data analytics.
  source_ids:
  - S3
  source_quote: But Skywise has also been used in support of formal investigations
    into serious incidents. One of these incidents took place in April 2022, when
    a TAP Air Portugal A320 equipped with two CFM56 engines was attempting to land
    with a gusty crosswind at Copenhagen Airport in Denmark.
  quote_location: When one out of a million happens section
  ai_attribution: direct
  attribution_evidence: Skywise's data analytics capabilities directly supported the
    investigation by enabling analysis of operational data to determine root causes.
  verification_status: verified
  evidence_level: method
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - augmentation
  outcome:
  - risk_avoidance
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
context_claims:
- id: CC-001
  context_type: temporal
  claim_title: Skywise launched in 2017
  claim_description: The Skywise platform was launched at the 2017 Paris Air Show
    in collaboration with Palantir Technologies.
  source_ids:
  - S1
  - S3
  source_quote: Launched in 2017, Skywise is fast becoming the open platform of reference
    used by major aviation players to improve operational performance
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
  context_type: organisational
  claim_title: Partnership with Palantir Technologies
  claim_description: Skywise is powered by Palantir's Foundry technology, representing
    a strategic technology partnership for big data analytics capabilities.
  source_ids:
  - S1
  - S3
  source_quote: Skywise is powered by Palantir's Foundry technology.
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
  claim_title: Aviation and aerospace industry focus
  claim_description: Skywise operates within the aviation and aerospace sector, serving
    airlines, aircraft manufacturers, and aviation service providers.
  source_ids:
  - S1
  - S2
  - S3
  source_quote: Skywise is fast becoming the open platform of reference used by major
    aviation players to improve operational performance
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
  context_type: strategic_intent
  claim_title: Open aerospace app-store vision
  claim_description: Airbus aims to create an open Aerospace 'app-store' through the
    Skywise Partner Programme to accelerate the industry's digital transformation.
  source_ids:
  - S1
  source_quote: The Partner Programme builds on the exponential growth of the Skywise
    platform and aims to further accelerate innovation by connecting Skywise users
    with a global network of leading developers. As such, the programme paves the
    way for an open Aerospace 'app-store' to speed up the industry's digital transformation.
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
  claim_title: Partner Programme with global IT services leaders
  claim_description: Accenture, Capgemini, FPT Software, IBM, and Sopra Steria signed
    agreements to become early adopters of the Skywise Partner Programme, receiving
    training and certification.
  source_ids:
  - S1
  source_quote: Accenture, Capgemini, FPT Software, IBM, and Sopra Steria have signed
    agreements with Airbus to become early adopters of the Skywise Partner Programme.
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
  claim_title: Cloud-based platform hosted in Europe
  claim_description: Skywise is a secure, cloud-based platform that is physically
    hosted in Europe, providing data sovereignty for European operations.
  source_ids:
  - S2
  source_quote: Skywise provides users with a single access point to their enriched
    data by bringing together aviation information from multiple sources into one
    secure, cloud-based platform physically hosted in Europe.
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
  claim_title: Predictive maintenance application
  claim_description: Skywise enables predictive maintenance services, allowing airlines
    to identify and address component issues before they cause operational disruptions.
  source_ids:
  - S2
  - S3
  source_quote: Airbus' new five-year pact with British operator easyJet to provide
    predictive maintenance services for its entire fleet of nearly 300 aircraft, using
    technology that relies on Skywise.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10397'
  apqc_name: Perform maintenance, repair, and overhaul (MRO) for assets
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
  claim_title: Flight safety and airworthiness management
  claim_description: Skywise supports flight safety operations by enabling proactive
    identification of design flaws and safety risks before they result in incidents
    or accidents.
  source_ids:
  - S3
  source_quote: With Skywise — a product known best as a tool aimed at increasing
    operating efficiency for airlines and manufacturing efficiency for the plane maker
    — Airbus is demonstrating how its massive trove of data can help build a safety
    bridge between design and operations
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10419'
  apqc_name: Manage environmental health and safety (EHS)
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
  claim_title: Shared value business model
  claim_description: Skywise operates on a voluntary shared value model where both
    airlines and manufacturer benefit from operational data sharing, with strict trust
    and usage guidelines.
  source_ids:
  - S3
  source_quote: Because participation in Skywise is wholly voluntary, the success
    of the platform relies on airlines trusting in what Airbus calls its 'shared value'
    business model, meaning that both the airlines and manufacturer benefit from the
    sharing of operational data.
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
  context_type: temporal
  claim_title: easyJet five-year agreement in 2018
  claim_description: In 2018, Airbus signed a five-year agreement with easyJet to
    provide predictive maintenance services for its fleet of nearly 300 aircraft.
  source_ids:
  - S2
  source_quote: The agreement with FPT Software was made public the same day as Airbus'
    new five-year pact with British operator easyJet to provide predictive maintenance
    services for its entire fleet of nearly 300 aircraft
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
  claim_title: A330neo emergency AD issued August 2022
  claim_description: On August 17, 2022, EASA issued an emergency airworthiness directive
    for A330neo aircraft following discovery of a pneumatic system flaw through Skywise
    analysis.
  source_ids:
  - S3
  source_quote: On Aug. 17, 2022, after a large Airbus A330neo carrier reported leaking
    high-pressure valves in the system that bleeds air off of the engines, the European
    Union Aviation Safety Agency issued an emergency airworthiness directive (AD)
    to operators of the widebody aircraft.
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
  context_type: products_services
  claim_title: Multi-aircraft type support
  claim_description: Skywise supports data analysis for both Airbus and non-Airbus
    aircraft fleets, providing cross-platform analytics capabilities.
  source_ids:
  - S1
  - S3
  source_quote: Today over 80 airlines around the world have connected their Airbus
    and non-Airbus fleet to Skywise.
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
  claim_title: Automated reporting and benchmarking
  claim_description: Skywise provides automated reporting and benchmarking capabilities
    by freeing data from organizational silos and aggregating information across the
    industry.
  source_ids:
  - S1
  source_quote: The platform frees data from organisational siloes, allowing automated
    reporting, benchmarking capacity, and access to applications improving airlines
    operations and reducing their costs.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10130'
  apqc_name: Manage business performance
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
  claim_title: Ian Goodwin as Director of Flight Safety
  claim_description: Ian Goodwin serves as Director of Flight Safety – Safety Enhancement
    for Airbus Product Safety, overseeing the use of data for safety applications.
  source_ids:
  - S3
  source_quote: After The Air Current approached Airbus with questions about the engineering
    investigation, the company made Ian Goodwin, director of flight safety – safety
    enhancement for Airbus Product Safety, available to discuss both the A330neo case
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
      direct: 7
      contributing: 1
  context_claims:
    total: 14
    verified: 13
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

# Aviation Data Platform and Predictive Analytics

## Executive Summary

Airbus: Over 80 airlines connected to Skywise platform by 2019.

## Key Findings

- **Over 80 airlines connected to Skywise platform by 2019** — verified (adoption)
  - Quote: "Today over 80 airlines around the world have connected their Airbus and non-Airbus fleet to Skywise."

- **60x increase in data collection with FOMAX system** — verified (outcome)
  - Quote: "Skywise is able to analyse data from other components on easyJet's aircraft thanks to the installation of Airbus' new flight operations and maintenance exchanger, called FOMAX – which collects 60-time..."

- **easyJet engineers removed components before faults occurred** — verified (method)
  - Quote: "This activity builds on extensive trials with the platform that allowed easyJet engineers to remove components before faults occurred, limiting delays and cancellations as a result."

- **Skywise prevented catastrophic A330neo accident** — needs_review (method)
  - Quote: "Seeking an explanation for the leaking valves, Airbus engineers turned to the company's big data platform, Skywise, in search of clues. By comparing operational and sensor data, they were ultimately a..."

- **11,900 aircraft connected to Skywise platform** — verified (adoption)
  - Quote: "Today, Airbus reports that more than 11,900 aircraft are connected to the platform (some users analyze data from other manufacturers' aircraft with the help of Skywise as well)."

- **500GB to 1TB daily data collection per aircraft** — verified (method)
  - Quote: "Skywise integrates data from many different sources, including the wealth of flight and health-and-usage data that is collected onboard modern aircraft, which is around 500 gigabytes per day for the A..."

- **Skywise enables prioritization of safety risks** — needs_review (method)
  - Quote: "With more data, we can have a look at a bigger picture. We can prioritize, and prioritization in operations and safety is very important. So if we get an issue that's identified, we can identify what ..."

- **Skywise supports formal safety investigations** — verified (method)
  - Quote: "But Skywise has also been used in support of formal investigations into serious incidents. One of these incidents took place in April 2022, when a TAP Air Portugal A320 equipped with two CFM56 engines..."

## Sources

- **S1**: https://www.airbus.com/en/newsroom/press-releases/2019-06-airbus-opens-skywise-to-global-it-services-leaders
- **S2**: https://www.airbus.com/en/newsroom/news/2018-03-airbus-skywise-data-platform-gains-momentum
- **S3**: https://theaircurrent.com/aviation-safety/skywise-big-data-airbus-catastrophic-accident-a330neo/
- **S4**: https://www.mulesoft.com/case-studies/api/integration-airbus
- **S5**: https://runwaygirlnetwork.com/2018/02/press-release-airbus-open-aviation-data-platform-skywise-continues-to-gain-market-traction/
