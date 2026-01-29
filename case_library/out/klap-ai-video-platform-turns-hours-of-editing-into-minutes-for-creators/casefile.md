---
case_id: klap-ai-video-platform-turns-hours-of-editing-into-minutes-for-creators
organisation: Klap/Zigg
title: AI-Powered Video Editing Platform
date_created: '2026-01-29'
date_updated: '2026-01-29'
sources:
- id: S1
  title: https://cloud.google.com/customers/klap-app
  url: https://cloud.google.com/customers/klap-app
  raw_file: ''
  text_file: sources/text/S1.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S2
  title: https://klap.app/blog/convert-long-video-to-short-form-content
  url: https://klap.app/blog/convert-long-video-to-short-form-content
  raw_file: ''
  text_file: sources/text/S2.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S3
  title: https://klap.app/blog/video-clip-generator-ai
  url: https://klap.app/blog/video-clip-generator-ai
  raw_file: ''
  text_file: sources/text/S3.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S4
  title: https://klap.app/blog/content-repurposing-strategy
  url: https://klap.app/blog/content-repurposing-strategy
  raw_file: ''
  text_file: sources/text/S4.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
value_claims:
- id: VC-001
  claim_title: Single engineer manages infrastructure for 2 million users
  claim_description: Klap's two-person technical team (one backend engineer managing
    infrastructure, one frontend engineer) successfully supports 2 million users worldwide
    on Google Cloud infrastructure.
  source_ids:
  - S1
  source_quote: Launched in 2023, Klap has since attracted more than two million users
    worldwide... The team needed a platform that could handle petabytes of video data,
    keep costs predictable, and give its two-person team — Champion manages the backend
    and infrastructure, while Timsit handles the frontend and design — full control
    of their stack.
  quote_location: Main body, infrastructure challenges section
  ai_attribution: contributing
  attribution_evidence: AI video processing is core product capability, but infrastructure
    management efficiency is enabled by Google Cloud platform automation and scalability
    features rather than AI directly.
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
  cognitive_depth: autonomous
  metric_raw:
    value: '2000000'
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
  claim_title: 7% month-over-month growth maintained with 99.9% uptime
  claim_description: Klap sustains steady 7% monthly growth rate while maintaining
    99.9% service uptime through automated scaling infrastructure on Google Cloud.
  source_ids:
  - S1
  source_quote: Today, as the company maintains steady 7% month-on-month growth, its
    architecture automatically scales to meet user demand, while leveraging spot instances
    to keep compute costs low.
  quote_location: Infrastructure scaling section
  ai_attribution: contributing
  attribution_evidence: Growth is driven by AI video editing product, but sustained
    uptime during growth is enabled by cloud infrastructure automation and auto-scaling
    capabilities.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  - optimization
  outcome:
  - business_growth
  - experience
  cognitive_depth: autonomous
  metric_raw:
    value: '7'
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
  claim_title: Storage and processing costs reduced to one-third of alternatives
  claim_description: By consolidating video processing, storage, and task management
    on Google Cloud, Klap reduced infrastructure costs to 33% of what they would have
    been with alternative providers.
  source_ids:
  - S1
  source_quote: This setup has enabled us to lower costs significantly. Since consolidating
    on Google Cloud, our storage and processing costs are a third of what they would
    have been elsewhere.
  quote_location: Cost optimization section
  ai_attribution: contributing
  attribution_evidence: Cost reduction achieved through cloud platform optimization
    and consolidation, supporting AI video processing workloads but not directly AI-driven.
  verification_status: needs_review
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
  - cost_reduction
  cognitive_depth: prescriptive
  metric_raw:
    value: '67'
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
  claim_title: Tenfold cost reduction after infrastructure consolidation
  claim_description: When viral traffic caused cost spike, moving to consolidated
    Compute Engine instance reduced costs by 10x instantly without service disruption.
  source_ids:
  - S1
  source_quote: When a TikTok video about us went viral, we suddenly had tens of thousands
    of new users. Our bill skyrocketed overnight. By moving everything to one large
    Compute Engine instance, we reduced our costs tenfold instantly.
  quote_location: Viral traffic incident section
  ai_attribution: contributing
  attribution_evidence: Cost optimization achieved through infrastructure architecture
    decisions to support AI video processing workloads during traffic spikes.
  verification_status: needs_review
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
  - cost_reduction
  cognitive_depth: prescriptive
  metric_raw:
    value: '10'
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
- id: VC-005
  claim_title: Video editing time reduced from hours to minutes
  claim_description: Klap's AI platform automatically transforms long-form video content
    into short-form clips in approximately 10 minutes, compared to hours of manual
    editing work.
  source_ids:
  - S1
  - S2
  source_quote: Users upload their content to Klap's web interface, where AI models
    use the audio to detect engaging 'short-worthy' moments and automatically reframe
    footage from landscape to portrait. Within 10 minutes, they receive a gallery
    of short, vertical videos ready to download, publish, or fine-tune.
  quote_location: Product description section
  ai_attribution: direct
  attribution_evidence: AI models directly perform video analysis, moment detection,
    and automated reframing to achieve time savings. Core AI capability drives the
    outcome.
  verification_status: needs_review
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - automation
  - augmentation
  outcome:
  - velocity
  cognitive_depth: autonomous
  metric_raw:
    value: '10'
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
  claim_title: 95% reduction in per-clip editing time with AI automation
  claim_description: AI video clip generation reduces per-clip production time from
    23-35 minutes to 1-2 minutes, achieving approximately 95% time savings compared
    to manual editing workflow.
  source_ids:
  - S3
  source_quote: The efficiency gain is enormous. AI video clip generation slashes
    the effort for each short clip, cutting per-clip labor by up to 95% compared to
    a manual process.
  quote_location: Manual vs AI workflow comparison table
  ai_attribution: direct
  attribution_evidence: AI directly automates finding moments, cutting, reframing,
    and captioning tasks that previously required manual effort. Time savings directly
    attributable to AI automation.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_creation
  mechanism:
  - automation
  outcome:
  - velocity
  - cost_reduction
  cognitive_depth: autonomous
  metric_raw:
    value: '95'
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
  claim_title: Improved uptime from 99.9% to 99.99% after migration
  claim_description: After migrating services to Google Cloud, Klap achieved 'four
    nine' (99.99%) uptime compared to 99.9% previously, representing significant reliability
    improvement.
  source_ids:
  - S1
  source_quote: The result is a more consistent, reliable user experience, with smoother
    video processing and 99.99% 'four nine' uptime as opposed to 99.9 beforehand.
  quote_location: Reliability improvements section
  ai_attribution: contributing
  attribution_evidence: Uptime improvement achieved through cloud infrastructure reliability
    supporting AI video processing services, not directly from AI capabilities.
  verification_status: needs_review
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
  - experience
  - risk_avoidance
  cognitive_depth: autonomous
  metric_raw:
    value: '99.99'
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
  claim_title: Enabled B2B expansion through infrastructure reliability
  claim_description: Greater reliability and scalability of Google Cloud infrastructure
    enabled Klap to expand into B2B enterprise market and secure new enterprise contracts
    requiring 99.9% uptime SLAs.
  source_ids:
  - S1
  source_quote: Faster processing, fewer errors, and greater uptime have opened the
    door to new enterprise contracts, where trust in infrastructure is a key part
    of the sales process... When clients see we're built entirely on Google Cloud,
    it gives them confidence that we're serious and scalable.
  quote_location: B2B expansion section
  ai_attribution: contributing
  attribution_evidence: Infrastructure reliability enables market expansion for AI
    video product, but expansion is indirect outcome of cloud platform capabilities
    rather than AI itself.
  verification_status: needs_review
  evidence_level: method
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
  - business_growth
  - revenue_lift
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
- id: VC-009
  claim_title: 1.7 million creators generated 3.3 million clips
  claim_description: Klap platform has enabled 1.7 million content creators to generate
    3.3 million video clips from their long-form content using AI automation.
  source_ids:
  - S4
  source_quote: At Klap, we've helped over 1.7 million creators generate 3.3 million
    clips from their long-form content.
  quote_location: Why Listen to Us section
  ai_attribution: direct
  attribution_evidence: AI video analysis and clip generation directly enables creators
    to produce clips. Volume of output directly attributable to AI automation capabilities.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - automation
  outcome:
  - velocity
  - business_growth
  cognitive_depth: autonomous
  metric_raw:
    value: '3300000'
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
- id: VC-010
  claim_title: Video editors spend 50% of time on repetitive non-creative tasks
  claim_description: Research shows video editors spend up to 50% of their time on
    repetitive, non-creative tasks like reframing and transcribing, which AI automation
    can eliminate.
  source_ids:
  - S2
  source_quote: Research into creative workflows has shown that editors can burn up
    to 50% of their time on repetitive, non-creative grunt work like reframing and
    transcribing.
  quote_location: Manual method section
  ai_attribution: contextual
  attribution_evidence: This is industry context establishing the problem AI solves,
    not a direct outcome claim from Klap's AI implementation.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
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
- id: VC-011
  claim_title: Social media team reduces monthly production time from 20 hours to
    1-2 hours
  claim_description: A social media team creating 20 shorts per month can reduce production
    time from 20 hours to 1-2 hours using AI-assisted workflow, achieving 90-95% time
    savings.
  source_ids:
  - S3
  source_quote: A social media team that once spent 20 hours a month creating 20 shorts
    can now achieve the same output in just 1-2 hours with an AI-assisted workflow.
  quote_location: Time savings analysis section
  ai_attribution: direct
  attribution_evidence: Time savings directly result from AI automation of video editing
    tasks. AI is the primary mechanism enabling the efficiency gain.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: secondary_high
  application_type: capability_creation
  mechanism:
  - automation
  outcome:
  - velocity
  - cost_reduction
  cognitive_depth: autonomous
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
- id: VC-012
  claim_title: Videos under one minute achieve 6.86% engagement rate
  claim_description: Analysis found that short-form videos under one minute duration
    have an average engagement rate of 6.86%, making strong initial hooks essential
    for performance.
  source_ids:
  - S3
  source_quote: A 2023 analysis found that videos under one minute have an average
    engagement rate of 6.86%, making a strong initial hook absolutely essential.
  quote_location: Hook and scene detection section
  ai_attribution: contextual
  attribution_evidence: Industry benchmark data providing context for why AI hook
    detection is valuable, not a direct outcome of Klap's AI implementation.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
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
- id: VC-013
  claim_title: 85% of social media videos watched on mute
  claim_description: Research shows 85% of social media videos are watched with sound
    off, making automated captions essential for content accessibility and message
    delivery.
  source_ids:
  - S3
  source_quote: With a reported 85% of social media videos being watched on mute,
    captions are no longer optional—they're essential.
  quote_location: Automated captioning section
  ai_attribution: contextual
  attribution_evidence: Industry statistic establishing context for why AI-generated
    captions are valuable, not a direct outcome claim from Klap's implementation.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
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
context_claims:
- id: CC-001
  context_type: organisational
  claim_title: Two-person technical team structure
  claim_description: 'Klap operates with a two-person technical team: one engineer
    managing backend and infrastructure, one handling frontend and design.'
  source_ids:
  - S1
  source_quote: The team needed a platform that could handle petabytes of video data,
    keep costs predictable, and give its two-person team — Champion manages the backend
    and infrastructure, while Timsit handles the frontend and design — full control
    of their stack.
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
  claim_title: Paris-based AI startup
  claim_description: Zigg is a Paris-based AI startup that created the Klap.app platform.
  source_ids:
  - S1
  source_quote: Zigg is the Paris-based AI startup behind Klap.app, a platform that
    automates video editing to make content sharing faster, smarter, and more accessible
    for millions of users.
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
  claim_title: Platform launched in 2023
  claim_description: Klap platform was launched in 2023 and has since grown to 2 million
    users.
  source_ids:
  - S1
  source_quote: Launched in 2023, Klap has since attracted more than two million users
    worldwide.
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
  claim_title: 2 million users worldwide
  claim_description: Klap platform serves more than 2 million users globally as of
    the case documentation.
  source_ids:
  - S1
  source_quote: Launched in 2023, Klap has since attracted more than two million users
    worldwide.
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
  context_type: sectoral
  claim_title: Technology sector - AI video editing
  claim_description: Klap operates in the technology sector, specifically AI-powered
    video editing and content creation tools.
  source_ids:
  - S1
  source_quote: 'Industry: Technology'
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
  context_type: products_services
  claim_title: AI-powered video clip generation platform
  claim_description: Klap is an AI-powered platform that automatically generates short-form
    vertical video clips from long-form content, with automated reframing, captioning,
    and editing.
  source_ids:
  - S1
  - S2
  - S3
  source_quote: The AI video platform Klap, powered by Google Cloud, turns hours of
    editing into minutes for two million creators worldwide.
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
  context_type: strategic_intent
  claim_title: Expanding into B2B enterprise market
  claim_description: Klap is preparing to scale its B2B offering and serve more enterprise
    clients through its API model, targeting customers requiring 99.9% uptime SLAs.
  source_ids:
  - S1
  source_quote: Zigg is preparing to scale its B2B offering and serve more enterprise
    clients through its API model. When clients see we're built entirely on Google
    Cloud, it gives them confidence that we're serious and scalable. Reliability is
    key for enterprise users — they require 99.9% uptime.
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
  context_type: functional
  claim_title: Video content processing and transcoding operations
  claim_description: Core operations involve compute-intensive video transcoding,
    AI processing for moment detection, automated reframing, and caption generation
    at petabyte scale.
  source_ids:
  - S1
  source_quote: Video transcoding is extremely compute-intensive. And as we grew,
    our infrastructure costs grew even faster. The team needed a platform that could
    handle petabytes of video data, keep costs predictable.
  verification_status: unverified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10640'
  apqc_name: Manage Information Technology (IT)
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
  context_type: sectoral
  claim_title: Serves content creator and social media market
  claim_description: Target market includes content creators, podcasters, YouTubers,
    and marketers who need to repurpose long-form content into short-form social media
    clips for TikTok, Instagram Reels, and YouTube Shorts.
  source_ids:
  - S2
  - S3
  - S4
  source_quote: The AI video platform Klap, powered by Google Cloud, turns hours of
    editing into minutes for two million creators worldwide.
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
  context_type: scale
  claim_title: Processes petabytes of video data
  claim_description: Klap's infrastructure handles petabytes of video data for storage
    and processing across its user base.
  source_ids:
  - S1
  source_quote: The team needed a platform that could handle petabytes of video data,
    keep costs predictable, and give its two-person team full control of their stack.
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
  context_type: strategic_intent
  claim_title: Exploring multimodal AI capabilities
  claim_description: Klap is expanding AI capabilities beyond speech-based editing
    to multimodal models that understand both audio and visual context, recognizing
    what happens on screen.
  source_ids:
  - S1
  source_quote: Looking ahead, Klap is expanding its AI capabilities beyond speech-based
    editing, exploring multimodal models that understand both audio and visual context
    and recognize not just what's said, but what happens on screen.
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
  context_type: organisational
  claim_title: 'Co-founders: Théo Champion (President) and Victor Timsit (General
    Manager)'
  claim_description: Zigg was co-founded by Théo Champion (President, manages backend
    and infrastructure) and Victor Timsit (General Manager, handles frontend and design).
  source_ids:
  - S1
  source_quote: Zigg co-founders, president Théo Champion and general manager Victor
    Timsit, set out to address this challenge with Klap.
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
verification_summary:
  value_claims:
    total: 13
    verified: 7
    needs_review: 6
    rejected: 0
    by_attribution:
      contributing: 6
      direct: 4
      contextual: 3
  context_claims:
    total: 12
    verified: 7
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

