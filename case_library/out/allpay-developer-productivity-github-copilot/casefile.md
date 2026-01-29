---
case_id: allpay-developer-productivity-github-copilot
organisation: allpay
title: Developer Productivity with GitHub Copilot
date_created: '2026-01-29'
date_updated: '2026-01-29'
sources:
- id: S1
  title: https://www.allpay.net/news/allpay-boosts-productivity-by-10-with-github-copilot...
  url: https://www.allpay.net/news/allpay-boosts-productivity-by-10-with-github-copilot-a-case-study-with-microsoft/
  raw_file: ''
  text_file: sources/text/S1.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S2
  title: https://www.pymnts.com/artificial-intelligence-2/2025/allpay-says-ai-transformat...
  url: https://www.pymnts.com/artificial-intelligence-2/2025/allpay-says-ai-transformation-boosts-productivity-software-releases/
  raw_file: ''
  text_file: sources/text/S2.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S3
  title: https://blogs.microsoft.com/blog/2025/04/22/https-blogs-microsoft-com-blog-2024-...
  url: https://blogs.microsoft.com/blog/2025/04/22/https-blogs-microsoft-com-blog-2024-11-12-how-real-world-businesses-are-transforming-with-ai/
  raw_file: ''
  text_file: sources/text/S3.txt
  extraction_method: unknown
  extraction_quality: high
  is_multi_page: false
  related_urls: []
