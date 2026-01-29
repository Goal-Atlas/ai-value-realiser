---
case_id: marriott-bonvoy-ai-personalization
organisation: Marriott International
title: AI-Powered Travel Personalization and Search
date_created: '2026-01-29'
date_updated: '2026-01-29'
sources:
- id: S1
  title: https://marriott.pressarea.com/en/pressrelease/details/24123
  url: https://marriott.pressarea.com/en/pressrelease/details/24123
  raw_file: ''
  text_file: sources/text/S1.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S2
  title: https://www.customerexperiencedive.com/news/marriott-bonvoy-ai-powered-search-pe...
  url: https://www.customerexperiencedive.com/news/marriott-bonvoy-ai-powered-search-personalize-vacation/712221/
  raw_file: ''
  text_file: sources/text/S2.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S3
  title: https://blog.adobe.com/en/publish/2024/03/28/personalization-scale-future-guest-...
  url: https://blog.adobe.com/en/publish/2024/03/28/personalization-scale-future-guest-experience
  raw_file: ''
  text_file: sources/text/S3.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S4
  title: https://business.adobe.com/blog/perspectives/personalization-and-technology-are-...
  url: https://business.adobe.com/blog/perspectives/personalization-and-technology-are-evolving-in-the-hotel-industry-from-keyless-rooms-to-virtual-reality
  raw_file: ''
  text_file: sources/text/S4.txt
  extraction_method: unknown
  extraction_quality: high
  is_multi_page: false
  related_urls: []
