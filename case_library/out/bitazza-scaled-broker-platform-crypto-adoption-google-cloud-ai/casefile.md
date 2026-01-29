---
case_id: bitazza-scaled-broker-platform-crypto-adoption-google-cloud-ai
organisation: Bitazza Thailand
title: Scaled Broker Platform for Crypto Adoption Using Google Cloud and AI
date_created: '2026-01-29'
date_updated: '2026-01-29'
sources:
- id: S1
  title: https://cloud.google.com/customers/bitazza
  url: https://cloud.google.com/customers/bitazza
  raw_file: ''
  text_file: sources/text/S1.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S2
  title: https://www.fuse.io/casestudies/bitazza
  url: https://www.fuse.io/casestudies/bitazza
  raw_file: ''
  text_file: sources/text/S2.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S3
  title: https://blogth.bitazza.com/en/blog/what-are-centralized-crypto-trading-platforms
  url: https://blogth.bitazza.com/en/blog/what-are-centralized-crypto-trading-platforms
  raw_file: ''
  text_file: sources/text/S3.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
value_claims:
- id: VC-001
  claim_title: Scaled data infrastructure to support $4.6 billion in transactions
  claim_description: Bitazza Thailand's data team built and scaled its data infrastructure
    on Google Cloud to drive $4.6 billion in transactions in 2024, handling complex
    digital assets, fiat currencies, and third-party feeds.
  source_ids:
  - S1
  source_quote: Functioning as a digital asset brokerage platform, its data team built
    and scaled its data infrastructure to drive $4.6B in transactions in 2024.
  quote_location: Body section
  ai_attribution: contributing
  attribution_evidence: Google Cloud AI services (Vertex AI Notebooks, BigQuery Notebooks)
    contributed to data infrastructure capabilities that enabled transaction processing,
    alongside core data warehouse functionality.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - optimization
  - automation
  outcome:
  - business_growth
  - revenue_lift
  cognitive_depth: predictive
  metric_raw:
    value: '4.6'
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
  claim_title: Accelerated financial statement creation by 75%
  claim_description: Bitazza Thailand reduced the time required to create financial
    statements from one year to three months, representing a 75% acceleration in the
    process using Google Cloud infrastructure.
  source_ids:
  - S1
  source_quote: Accelerated financial statement creation by 75%, cutting the process
    from one year to three months
  quote_location: Header section
  ai_attribution: contributing
  attribution_evidence: BigQuery and AI-powered data analytics tools enabled faster
    data processing and analysis, contributing to the acceleration alongside automated
    workflows.
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
- id: VC-003
  claim_title: Near-real-time regulatory compliance reporting
  claim_description: Bitazza Thailand maintains regulatory compliance with near-real-time
    data reports, processing and submitting accurate daily aggregated millions of
    transactions to SEC, AMLO, and BOT using BigQuery and Google Sheets.
  source_ids:
  - S1
  source_quote: Bitazza Thailand must process near-real-time and submit accurate daily
    aggregated millions of transactions. The compliance and risk team uses Google
    Sheets and BigQuery to generate these trusted, near-real-time reports.
  quote_location: Compliance section
  ai_attribution: contributing
  attribution_evidence: BigQuery's data processing capabilities and integration with
    Sheets enable near-real-time reporting, with AI/ML capabilities supporting data
    analysis and pattern detection.
  verification_status: needs_review
  evidence_level: method
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  - optimization
  outcome:
  - risk_avoidance
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
- id: VC-004
  claim_title: Enabled data team to manage CI/CD without dedicated DevOps engineer
  claim_description: Bitazza Thailand's data team can build and run their own CI/CD
    pipelines using Cloud Build, Cloud Run, and related services without requiring
    a dedicated DevOps engineer, reducing operational overhead.
  source_ids:
  - S1
  source_quote: Empowers data team to build and run their own CI/CD pipelines, without
    a dedicated DevOps engineer
  quote_location: Header section
  ai_attribution: contextual
  attribution_evidence: Cloud automation tools enable self-service capabilities, though
    not directly AI-powered. AI is part of broader Google Cloud ecosystem used by
    the team.
  verification_status: verified
  evidence_level: method
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - cost_reduction
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
- id: VC-005
  claim_title: Proactive fraud detection and risk mitigation
  claim_description: The compliance team uses digital asset reports generated from
    BigQuery to proactively detect suspicious trading patterns or fraudulent activities
    and mitigate risk before it escalates, protecting the company and customers.
  source_ids:
  - S1
  source_quote: The team uses digital asset reports to proactively detect suspicious
    trading patterns or fraudulent activities and mitigate risk before it escalates.
  quote_location: Compliance section
  ai_attribution: contributing
  attribution_evidence: BigQuery analytics combined with AI/ML capabilities (Vertex
    AI, BigQuery ML) enable pattern detection and predictive risk analysis for fraud
    prevention.
  verification_status: needs_review
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - optimization
  - augmentation
  outcome:
  - risk_avoidance
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
- id: VC-006
  claim_title: Accelerated machine learning lifecycle with integrated notebooks
  claim_description: Vertex AI Notebooks and BigQuery Notebooks enable the team to
    rapidly create data models on BigQuery data without moving data, accelerating
    the entire machine learning lifecycle from development to deployment.
  source_ids:
  - S1
  source_quote: BigQuery Notebooks offer a familiar notebook interface, combining
    the power of BigQuery with the flexibility of Python libraries. This enables the
    team to rapidly create data models on their BigQuery data, eliminating the need
    to move data.
  quote_location: Data science section
  ai_attribution: direct
  attribution_evidence: Vertex AI Notebooks and BigQuery Notebooks are AI/ML-specific
    tools that directly enable machine learning model development, training, and deployment.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_creation
  mechanism:
  - innovation
  - augmentation
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
  claim_title: Over 100,000 transactions under $0.01 on Freedom Wallet
  claim_description: Bitazza's Freedom Wallet, built on Fuse Network infrastructure,
    has processed more than 100,000 transactions at under $0.01 per transaction, enabling
    cost-effective Web3 payments for businesses and users.
  source_ids:
  - S2
  source_quote: To date, thousands of wallets have been created by end users, with
    more than 100 thousand transactions completed for under $0.01 on Fuse Network.
  quote_location: End results section
  ai_attribution: contextual
  attribution_evidence: Transaction processing is primarily blockchain infrastructure.
    AI mentioned in broader context of Bitazza's technology stack but not directly
    attributed to this specific outcome.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - optimization
  outcome:
  - cost_reduction
  - business_growth
  cognitive_depth: descriptive
  metric_raw:
    value: '100000'
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
- id: VC-008
  claim_title: Thousands of wallets created by end users
  claim_description: Bitazza's Freedom Wallet solution has enabled thousands of end
    users to create wallets, expanding the platform's reach and supporting Web3 adoption
    across Southeast Asia.
  source_ids:
  - S2
  source_quote: To date, thousands of wallets have been created by end users, with
    more than 100 thousand transactions completed for under $0.01 on Fuse Network.
  quote_location: End results section
  ai_attribution: contextual
  attribution_evidence: Wallet creation is primarily a blockchain/platform feature.
    AI is part of Bitazza's broader technology ecosystem but not directly attributed
    to wallet creation.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - innovation
  outcome:
  - business_growth
  cognitive_depth: descriptive
  metric_raw:
    value: thousands
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
  claim_title: Bitazza Thailand is a licensed digital asset broker
  claim_description: Bitazza Thailand operates as a licensed digital asset broker
    under the oversight of Thailand's Securities and Exchange Commission (SEC), Anti-Money
    Laundering Office (AMLO), and Bank of Thailand (BOT).
  source_ids:
  - S1
  source_quote: Bitazza Thailand, as a licensed digital asset broker, is a key driver
    of crypto adoption in Thailand
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
  claim_title: Financial Services - Digital Asset Brokerage
  claim_description: Bitazza operates in the financial services sector, specifically
    as a digital asset brokerage platform providing cryptocurrency trading and related
    services.
  source_ids:
  - S1
  - S3
  source_quote: 'Industry: Financial Services'
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
  context_type: organisational
  claim_title: Thailand-based operations in top 20 global crypto market
  claim_description: Bitazza Thailand operates in Thailand, a nation consistently
    ranked among the global top 20 crypto markets, positioning the company in a significant
    regional market.
  source_ids:
  - S1
  source_quote: Bitazza Thailand, as a licensed digital asset broker, is a key driver
    of crypto adoption in Thailand, a nation consistently ranked among the global
    top 20 crypto markets.
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
  context_type: scale
  claim_title: Handles terabytes of data from multiple sources
  claim_description: Bitazza Thailand's data infrastructure consolidates terabytes
    of data from internal and external sources, including digital assets, fiat currencies,
    and third-party feeds.
  source_ids:
  - S1
  source_quote: BigQuery serves as Bitazza Thailand's central data warehouse, consolidating
    terabytes of data from internal and external sources.
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
  claim_title: Regulatory compliance and risk management function
  claim_description: Bitazza Thailand operates under strict regulatory oversight requiring
    daily reporting of millions of transactions to SEC, AMLO, and BOT, with dedicated
    compliance and risk management capabilities.
  source_ids:
  - S1
  source_quote: Operating under the oversight of the Securities and Exchange Commission
    (SEC), the Anti-Money Laundering Office (AMLO), and the Bank of Thailand (BOT),
    Bitazza Thailand must process near-real-time and submit accurate daily aggregated
    millions of transactions.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10423'
  apqc_name: Manage compliance
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
  claim_title: Aim to become fully data-driven organization
  claim_description: Bitazza Thailand's strategic goal is to become a fully data-driven
    organization, leveraging Google Cloud infrastructure and AI capabilities to achieve
    this transformation.
  source_ids:
  - S1
  source_quote: With Google Cloud, our aim to become a fully data-driven organization
    is just within reach
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
  context_type: products_services
  claim_title: Multi-product ecosystem including exchange, wallet, and business solutions
  claim_description: Bitazza offers a comprehensive product ecosystem including centralized
    exchange trading (80+ currencies), Freedom Wallet (non-custodial), Freedom Card
    (Visa card), Freedom World (business platform), and OTC services.
  source_ids:
  - S2
  - S3
  source_quote: Bitazza is an ASEAN-based centralized broker crypto trading platform
    certified by Thailand's SEC that offers a comprehensive range of cryptocurrency
    services, including coin trading and financial solutions for individuals and businesses.
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
  context_type: organisational
  claim_title: Small executive team of fewer than ten members
  claim_description: Bitazza operates with a dedicated executive team of fewer than
    ten members working to expand reach and deliver Web3 payment solutions across
    Southeast Asia.
  source_ids:
  - S2
  source_quote: The dedicated executive team of fewer than ten members works continuously
    to onboard new operators, expand their reach, and deliver Web3 payment solutions
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
  context_type: temporal
  claim_title: 2024 transaction volume and infrastructure scaling
  claim_description: The $4.6 billion in transactions and infrastructure capabilities
    described represent Bitazza's operational scale in 2024.
  source_ids:
  - S1
  source_quote: its data team built and scaled its data infrastructure to drive $4.6B
    in transactions in 2024
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
  context_type: functional
  claim_title: Data engineering and analytics function
  claim_description: Bitazza has a dedicated data team responsible for building and
    managing data infrastructure, analytics, machine learning, and serving multiple
    business units including finance, marketing, and product.
  source_ids:
  - S1
  source_quote: Bitazza Thailand's data team turned to Google Cloud for its ease of
    use and scalability, enabling the data team to support an expanding range of use
    cases.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10866'
  apqc_name: Manage enterprise information
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
  claim_title: Exploring AI for KYC operations optimization
  claim_description: Bitazza Thailand plans to continue innovation with Google Cloud
    AI, exploring AI tools integrated with data warehouse to streamline Know-Your-Customer
    (KYC) operations and reduce operating time without compromising security.
  source_ids:
  - S1
  source_quote: The team is exploring AI tools that integrate directly with its data
    warehouse. This initiative aims to streamline critical internal processes, such
    as the Know-Your-Customer (KYC) operations, which can reduce operating time without
    compromising security.
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
  context_type: sectoral
  claim_title: Gateway for crypto adoption in Southeast Asia
  claim_description: Bitazza positions itself as a gateway for cryptocurrency adoption
    in Southeast Asia and beyond, particularly for B2B, retail, and Web3 utilities
    in everyday life.
  source_ids:
  - S2
  source_quote: it sets its sites as a gateway for crypto adoption in South East Asia
    and beyond, particularly for business-to-business, retail, and Web3 utilities
    in everyday life.
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
      contributing: 4
      contextual: 3
      direct: 1
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