# AI-Powered Video Editing Platform

## Executive Summary

Klap/Zigg: Single engineer manages infrastructure for 2 million users.

## Key Findings

- **Single engineer manages infrastructure for 2 million users** — needs_review (outcome)
  - Quote: "Launched in 2023, Klap has since attracted more than two million users worldwide... The team needed a platform that could handle petabytes of video data, keep costs predictable, and give its two-perso..."

- **7% month-over-month growth maintained with 99.9% uptime** — verified (outcome)
  - Quote: "Today, as the company maintains steady 7% month-on-month growth, its architecture automatically scales to meet user demand, while leveraging spot instances to keep compute costs low."

- **Storage and processing costs reduced to one-third of alternatives** — needs_review (outcome)
  - Quote: "This setup has enabled us to lower costs significantly. Since consolidating on Google Cloud, our storage and processing costs are a third of what they would have been elsewhere."

- **Tenfold cost reduction after infrastructure consolidation** — needs_review (outcome)
  - Quote: "When a TikTok video about us went viral, we suddenly had tens of thousands of new users. Our bill skyrocketed overnight. By moving everything to one large Compute Engine instance, we reduced our costs..."

- **Video editing time reduced from hours to minutes** — needs_review (outcome)
  - Quote: "Users upload their content to Klap's web interface, where AI models use the audio to detect engaging 'short-worthy' moments and automatically reframe footage from landscape to portrait. Within 10 minu..."