value_claims:
- id: VC-001
  claim_title: AI adoption for travel planning increased from 26% to 50% over two
    years
  claim_description: Half of all EMEA travelers now use AI to plan or research holidays,
    up from 41% last year and 26% two years prior, demonstrating rapid adoption and
    growing trust in AI for travel planning.
  source_ids:
  - S1
  source_quote: half of all travellers in the research (50%) saying they have used
    AI to plan or research a holiday - this is up from 41% last year and just 26%
    the year before
  quote_location: Trust in AI builds section
  ai_attribution: direct
  attribution_evidence: The claim directly measures AI adoption rates for travel planning,
    showing clear progression in AI usage over time.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - augmentation
  outcome:
  - experience
  cognitive_depth: descriptive
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
- id: VC-002
  claim_title: 50% of travelers comfortable booking accommodation through AI platforms
  claim_description: Half of surveyed travelers indicate they would feel comfortable
    booking holiday accommodation through AI platforms in the future, with only 18%
    expressing discomfort.
  source_ids:
  - S1
  source_quote: half (50%) say that in future they would feel 'comfortable' booking
    holiday accommodation through AI platforms. Just 18% say the idea makes them 'uncomfortable'.
  quote_location: Trust in AI builds section
  ai_attribution: direct
  attribution_evidence: Measures consumer confidence and willingness to use AI for
    booking decisions, indicating readiness for AI-driven transactions.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - automation
  outcome:
  - experience
  cognitive_depth: predictive
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
  claim_title: AI search tool provides personalized rental options from 140,000 properties
  claim_description: Marriott Bonvoy launched an AI-powered search tool that accepts
    natural language queries to provide personalized vacation rental recommendations
    from a pool of 140,000 properties with activity suggestions.
  source_ids:
  - S2
  source_quote: Homes & Villas by Marriott Bonvoy, a luxury home rental offering,
    is testing an AI search tool designed to provide customers with personalized rental
    options from a pool of 140,000 properties.
  quote_location: Dive Brief section
  ai_attribution: direct
  attribution_evidence: AI directly enables natural language search and personalization
    capabilities that did not exist with traditional search.
  verification_status: verified
  evidence_level: method
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - augmentation
  - optimization
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
- id: VC-004
  claim_title: Adobe Experience Cloud enables one-to-one personalization at scale
  claim_description: Marriott deployed Adobe Experience Platform with Real-Time CDP
    and Journey Optimizer to unify guest data across channels and deliver precise
    one-to-one personalization throughout the guest journey.
  source_ids:
  - S3
  source_quote: Adobe Experience Platform, including Adobe Real-Time Customer Data
    Platform and Adobe Journey Optimizer, enable Marriott to unify data across channels
    and understand guests' needs, with insights to orchestrate personalization at
    scale.
  quote_location: Opening section
  ai_attribution: direct
  attribution_evidence: AI-powered platform directly enables real-time data unification
    and personalization orchestration that was not possible at this scale previously.
  verification_status: verified
  evidence_level: method
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - optimization
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
- id: VC-005
  claim_title: AI personalization supports direct bookings and loyalty expansion
  claim_description: Adobe Experience Cloud solutions help Marriott build guest loyalty
    over time, support direct bookings, drive loyalty program expansion, and deliver
    high-touch on-property experiences.
  source_ids:
  - S3
  source_quote: Adobe solutions help Marriott build guest loyalty over time, support
    direct bookings and loyalty expansion, and help guests receive a high-touch experience
    on property.
  quote_location: Why targeted personalization matters section
  ai_attribution: contributing
  attribution_evidence: AI contributes to business outcomes through personalization
    capabilities, though other factors also influence bookings and loyalty.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - optimization
  - augmentation
  outcome:
  - revenue_lift
  - business_growth
  cognitive_depth: prescriptive
  metric_raw:
    value: qualitative
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
  claim_title: Natural language AI search enables amenity-based vacation discovery
  claim_description: AI search tool allows customers to find vacation rentals based
    on preferred amenities rather than specific destinations, accepting queries with
    varying detail levels and matching multiple descriptors.
  source_ids:
  - S2
  source_quote: The search engine can also suggest vacation rentals based on preferred
    amenities rather than specific destinations. Customers can include as little or
    as much detail as they'd like, and the AI tool will offer suggestions that meet
    as many of the descriptors in their query as possible.
  quote_location: Dive Insight section
  ai_attribution: direct
  attribution_evidence: AI directly enables natural language understanding and multi-criteria
    matching that traditional search cannot perform.
  verification_status: verified
  evidence_level: method
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - augmentation
  - innovation
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
- id: VC-007
  claim_title: AI personalization deployed across 30+ brands and 8,800 properties
  claim_description: Adobe Experience Cloud helps Marriott match individuals with
    best options across its portfolio of more than 30 brands and nearly 8,800 properties
    through personalized recommendations.
  source_ids:
  - S3
  source_quote: Help the company match individuals with the best options across its
    portfolio of more than 30 brands and nearly 8,800 properties
  quote_location: Leveraging Experience Cloud section
  ai_attribution: direct
  attribution_evidence: AI directly enables personalized matching at scale across
    massive property portfolio that would be impossible manually.
  verification_status: verified
  evidence_level: method
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - optimization
  - automation
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
context_claims:
- id: CC-001
  context_type: temporal
  claim_title: Research conducted July 2025 for 2026 travel trends
  claim_description: Research conducted by Mortar Research between July 14-21, 2025,
    analyzing travel sentiment and trends for 2026.
  source_ids:
  - S1
  source_quote: Research conducted by Mortar Research amongst 22,266 adults in the
    UK, Italy, Spain, Germany, France, UAE, Saudi Arabia, Poland, Türkiye, South Africa,
    and Egypt between 14th-21st July 2025.
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
  context_type: scale
  claim_title: Research sample of 22,266 adults across 11 EMEA markets
  claim_description: Study included over 22,000 respondents across 11 key travel markets
    in Europe, Middle East and Africa, with minimum 2,000 respondents per market.
  source_ids:
  - S1
  source_quote: Research conducted by Mortar Research amongst 22,266 adults in the
    UK, Italy, Spain, Germany, France, UAE, Saudi Arabia, Poland, Türkiye, South Africa,
    and Egypt
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
  claim_title: Hospitality and travel industry focus
  claim_description: Marriott International operates in the hospitality sector, specifically
    hotel and vacation rental services through the Marriott Bonvoy loyalty program.
  source_ids:
  - S1
  - S2
  - S3
  source_quote: Marriott Bonvoy, Marriott International's award-winning travel program
    and marketplace
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
  claim_title: Marriott operates 30+ brands across 8,800 properties
  claim_description: Marriott International's portfolio includes more than 30 hotel
    brands and nearly 8,800 properties globally.
  source_ids:
  - S3
  source_quote: its portfolio of more than 30 brands and nearly 8,800 properties
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
  claim_title: Homes & Villas luxury rental offering with 140,000 properties
  claim_description: Marriott Bonvoy operates Homes & Villas, a luxury home rental
    service offering access to 140,000 vacation rental properties.
  source_ids:
  - S2
  source_quote: Homes & Villas by Marriott Bonvoy, a luxury home rental offering,
    is testing an AI search tool designed to provide customers with personalized rental
    options from a pool of 140,000 properties.
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
  claim_title: Personalization at center of customer interaction strategy
  claim_description: Marriott is strategically positioning personalization at the
    center of customer interactions to create seamless, intuitive travel experiences.
  source_ids:
  - S3
  source_quote: At Marriott, we are putting personalization at the center of how we
    interact with our customers in an effort to create seamless, intuitive travel
    experiences
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
  claim_title: Marketing and customer experience function
  claim_description: AI initiatives support marketing technology, digital content,
    data activation, and audience strategy functions within Marriott.
  source_ids:
  - S3
  source_quote: Amit Manurkar, VP, Digital Content & MarTech, Marriott International
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
- id: CC-008
  context_type: organisational
  claim_title: Partnership with Publicis Sapient for AI development
  claim_description: Marriott developed AI search tool in partnership with Publicis
    Sapient, a digital transformation consultancy.
  source_ids:
  - S2
  source_quote: Developed in partnership with Publicis Sapient, the search tool can
    accept natural language queries
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
  claim_title: Decade-long partnership with Adobe expanded
  claim_description: Marriott has maintained a 10-year relationship with Adobe, previously
    using Creative Cloud and Experience Manager, now expanded to include Experience
    Platform.
  source_ids:
  - S3
  source_quote: This announcement expands a decade-long relationship between our companies,
    where applications such as Adobe Creative Cloud and Adobe Experience Manager have
    supported Marriott's digital growth initiatives.
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
  claim_title: AI search tool launched in phases starting late 2024
  claim_description: AI search tool launched on Homes & Villas website with mobile
    app rollout planned for coming weeks after initial launch.
  source_ids:
  - S2
  source_quote: The AI search tool launched on the Homes & Villas by Marriott Bonvoy
    website last week and will roll out to the mobile app in the coming weeks.
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
  claim_title: Customer data platform and journey orchestration
  claim_description: Implementation spans customer data management, real-time personalization,
    and journey orchestration across digital touchpoints.
  source_ids:
  - S3
  source_quote: Adobe Real-Time Customer Data Platform and Adobe Journey Optimizer,
    enable Marriott to unify data across channels and understand guests' needs
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
verification_summary:
  value_claims:
    total: 7
    verified: 7
    needs_review: 0
    rejected: 0
    by_attribution:
      direct: 6
      contributing: 1
  context_claims:
    total: 11
    verified: 11
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