# Scaled Broker Platform for Crypto Adoption Using Google Cloud and AI

## Executive Summary

Bitazza Thailand: Scaled data infrastructure to support $4.6 billion in transactions.

## Key Findings

- **Scaled data infrastructure to support $4.6 billion in transactions** — verified (outcome)
  - Quote: "Functioning as a digital asset brokerage platform, its data team built and scaled its data infrastructure to drive $4.6B in transactions in 2024."

- **Accelerated financial statement creation by 75%** — verified (outcome)
  - Quote: "Accelerated financial statement creation by 75%, cutting the process from one year to three months"

- **Near-real-time regulatory compliance reporting** — needs_review (method)
  - Quote: "Bitazza Thailand must process near-real-time and submit accurate daily aggregated millions of transactions. The compliance and risk team uses Google Sheets and BigQuery to generate these trusted, near..."

- **Enabled data team to manage CI/CD without dedicated DevOps engineer** — verified (method)
  - Quote: "Empowers data team to build and run their own CI/CD pipelines, without a dedicated DevOps engineer"

- **Proactive fraud detection and risk mitigation** — needs_review (method)
  - Quote: "The team uses digital asset reports to proactively detect suspicious trading patterns or fraudulent activities and mitigate risk before it escalates."

- **Accelerated machine learning lifecycle with integrated notebooks** — verified (method)
  - Quote: "BigQuery Notebooks offer a familiar notebook interface, combining the power of BigQuery with the flexibility of Python libraries. This enables the team to rapidly create data models on their BigQuery ..."

- **Over 100,000 transactions under $0.01 on Freedom Wallet** — verified (outcome)
  - Quote: "To date, thousands of wallets have been created by end users, with more than 100 thousand transactions completed for under $0.01 on Fuse Network."

- **Thousands of wallets created by end users** — verified (adoption)
  - Quote: "To date, thousands of wallets have been created by end users, with more than 100 thousand transactions completed for under $0.01 on Fuse Network."

## Sources

- **S1**: https://cloud.google.com/customers/bitazza
- **S2**: https://www.fuse.io/casestudies/bitazza
- **S3**: https://blogth.bitazza.com/en/blog/what-are-centralized-crypto-trading-platforms
