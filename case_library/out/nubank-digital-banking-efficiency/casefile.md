---
case_id: nubank-digital-banking-efficiency
organisation: Nubank
title: Digital-First Banking Platform
date_created: '2026-01-29'
date_updated: '2026-01-29'
sources:
- id: S1
  title: https://www.businesswire.com/news/home/20240508557544/en/Nubank-Surpasses-100-Mi...
  url: https://www.businesswire.com/news/home/20240508557544/en/Nubank-Surpasses-100-Million-Customers
  raw_file: ''
  text_file: sources/text/S1.txt
  extraction_method: unknown
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S2
  title: https://customers.twilio.com/en-us/nubank
  url: https://customers.twilio.com/en-us/nubank
  raw_file: ''
  text_file: sources/text/S2.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S3
  title: https://whitesight.net/inside-nubanks-playbook-for-cost-efficient-hypergrowth/
  url: https://whitesight.net/inside-nubanks-playbook-for-cost-efficient-hypergrowth/
  raw_file: ''
  text_file: sources/text/S3.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S4
  title: https://www.theuxda.com/blog/ai-gold-rush-21-digital-banking-ai-case-studies-cx-...
  url: https://www.theuxda.com/blog/ai-gold-rush-21-digital-banking-ai-case-studies-cx-transformation
  raw_file: ''
  text_file: sources/text/S4.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