- **95% reduction in per-clip editing time with AI automation** — verified (outcome)
  - Quote: "The efficiency gain is enormous. AI video clip generation slashes the effort for each short clip, cutting per-clip labor by up to 95% compared to a manual process."

- **Improved uptime from 99.9% to 99.99% after migration** — needs_review (outcome)
  - Quote: "The result is a more consistent, reliable user experience, with smoother video processing and 99.99% 'four nine' uptime as opposed to 99.9 beforehand."

- **Enabled B2B expansion through infrastructure reliability** — needs_review (method)
  - Quote: "Faster processing, fewer errors, and greater uptime have opened the door to new enterprise contracts, where trust in infrastructure is a key part of the sales process... When clients see we're built e..."

- **1.7 million creators generated 3.3 million clips** — verified (adoption)
  - Quote: "At Klap, we've helped over 1.7 million creators generate 3.3 million clips from their long-form content."

- **Video editors spend 50% of time on repetitive non-creative tasks** — verified (method)
  - Quote: "Research into creative workflows has shown that editors can burn up to 50% of their time on repetitive, non-creative grunt work like reframing and transcribing."

- **Social media team reduces monthly production time from 20 hours to 1-2 hours** — verified (outcome)
  - Quote: "A social media team that once spent 20 hours a month creating 20 shorts can now achieve the same output in just 1-2 hours with an AI-assisted workflow."

- **Videos under one minute achieve 6.86% engagement rate** — verified (method)
  - Quote: "A 2023 analysis found that videos under one minute have an average engagement rate of 6.86%, making a strong initial hook absolutely essential."

- **85% of social media videos watched on mute** — verified (method)
  - Quote: "With a reported 85% of social media videos being watched on mute, captions are no longer optional—they're essential."

## Sources

- **S1**: https://cloud.google.com/customers/klap-app
- **S2**: https://klap.app/blog/convert-long-video-to-short-form-content
- **S3**: https://klap.app/blog/video-clip-generator-ai
- **S4**: https://klap.app/blog/content-repurposing-strategy
