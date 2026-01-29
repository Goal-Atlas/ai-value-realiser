---
case_id: air-france-klm-content-velocity-localization
organisation: Air France-KLM
title: Digital Content Management and Infrastructure Optimization
date_created: '2026-01-29'
date_updated: '2026-01-29'
sources:
- id: S1
  title: https://cmscritic.com/contentstack-selected-by-air-france-klm-to-support-composa...
  url: https://cmscritic.com/contentstack-selected-by-air-france-klm-to-support-composable-digital-experience-transformation
  raw_file: ''
  text_file: sources/text/S1.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S2
  title: https://www.atlassian.com/customers/air-france-klm
  url: https://www.atlassian.com/customers/air-france-klm
  raw_file: ''
  text_file: sources/text/S2.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S3
  title: https://blogs.opentext.com/air-france-klm-lifts-information-management-efficienc...
  url: https://blogs.opentext.com/air-france-klm-lifts-information-management-efficiency-to-new-heights/
  raw_file: ''
  text_file: sources/text/S3.txt
  extraction_method: unknown
  extraction_quality: high
  is_multi_page: false
  related_urls: []
value_claims:
- id: VC-001
  claim_title: Annual cost savings of $600,000 from cloud migration
  claim_description: Air France-KLM saved $600,000 per year by migrating from Atlassian
    Data Center (60 servers at $10,000/year each) to Atlassian Cloud Premium, eliminating
    server maintenance costs.
  source_ids:
  - S2
  source_quote: On Atlassian Data Center, Air France-KLM used 60 servers to run Jira
    and Confluence, each costing $10,000 per year to maintain. Migrating to Atlassian
    cloud immediately reduced annual costs by $600,000.
  quote_location: Impact section
  ai_attribution: contextual
  attribution_evidence: AI features mentioned as available only on cloud and part
    of decision rationale, but cost savings primarily from cloud infrastructure migration
    rather than AI directly.
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
    value: '600000'
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
  claim_title: Elimination of 48+ hours monthly downtime
  claim_description: Migration to Atlassian Cloud eliminated more than 48 hours of
    downtime per month previously required for maintenance and backups, including
    12-hour downtimes every three months for re-indexing.
  source_ids:
  - S2
  source_quote: Atlassian cloud has also eliminated days' worth of downtime previously
    required to maintain and run backups for Jira and Confluence Data Center. There
    were scenarios where we'd upgraded to a newer version, but then Jira would re-index,
    which created at least 12 hours of downtime every three months.
  quote_location: Impact section
  ai_attribution: contextual
  attribution_evidence: AI mentioned as cloud-only feature driving migration decision,
    but downtime elimination is primarily from cloud infrastructure benefits rather
    than AI functionality.
  verification_status: needs_review
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
  - velocity
  cognitive_depth: descriptive
  metric_raw:
    value: '48'
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
  claim_title: Daily productivity gains of up to 2,500 hours across organization
  claim_description: Individual time savings of 5-15 minutes per day per user, multiplied
    across 10,000 employees, results in up to 2,500 hours of productivity gains daily
    through improved platform flexibility and ease of use.
  source_ids:
  - S2
  source_quote: Even if these changes save each user 5-15 minutes a day, when multiplied
    by 10,000 people, that's a lot of productivity gains.
  quote_location: Impact section
  ai_attribution: contextual
  attribution_evidence: AI features cited as key cloud benefit, but productivity gains
    attributed to overall platform improvements including mobile apps, layout flexibility,
    and user experience enhancements.
  verification_status: needs_review
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - optimization
  - augmentation
  outcome:
  - velocity
  cognitive_depth: descriptive
  metric_raw:
    value: '2500'
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
  claim_title: Improved content velocity through composable DXP architecture
  claim_description: Contentstack's composable DXP enables Air France-KLM to deliver
    more consistent content across all touchpoints and markets with streamlined publishing
    processes for developers, content creators, and SEO specialists.
  source_ids:
  - S1
  source_quote: Migrating to Contentstack contributes to delivering more consistent
    content across all our touchpoints and all markets. At the same time, it enables
    us to integrate our existing tech stack and adapt quickly to the changing landscape.
  quote_location: Quote from Hugo Rousset, VP Digital Products & Services
  ai_attribution: contributing
  attribution_evidence: Composable DXP with API-first architecture enables agile content
    management and personalization, though not explicitly AI-powered, supports AI-driven
    personalization capabilities.
  verification_status: verified
  evidence_level: method
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - optimization
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
  claim_title: Enhanced personalized customer journey capabilities
  claim_description: Contentstack enables Air France-KLM to get ahead of customer
    needs by providing personalized user journeys across digital touchpoints, supporting
    seamless omnichannel experiences worldwide.
  source_ids:
  - S1
  source_quote: We needed a solution that allows us to get ahead of customer needs,
    providing them a personalized user journey.
  quote_location: Quote from Hugo Rousset, VP Digital Products & Services
  ai_attribution: contributing
  attribution_evidence: Personalization capabilities typically leverage AI/ML for
    customer behavior prediction and content recommendations, though specific AI implementation
    not detailed.
  verification_status: verified
  evidence_level: method
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - augmentation
  - optimization
  outcome:
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
- id: VC-006
  claim_title: Accelerated technology adaptation and agility
  claim_description: Composable architecture enables Air France-KLM to adapt quickly
    to changing customer needs and market conditions without compromising quality,
    supporting rapid and agile internal workflows.
  source_ids:
  - S1
  source_quote: By harvesting the power of composable, headless technology, Air France-KLM
    is now better equipped to adapt to change without having to compromise on quality.
    In partnership with Contentstack, they're able to continue delivering superior
    digital experiences while benefiting from rapid, agile, and reliable internal
    workflows.
  quote_location: Quote from Ramon Weterings, VP Sales EMEA at Contentstack
  ai_attribution: contextual
  attribution_evidence: Agility improvements stem from composable architecture rather
    than AI directly, though architecture enables AI integration and supports AI-driven
    capabilities.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
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
- id: VC-007
  claim_title: Improved talent attraction through modern AI-enabled tools
  claim_description: Access to latest features including AI capabilities on Atlassian
    Cloud makes Air France-KLM more attractive to new generation of employees who
    want to work with cutting-edge technology.
  source_ids:
  - S2
  source_quote: The new generation of potential employees want to work with the latest
    and greatest. Compared to Data Center, Jira and Confluence Cloud have features
    and functionalities, like AI, that make us an attractive workplace.
  quote_location: Quote from Jordy Essed, DevNet Team Product Owner
  ai_attribution: direct
  attribution_evidence: AI features explicitly cited as key differentiator for talent
    attraction, directly contributing to organizational capability to recruit top
    talent.
  verification_status: verified
  evidence_level: method
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - innovation
  outcome:
  - business_growth
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
- id: VC-008
  claim_title: Expanded platform adoption across 20+ business and technical teams
  claim_description: Migration to cloud with AI features drove organic adoption, with
    more non-developer users than developers now on platform, spanning teams from
    Flight Operations to HR to Security.
  source_ids:
  - S2
  source_quote: Other teams often come to us asking to upgrade to Atlassian cloud
    because they see how it could improve their life and deliver a better experience
    for the end user. Now, we have more non-developer users on the platform than developers.
  quote_location: Quote from Nathan Wattimena, Scrum Master
  ai_attribution: contributing
  attribution_evidence: AI features mentioned as driver for cloud migration that enabled
    broader adoption, contributing to but not solely responsible for platform expansion.
  verification_status: needs_review
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - augmentation
  outcome:
  - velocity
  cognitive_depth: descriptive
  metric_raw:
    value: '20'
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
  claim_title: Six-month migration timeline with rapid benefit realization
  claim_description: Complete migration to Atlassian Cloud Premium accomplished in
    only six months, with measurable benefits visible within a few months post-migration.
  source_ids:
  - S2
  source_quote: 'It''s amazing: The migration process took only six months, and we''re
    seeing benefits a few months later.'
  quote_location: Quote from Mohamed Haddadi, Manager of IT Operations
  ai_attribution: contextual
  attribution_evidence: AI features part of cloud platform benefits, but migration
    speed primarily attributed to cloud migration tools and partner support rather
    than AI directly.
  verification_status: needs_review
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
  - velocity
  cognitive_depth: descriptive
  metric_raw:
    value: '6'
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
context_claims:
- id: CC-001
  context_type: organisational
  claim_title: Air France-KLM is 100+ year old European airline group
  claim_description: KLM is the oldest airline in Europe, founded in early 1900s,
    later merged with Air France to form Air France-KLM group.
  source_ids:
  - S2
  source_quote: 'Over 100 years later, the company holds two impressive titles: the
    oldest airline in Europe and a leader in the competitive, fast-changing aviation
    industry.'
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
  claim_title: Aviation industry sector
  claim_description: 'Air France-KLM operates in the aviation industry with three
    core enterprises: passenger travel, cargo, and engineering and maintenance.'
  source_ids:
  - S2
  source_quote: 'When KLM merged with Air France to become Air France-KLM, the two
    aviation leaders came together to provide the best service in the industry for
    three core enterprises: passenger travel, cargo, and engineering and maintenance.'
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
  context_type: strategic_intent
  claim_title: Digital transformation and composable architecture strategy
  claim_description: Air France-KLM pursuing composable digital experience transformation
    to provide seamless omnichannel customer experiences worldwide.
  source_ids:
  - S1
  source_quote: 'Air France-KLM to support its new digital transformation initiative:
    a composable solution that aims to provide seamless and curated omnichannel experiences
    to its customers worldwide.'
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
  claim_title: Cloud-first organizational strategy
  claim_description: Air France-KLM making organizational shift to cloud technology
    across the enterprise.
  source_ids:
  - S2
  source_quote: At the same time, Air France-KLM was making an organizational shift
    to cloud technology.
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
  claim_title: 10,000+ employees using collaboration platform
  claim_description: Air France-KLM has approximately 10,000 employees using Atlassian
    collaboration tools.
  source_ids:
  - S2
  source_quote: Even if these changes save each user 5-15 minutes a day, when multiplied
    by 10,000 people, that's a lot of productivity gains.
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
  context_type: temporal
  claim_title: Atlassian tools adoption began in late 1990s/early 2000s
  claim_description: Air France-KLM began using Jira for issue tracking and Confluence
    for IT knowledge management in the late 90s and early 2000s.
  source_ids:
  - S2
  source_quote: Air France-KLM's investment in collaborative, efficient technology
    began in the late 90s and early 2000s, with Jira for issue tracking and Confluence
    for IT knowledge management.
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
  claim_title: Agile and DevOps adoption in 2010s
  claim_description: Air France-KLM began adopting agile and DevOps practices in the
    2010s, expanding use of Atlassian tools.
  source_ids:
  - S2
  source_quote: When the airline began adopting more modern practices in the 2010s,
    including agile and DevOps, teams expanded their use of Atlassian tools to support
    their work.
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
  claim_title: Marketing and customer experience management
  claim_description: Air France-KLM implementing composable DXP for consumer websites
    and digital touchpoints to deliver personalized customer experiences.
  source_ids:
  - S1
  source_quote: Contentstack is being implemented to integrate with Air France-KLM's
    consumer websites, powering the next generation of digital experiences, with additional
    websites to follow later this year.
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
- id: CC-009
  context_type: functional
  claim_title: IT operations and infrastructure management
  claim_description: Air France-KLM managing enterprise collaboration tools, CI/CD
    pipelines, and cloud infrastructure through DevNet team.
  source_ids:
  - S2
  source_quote: DevNet team, which manages the company's Atlassian toolstack and continuous
    improvement/continuous delivery (CI/CD) pipeline.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10.0'
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
- id: CC-010
  context_type: functional
  claim_title: Content creation and digital publishing
  claim_description: Air France-KLM has content creators, SEO specialists, and e-commerce
    developers managing multi-market digital content.
  source_ids:
  - S1
  source_quote: Contentstack will be part of a composable digital strategy that empowers
    Air France-KLM to create seamless and personalized customer journeys, with streamlined
    publishing processes for e-commerce developers, content creators, and SEO specialists.
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
- id: CC-011
  context_type: organisational
  claim_title: Culture of innovation and industry leadership
  claim_description: Air France-KLM positions itself as innovation leader, first to
    implement aviation advancements from sustainable biofuels to VR headsets.
  source_ids:
  - S2
  source_quote: Over the years, Air France-KLM has been among the first to implement
    countless aviation advancements, from the latest sustainable biofuels and aircrafts
    like the Dreamliner, to cutting-edge operational tools and in-flight entertainment
    like personal virtual reality headsets.
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
  claim_title: Global omnichannel customer touchpoints
  claim_description: Air France-KLM operates multiple digital and physical customer
    touchpoints across global markets including websites, mobile, and in-flight experiences.
  source_ids:
  - S1
  source_quote: Whether it's onboard our aircraft or on our digital touchpoints, we
    aim to offer unique experiences to our customers.
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
- id: CC-013
  context_type: organisational
  claim_title: GDPR compliance requirements
  claim_description: Air France-KLM must comply with strict GDPR regulations, influencing
    technology platform selection.
  source_ids:
  - S2
  source_quote: The team also appreciated that working on the Atlassian cloud platform
    would ensure compliance with strict GDPR regulations.
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
  context_type: temporal
  claim_title: Cloud migration completed in 2023-2024 timeframe
  claim_description: Atlassian Cloud migration completed in six months with benefits
    visible shortly after, based on recent case study publication.
  source_ids:
  - S2
  source_quote: 'It''s amazing: The migration process took only six months, and we''re
    seeing benefits a few months later.'
  verification_status: inferred
  verification_confidence: medium
  inferred_from: Case study publication timing and migration completion references
    suggest 2023-2024 timeframe
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
    total: 9
    verified: 5
    needs_review: 4
    rejected: 0
    by_attribution:
      contextual: 5
      contributing: 3
      direct: 1
  context_claims:
    total: 14
    verified: 11
    unverified: 2
    inferred: 1
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