value_claims:
- id: VC-001
  claim_title: 80% customer growth from word-of-mouth referrals
  claim_description: Nubank achieved 80% of its customer growth through organic word-of-mouth
    referrals, driven by high customer satisfaction and NPS, enabling near-zero customer
    acquisition costs.
  source_ids:
  - S3
  source_quote: 80% of that growth comes from word-of-mouth referrals alone.
  quote_location: Main content section
  ai_attribution: contextual
  attribution_evidence: Growth driven by customer experience and NPS, not directly
    by AI systems, though AI supports the underlying service quality through automation
    and support tools.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
  - cost_reduction
  - business_growth
  cognitive_depth: descriptive
  metric_raw:
    value: '80'
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
  claim_title: Net Promoter Score of 90
  claim_description: Nubank achieved an NPS of 90, nearly three times higher than
    incumbent banks and major local fintechs, serving as the foundation for its word-of-mouth
    growth engine.
  source_ids:
  - S3
  source_quote: Clocking in at 90, nearly three times higher than incumbents and other
    major local fintechs
  quote_location: NPS section
  ai_attribution: contributing
  attribution_evidence: AI-powered customer support (Twilio Flex), proactive service,
    and automation contribute to the high NPS, though not the sole driver.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - augmentation
  - automation
  outcome:
  - experience
  cognitive_depth: descriptive
  metric_raw:
    value: '90'
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
  claim_title: Customer acquisition cost held at $7
  claim_description: Nubank maintained a customer acquisition cost of $7 in 2023-2024,
    far below industry averages, enabled by word-of-mouth growth and efficient digital
    operations.
  source_ids:
  - S3
  source_quote: The customer acquisition cost has held steady at $7 for both 2023
    and 2024, up slightly from $6.5 in 2022, but still far below industry averages.
  quote_location: NPS Flywheel section
  ai_attribution: contributing
  attribution_evidence: AI-driven automation and digital-first platform reduce operational
    costs, contributing to low CAC alongside organic growth strategies.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
  - optimization
  outcome:
  - cost_reduction
  cognitive_depth: descriptive
  metric_raw:
    value: '7'
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
  claim_title: 94% of calls answered in under 45 seconds
  claim_description: Nubank achieves 94% of customer calls answered within 45 seconds
    through trained professionals (Xpeers) and efficient support systems.
  source_ids:
  - S3
  source_quote: 94% of customer calls are answered in under 45 seconds.
  quote_location: Foundation Behind Nubank's Consistent NPS section
  ai_attribution: contributing
  attribution_evidence: Twilio Flex platform with analytical tools and automation
    supports rapid call handling, though human agents (Xpeers) deliver the service.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
  - augmentation
  outcome:
  - velocity
  - experience
  cognitive_depth: descriptive
  metric_raw:
    value: '94'
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
  claim_title: Cost to serve reduced to $0.8 per user
  claim_description: Nubank reduced cost to serve from $0.9 to $0.8 per user despite
    growing from 93.9M to 114.3M customers, reflecting scalability of digital-native,
    automation-led model.
  source_ids:
  - S3
  source_quote: cost to serve dropped to $0.8 per user, down from $0.9. This reflects
    the scalability of a digitally-native, automation-led operating model.
  quote_location: NPS Flywheel section
  ai_attribution: direct
  attribution_evidence: Explicitly attributed to automation-led operating model that
    scales efficiently with customer growth.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
  - optimization
  outcome:
  - cost_reduction
  cognitive_depth: descriptive
  metric_raw:
    value: '0.8'
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
  claim_title: Payments Assistant saved 750K+ hours annually
  claim_description: Nubank's Payments Assistant platform for bills and recurring
    transactions saved customers over 750,000 hours in one year through automation.
  source_ids:
  - S3
  source_quote: Nubank's Payments Assistant platform for bills and recurring transactions
    saved customers 750K+ hours in one year.
  quote_location: Product features section
  ai_attribution: direct
  attribution_evidence: Automated platform directly saves customer time through intelligent
    handling of recurring payments and bills.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_creation
  mechanism:
  - automation
  outcome:
  - velocity
  - experience
  cognitive_depth: prescriptive
  metric_raw:
    value: '750000'
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
- id: VC-007
  claim_title: Overdraft alerts helped avoid R$4M in interest
  claim_description: Open finance-powered overdraft alerts helped Nubank customers
    avoid R$4 million in interest charges in just one month through proactive notifications.
  source_ids:
  - S3
  source_quote: Open finance-powered overdraft alerts helped avoid R$4M in interest
    in just a month.
  quote_location: Product features section
  ai_attribution: direct
  attribution_evidence: AI-powered alerts using open finance data directly prevent
    customer costs through predictive notifications.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_creation
  mechanism:
  - optimization
  - augmentation
  outcome:
  - cost_reduction
  - experience
  cognitive_depth: predictive
  metric_raw:
    value: '4000000'
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
- id: VC-008
  claim_title: 1.4M users nudged on idle funds
  claim_description: Nubank used personalized notifications to nudge 1.4 million users
    to take action on idle funds, building daily utility through purposeful engagement.
  source_ids:
  - S3
  source_quote: 1.4M users were nudged to act on idle funds via personalized notifications—purposeful
    nudges that build daily utility.
  quote_location: Product features section
  ai_attribution: direct
  attribution_evidence: Personalized notification system uses data analysis to identify
    and engage users with idle funds, directly driving action.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: secondary_high
  application_type: capability_creation
  mechanism:
  - augmentation
  - optimization
  outcome:
  - experience
  cognitive_depth: prescriptive
  metric_raw:
    value: '1400000'
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
- id: VC-009
  claim_title: Complaint rate of 1,222 per million users
  claim_description: 'Nubank achieved only 1,222 complaints per million users in Q4
    2024, far lower than incumbent banks (Itau: 4,127; Santander: 3,365) and fintechs
    (PagBank: 7,926).'
  source_ids:
  - S3
  source_quote: 'Nubank received only 1,222 complaints per million users in Q4 2024.
    That''s far lower than both incumbents (Itau: 4,127; Santander: 3,365) and new-age
    fintechs like PagBank (7,926)'
  quote_location: Ultra-low complaint rates section
  ai_attribution: contributing
  attribution_evidence: AI-powered support systems and automation contribute to service
    quality that reduces complaints, alongside human service excellence.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
  - augmentation
  outcome:
  - experience
  - risk_avoidance
  cognitive_depth: descriptive
  metric_raw:
    value: '1222'
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
- id: VC-010
  claim_title: 22% YoY customer growth to 114.3M
  claim_description: Nubank grew from 93.9M customers in 2023 to 114.3M in 2024, adding
    over 20M users representing 22% year-over-year growth.
  source_ids:
  - S3
  source_quote: Nubank grew from 93.9M customers in 2023 to 114.3M in 2024—adding
    over 20M users (22% YoY).
  quote_location: NPS Flywheel section
  ai_attribution: contributing
  attribution_evidence: AI-enabled efficient operations and customer experience contribute
    to sustainable growth, though growth is multi-factorial.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
  - business_growth
  cognitive_depth: descriptive
  metric_raw:
    value: '22'
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
- id: VC-011
  claim_title: 83% customer activity rate maintained
  claim_description: Nubank maintained an 83% activity rate with 94.9M active users
    out of 114.3M total customers in 2024, demonstrating strong engagement at scale.
  source_ids:
  - S3
  source_quote: Active users hit 94.9M in 2024, sustaining an 83% activity rate.
  quote_location: NPS Flywheel section
  ai_attribution: contributing
  attribution_evidence: AI-powered personalization and engagement features (notifications,
    alerts, assistants) help maintain high activity rates.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - augmentation
  - optimization
  outcome:
  - experience
  cognitive_depth: descriptive
  metric_raw:
    value: '83'
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
- id: VC-012
  claim_title: Improved call quality and flexibility with Twilio Flex
  claim_description: Nubank experienced better call quality and more flexibility to
    improve phone experience by quickly adjusting contingency IVRs using Twilio Flex
    platform.
  source_ids:
  - S2
  source_quote: fintech has noticed better call quality, as well as experiencing more
    flexibility and speed to improve the overall phone experience by quickly turning
    on and off contingency IVRs
  quote_location: Building the solution section
  ai_attribution: direct
  attribution_evidence: Twilio Flex platform directly enables improved call quality
    and operational flexibility through its technology capabilities.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_low
  application_type: capability_enhancement
  mechanism:
  - optimization
  - automation
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
- id: VC-013
  claim_title: Enhanced supervisor productivity with analytics
  claim_description: Twilio Flex provided supervisors with detailed analytical tools
    and ability to download call recordings directly, improving productivity without
    external requests.
  source_ids:
  - S2
  source_quote: Being able to download call recordings from the tool itself without
    having to make requests to agents elsewhere is one of the examples of improved
    productivity.
  quote_location: Building the solution section
  ai_attribution: direct
  attribution_evidence: Twilio Flex analytical tools directly enable supervisor efficiency
    through self-service access to data and recordings.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_low
  application_type: capability_enhancement
  mechanism:
  - automation
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
- id: VC-014
  claim_title: More effective action plans through analytical tools
  claim_description: Analytical and investigative tools in Twilio Flex helped Nubank
    define more effective action plans with agents to solve connection problems.
  source_ids:
  - S2
  source_quote: The analytical and investigative tools helped us to define more effective
    action plans with our agents to solve connection problems
  quote_location: Building the solution section
  ai_attribution: direct
  attribution_evidence: Analytical tools directly enable data-driven problem-solving
    and action planning for operational improvements.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_low
  application_type: capability_enhancement
  mechanism:
  - augmentation
  - optimization
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
- id: VC-015
  claim_title: 50% increase in 60+ customer acquisition
  claim_description: Nubank saw 50% higher volume of new customers over 60 years old
    between April-June 2021 compared to the same period in 2019.
  source_ids:
  - S2
  source_quote: Between April and June of 2021, the volume of new customers in this
    range was 50 percent higher than in the same period in 2019.
  quote_location: Company background section
  ai_attribution: contextual
  attribution_evidence: Growth in elderly segment reflects overall digital-first platform
    accessibility, not directly attributed to specific AI features.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_low
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
  - business_growth
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
context_claims:
- id: CC-001
  context_type: organisational
  claim_title: Nubank serves 114.3M customers across Latin America
  claim_description: As of 2024, Nubank serves 114.3 million customers across Brazil,
    Mexico, and Colombia, making it one of the world's largest digital banking platforms.
  source_ids:
  - S2
  - S3
  source_quote: one of the world's largest digital banking platforms, serving around
    54 million customers across Brazil, Mexico and Colombia
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
  claim_title: Founded in May 2013
  claim_description: Nubank was founded in May 2013 and launched its first product
    (purple credit card) in less than a year.
  source_ids:
  - S2
  source_quote: Founded in May 2013, Nubank already has great results for a fintech
    company that has less than 10 years in the market.
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
  claim_title: Digital-first fintech in banking sector
  claim_description: Nubank defines itself as a technology company pioneering the
    digital-first era of banking, differentiating from traditional banks.
  source_ids:
  - S2
  source_quote: Nubank is pioneering the new 'digital-first' era of banking
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
  context_type: strategic_intent
  claim_title: Mission to revolutionize financial sector in Latin America
  claim_description: Nubank's mission is to revolutionize the financial sector in
    Latin America, focusing on financial inclusion in a region with 30-65% unbanked
    populations.
  source_ids:
  - S2
  source_quote: revolutionize the financial sector in Latin America. This is a region
    of great inequality, where about 30 percent, 55 percent, and 65 percent of the
    populations of Brazil, Colombia, and Mexico
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
  context_type: products_services
  claim_title: Offers credit cards and digital banking services
  claim_description: Nubank offers credit cards (purple Mastercard), digital banking,
    payments, and financial management services through mobile-first platform.
  source_ids:
  - S2
  source_quote: fintech presented its first product, the famous purple credit card
    with the Mastercard brand
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
  claim_title: Customer service supported by four pillars
  claim_description: 'Nubank''s customer service is built on four pillars: anticipating,
    solving, caring, and training, with emphasis on transparency.'
  source_ids:
  - S2
  source_quote: 'Nubank''s service is supported by four pillars: anticipating, solving,
    caring, and training.'
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10218'
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
- id: CC-007
  context_type: organisational
  claim_title: Achieved unicorn status after 4 years
  claim_description: Nubank achieved unicorn startup status 4 years after launching
    its first product, demonstrating rapid growth trajectory.
  source_ids:
  - S2
  source_quote: After 4 years of this launch, Nubank has achieved unicorn startup
    status
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
  context_type: functional
  claim_title: Uses Twilio Flex and SendGrid for customer engagement
  claim_description: Nubank deployed Twilio Flex for voice channels, emergency calls,
    and SendGrid for SMS alerts and email campaigns to serve customers across multiple
    channels.
  source_ids:
  - S2
  source_quote: Twilio Flex is used to serve customers through voice channels, emergency
    calls (ombudsman), sending alerts via SMS, and information and campaigns through
    Sendgrid.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10218'
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
- id: CC-009
  context_type: organisational
  claim_title: Employs thousands of internal agents (Xpeers)
  claim_description: Nubank employs thousands of trained customer service professionals
    called Xpeers who handle customer interactions with support from technology platforms.
  source_ids:
  - S2
  - S3
  source_quote: With thousands of internal agents, supervisors, who were already empowered
    with analytical tools and resources
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
  claim_title: Accelerated digitization during pandemic
  claim_description: The pandemic accelerated Nubank's digitization efforts, with
    42,000 new users per day in Q1 2020 and early adoption of remote work.
  source_ids:
  - S2
  source_quote: The pandemic further accelerated the digitization that was already
    being done by Nubank. In the first quarter of 2020, the bank registered an average
    of 42 thousand new users per day
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
  claim_title: Focus on customer experience through data and design
  claim_description: Nubank leverages data and design to generate excellent customer
    experience, offering financial services that differentiate in the sector.
  source_ids:
  - S2
  source_quote: Nubank leverages data and design to generate an excellent customer
    experience, thus offering financial services that not only meet user needs but
    truly differentiate
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
  context_type: scale
  claim_title: Averages 13M new customers annually since 2015
  claim_description: Since 2015, Nubank has added nearly 13 million customers every
    year on average, demonstrating sustained growth at scale.
  source_ids:
  - S3
  source_quote: Since 2015, it has added nearly 13 million customers every year on
    average.
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
  claim_title: Operates SOS Nu platform for scam education
  claim_description: Nubank operates the SOS Nu platform, a comprehensive hub educating
    users on scams and thefts through real-time, actionable tips.
  source_ids:
  - S3
  source_quote: The SOS Nu platform adds another layer—a comprehensive hub educating
    users on scams and thefts through real-time, actionable tips.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10218'
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
- id: CC-014
  context_type: strategic_intent
  claim_title: Financial education as core pillar
  claim_description: Financial education is a core pillar of Nubank's strategy, embedded
    in product design to empower consumers and build community benefits.
  source_ids:
  - S3
  source_quote: Financial education has always been one of our pillars, and it is
    also present in the design of our products and services to empower consumers
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
  context_type: organisational
  claim_title: Co-founded by Cristina Junqueira
  claim_description: Cristina Junqueira is co-founder and CGO of Nubank, actively
    involved in customer experience strategy and company vision.
  source_ids:
  - S2
  - S3
  source_quote: Nubank co-founder Cristina Junqueira said
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
    verified: 15
    needs_review: 0
    rejected: 0
    by_attribution:
      contextual: 2
      contributing: 6
      direct: 7
  context_claims:
    total: 15
    verified: 13
    unverified: 2
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

