---
case_id: tii-trains-open-source-llms-google-cloud-efficiency
org: Technology Innovation Institute (TII)
use_case: Open Source LLM Training and Efficiency
date_added: 2024-01-15
last_updated: 2024-01-15
source_batch: gemini_general_2026_01
batch_notes: From Gemini general research 2026-01
highlighted_value: processes 1,000+ tokens per second with Cloud GPUs
tier: transformation
tier_confidence: high
tier_rationale: TII is creating and distributing open-source LLMs as core products.
  Remove the AI and there's no product - they're not optimizing existing operations
  but creating AI capabilities as their primary output.
primary_impact: business_model
industry_cluster: operations
---


# TII Trains Open Source LLMs on Google Cloud for Maximum Efficiency

## Executive Summary

The Technology Innovation Institute (TII), through its Artificial Intelligence and Digital Science Research Center (AIRC), has successfully leveraged Google Cloud infrastructure to train its acclaimed Falcon family of open-source large language models. The implementation demonstrates significant performance improvements, including processing over 14 trillion tokens efficiently and achieving model inference speeds exceeding 1,000 tokens per second. Key technical achievements include doubled GPU utilization rates compared to managed services and enhanced reliability for large-scale training operations. The partnership has enabled TII to accelerate their AI model development while maintaining their commitment to open-source accessibility.

## Detailed Findings

### Performance Metrics - APPROVED Claims

**C1: Token Processing Efficiency**
- **Claim**: Processes 14 trillion+ tokens efficiently for training Falcon models
- **Status**: APPROVED
- **Evidence**: Direct quantifiable metric with specific token volume processed for Falcon model training
- **Impact**: Demonstrates massive scale processing capability

**C2: Model Inference Speed**
- **Claim**: AI models process 1,000+ tokens per second with Cloud GPUs
- **Status**: APPROVED
- **Evidence**: Specific performance benchmark showing real-time processing capabilities
- **Impact**: Indicates high-performance inference suitable for production applications

**C6: Measured Processing Performance**
- **Claim**: Models measured processing more than a thousand tokens per second
- **Status**: APPROVED
- **Evidence**: Confirmed measurement data supporting inference speed claims
- **Impact**: Validates consistent high-performance model execution

### Infrastructure Efficiency - NEEDS REVIEW Claims

**C3 - GPU Utilization Improvement (NEEDS_REVIEW)**
- **Status**: NEEDS_REVIEW
- **Claim**: GPU utilization rates doubled compared to managed services
- **Evidence**: "GPU utilization rates are double what they would have been with a managed service"
- **Source**: S1
- **Issue**: Specific quantifiable claim (doubled utilization rates) but lacks baseline comparison data. Quote supports the claim but would benefit from more context about the comparison methodology.
- **Recommendation**: Seek additional data on original utilization rates and measurement criteria

**C8 - Efficiency Gains (NEEDS_REVIEW)**
- **Status**: NEEDS_REVIEW
- **Claim**: Unlocked serious efficiency gains through Google Cloud support
- **Evidence**: "Google Cloud has helped us to unlock some serious efficiency gains"
- **Source**: S1
- **Issue**: Vague claim about 'serious efficiency gains' without quantification. Quote is relevant but lacks specific metrics to verify the extent of gains.
- **Recommendation**: Request specific metrics on efficiency improvements (cost, time, resource utilization)

**C4 - Go-to-Market Acceleration (NEEDS_REVIEW)**
- **Status**: NEEDS_REVIEW
- **Claim**: Accelerated go-to-market times by streamlining environment
- **Evidence**: "Accelerates go-to-market times by streamlining the environment to deliver robust, mature products ready for users"
- **Source**: S1
- **Issue**: Vague claim about 'accelerated go-to-market times' without specific metrics. Quote is relevant but doesn't provide measurable evidence of acceleration.
- **Recommendation**: Obtain concrete data on development cycle improvements

**C5 - Training Speed Enhancement (NEEDS_REVIEW)**
- **Status**: NEEDS_REVIEW
- **Claim**: Dramatically sped up training runs
- **Evidence**: "Dr. Hacid and his team have been able to speed up training runs dramatically, and the AI models are showing excellent results"
- **Source**: S1
- **Issue**: Vague claim using 'dramatically sped up' without specific metrics or timeframes. Quote is relevant but lacks quantifiable evidence.
- **Recommendation**: Request specific training time comparisons (before/after migration)

**C7 - Reliability at Scale (NEEDS_REVIEW)**
- **Status**: NEEDS_REVIEW
- **Claim**: Delivers reliability at scale for uninterrupted training runs
- **Evidence**: "Delivers reliability at scale, ensuring uninterrupted training runs for even the largest LLMs"
- **Source**: S1
- **Issue**: General claim about reliability and scale without specific metrics. Quote is relevant but doesn't provide measurable evidence of reliability performance.
- **Recommendation**: Seek data on system availability and training job completion rates

## Technical Architecture Highlights

- **Infrastructure**: AI Hypercomputer with customized hardware matching model architecture
- **Compute**: Cloud GPUs on A3 Mega Google Kubernetes Engine clusters, A3 Ultra (H200 Nvidia)
- **Storage**: Managed Lustre for high-bandwidth, low-latency performance
- **Management**: Kueue job-queuing system, Cluster Director, Dynamic Workload Scheduler
- **Strategy**: Multi-cloud approach for resilience and independence

## Sources

### S1: TII Case Study | Google Cloud
- **Type**: Case Study
- **URL**: https://cloud.google.com/customers/tii
- **Status**: Primary source with comprehensive technical details
- **Reliability**: High - Official Google Cloud customer case study

### S2: Serving Open Source LLMs on GKE using vLLM framework
- **Type**: Blog Post
- **URL**: https://medium.com/google-cloud/serving-open-source-llms-on-gke-using-vllm-framework-5e522b3679ee
- **Status**: Content unavailable (403 Forbidden)
- **Impact**: Limited - Unable to verify additional technical details

## Recommendations

1. **Quantify Vague Claims**: Obtain specific metrics for efficiency gains, speed improvements, and reliability measures
2. **Baseline Comparisons**: Establish clear before/after comparisons for GPU utilization and training performance
3. **Additional Sources**: Seek independent verification of performance claims through technical publications or benchmarks
4. **Cost Analysis**: Include cost-efficiency metrics alongside performance improvements