value_claims:
- id: VC-001
  claim_title: 10% increase in overall developer productivity
  claim_description: allpay estimates that the team's use of GitHub Copilot has increased
    developer productivity by 10% overall across development activities.
  source_ids:
  - S1
  source_quote: allpay estimates that, overall, the team's use of GitHub Copilot has
    increased developer productivity by 10%.
  quote_location: Mid-document, section 'Different, faster ways to solve problems'
  ai_attribution: direct
  attribution_evidence: The productivity increase is explicitly attributed to the
    team's use of GitHub Copilot, with no other contributing factors mentioned for
    this specific metric.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - augmentation
  - automation
  outcome:
  - velocity
  cognitive_depth: generative
  metric_raw:
    value: '10'
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
  claim_title: 80% time saving in specific use cases
  claim_description: For certain development tasks like creating stored procedures,
    GitHub Copilot delivers up to 80% time savings, reducing task time from one hour
    to five minutes.
  source_ids:
  - S1
  source_quote: I could have a set of stored procedures created now in five minutes,
    whereas it might have taken someone an hour to write stored procedures previously
  quote_location: Mid-document, section 'Different, faster ways to solve problems'
  ai_attribution: direct
  attribution_evidence: The time saving is directly attributed to GitHub Copilot's
    ability to generate stored procedures, with specific before/after comparison provided.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - velocity
  cognitive_depth: generative
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
- id: VC-003
  claim_title: Service setup time reduced from one week to one day
  claim_description: GitHub Copilot enables developers to set up a depth of service
    in one day, compared to the week it previously required, representing an 85% time
    reduction.
  source_ids:
  - S1
  source_quote: And we can have a depth of service set up in a day, rather than the
    week it took before.
  quote_location: Mid-document, section 'Different, faster ways to solve problems'
  ai_attribution: direct
  attribution_evidence: The reduction in service setup time is directly attributed
    to GitHub Copilot usage, mentioned immediately after stored procedure example.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  - augmentation
  outcome:
  - velocity
  cognitive_depth: generative
  metric_raw:
    value: '85'
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
  claim_title: 25% increase in delivery volume to production
  claim_description: In combination with organizational changes, GitHub Copilot adoption
    has driven up delivery volume into production by 25%, with more releases in 9
    months than in the entire previous year.
  source_ids:
  - S1
  source_quote: In combination with some organisational changes, the adoption of GitHub
    Copilot has driven up delivery volume into production by 25%.
  quote_location: Mid-document, section 'Different, faster ways to solve problems'
  ai_attribution: contributing
  attribution_evidence: The source explicitly states the increase is 'in combination
    with some organisational changes', indicating GitHub Copilot is a contributing
    but not sole factor.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - augmentation
  - automation
  outcome:
  - velocity
  cognitive_depth: generative
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
- id: VC-005
  claim_title: Improved code quality and reduced defects
  claim_description: GitHub Copilot has helped raise the quality of code, testing,
    and applications, with reduced time spent on rework and defect fixing, and fewer
    incidents reported.
  source_ids:
  - S1
  source_quote: At the same time as getting codes out the door faster, GitHub Copilot
    is helping us to raise the quality of code, testing, and applications. The amount
    of time we are spending on rework and defect fixing has dropped. We're getting
    fewer incidents.
  quote_location: Section 'Driving up quality'
  ai_attribution: direct
  attribution_evidence: The IT Director directly attributes improvements in code quality,
    reduced rework time, and fewer incidents to GitHub Copilot usage.
  verification_status: needs_review
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - augmentation
  - optimization
  outcome:
  - velocity
  - cost_reduction
  cognitive_depth: generative
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
  claim_title: Enhanced code coverage through improved unit testing
  claim_description: GitHub Copilot has improved code coverage and test quality by
    generating unit tests with full solution context, addressing a task developers
    typically dislike.
  source_ids:
  - S1
  source_quote: Using GitHub Copilot has definitely improved our code coverage and
    the quality of our tests. Because Copilot has the context of the solution, it
    is able to generate the tests and suggest different tests and different things
    to test.
  quote_location: Section 'Driving up quality'
  ai_attribution: direct
  attribution_evidence: The improvement in code coverage and test quality is directly
    attributed to GitHub Copilot's ability to generate contextual unit tests.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
  - augmentation
  outcome:
  - velocity
  cognitive_depth: generative
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
  claim_title: Accelerated junior developer onboarding and confidence
  claim_description: GitHub Copilot provides immediate answers to junior developers,
    functioning like pair programming, reducing time stuck on problems and increasing
    confidence in code quality.
  source_ids:
  - S1
  source_quote: Whereas previously people would have got stuck or had to go find help
    by asking another developer or an online search, now we just ask GitHub Copilot.
    It gives our junior developers the confidence that their codes are going to work.
  quote_location: Section 'Support for junior team members'
  ai_attribution: direct
  attribution_evidence: The acceleration and confidence building for junior developers
    is directly attributed to GitHub Copilot's immediate assistance capabilities.
  verification_status: needs_review
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - augmentation
  outcome:
  - velocity
  - experience
  cognitive_depth: generative
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
  claim_title: Improved legacy code comprehension efficiency
  claim_description: GitHub Copilot helps developers understand legacy code more efficiently,
    especially when original authors have moved on, by explaining code functionality
    on demand.
  source_ids:
  - S1
  source_quote: Copilot helps people touching legacy code understand it better, especially
    when the people who originally wrote the code have moved on. You can get GitHub
    Copilot to explain the legacy code to you. It's definitely increased efficiency
    that way.
  quote_location: Section 'Making sense of legacy code'
  ai_attribution: direct
  attribution_evidence: The efficiency increase in understanding legacy code is directly
    attributed to GitHub Copilot's code explanation capabilities.
  verification_status: needs_review
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - augmentation
  outcome:
  - velocity
  cognitive_depth: generative
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
  claim_title: Faster debugging and problem resolution
  claim_description: GitHub Copilot makes debugging more digestible and understandable,
    providing near-instant solutions instead of requiring a full day of debugging
    and investigation.
  source_ids:
  - S1
  source_quote: Rather than spending a whole day debugging and figuring things out,
    Copilot makes it more digestible and understandable, so the solution is pretty
    instant.
  quote_location: Section 'Making sense of legacy code'
  ai_attribution: direct
  attribution_evidence: The reduction in debugging time from a full day to near-instant
    is directly attributed to GitHub Copilot's problem-solving assistance.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
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
- id: VC-010
  claim_title: Increased frequency of code reviews
  claim_description: GitHub Copilot frees up developer time, enabling more frequent
    code reviews that ensure standardization and significantly improve code quality.
  source_ids:
  - S1
  source_quote: GitHub Copilot frees up time for frequent code reviews, ensuring standardisation
    and significantly improving code quality.
  quote_location: Section 'Driving up quality', attributed to Adrian Michalowski
  ai_attribution: direct
  attribution_evidence: The increase in code review frequency is directly attributed
    to time freed up by GitHub Copilot, which then enables quality improvements.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
  - velocity
  cognitive_depth: generative
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
- id: VC-011
  claim_title: Developer time redirected to innovation and quality improvement
  claim_description: Productivity gains from GitHub Copilot enable developers to focus
    on innovation, including building new AI-powered solutions for PR review and quality
    checking.
  source_ids:
  - S1
  source_quote: allpay is using the time returned to the business through the productivity
    gains made by the developer's use of GitHub Copilot to drive additional quality
    improvement and innovation. We've built a new solution using Azure AI Services
    that reviews the pull requests.
  quote_location: Section 'Developer time is redirected to innovation'
  ai_attribution: direct
  attribution_evidence: The freed-up time for innovation is directly attributed to
    productivity gains from GitHub Copilot, enabling creation of additional AI solutions.
  verification_status: needs_review
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_creation
  mechanism:
  - innovation
  outcome:
  - velocity
  - business_growth
  cognitive_depth: generative
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
- id: VC-012
  claim_title: Improved cross-team consistency and standardization
  claim_description: Time savings from GitHub Copilot enable horizontal work across
    12-14 squads to ensure consistency and best practice implementation.
  source_ids:
  - S1
  source_quote: Consistency across 12 or 14 squads is really hard to manage. We actually
    have time now to work horizontally across the teams to ensure consistency and
    best practice.
  quote_location: Section 'Developer time is redirected to innovation'
  ai_attribution: direct
  attribution_evidence: The ability to work on consistency across teams is directly
    attributed to time freed up by GitHub Copilot productivity gains.
  verification_status: needs_review
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
  - velocity
  cognitive_depth: generative
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
  claim_title: allpay is a UK-based payment system provider
  claim_description: allpay has been at the forefront of payment system innovation
    since its founding in 1994, operating as a financial services provider.
  source_ids:
  - S1
  source_quote: allpay has been at the forefront of payment system innovation since
    its founding in 1994. As a financial services provider, compliance, security,
    and data governance were key considerations
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
- id: CC-002
  context_type: temporal
  claim_title: Cloud migration initiated in 2019
  claim_description: By 2019, allpay recognized its existing IT infrastructure would
    not support future growth and began planning migration to Microsoft Azure.
  source_ids:
  - S1
  source_quote: By 2019, the team recognised that its existing IT infrastructure would
    not support future growth plans. Seizing this opportunity for modernisation, the
    IT team began planning a migration from its existing on-premises and colocation
    setup to Microsoft Azure.
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
  claim_title: Financial services sector with regulatory requirements
  claim_description: allpay operates as a regulated financial services organization
    with strict compliance, security, and data governance requirements.
  source_ids:
  - S1
  source_quote: As a financial services provider, compliance, security, and data governance
    were key considerations when choosing Azure. We are a regulated organisation
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
  claim_title: Twin-track cloud migration strategy
  claim_description: 'allpay implemented a twin-track approach: greenfield cloud-native
    development in Azure while preparing to migrate existing application stack.'
  source_ids:
  - S1
  source_quote: We planned a twin-track cloud migration. We initiated greenfield cloud-native
    development in Azure while preparing to migrate our existing application stack
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
  context_type: scale
  claim_title: Development organization with 12-14 squads
  claim_description: allpay's development organization consists of 12 to 14 squads
    working across multiple projects.
  source_ids:
  - S1
  source_quote: Consistency across 12 or 14 squads is really hard to manage
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
  claim_title: Software development and engineering function
  claim_description: The GitHub Copilot implementation is within allpay's software
    development and engineering function, involving coding, testing, and application
    delivery.
  source_ids:
  - S1
  source_quote: GitHub Copilot is an AI coding assistant that helps engineers and
    developers to write code faster and with less effort
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10961'
  apqc_name: Develop and Manage Products and Services
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
  context_type: strategic_intent
  claim_title: Elimination of shadow AI usage
  claim_description: allpay adopted GitHub Copilot partly to eliminate shadow AI usage
    (like ChatGPT) and ensure data protection within Microsoft tenancy.
  source_ids:
  - S1
  source_quote: People were beginning to explore ChatGPT and we wanted to ensure that
    we eliminated such shadow AI. It made sense for us to move towards Copilot because
    the data is then protected within our existing Microsoft tenancy.
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
  context_type: products_services
  claim_title: Microsoft Azure technology stack
  claim_description: allpay uses a comprehensive Microsoft technology stack including
    Azure, Power Platform, Azure Data Factory, Azure Data Explorer, Azure OpenAI,
    and GitHub Copilot.
  source_ids:
  - S1
  source_quote: Our Microsoft stack gives us options beyond simply looking to code
    our way out of a problem. We can use Power Platform for some of our automations.
    We can use the data warehouse technologies like Azure Data Factory and Azure Data
    Explorer.
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
- id: CC-009
  context_type: temporal
  claim_title: GitHub Copilot adoption timeframe
  claim_description: The case study references results from nine months of GitHub
    Copilot usage, comparing to the previous full year baseline.
  source_ids:
  - S1
  source_quote: In terms of releases out the door, in the nine months of this year
    to date, we have already delivered more than the 900 delivered in the whole of
    last year.
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
  context_type: organisational
  claim_title: UK data residency requirement
  claim_description: UK data residency was an important factor in allpay's choice
    of Azure for cloud migration.
  source_ids:
  - S1
  source_quote: The benefits of UK data residency, Azure's extensive tooling, and
    seamless integration with Microsoft toolsets were also important factors.
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
    total: 12
    verified: 7
    needs_review: 5
    rejected: 0
    by_attribution:
      direct: 11
      contributing: 1
  context_claims:
    total: 10
    verified: 5
    unverified: 5
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