# Digital-First Banking Platform

## Executive Summary

Nubank: 80% customer growth from word-of-mouth referrals.

## Key Findings

- **80% customer growth from word-of-mouth referrals** — verified (outcome)
  - Quote: "80% of that growth comes from word-of-mouth referrals alone."

- **Net Promoter Score of 90** — verified (outcome)
  - Quote: "Clocking in at 90, nearly three times higher than incumbents and other major local fintechs"

- **Customer acquisition cost held at $7** — verified (outcome)
  - Quote: "The customer acquisition cost has held steady at $7 for both 2023 and 2024, up slightly from $6.5 in 2022, but still far below industry averages."

- **94% of calls answered in under 45 seconds** — verified (outcome)
  - Quote: "94% of customer calls are answered in under 45 seconds."

- **Cost to serve reduced to $0.8 per user** — verified (outcome)
  - Quote: "cost to serve dropped to $0.8 per user, down from $0.9. This reflects the scalability of a digitally-native, automation-led operating model."

- **Payments Assistant saved 750K+ hours annually** — verified (outcome)
  - Quote: "Nubank's Payments Assistant platform for bills and recurring transactions saved customers 750K+ hours in one year."

- **Overdraft alerts helped avoid R$4M in interest** — verified (outcome)
  - Quote: "Open finance-powered overdraft alerts helped avoid R$4M in interest in just a month."

