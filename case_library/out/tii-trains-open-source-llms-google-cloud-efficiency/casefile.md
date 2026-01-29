---
case_id: tii-trains-open-source-llms-google-cloud-efficiency
organisation: Technology Innovation Institute (TII)
title: Open Source LLM Training and Efficiency
date_created: '2026-01-29'
date_updated: '2026-01-29'
sources:
- id: S1
  title: https://cloud.google.com/customers/tii
  url: https://cloud.google.com/customers/tii
  raw_file: ''
  text_file: sources/text/S1.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S2
  title: https://medium.com/google-cloud/serving-open-source-llms-on-gke-using-vllm-frame...
  url: https://medium.com/google-cloud/serving-open-source-llms-on-gke-using-vllm-framework-5e522b3679ee
  raw_file: ''
  text_file: sources/text/S2.txt
  extraction_method: unknown
  extraction_quality: high
  is_multi_page: false
  related_urls: []
value_claims:
- id: VC-001
  claim_title: Processed 14 trillion+ tokens efficiently for Falcon LLM training
  claim_description: TII successfully processed over 14 trillion tokens using Google
    Cloud infrastructure, enabling efficient training of the latest Falcon large language
    models at massive scale.
  source_ids:
  - S1
  source_quote: Processes 14 trillion+ tokens efficiently, enabling the training of
    the latest Falcon models
  quote_location: Header section
  ai_attribution: direct
  attribution_evidence: The token processing is directly attributed to training AI
    models (Falcon LLMs) on Google Cloud infrastructure, with AI being the core workload.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
  - velocity
  cognitive_depth: generative
  metric_raw:
    value: '14000000000000'
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
  claim_title: Achieved 1,000+ tokens per second processing speed
  claim_description: TII's Falcon models achieved processing speeds exceeding 1,000
    tokens per second using Cloud GPUs, demonstrating high-performance AI model inference
    capabilities.
  source_ids:
  - S1
  source_quote: With Cloud GPUs, TII's models have been measured processing more than
    a thousand tokens per second.
  quote_location: Performance results section
  ai_attribution: direct
  attribution_evidence: Token processing speed directly measures AI model performance
    and is explicitly attributed to the Falcon LLM models running on Cloud GPUs.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
  - velocity
  cognitive_depth: generative
  metric_raw:
    value: '1000'
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
  claim_title: Doubled GPU utilization rates through granular cluster control
  claim_description: Using Kueue and Cluster Director for granular control, TII achieved
    GPU utilization rates double what would have been possible with a managed service,
    maximizing infrastructure efficiency.
  source_ids:
  - S1
  source_quote: GPU utilization rates are double what they would have been with a
    managed service.
  quote_location: Infrastructure management section
  ai_attribution: contributing
  attribution_evidence: GPU utilization supports AI model training but the improvement
    is attributed to infrastructure management tools rather than AI itself.
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
    value: '2'
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
- id: VC-004
  claim_title: Accelerated time-to-market for Falcon model releases
  claim_description: By fine-tuning their Google Cloud environment, TII reduced the
    time required to bring new Falcon models to market, releasing stable and mature
    products faster.
  source_ids:
  - S1
  source_quote: By fine-tuning their environment on Google Cloud, the institute has
    been able to cut the time it takes to bring new Falcon models to market, releasing
    products that are stable, mature, and ready for real-world use.
  quote_location: Results section
  ai_attribution: direct
  attribution_evidence: Time-to-market reduction is directly attributed to AI model
    development and training infrastructure improvements for Falcon LLMs.
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
- id: VC-005
  claim_title: Dramatically accelerated training run speeds
  claim_description: Working with Google Cloud infrastructure, TII achieved dramatic
    speed improvements in training runs for their Falcon large language models.
  source_ids:
  - S1
  source_quote: Dr. Hacid and his team have been able to speed up training runs dramatically,
    and the AI models are showing excellent results.
  quote_location: Results section
  ai_attribution: direct
  attribution_evidence: Training run speed directly measures AI model development
    velocity and is explicitly attributed to the Falcon LLM training process.
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
- id: VC-006
  claim_title: Achieved uninterrupted training for largest LLMs at scale
  claim_description: Google Cloud infrastructure provided reliability at scale, enabling
    TII to run even the largest training jobs without interruption, ensuring consistent
    model development.
  source_ids:
  - S1
  source_quote: The setup also brings reliability at scale, so even the biggest training
    jobs can run without interruption.
  quote_location: Results section
  ai_attribution: direct
  attribution_evidence: Uninterrupted training directly supports AI model development
    and is explicitly attributed to large language model training workloads.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
  - risk_avoidance
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
  claim_title: Unlocked serious efficiency gains in LLM training
  claim_description: With close support from Google Cloud, TII achieved significant
    efficiency improvements in their AI model training environment and codebase optimization.
  source_ids:
  - S1
  source_quote: Google Cloud has helped us to unlock some serious efficiency gains.
  quote_location: Dr. Hacid quote
  ai_attribution: direct
  attribution_evidence: Efficiency gains are explicitly attributed to AI model training
    environment improvements for the Falcon LLM program.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
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
- id: VC-008
  claim_title: Enabled global reach for open source Falcon LLMs
  claim_description: Google Cloud infrastructure enabled TII to share robust, reliable
    Falcon models globally as open source tools accessible to anyone, expanding their
    impact worldwide.
  source_ids:
  - S1
  source_quote: Thanks to the ubiquity of Google Cloud and its expertise in AI, TII
    can share its models with the wider world, releasing open source tools that are
    robust, reliable, and accessible to anyone who wants to use them.
  quote_location: Impact section
  ai_attribution: direct
  attribution_evidence: Global distribution capability directly supports the AI models
    (Falcon LLMs) and their accessibility as open source tools.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - optimization
  outcome:
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
context_claims:
- id: CC-001
  context_type: organisational
  claim_title: TII is a government research entity in Abu Dhabi
  claim_description: Technology Innovation Institute (TII) is a government entity
    in Abu Dhabi with the Artificial Intelligence and Digital Science Research Center
    (AIRC) as one of nine research centers.
  source_ids:
  - S1
  source_quote: We are a government entity, but we're not just targeting users in
    the UAE government
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
  claim_title: TII operates in government and public sector
  claim_description: TII is classified as operating in the Government and Public Sector
    industry, based in the United Arab Emirates.
  source_ids:
  - S1
  source_quote: 'Industry: Government and Public Sector'
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
  claim_title: Falcon LLM program started in 2023
  claim_description: TII released the first iteration of its Falcon large language
    model in 2023, marking the beginning of the Falcon family of models.
  source_ids:
  - S1
  source_quote: In 2023, TII released the first iteration of its Falcon LLM.
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
  claim_title: Google Cloud adoption began in 2024
  claim_description: TII began training its next generation of Falcon models on Google
    Cloud infrastructure in 2024.
  source_ids:
  - S1
  source_quote: In 2024, the institute began training its next generation of Falcon
    models on Google Cloud.
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
  claim_title: Multi-cloud strategy for resilience and independence
  claim_description: TII pursues a multi-cloud strategy to ensure resilience and independence
    in its infrastructure approach.
  source_ids:
  - S1
  source_quote: From the start of the Falcon program, TII has pursued a multi-cloud
    strategy to ensure resilience and independence.
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
  claim_title: Focus on accessible and useful AI solutions
  claim_description: TII's AIRC focuses on developing AI solutions that are accessible
    and useful to a broad community, with global impact through open source models.
  source_ids:
  - S1
  source_quote: Although the AIRC works at the bleeding edge of technology, its focus
    is on solutions that are accessible and useful to a broad community.
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
  claim_title: Falcon LLM family covers multiple modalities
  claim_description: The Falcon family has expanded to cover text, image, audio, and
    video use cases, with models adaptable to hardware from supercomputers to personal
    laptops.
  source_ids:
  - S1
  source_quote: Since then, the Falcon family has expanded to cover a wide range of
    use cases, from text and image to audio and video, with models adaptable to hardware
    ranging from powerful supercomputers to personal laptops.
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
  claim_title: Research and development function
  claim_description: TII operates research centers employing scientists, researchers,
    and engineers to push boundaries of AI and machine learning.
  source_ids:
  - S1
  source_quote: The Artificial Intelligence and Digital Science Research Center (AIRC)
    is one of nine research centers at Abu Dhabi's Technology Innovation Institute
    (TII) employing teams of scientists, researchers, and engineers to push the boundaries
    of AI and machine learning.
  verification_status: verified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10880'
  apqc_name: Manage product and service portfolio
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
  claim_title: Global presence and impact with Falcon LLMs
  claim_description: The Falcon LLMs have given TII a global presence with worldwide
    impact as one of the world's most popular, feature-rich open source LLMs.
  source_ids:
  - S1
  source_quote: The Falcon LLMs have given us a global presence with a global impact.
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
  context_type: strategic_intent
  claim_title: Expansion beyond AI into other research areas
  claim_description: TII plans to expand Google Cloud usage beyond AI into security,
    quantum computing, and robotics research areas.
  source_ids:
  - S1
  source_quote: Looking ahead, TII's ambitions go beyond AI alone. Building on the
    experience of running Falcon on Google Cloud, the institute is preparing to expand
    its use of the infrastructure into other research areas, including security, quantum
    computing, and robotics.
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
      direct: 7
      contributing: 1
  context_claims:
    total: 10
    verified: 10
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

