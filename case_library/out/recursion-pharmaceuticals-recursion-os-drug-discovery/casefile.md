---
case_id: recursion-pharmaceuticals-recursion-os-drug-discovery
organisation: Recursion Pharmaceuticals
title: AI-Enabled Drug Discovery Platform
date_created: '2026-01-29'
date_updated: '2026-01-29'
sources:
- id: S1
  title: https://cloud.google.com/customers/recursion
  url: https://cloud.google.com/customers/recursion
  raw_file: ''
  text_file: sources/text/S1.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S2
  title: https://ir.recursion.com/news-releases/news-release-details/recursion-and-exscie...
  url: https://ir.recursion.com/news-releases/news-release-details/recursion-and-exscientia-two-leaders-ai-drug-discovery-space
  raw_file: ''
  text_file: sources/text/S2.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S3
  title: https://ir.recursion.com/news-releases/news-release-details/recursion-provides-b...
  url: https://ir.recursion.com/news-releases/news-release-details/recursion-provides-business-updates-and-reports-fourth-quarter-1
  raw_file: ''
  text_file: sources/text/S3.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S4
  title: https://ir.recursion.com/news-releases/news-release-details/recursion-gives-guid...
  url: https://ir.recursion.com/news-releases/news-release-details/recursion-gives-guidance-seven-clinical-readouts-within-18
  raw_file: ''
  text_file: sources/text/S4.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
- id: S5
  title: https://www.biopharmadive.com/news/recursion-study-results-cerebral-cavernous-ma...
  url: https://www.biopharmadive.com/news/recursion-study-results-cerebral-cavernous-malformation-ai-drug/725846/
  raw_file: ''
  text_file: sources/text/S5.txt
  extraction_method: trafilatura
  extraction_quality: high
  is_multi_page: false
  related_urls: []