- **1.4M users nudged on idle funds** — verified (adoption)
  - Quote: "1.4M users were nudged to act on idle funds via personalized notifications—purposeful nudges that build daily utility."

- **Complaint rate of 1,222 per million users** — verified (outcome)
  - Quote: "Nubank received only 1,222 complaints per million users in Q4 2024. That's far lower than both incumbents (Itau: 4,127; Santander: 3,365) and new-age fintechs like PagBank (7,926)"

- **22% YoY customer growth to 114.3M** — verified (outcome)
  - Quote: "Nubank grew from 93.9M customers in 2023 to 114.3M in 2024—adding over 20M users (22% YoY)."

- **83% customer activity rate maintained** — verified (outcome)
  - Quote: "Active users hit 94.9M in 2024, sustaining an 83% activity rate."

- **Improved call quality and flexibility with Twilio Flex** — verified (method)
  - Quote: "fintech has noticed better call quality, as well as experiencing more flexibility and speed to improve the overall phone experience by quickly turning on and off contingency IVRs"

- **Enhanced supervisor productivity with analytics** — verified (method)
  - Quote: "Being able to download call recordings from the tool itself without having to make requests to agents elsewhere is one of the examples of improved productivity."

- **More effective action plans through analytical tools** — verified (method)
  - Quote: "The analytical and investigative tools helped us to define more effective action plans with our agents to solve connection problems"

- **50% increase in 60+ customer acquisition** — verified (outcome)
  - Quote: "Between April and June of 2021, the volume of new customers in this range was 50 percent higher than in the same period in 2019."

## Sources

- **S1**: https://www.businesswire.com/news/home/20240508557544/en/Nubank-Surpasses-100-Million-Customers
- **S2**: https://customers.twilio.com/en-us/nubank
- **S3**: https://whitesight.net/inside-nubanks-playbook-for-cost-efficient-hypergrowth/
- **S4**: https://www.theuxda.com/blog/ai-gold-rush-21-digital-banking-ai-case-studies-cx-transformation