# Digital Content Management and Infrastructure Optimization

## Executive Summary

Air France-KLM: Annual cost savings of $600,000 from cloud migration.

## Key Findings

- **Annual cost savings of $600,000 from cloud migration** — verified (outcome)
  - Quote: "On Atlassian Data Center, Air France-KLM used 60 servers to run Jira and Confluence, each costing $10,000 per year to maintain. Migrating to Atlassian cloud immediately reduced annual costs by $600,00..."

- **Elimination of 48+ hours monthly downtime** — needs_review (outcome)
  - Quote: "Atlassian cloud has also eliminated days' worth of downtime previously required to maintain and run backups for Jira and Confluence Data Center. There were scenarios where we'd upgraded to a newer ver..."

- **Daily productivity gains of up to 2,500 hours across organization** — needs_review (outcome)
  - Quote: "Even if these changes save each user 5-15 minutes a day, when multiplied by 10,000 people, that's a lot of productivity gains."

- **Improved content velocity through composable DXP architecture** — verified (method)
  - Quote: "Migrating to Contentstack contributes to delivering more consistent content across all our touchpoints and all markets. At the same time, it enables us to integrate our existing tech stack and adapt q..."

- **Enhanced personalized customer journey capabilities** — verified (method)
  - Quote: "We needed a solution that allows us to get ahead of customer needs, providing them a personalized user journey."

- **Accelerated technology adaptation and agility** — verified (method)
  - Quote: "By harvesting the power of composable, headless technology, Air France-KLM is now better equipped to adapt to change without having to compromise on quality. In partnership with Contentstack, they're ..."

- **Improved talent attraction through modern AI-enabled tools** — verified (method)
  - Quote: "The new generation of potential employees want to work with the latest and greatest. Compared to Data Center, Jira and Confluence Cloud have features and functionalities, like AI, that make us an attr..."

- **Expanded platform adoption across 20+ business and technical teams** — needs_review (adoption)
  - Quote: "Other teams often come to us asking to upgrade to Atlassian cloud because they see how it could improve their life and deliver a better experience for the end user. Now, we have more non-developer use..."

- **Six-month migration timeline with rapid benefit realization** — needs_review (outcome)
  - Quote: "It's amazing: The migration process took only six months, and we're seeing benefits a few months later."

## Sources

- **S1**: https://cmscritic.com/contentstack-selected-by-air-france-klm-to-support-composable-digital-experience-transformation
- **S2**: https://www.atlassian.com/customers/air-france-klm
- **S3**: https://blogs.opentext.com/air-france-klm-lifts-information-management-efficiency-to-new-heights/