# Open Source LLM Training and Efficiency

## Executive Summary

Technology Innovation Institute (TII): Processed 14 trillion+ tokens efficiently for Falcon LLM training.

## Key Findings

- **Processed 14 trillion+ tokens efficiently for Falcon LLM training** — verified (outcome)
  - Quote: "Processes 14 trillion+ tokens efficiently, enabling the training of the latest Falcon models"

- **Achieved 1,000+ tokens per second processing speed** — verified (outcome)
  - Quote: "With Cloud GPUs, TII's models have been measured processing more than a thousand tokens per second."

- **Doubled GPU utilization rates through granular cluster control** — verified (outcome)
  - Quote: "GPU utilization rates are double what they would have been with a managed service."

- **Accelerated time-to-market for Falcon model releases** — verified (method)
  - Quote: "By fine-tuning their environment on Google Cloud, the institute has been able to cut the time it takes to bring new Falcon models to market, releasing products that are stable, mature, and ready for r..."

- **Dramatically accelerated training run speeds** — verified (method)
  - Quote: "Dr. Hacid and his team have been able to speed up training runs dramatically, and the AI models are showing excellent results."

- **Achieved uninterrupted training for largest LLMs at scale** — verified (method)
  - Quote: "The setup also brings reliability at scale, so even the biggest training jobs can run without interruption."

- **Unlocked serious efficiency gains in LLM training** — verified (method)
  - Quote: "Google Cloud has helped us to unlock some serious efficiency gains."

- **Enabled global reach for open source Falcon LLMs** — verified (method)
  - Quote: "Thanks to the ubiquity of Google Cloud and its expertise in AI, TII can share its models with the wider world, releasing open source tools that are robust, reliable, and accessible to anyone who wants..."

## Sources

- **S1**: https://cloud.google.com/customers/tii
- **S2**: https://medium.com/google-cloud/serving-open-source-llms-on-gke-using-vllm-framework-5e522b3679ee