value_claims:
- id: VC-001
  claim_title: Accelerated deep learning model training from 24 hours to 15 minutes
    using TPUs
  claim_description: Recursion reduced deep learning model training time from over
    24 hours on local GPU clusters to as little as 15 minutes using Cloud TPU pods,
    enabling researchers to get answers in minutes or hours versus days.
  source_ids:
  - S1
  source_quote: It takes us now a little over 24 hours to train models on our local
    GPU cluster. It will take us, depending on the size of the TPU pod, anywhere from
    7 hours to 15 minutes.
  quote_location: Moving from GPUs to TPUs section
  ai_attribution: direct
  attribution_evidence: TPU technology directly enabled the reduction in training
    time through specialized hardware designed for machine learning pattern matching.
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
    value: 24 hours to 15 minutes
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
  claim_title: First machine learning-discovered drug candidate to reach Phase 1 clinical
    trial
  claim_description: Recursion advanced a compound for cerebral cavernous malformation
    into Phase 1 clinical development in under two years, representing one of the
    first drug candidates found using machine learning to reach human testing.
  source_ids:
  - S1
  source_quote: The candidate is among the first to make it to human testing that
    was found using machine learning. It typically takes at least 10 years to develop
    a new drug.
  quote_location: Accelerating drug discovery section
  ai_attribution: direct
  attribution_evidence: Machine learning was the primary method used to identify and
    select the drug candidate that advanced to clinical trials.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - innovation
  outcome:
  - velocity
  cognitive_depth: predictive
  metric_raw:
    value: '2'
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
  claim_title: 10x reduction in drug discovery and development time
  claim_description: Recursion's AI-enabled platform combining chemistry, automated
    biology, and cloud computing aims to cut the time to discover and develop new
    medicines by a factor of 10.
  source_ids:
  - S1
  source_quote: The company, headquartered in Salt Lake City, Utah, has built a drug
    discovery platform that combines chemistry, automated biology, and cloud computing
    tools to reveal new therapeutic candidates, potentially cutting the time to discover
    and develop a new medicine by a factor of 10.
  quote_location: Accelerating drug discovery section
  ai_attribution: contributing
  attribution_evidence: AI is one component of a platform combining multiple technologies
    (chemistry, automated biology, cloud computing) that together enable the time
    reduction.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_enhancement
  mechanism:
  - optimization
  - automation
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
- id: VC-004
  claim_title: Goal to discover 100 clinical candidates in 10 years
  claim_description: Recursion aims to discover 100 clinical candidates in the first
    10 years of the company, which would be orders of magnitude more than even the
    largest pharmaceutical companies can achieve.
  source_ids:
  - S1
  source_quote: Our goal is to discover 100 clinical candidates in the first 10 years
    of the company, which would be orders of magnitude more than even the largest
    pharmaceutical companies can achieve right now
  quote_location: Accelerating drug discovery section
  ai_attribution: contributing
  attribution_evidence: AI-enabled platform is a key enabler of the scale and velocity
    required to achieve this ambitious discovery target.
  verification_status: verified
  evidence_level: method
  evidence_grade: secondary_high
  application_type: capability_creation
  mechanism:
  - automation
  - optimization
  outcome:
  - velocity
  - business_growth
  cognitive_depth: predictive
  metric_raw:
    value: '100'
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
- id: VC-005
  claim_title: 10x increase in data generation capacity
  claim_description: Recursion expanded high throughput lab operations in early 2017,
    increasing data generation approximately tenfold to approach 20 terabytes per
    week.
  source_ids:
  - S1
  source_quote: In early 2017, Recursion expanded and improved its high throughput
    lab operations responsible for generating the microscopy images. That scale-up
    basically increased our data generation about tenfold
  quote_location: Exploring a big data solution section
  ai_attribution: contextual
  attribution_evidence: The increase in data generation was driven by lab automation
    improvements, which creates the data foundation for AI analysis but is not directly
    AI-enabled.
  verification_status: needs_review
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - velocity
  cognitive_depth: descriptive
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
- id: VC-006
  claim_title: 90x lab throughput improvement over manual approach
  claim_description: ADME industrialization achieved an estimated 90 times the amount
    of lab throughput compared to a manual approach.
  source_ids:
  - S4
  source_quote: 'ADME industrialization: potential to achieve an estimated 90 times
    the amount of lab throughput over a manual approach.'
  quote_location: Platform updates section
  ai_attribution: contributing
  attribution_evidence: AI-enabled automation and optimization of ADME processes contributed
    to the throughput improvement alongside lab automation technologies.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  - optimization
  outcome:
  - velocity
  cognitive_depth: prescriptive
  metric_raw:
    value: '90'
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
- id: VC-007
  claim_title: 90% prediction accuracy for compound failure in disease assays
  claim_description: Multimodal mapping enabled 90% success in predicting compounds
    that failed later disease-relevant assays in internal tests and 60% ability to
    predict compounds that passed.
  source_ids:
  - S4
  source_quote: Multimodal mapping has enabled us in certain experiments to achieve
    90% success on our ability to predict compounds that failed later disease-relevant
    assays in internal tests and 60% ability to predict compounds that passed
  quote_location: Platform updates section
  ai_attribution: direct
  attribution_evidence: AI-driven multimodal mapping directly enabled the predictive
    capability to identify compound success/failure before expensive later-stage testing.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - optimization
  outcome:
  - cost_reduction
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
- id: VC-008
  claim_title: Combined pipeline of 10+ clinical and preclinical programs
  claim_description: Post-combination with Exscientia, Recursion unveiled a technology-enabled
    portfolio with more than 10 clinical and preclinical programs, 10 advanced discovery
    programs, and more than 10 partnered programs.
  source_ids:
  - S2
  source_quote: Recursion unveils post-combination technology-enabled portfolio with
    more than 10 clinical and preclinical programs, 10 advanced discovery programs,
    and more than 10 partnered programs
  quote_location: Opening summary section
  ai_attribution: contributing
  attribution_evidence: AI-enabled drug discovery platforms from both companies contributed
    to building the combined pipeline, though not all programs are AI-discovered.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - innovation
  outcome:
  - business_growth
  cognitive_depth: predictive
  metric_raw:
    value: 10+
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
  claim_title: Approximately $330M in partnership funding received
  claim_description: The combined company has received approximately $330 million
    in upfront and milestone payments from therapeutic partnerships representing more
    than 10 partnered programs.
  source_ids:
  - S2
  source_quote: The combined company has received approximately $330 million in upfront
    and milestone payments
  quote_location: Partnerships section
  ai_attribution: contributing
  attribution_evidence: AI-enabled drug discovery platform capabilities were key to
    securing partnership agreements and associated funding, though partnerships involve
    multiple value drivers.
  verification_status: needs_review
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - innovation
  outcome:
  - revenue_lift
  cognitive_depth: predictive
  metric_raw:
    value: '330'
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
- id: VC-010
  claim_title: Trillions of searchable relationships across biology and chemistry
  claim_description: Recursion leverages machine-learning algorithms to distill from
    its dataset a collection of trillions of searchable relationships across biology
    and chemistry unconstrained by human bias.
  source_ids:
  - S2
  source_quote: Recursion leverages sophisticated machine-learning algorithms to distill
    from its dataset a collection of trillions of searchable relationships across
    biology and chemistry unconstrained by human bias.
  quote_location: About Recursion section
  ai_attribution: direct
  attribution_evidence: Machine learning algorithms directly enable the extraction
    and organization of trillions of relationships from biological and chemical datasets.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - innovation
  outcome:
  - velocity
  cognitive_depth: predictive
  metric_raw:
    value: trillions
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
- id: VC-011
  claim_title: Millions of wet lab experiments weekly at scale
  claim_description: Recursion commands massive experimental scale, conducting up
    to millions of wet lab experiments weekly through its automated platform.
  source_ids:
  - S2
  - S4
  source_quote: By commanding massive experimental scale—up to millions of wet lab
    experiments weekly—and massive computational scale
  quote_location: About Recursion section
  ai_attribution: contributing
  attribution_evidence: AI-driven automation and orchestration enables the scale of
    experimentation, working in conjunction with robotic lab automation systems.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - automation
  outcome:
  - velocity
  cognitive_depth: prescriptive
  metric_raw:
    value: millions
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
- id: VC-012
  claim_title: Causal AI models trained on 20+ petabytes of patient data
  claim_description: Recursion trained causal AI models leveraging over 20 petabytes
    of multimodal precision oncology patient data from Tempus to support discovery
    of biomarker-enriched therapeutics at scale.
  source_ids:
  - S3
  source_quote: We have been training causal AI models leveraging over 20 petabytes
    of multimodal precision oncology patient data from Tempus to support the discovery
    of potential biomarker-enriched therapeutics at scale.
  quote_location: Platform - Causal AI Modeling section
  ai_attribution: direct
  attribution_evidence: Causal AI models directly enable the analysis of massive patient
    datasets to identify therapeutic opportunities and biomarkers.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - innovation
  outcome:
  - velocity
  cognitive_depth: predictive
  metric_raw:
    value: '20'
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
- id: VC-013
  claim_title: Novel directed-oncology program from AI-driven patient data analysis
  claim_description: Causal AI work with Tempus patient data resulted in a directed-oncology
    program against a novel gene/disease relationship in a large oncology indication.
  source_ids:
  - S3
  source_quote: This work has already resulted in a directed-oncology program against
    a novel gene/disease relationship in a large oncology indication.
  quote_location: Platform - Causal AI Modeling section
  ai_attribution: direct
  attribution_evidence: Causal AI analysis of patient data directly identified the
    novel gene/disease relationship that led to the new oncology program.
  verification_status: verified
  evidence_level: outcome
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - innovation
  outcome:
  - business_growth
  cognitive_depth: predictive
  metric_raw:
    value: '1'
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
- id: VC-014
  claim_title: LOWE enables natural language drug discovery workflow orchestration
  claim_description: LOWE (Large Language Model-Orchestrated Workflow Engine) allows
    drug discovery scientists to orchestrate complex wet and dry-lab workflows via
    natural language prompts, putting state-of-the-art AI tools in the hands of every
    scientist.
  source_ids:
  - S3
  source_quote: LOWE supports drug discovery programs by orchestrating complex wet
    and dry-lab workflows via natural language prompts. Through its natural language
    interface and interactive graphics, LOWE can put state-of-the-art AI tools into
    the hands of every drug discovery scientist.
  quote_location: Platform - LOWE section
  ai_attribution: direct
  attribution_evidence: LLM technology directly enables the natural language interface
    and workflow orchestration capabilities that democratize access to AI tools.
  verification_status: needs_review
  evidence_level: method
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - augmentation
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
- id: VC-015
  claim_title: Seven clinical trial readouts expected within 18 months
  claim_description: Recursion provided guidance on seven clinical trial readouts
    expected within approximately 18 months across multiple therapeutic areas including
    rare diseases and oncology.
  source_ids:
  - S4
  source_quote: Seven Clinical Trial Readouts expected within approximately 18 months
  quote_location: Updated pipeline guidance section
  ai_attribution: contributing
  attribution_evidence: AI-enabled drug discovery platform contributed to identifying
    and advancing these candidates to clinical trials, though clinical execution involves
    many factors.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_enhancement
  mechanism:
  - innovation
  outcome:
  - velocity
  - business_growth
  cognitive_depth: predictive
  metric_raw:
    value: '7'
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
- id: VC-016
  claim_title: First genome-scale transcriptomics knockout map built
  claim_description: Recursion built its first genome-scale transcriptomics knockout
    map as part of platform development to enable comprehensive understanding of gene
    function.
  source_ids:
  - S4
  source_quote: Built our first genome-scale transcriptomics knockout map.
  quote_location: Platform updates section
  ai_attribution: contributing
  attribution_evidence: AI and machine learning tools contributed to analyzing and
    organizing the genome-scale data, working alongside experimental biology capabilities.
  verification_status: verified
  evidence_level: adoption
  evidence_grade: primary
  application_type: capability_creation
  mechanism:
  - innovation
  outcome:
  - velocity
  cognitive_depth: descriptive
  metric_raw:
    value: '1'
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
  context_type: temporal
  claim_title: Company founded in 2013
  claim_description: Recursion Pharmaceuticals was founded in 2013 to combine experimental
    biology, bioinformatics, and artificial intelligence for drug discovery.
  source_ids:
  - S1
  source_quote: Founded in 2013, Recursion Pharmaceuticals combines experimental biology,
    bioinformatics, and artificial intelligence
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
  claim_title: Headquarters in Salt Lake City, Utah
  claim_description: Recursion Pharmaceuticals is headquartered in Salt Lake City,
    Utah, United States.
  source_ids:
  - S1
  - S2
  - S4
  source_quote: The company, headquartered in Salt Lake City, Utah
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
  claim_title: Pharmaceutical and biotechnology sector
  claim_description: Recursion operates in the pharmaceutical and biotechnology industry,
    specifically focused on drug discovery and development.
  source_ids:
  - S1
  - S2
  source_quote: Recursion Pharmaceuticals is creating an AI-enabled human biology
    map to accelerate discovery of treatments for rare, untreated diseases.
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
  context_type: functional
  claim_title: Research and development function
  claim_description: Recursion's primary function is pharmaceutical research and development,
    specifically drug discovery using AI-enabled platforms.
  source_ids:
  - S1
  - S2
  - S3
  source_quote: Recursion is a leading clinical stage TechBio company decoding biology
    to industrialize drug discovery.
  verification_status: unverified
  verification_confidence: high
  inferred_from: null
  apqc_code: '10391'
  apqc_name: Perform research and development
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
  claim_title: Vision to build map of human cellular biology
  claim_description: Recursion's ultimate vision is building a map of human cellular
    biology to shift the pace and scale at which new treatments could benefit patients.
  source_ids:
  - S1
  source_quote: Recursion's ultimate vision is building a map of human cellular biology
    to shift the pace and scale at which new treatments could benefit patients.
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
  claim_title: Focus on rare disease treatments
  claim_description: Recursion initially focused on identifying treatments for rare
    diseases that can be modeled at the cellular level, with less than 5% of rare
    diseases having FDA-approved treatments.
  source_ids:
  - S1
  source_quote: There are approximately 6,000 rare diseases affecting an estimated
    25 million people – many of them young children – in the United States alone.
    The high cost and extremely long timelines of conventional drug development are
    even more daunting for rare diseases. As a result, less than 5 percent of rare
    diseases have FDA-approved treatments.
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
  context_type: scale
  claim_title: Clinical-stage biotechnology company
  claim_description: Recursion is a clinical-stage company with multiple programs
    in clinical trials and preclinical development.
  source_ids:
  - S2
  - S4
  source_quote: Recursion is a leading, clinical-stage TechBio company decoding biology
    to industrialize drug discovery.
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
  claim_title: Approximately 800 employees post-combination
  claim_description: Following the combination with Exscientia in November 2024, Recursion
    has approximately 800 employees.
  source_ids:
  - S2
  source_quote: The combined company will have approximately 800 employees with the
    headquarters remaining in Salt Lake City
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
  claim_title: Combination with Exscientia completed November 2024
  claim_description: Recursion and Exscientia officially combined in November 2024
    to advance the industrialization of drug discovery.
  source_ids:
  - S2
  source_quote: Recursion and Exscientia, two leaders in the AI drug discovery space,
    have officially combined to advance the industrialization of drug discovery
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
  claim_title: Partnership strategy with major pharmaceutical companies
  claim_description: Recursion has established strategic partnerships with Bayer (oncology
    and fibrosis) and Roche-Genentech (neuroscience and GI oncology) for collaborative
    drug discovery.
  source_ids:
  - S3
  - S4
  source_quote: We continue to advance efforts to discover potential new therapeutics
    with our strategic partners in the areas of undruggable oncology (Bayer) as well
    as neuroscience and a single indication in gastrointestinal oncology (Roche-Genentech).
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
  context_type: products_services
  claim_title: Hybrid lab-to-cloud platform architecture
  claim_description: Recursion operates a hybrid platform combining on-premises wet
    lab operations with cloud-based computational infrastructure for drug discovery.
  source_ids:
  - S1
  source_quote: Recursion Pharmaceuticals combines experimental biology, bioinformatics,
    and artificial intelligence in a hybrid lab-to-cloud platform
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
  claim_title: One of the most powerful supercomputers in the sector
  claim_description: Recursion owns and operates what it believes is one of the fastest
    supercomputers deployed in the pharmaceutical sector.
  source_ids:
  - S4
  source_quote: owning and operating what Recursion believes is one of the fastest
    supercomputers deployed in the sector
  verification_status: verified
  verification_confidence: medium
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
  context_type: temporal
  claim_title: Google Cloud partnership established by 2017
  claim_description: Recursion selected Google Cloud as its cloud partner in early
    2017 when scaling up data generation and processing capabilities.
  source_ids:
  - S1
  source_quote: In early 2017, Recursion expanded and improved its high throughput
    lab operations responsible for generating the microscopy images.
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
  context_type: products_services
  claim_title: Recursion Operating System (OS) as core platform
  claim_description: The Recursion Operating System (OS) is the company's central
    platform built across diverse technologies that continuously expands proprietary
    biological, chemical and patient-centric datasets.
  source_ids:
  - S2
  - S3
  source_quote: Central to its mission is the Recursion Operating System (OS), a platform
    built across diverse technologies that continuously expands one of the world's
    largest proprietary biological, chemical and patient-centric datasets.
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
  context_type: sectoral
  claim_title: Addressing Eroom's Law paradox in drug discovery
  claim_description: Recursion aims to address Eroom's Law, the paradox where drug
    discovery has become increasingly slower and more expensive despite improvements
    in medical technology.
  source_ids:
  - S1
  source_quote: 'It''s a paradox, which observers call Eroom''s Law: drug discovery,
    despite improvements in medical technology, has become increasingly slower and
    more expensive.'
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
    total: 16
    verified: 13
    needs_review: 3
    rejected: 0
    by_attribution:
      direct: 7
      contributing: 8
      contextual: 1
  context_claims:
    total: 15
    verified: 13
    unverified: 2
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