# Developer Productivity with GitHub Copilot

## Executive Summary

allpay: 10% increase in overall developer productivity.

## Key Findings

- **10% increase in overall developer productivity** — verified (outcome)
  - Quote: "allpay estimates that, overall, the team's use of GitHub Copilot has increased developer productivity by 10%."

- **80% time saving in specific use cases** — verified (outcome)
  - Quote: "I could have a set of stored procedures created now in five minutes, whereas it might have taken someone an hour to write stored procedures previously"

- **Service setup time reduced from one week to one day** — verified (outcome)
  - Quote: "And we can have a depth of service set up in a day, rather than the week it took before."

- **25% increase in delivery volume to production** — verified (outcome)
  - Quote: "In combination with some organisational changes, the adoption of GitHub Copilot has driven up delivery volume into production by 25%."

- **Improved code quality and reduced defects** — needs_review (method)
  - Quote: "At the same time as getting codes out the door faster, GitHub Copilot is helping us to raise the quality of code, testing, and applications. The amount of time we are spending on rework and defect fix..."

- **Enhanced code coverage through improved unit testing** — verified (method)
  - Quote: "Using GitHub Copilot has definitely improved our code coverage and the quality of our tests. Because Copilot has the context of the solution, it is able to generate the tests and suggest different tes..."

