---
case_id: johnson-controls-automates-invoice-processing
organisation: Johnson Controls
title: Invoice Processing Automation
date_created: '2026-01-29'
date_updated: '2026-01-29'
sources:
- id: S1
  title: https://indicodata.ai/blog/johnson-controls-unlocks-its-unstructured-data-with-i...
  url: https://indicodata.ai/blog/johnson-controls-unlocks-its-unstructured-data-with-intelligent-document-processing/
  raw_file: ''
  text_file: sources/text/S1.txt
  extraction_method: unknown
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S2
  title: https://debtregister.com/johnson-controls-case-study-streamlining-global-receiva...
  url: https://debtregister.com/johnson-controls-case-study-streamlining-global-receivables-for-a-fortune-500-industry-leader/
  raw_file: ''
  text_file: sources/text/S2.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S3
  title: https://www.microsoft.com/en-us/power-platform/blog/power-apps/johnson-controls-...
  url: https://www.microsoft.com/en-us/power-platform/blog/power-apps/johnson-controls-simplifies-their-infrastructure-saving-3610-hours-on-training-enablement/
  raw_file: ''
  text_file: sources/text/S3.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
value_claims:
- id: VC-001
  claim_title: Collection rate increased from 20% to 27% with Debt Register platform
  claim_description: Johnson Controls improved its accounts receivable collection
    rate by 7 percentage points (from 20% to 27%) after implementing the Debt Register
    cloud-based AR platform, resulting in $1.8M in annual savings.
  source_ids:
  - S2
  source_quote: 'Before Debt Register: 20% collection rate, costing $3.6M annually.
    With Debt Register: collection rate increased to 27%, saving $1.8M annually'
  quote_location: The Results section
  ai_attribution: contributing
  attribution_evidence: The platform uses automated alerts, real-time engagement tracking,
    and analytics to support collections, but human credit teams still drive payment
    outcomes.
  verification_status: needs_review
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  - optimization
  outcome:
  - cost_reduction
  - velocity
  cognitive_depth: descriptive
  metric_raw:
    value: '27'
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
  claim_title: Combined collection approach increased total collections by $17M
  claim_description: Using Debt Register platform combined with debt collection agencies
    (DCAs), Johnson Controls raised its total collection rate to 36%, resulting in
    $17M in increased overall collections.
  source_ids:
  - S2
  source_quote: 'Combined (Debt Register + DCAs): total collection rate rose to 36%,
    increasing overall collections by $17M'
  quote_location: The Results section
  ai_attribution: contributing
  attribution_evidence: The Debt Register platform contributes to the combined approach
    through automation and engagement tracking, but works alongside DCAs and human
    teams.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  - optimization
  outcome:
  - revenue_lift
  - business_growth
  cognitive_depth: descriptive
  metric_raw:
    value: '17'
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
  claim_title: Training management automation saved 3,610 hours annually
  claim_description: Johnson Controls reduced training backend process management
    time from 4,870 hours to 1,260 hours annually (saving 3,610 hours) by implementing
    COBALT system built on Microsoft Power Platform.
  source_ids:
  - S3
  source_quote: From better NPS ratings, scheduling, to roster completion lag – what
    previously required 4,870 hours was reduced to 1,160 hours, allowing employees
    to focus on more strategic tasks.
  quote_location: Main content section
  ai_attribution: direct
  attribution_evidence: Power Apps and Power Automate directly automated manual data
    collection, scheduling, tracking, and survey processes that previously required
    manual intervention.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - velocity
  - cost_reduction
  cognitive_depth: descriptive
  metric_raw:
    value: '3610'
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
  claim_title: Training throughput increased by 400%
  claim_description: Johnson Controls increased training throughput by 400% after
    implementing the COBALT system built on Power Platform, enabling them to handle
    over 60 training events per month.
  source_ids:
  - S3
  source_quote: They saved 3,610 hours on backend process management and increased
    training throughput by 400%.
  quote_location: Introduction section
  ai_attribution: direct
  attribution_evidence: The Power Platform automation directly enabled the scaling
    of training operations by eliminating manual processes and standardizing workflows.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  - optimization
  outcome:
  - velocity
  - business_growth
  cognitive_depth: descriptive
  metric_raw:
    value: '400'
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
  claim_title: Real-time engagement tracking improves follow-up precision
  claim_description: Debt Register platform provides real-time tracking of email opens
    and reads, enabling Johnson Controls credit teams to improve follow-up precision
    and prioritization in AR collections.
  source_ids:
  - S2
  source_quote: Real-time engagement tracking (email opens/reads) to improve follow-up
    precision
  quote_location: Our Solution section
  ai_attribution: direct
  attribution_evidence: The platform directly provides automated tracking capabilities
    that were not previously available, enabling data-driven follow-up decisions.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_creation
  mechanism:
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
- id: VC-006
  claim_title: Automated alerts boost customer responsiveness in collections
  claim_description: Debt Register platform uses automated alerts highlighting potential
    credit-rating impact, which boosts customer responsiveness to payment requests
    and improves collection outcomes.
  source_ids:
  - S2
  source_quote: Automated alerts highlighting potential credit-rating impact, boosting
    responsiveness
  quote_location: Our Solution section
  ai_attribution: direct
  attribution_evidence: The platform directly generates automated alerts that influence
    customer behavior, a capability that did not exist in the previous manual process.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_creation
  mechanism:
  - automation
  outcome:
  - velocity
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
  claim_title: Centralized dashboard enables accurate tracking of training metrics
  claim_description: Power BI integration in COBALT system provides Johnson Controls
    with a central dashboard to track completion rates, drop rates, and NPS with accuracy
    and efficiency, improving training program management.
  source_ids:
  - S3
  source_quote: Additionally, having integrated Power BI they now also have a central
    dashboard to track completion rates, drop rates, and NPS (Net Promoter Score)
    with accuracy and efficiency.
  quote_location: Main content section
  ai_attribution: direct
  attribution_evidence: Power BI directly provides analytics and visualization capabilities
    that consolidate previously scattered data into actionable insights.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_creation
  mechanism:
  - augmentation
  outcome:
  - experience
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
- id: VC-008
  claim_title: Bulk upload capability reduces manual AR work
  claim_description: Debt Register's cloud-based platform supports bulk uploads of
    account data, saving time and reducing manual work for Johnson Controls' high-volume
    AR operations processing 100,000 invoices monthly.
  source_ids:
  - S2
  source_quote: Cloud-based platform supporting bulk uploads to save time and reduce
    manual work
  quote_location: Our Solution section
  ai_attribution: direct
  attribution_evidence: The platform directly automates data upload processes that
    previously required manual entry, eliminating repetitive manual tasks.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - velocity
  - cost_reduction
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
context_claims:
- id: CC-001
  context_type: organisational
  claim_title: Johnson Controls is a Fortune 500 company with $25B+ annual revenue
  claim_description: Johnson Controls is a Fortune 500 leader in building technology
    with more than $25 billion in annual revenue, delivering solutions across HVAC,
    fire protection, security, and sustainability.
  source_ids:
  - S2
  source_quote: Johnson Controls is a Fortune 500 leader in building technology with
    more than $25B in annual revenue.
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
  claim_title: Johnson Controls operates in 150+ countries with 100,000 employees
  claim_description: Johnson Controls has operations in more than 150 countries and
    approximately 100,000 employees requiring training and operational support.
  source_ids:
  - S2
  - S3
  source_quote: With operations in 150+ countries and approximately 100,000 invoices
    processed each month
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
  claim_title: Johnson Controls processes 100,000 invoices monthly
  claim_description: Johnson Controls runs accounts receivable at massive scale, processing
    approximately 100,000 invoices each month across B2B and B2C customers.
  source_ids:
  - S2
  source_quote: approximately 100,000 invoices processed each month, Johnson Controls
    runs AR at massive scale
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
  context_type: sectoral
  claim_title: Johnson Controls operates in building technology sector
  claim_description: Johnson Controls is a world leader in building smart, healthy
    and sustainable buildings, delivering solutions across HVAC, fire protection,
    security, and sustainability.
  source_ids:
  - S2
  - S3
  source_quote: Johnson Controls is a Fortune 500 leader in building technology with
    more than $25B in annual revenue. It delivers solutions across HVAC, fire protection,
    security, and sustainability
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
  claim_title: AR collections and credit management function
  claim_description: Johnson Controls operates accounts receivable collections and
    credit management functions to improve cash flow and accelerate payment timelines
    across global operations.
  source_ids:
  - S2
  source_quote: Johnson Controls wanted to strengthen its credit and collections operation
    to improve cash flow and accelerate payment timelines.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10404'
  apqc_name: Manage accounts receivable (AR)
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
  claim_title: Employee training and development function
  claim_description: Johnson Controls operates a large-scale training and quality
    assurance function managing over 60 training events per month for 100,000+ employees.
  source_ids:
  - S3
  source_quote: Johnson Controls, a world leader in building smart, healthy and sustainable
    buildings, has more than 100,000 employees that require training which needs to
    be scheduled, tracked, measured, and analyzed.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10247'
  apqc_name: Develop and train employees
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
  claim_title: Goal to improve cash flow and reduce overdue invoices
  claim_description: Johnson Controls aimed to strengthen credit and collections operations
    to improve cash flow, accelerate payment timelines, and reduce overdue invoices
    across its global AR portfolio.
  source_ids:
  - S2
  source_quote: 'Johnson Controls wanted to strengthen its credit and collections
    operation to improve cash flow and accelerate payment timelines. Key goals included:
    Reducing overdue invoices and improving accounts receivable (AR) collections'
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
  context_type: strategic_intent
  claim_title: Need for scalable global solution with system integration
  claim_description: Johnson Controls required a solution that could scale globally
    across 150+ countries and integrate cleanly with existing systems to support high-volume
    operations.
  source_ids:
  - S2
  source_quote: Ensuring the solution could scale globally and integrate cleanly with
    existing systems
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
  claim_title: Pre-implementation AR challenges with manual processes
  claim_description: Before implementing Debt Register, Johnson Controls faced AR
    friction including unresponsive customers, limited visibility into message delivery,
    high account volume complexity, and manual record updates causing delays.
  source_ids:
  - S2
  source_quote: 'Before Debt Register, the team faced common AR friction points that
    slowed collections: Customers often didn''t respond to traditional collection
    letters and email follow-ups; Limited visibility into whether messages reached
    the right contact'
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
  claim_title: Pre-implementation training challenges with no aggregation mechanism
  claim_description: Before COBALT implementation, Johnson Controls had no mechanism
    to share or aggregate training information, relied on manual intervention, and
    experienced low NPS scores around training programs.
  source_ids:
  - S3
  source_quote: There was no mechanism in place to share or aggregate information
    within systems or received from trainees. Manual intervention was the default
    reaction. This also had a direct impact on low NPS (Net Promoter Score) around
    training.
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
- id: CC-011
  context_type: products_services
  claim_title: COBALT training management system built on Microsoft Power Platform
  claim_description: Johnson Controls developed COBALT (Central Ops Buildings Administered
    Learning Tracker), an end-to-end system to deploy and track training, built using
    Power Apps, Power Automate, Power BI, and integrated with SharePoint and Teams.
  source_ids:
  - S3
  source_quote: Cody started utilizing Power Apps and Power Automate to create COBALT
    (Central Ops Buildings Administered Learning Tracker), an end-to-end system to
    deploy and track training.
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
  claim_title: Debt Register cloud-based AR collections platform
  claim_description: Johnson Controls implemented Debt Register, a cloud-based accounts
    receivable platform with bulk upload, real-time engagement tracking, automated
    alerts, and reporting analytics capabilities.
  source_ids:
  - S2
  source_quote: 'Debt Register helped Johnson Controls modernize AR outreach and improve
    collections performance with a scalable workflow: Cloud-based platform supporting
    bulk uploads; Real-time engagement tracking; Automated alerts'
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
  context_type: scale
  claim_title: Training operations handle 60+ events per month
  claim_description: After implementing COBALT, Johnson Controls training operations
    can handle over 60 training events per month with standardized processes and centralized
    data management.
  source_ids:
  - S3
  source_quote: COBALT now allows Johnson Controls to handle over 60 training events
    per month.
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
    verified: 7
    needs_review: 1
    rejected: 0
    by_attribution:
      contributing: 2
      direct: 6
  context_claims:
    total: 13
    verified: 9
    unverified: 4
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