# AI-Powered Travel Personalization and Search

## Executive Summary

Marriott International: AI adoption for travel planning increased from 26% to 50% over two years.

## Key Findings

- **AI adoption for travel planning increased from 26% to 50% over two years** — verified (adoption)
  - Quote: "half of all travellers in the research (50%) saying they have used AI to plan or research a holiday - this is up from 41% last year and just 26% the year before"

- **50% of travelers comfortable booking accommodation through AI platforms** — verified (adoption)
  - Quote: "half (50%) say that in future they would feel 'comfortable' booking holiday accommodation through AI platforms. Just 18% say the idea makes them 'uncomfortable'."

- **AI search tool provides personalized rental options from 140,000 properties** — verified (method)
  - Quote: "Homes & Villas by Marriott Bonvoy, a luxury home rental offering, is testing an AI search tool designed to provide customers with personalized rental options from a pool of 140,000 properties."

- **Adobe Experience Cloud enables one-to-one personalization at scale** — verified (method)
  - Quote: "Adobe Experience Platform, including Adobe Real-Time Customer Data Platform and Adobe Journey Optimizer, enable Marriott to unify data across channels and understand guests' needs, with insights to or..."

- **AI personalization supports direct bookings and loyalty expansion** — verified (outcome)
  - Quote: "Adobe solutions help Marriott build guest loyalty over time, support direct bookings and loyalty expansion, and help guests receive a high-touch experience on property."

- **Natural language AI search enables amenity-based vacation discovery** — verified (method)
  - Quote: "The search engine can also suggest vacation rentals based on preferred amenities rather than specific destinations. Customers can include as little or as much detail as they'd like, and the AI tool wi..."

- **AI personalization deployed across 30+ brands and 8,800 properties** — verified (method)
  - Quote: "Help the company match individuals with the best options across its portfolio of more than 30 brands and nearly 8,800 properties"

## Sources

- **S1**: https://marriott.pressarea.com/en/pressrelease/details/24123
- **S2**: https://www.customerexperiencedive.com/news/marriott-bonvoy-ai-powered-search-personalize-vacation/712221/
- **S3**: https://blog.adobe.com/en/publish/2024/03/28/personalization-scale-future-guest-experience
- **S4**: https://business.adobe.com/blog/perspectives/personalization-and-technology-are-evolving-in-the-hotel-industry-from-keyless-rooms-to-virtual-reality