- **Accelerated junior developer onboarding and confidence** — needs_review (method)
  - Quote: "Whereas previously people would have got stuck or had to go find help by asking another developer or an online search, now we just ask GitHub Copilot. It gives our junior developers the confidence tha..."

- **Improved legacy code comprehension efficiency** — needs_review (method)
  - Quote: "Copilot helps people touching legacy code understand it better, especially when the people who originally wrote the code have moved on. You can get GitHub Copilot to explain the legacy code to you. It..."

- **Faster debugging and problem resolution** — verified (method)
  - Quote: "Rather than spending a whole day debugging and figuring things out, Copilot makes it more digestible and understandable, so the solution is pretty instant."

- **Increased frequency of code reviews** — verified (method)
  - Quote: "GitHub Copilot frees up time for frequent code reviews, ensuring standardisation and significantly improving code quality."

- **Developer time redirected to innovation and quality improvement** — needs_review (method)
  - Quote: "allpay is using the time returned to the business through the productivity gains made by the developer's use of GitHub Copilot to drive additional quality improvement and innovation. We've built a new..."

- **Improved cross-team consistency and standardization** — needs_review (method)
  - Quote: "Consistency across 12 or 14 squads is really hard to manage. We actually have time now to work horizontally across the teams to ensure consistency and best practice."

## Sources

- **S1**: https://www.allpay.net/news/allpay-boosts-productivity-by-10-with-github-copilot-a-case-study-with-microsoft/
- **S2**: https://www.pymnts.com/artificial-intelligence-2/2025/allpay-says-ai-transformation-boosts-productivity-software-releases/
- **S3**: https://blogs.microsoft.com/blog/2025/04/22/https-blogs-microsoft-com-blog-2024-11-12-how-real-world-businesses-are-transforming-with-ai/