# AI-Enabled Drug Discovery Platform

## Executive Summary

Recursion Pharmaceuticals: Accelerated deep learning model training from 24 hours to 15 minutes using TPUs.

## Key Findings

- **Accelerated deep learning model training from 24 hours to 15 minutes using TPUs** — verified (outcome)
  - Quote: "It takes us now a little over 24 hours to train models on our local GPU cluster. It will take us, depending on the size of the TPU pod, anywhere from 7 hours to 15 minutes."

- **First machine learning-discovered drug candidate to reach Phase 1 clinical trial** — verified (outcome)
  - Quote: "The candidate is among the first to make it to human testing that was found using machine learning. It typically takes at least 10 years to develop a new drug."

- **10x reduction in drug discovery and development time** — verified (method)
  - Quote: "The company, headquartered in Salt Lake City, Utah, has built a drug discovery platform that combines chemistry, automated biology, and cloud computing tools to reveal new therapeutic candidates, pote..."

- **Goal to discover 100 clinical candidates in 10 years** — verified (method)
  - Quote: "Our goal is to discover 100 clinical candidates in the first 10 years of the company, which would be orders of magnitude more than even the largest pharmaceutical companies can achieve right now"

- **10x increase in data generation capacity** — needs_review (outcome)
  - Quote: "In early 2017, Recursion expanded and improved its high throughput lab operations responsible for generating the microscopy images. That scale-up basically increased our data generation about tenfold"