# Invoice Processing Automation

## Executive Summary

Johnson Controls: Collection rate increased from 20% to 27% with Debt Register platform.

## Key Findings

- **Collection rate increased from 20% to 27% with Debt Register platform** — needs_review (outcome)
  - Quote: "Before Debt Register: 20% collection rate, costing $3.6M annually. With Debt Register: collection rate increased to 27%, saving $1.8M annually"

- **Combined collection approach increased total collections by $17M** — verified (outcome)
  - Quote: "Combined (Debt Register + DCAs): total collection rate rose to 36%, increasing overall collections by $17M"

- **Training management automation saved 3,610 hours annually** — verified (outcome)
  - Quote: "From better NPS ratings, scheduling, to roster completion lag – what previously required 4,870 hours was reduced to 1,160 hours, allowing employees to focus on more strategic tasks."

- **Training throughput increased by 400%** — verified (outcome)
  - Quote: "They saved 3,610 hours on backend process management and increased training throughput by 400%."

- **Real-time engagement tracking improves follow-up precision** — verified (method)
  - Quote: "Real-time engagement tracking (email opens/reads) to improve follow-up precision"

- **Automated alerts boost customer responsiveness in collections** — verified (method)
  - Quote: "Automated alerts highlighting potential credit-rating impact, boosting responsiveness"

- **Centralized dashboard enables accurate tracking of training metrics** — verified (method)
  - Quote: "Additionally, having integrated Power BI they now also have a central dashboard to track completion rates, drop rates, and NPS (Net Promoter Score) with accuracy and efficiency."

- **Bulk upload capability reduces manual AR work** — verified (method)
  - Quote: "Cloud-based platform supporting bulk uploads to save time and reduce manual work"

## Sources

- **S1**: https://indicodata.ai/blog/johnson-controls-unlocks-its-unstructured-data-with-intelligent-document-processing/
- **S2**: https://debtregister.com/johnson-controls-case-study-streamlining-global-receivables-for-a-fortune-500-industry-leader/
- **S3**: https://www.microsoft.com/en-us/power-platform/blog/power-apps/johnson-controls-simplifies-their-infrastructure-saving-3610-hours-on-training-enablement/