- **90x lab throughput improvement over manual approach** — verified (outcome)
  - Quote: "ADME industrialization: potential to achieve an estimated 90 times the amount of lab throughput over a manual approach."

- **90% prediction accuracy for compound failure in disease assays** — verified (outcome)
  - Quote: "Multimodal mapping has enabled us in certain experiments to achieve 90% success on our ability to predict compounds that failed later disease-relevant assays in internal tests and 60% ability to predi..."

- **Combined pipeline of 10+ clinical and preclinical programs** — verified (adoption)
  - Quote: "Recursion unveils post-combination technology-enabled portfolio with more than 10 clinical and preclinical programs, 10 advanced discovery programs, and more than 10 partnered programs"

- **Approximately $330M in partnership funding received** — needs_review (outcome)
  - Quote: "The combined company has received approximately $330 million in upfront and milestone payments"

- **Trillions of searchable relationships across biology and chemistry** — verified (adoption)
  - Quote: "Recursion leverages sophisticated machine-learning algorithms to distill from its dataset a collection of trillions of searchable relationships across biology and chemistry unconstrained by human bias..."

- **Millions of wet lab experiments weekly at scale** — verified (adoption)
  - Quote: "By commanding massive experimental scale—up to millions of wet lab experiments weekly—and massive computational scale"

- **Causal AI models trained on 20+ petabytes of patient data** — verified (adoption)
  - Quote: "We have been training causal AI models leveraging over 20 petabytes of multimodal precision oncology patient data from Tempus to support the discovery of potential biomarker-enriched therapeutics at s..."

- **Novel directed-oncology program from AI-driven patient data analysis** — verified (outcome)
  - Quote: "This work has already resulted in a directed-oncology program against a novel gene/disease relationship in a large oncology indication."

- **LOWE enables natural language drug discovery workflow orchestration** — needs_review (method)
  - Quote: "LOWE supports drug discovery programs by orchestrating complex wet and dry-lab workflows via natural language prompts. Through its natural language interface and interactive graphics, LOWE can put sta..."

- **Seven clinical trial readouts expected within 18 months** — verified (adoption)
  - Quote: "Seven Clinical Trial Readouts expected within approximately 18 months"

- **First genome-scale transcriptomics knockout map built** — verified (adoption)
  - Quote: "Built our first genome-scale transcriptomics knockout map."

## Sources

- **S1**: https://cloud.google.com/customers/recursion
- **S2**: https://ir.recursion.com/news-releases/news-release-details/recursion-and-exscientia-two-leaders-ai-drug-discovery-space
- **S3**: https://ir.recursion.com/news-releases/news-release-details/recursion-provides-business-updates-and-reports-fourth-quarter-1
- **S4**: https://ir.recursion.com/news-releases/news-release-details/recursion-gives-guidance-seven-clinical-readouts-within-18
- **S5**: https://www.biopharmadive.com/news/recursion-study-results-cerebral-cavernous-malformation-ai-drug/725846/
