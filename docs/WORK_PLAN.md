# AI Value Realiser - Work Plan

**Version:** 1.0  
**Date:** 2026-01-19  
**Status:** Planning

---

## Executive Summary

This work plan outlines the implementation roadmap to complete the AI Value Realiser, transforming it from a well-structured foundation with data models into a fully functional system capable of processing AI value creation cases.

**Current State:** Foundation complete (schemas, ontology, structure)  
**Target State:** Fully functional pipeline with CLI, data persistence, and testing  
**Estimated Timeline:** 8-12 weeks (depending on team size and priorities)

---

## Phase Overview

| Phase | Focus | Duration | Dependencies |
|-------|-------|----------|--------------|
| **Phase 1** | Core Pipeline (Steps 2, 1, 3, 4) | 4-5 weeks | None |
| **Phase 2** | Data Persistence & CLI | 2-3 weeks | Phase 1 |
| **Phase 3** | Human Validation Workflow | 1-2 weeks | Phase 2 |
| **Phase 4** | Testing & Quality | 1-2 weeks | Phase 3 |
| **Phase 5** | Company Profiler (Future) | TBD | Phase 4 |
| **Phase 6** | Opportunity Analyser (Future) | TBD | Phase 5 |

---

## Phase 1: Core Pipeline Implementation

**Goal:** Build the 5-step provenance pipeline to process cases from source discovery to verification.

**Priority:** CRITICAL - Blocks all other functionality

### 1.1 Step 2: Content Extraction (Week 1)

**Why First:** Deterministic, no AI dependencies, can be tested immediately.

#### Tasks:

1. **HTTP Client Setup**
   - [ ] Create `case_library/pipeline/extraction.py`
   - [ ] Implement HTTP client with retry logic (3× exponential backoff)
   - [ ] Handle status codes: retry on [429, 500, 502, 503, 504], fail on [401, 403, 404]
   - [ ] Add timeout handling
   - [ ] Unit tests for retry logic

2. **Content Extraction Chain**
   - [ ] Implement PDF extraction using `pypdf`
   - [ ] Implement HTML extraction using `trafilatura` (primary)
   - [ ] Implement fallback to `beautifulsoup4` for complex HTML
   - [ ] Handle encoding issues
   - [ ] Minimum content validation (200 characters)
   - [ ] Unit tests for each extraction method

3. **Multi-Page Detection**
   - [ ] Create `case_library/pipeline/multipage.py`
   - [ ] Implement pagination pattern detection (regex)
   - [ ] Implement chapter/part structure detection
   - [ ] Implement series detection
   - [ ] URL relationship classification
   - [ ] Confidence scoring (high/medium/low)
   - [ ] Unit tests for pattern detection

4. **Source Extraction Model**
   - [ ] Create `SourceExtraction` factory functions
   - [ ] Implement extraction result serialization
   - [ ] Add error handling and status tracking
   - [ ] Integration tests with real URLs (test suite)

**Deliverables:**
- `case_library/pipeline/extraction.py` (HTTP + extraction)
- `case_library/pipeline/multipage.py` (multi-page detection)
- `tests/test_extraction.py` (comprehensive tests)
- Documentation: extraction patterns, error handling

**Acceptance Criteria:**
- Can extract content from PDF, HTML, and complex web pages
- Retry logic works correctly for transient failures
- Multi-page detection identifies continuation patterns
- Minimum 90% success rate on test URLs

---

### 1.2 Step 1: Source Discovery (Week 2)

**Why Second:** Requires AI integration, but simpler than claim extraction.

#### Tasks:

1. **Web Search Integration**
   - [ ] Choose search API (Google Custom Search / SerpAPI / DuckDuckGo)
   - [ ] Create `case_library/pipeline/discovery.py`
   - [ ] Implement search query generation from (organisation, topic)
   - [ ] Handle API rate limits
   - [ ] Add search result caching (optional)

2. **AI Source Selection**
   - [ ] Integrate Anthropic Claude API
   - [ ] Create prompt template for source selection
   - [ ] Implement source prioritization logic
   - [ ] Extract URLs, titles, snippets
   - [ ] Log search query, results, selection rationale
   - [ ] Handle API failures gracefully

3. **Source Quality Assessment**
   - [ ] Implement source type detection (organisation_itself, consultancy, etc.)
   - [ ] Implement evidence grade assignment (primary/secondary)
   - [ ] Create source metadata extraction
   - [ ] Unit tests for source selection

4. **Retry & Error Handling**
   - [ ] Implement 3× retry on search failures
   - [ ] Refine search terms on failure
   - [ ] Flag case as NEEDS_REVIEW if all retries fail
   - [ ] Integration tests

**Deliverables:**
- `case_library/pipeline/discovery.py`
- `case_library/pipeline/prompts.py` (prompt templates)
- `tests/test_discovery.py`
- Configuration for API keys

**Acceptance Criteria:**
- Returns 5-10 prioritized URLs for given organisation + topic
- Source selection rationale is logged
- Handles API failures gracefully
- Minimum 80% success rate on test queries

---

### 1.3 Step 3: Claim Extraction (Week 3)

**Why Third:** Most complex AI step, builds on extraction.

#### Tasks:

1. **AI Claim Extraction**
   - [ ] Create `case_library/pipeline/claims.py`
   - [ ] Design prompt template for value claim extraction
   - [ ] Design prompt template for context claim extraction
   - [ ] Implement structured output parsing (JSON)
   - [ ] Handle AI response validation
   - [ ] Extract source quotes with location tracking

2. **Attribution Assignment**
   - [ ] Implement AI attribution level detection (direct/contributing/contextual)
   - [ ] Extract attribution evidence
   - [ ] Validate attribution logic
   - [ ] Unit tests for attribution classification

3. **Claim Structuring**
   - [ ] Create `ValueClaim` instances from AI output
   - [ ] Create `ContextClaim` instances from AI output
   - [ ] Validate claim structure against schemas
   - [ ] Handle malformed AI responses
   - [ ] Error recovery strategies

4. **Batch Processing**
   - [ ] Process multiple sources efficiently
   - [ ] Handle rate limits
   - [ ] Progress tracking
   - [ ] Integration tests

**Deliverables:**
- `case_library/pipeline/claims.py`
- Updated `case_library/pipeline/prompts.py`
- `tests/test_claims.py`
- Claim extraction examples

**Acceptance Criteria:**
- Extracts value claims and context claims from source content
- Correctly assigns attribution levels
- Handles edge cases (no claims, ambiguous claims)
- Minimum 70% precision on test cases

---

### 1.4 Step 4: Verification & Categorisation (Week 4)

**Why Fourth:** Requires both AI and deterministic logic.

#### Tasks:

1. **Quote Verification**
   - [ ] Create `case_library/pipeline/verification.py`
   - [ ] Implement quote search in source content
   - [ ] Fuzzy matching for quote variations
   - [ ] Set verification status (verified/needs_review)
   - [ ] Track quote locations
   - [ ] Unit tests for quote matching

2. **Ontology Classification**
   - [ ] Create `case_library/ontology/classifier.py`
   - [ ] Implement mechanism classification (1-2 tags)
   - [ ] Implement outcome classification (1-4 tags)
   - [ ] Implement cognitive depth classification
   - [ ] Use ontology YAML for definitions
   - [ ] Calculate confidence scores
   - [ ] Unit tests for classification

3. **Evidence Type Assignment**
   - [ ] Detect outcome validation (quantified metrics)
   - [ ] Detect method validation (qualitative approaches)
   - [ ] Assign application type (enhancement/creation)
   - [ ] Evidence grade assignment

4. **Metric Extraction**
   - [ ] Extract raw metrics from claims
   - [ ] Parse currency, percentages, counts
   - [ ] Classify quantification level (absolute/relative/qualitative)
   - [ ] Assign magnitude bands (small/medium/large/transformational)

5. **Verification Summary**
   - [ ] Calculate verification summary statistics
   - [ ] Generate case status
   - [ ] Set confidence levels
   - [ ] Integration tests

**Deliverables:**
- `case_library/pipeline/verification.py`
- `case_library/ontology/classifier.py`
- `tests/test_verification.py`
- `tests/test_classifier.py`

**Acceptance Criteria:**
- Verifies quotes with 90%+ accuracy
- Classifies ontology dimensions correctly
- Generates accurate verification summaries
- Handles edge cases (no quotes, ambiguous metrics)

---

### 1.5 Pipeline Orchestration (Week 5)

**Goal:** Wire all steps together into a cohesive pipeline.

#### Tasks:

1. **Pipeline Runner**
   - [ ] Create `case_library/pipeline/runner.py`
   - [ ] Implement pipeline orchestration (Steps 1-4)
   - [ ] Add progress tracking
   - [ ] Implement error handling and recovery
   - [ ] Add pipeline state management

2. **Build Log Management**
   - [ ] Create `BuildLog` instances for each run
   - [ ] Track step timings and status
   - [ ] Log errors and warnings
   - [ ] Serialize build logs to JSON

3. **Case File Generation**
   - [ ] Create `Case` instances from pipeline output
   - [ ] Generate casefile structure
   - [ ] Validate case structure
   - [ ] Integration tests for full pipeline

4. **CLI Integration (Basic)**
   - [ ] Add `case build` command stub
   - [ ] Wire pipeline runner to CLI
   - [ ] Add basic error reporting

**Deliverables:**
- `case_library/pipeline/runner.py`
- `case_library/pipeline/__init__.py` (exports)
- `tests/test_pipeline_integration.py`
- End-to-end test with real case

**Acceptance Criteria:**
- Can process a case from organisation + topic to complete case file
- Build log tracks all steps
- Handles failures gracefully
- Produces valid Case instances

---

## Phase 2: Data Persistence & CLI

**Goal:** Enable saving/loading cases and provide user-friendly CLI.

**Duration:** 2-3 weeks

### 2.1 Data Persistence (Week 6)

#### Tasks:

1. **Case File I/O**
   - [ ] Create `case_library/data/io.py`
   - [ ] Implement case serialization (JSON/YAML)
   - [ ] Implement case deserialization
   - [ ] Handle schema versioning
   - [ ] Validate on load

2. **File Structure**
   - [ ] Define case file structure (`case_library/data/cases/{case_id}/`)
   - [ ] Implement casefile.md generation
   - [ ] Implement sources/ directory structure
   - [ ] Implement build.json storage
   - [ ] Add case metadata management

3. **Case Management**
   - [ ] Create `case_library/data/manager.py`
   - [ ] Implement case listing
   - [ ] Implement case loading by ID
   - [ ] Implement case saving
   - [ ] Add case search/filtering
   - [ ] Unit tests

**Deliverables:**
- `case_library/data/io.py`
- `case_library/data/manager.py`
- `tests/test_data_io.py`
- Case file format documentation

**Acceptance Criteria:**
- Can save and load cases reliably
- Handles schema migrations
- Case files are human-readable
- Performance: <100ms to load a case

---

### 2.2 CLI Implementation (Week 7)

#### Tasks:

1. **Case Commands**
   - [ ] Implement `case list` command
     - List all cases with metadata
     - Filter by status, organisation
     - Format output (table/JSON)
   - [ ] Implement `case build` command
     - Accept organisation + topic
     - Run full pipeline
     - Save case to disk
     - Progress reporting
   - [ ] Implement `case validate` command
     - Validate case file structure
     - Check schema compliance
     - Report issues
   - [ ] Implement `case show` command (bonus)
     - Display case details
     - Pretty-print case structure

2. **Ontology Commands**
   - [ ] Implement `ontology show` command
     - Display current ontology
     - Show definitions and examples
   - [ ] Implement `ontology stats` command
     - Show usage statistics across cases
     - Show co-occurrence patterns

3. **CLI Enhancements**
   - [ ] Add progress bars (rich library)
   - [ ] Add colored output
   - [ ] Add error messages and help text
   - [ ] Add configuration file support
   - [ ] Integration tests for CLI

**Deliverables:**
- Complete `tools/cli.py` implementation
- `tests/test_cli.py`
- CLI documentation
- Example usage

**Acceptance Criteria:**
- All CLI commands work end-to-end
- User-friendly error messages
- Progress tracking for long operations
- Help text is comprehensive

---

### 2.3 Configuration Management (Week 8)

#### Tasks:

1. **Settings System**
   - [ ] Create `case_library/config.py`
   - [ ] Implement environment variable loading
   - [ ] Implement config file support (TOML/YAML)
   - [ ] Add default configurations
   - [ ] Validate configuration

2. **API Key Management**
   - [ ] Secure API key storage
   - [ ] Support multiple API providers
   - [ ] Add key rotation support
   - [ ] Documentation for setup

3. **Logging Framework**
   - [ ] Set up structured logging
   - [ ] Add log levels and formatting
   - [ ] Add log file rotation
   - [ ] Integrate with pipeline steps

**Deliverables:**
- `case_library/config.py`
- `case_library/logging.py` (or integration)
- Configuration template
- Setup documentation

**Acceptance Criteria:**
- Configuration is easy to set up
- API keys are secure
- Logging provides useful debugging info

---

## Phase 3: Human Validation Workflow

**Goal:** Support the human review process (Step 5).

**Duration:** 1-2 weeks

### 3.1 Validation Interface (Week 9)

#### Tasks:

1. **Review Queue Management**
   - [ ] Create `case_library/validation/queue.py`
   - [ ] Implement case prioritization
   - [ ] Track review status
   - [ ] Add queue filtering

2. **Review Interface (CLI)**
   - [ ] Implement `case review` command
   - [ ] Display claims for review
   - [ ] Accept reviewer input (valid/invalid/unclear)
   - [ ] Support adding missed claims
   - [ ] Update case with review results

3. **Review Tracking**
   - [ ] Update `HumanValidation` records
   - [ ] Track reviewer ID and timestamp
   - [ ] Generate `HumanValidationSummary`
   - [ ] Update case status

**Deliverables:**
- `case_library/validation/queue.py`
- `case_library/validation/reviewer.py`
- Updated CLI with review command
- `tests/test_validation.py`

**Acceptance Criteria:**
- Reviewers can efficiently review cases
- Review data is properly tracked
- Case status updates correctly

---

### 3.2 Tier 2 & 3 Support (Week 10 - Optional)

#### Tasks:

1. **Tier 2 Blind Extraction**
   - [ ] Implement blind extraction workflow
   - [ ] Calculate precision/recall
   - [ ] Generate comparison reports

2. **Tier 3 Calibration**
   - [ ] Implement inter-rater agreement calculation
   - [ ] Generate calibration reports
   - [ ] Support multiple reviewers

**Deliverables:**
- `case_library/validation/tier2.py`
- `case_library/validation/tier3.py`
- Calibration tools

**Note:** Can be deferred if not immediately needed.

---

## Phase 4: Testing & Quality

**Goal:** Comprehensive test coverage and code quality.

**Duration:** 1-2 weeks

### 4.1 Test Coverage (Week 11)

#### Tasks:

1. **Integration Tests**
   - [ ] End-to-end pipeline tests
   - [ ] CLI integration tests
   - [ ] Data persistence tests
   - [ ] Error handling tests

2. **Test Data**
   - [ ] Create test case library
   - [ ] Create mock API responses
   - [ ] Create test fixtures
   - [ ] Add test utilities

3. **Performance Tests**
   - [ ] Pipeline performance benchmarks
   - [ ] Memory usage tests
   - [ ] Large case handling

4. **Test Infrastructure**
   - [ ] Set up pytest configuration
   - [ ] Add coverage reporting
   - [ ] Add CI/CD test runs (GitHub Actions)

**Deliverables:**
- Comprehensive test suite
- Test coverage >80%
- CI/CD pipeline
- Test documentation

**Acceptance Criteria:**
- All critical paths are tested
- Tests run in CI/CD
- Coverage report is generated
- Tests are fast and reliable

---

### 4.2 Code Quality (Week 12)

#### Tasks:

1. **Linting & Formatting**
   - [ ] Run ruff on all code
   - [ ] Fix all linting issues
   - [ ] Set up pre-commit hooks
   - [ ] Add formatting checks

2. **Type Checking**
   - [ ] Run mypy on all code
   - [ ] Fix type errors
   - [ ] Add type stubs if needed
   - [ ] Strict type checking

3. **Documentation**
   - [ ] Add docstrings to all functions
   - [ ] Update README with usage examples
   - [ ] Create architecture documentation
   - [ ] Add API documentation

4. **Code Review**
   - [ ] Review all code for best practices
   - [ ] Refactor as needed
   - [ ] Optimize performance bottlenecks

**Deliverables:**
- Clean, linted codebase
- Full type coverage
- Comprehensive documentation
- Pre-commit hooks

**Acceptance Criteria:**
- Zero linting errors
- Zero type errors
- All functions documented
- Code follows best practices

---

## Phase 5: Company Profiler (Future)

**Goal:** Build structured profiles of client organisations.

**Status:** Not yet specified - placeholder for future work

### Estimated Tasks:

- [ ] Define profiler data models
- [ ] Implement company data extraction
- [ ] Implement sector/function classification
- [ ] Implement scale assessment
- [ ] Create profiler CLI commands
- [ ] Integration with opportunity analyser

**Note:** Requires specification before implementation.

---

## Phase 6: Opportunity Analyser (Future)

**Goal:** Match organisation profiles to relevant cases.

**Status:** Not yet specified - placeholder for future work

### Estimated Tasks:

- [ ] Define matching algorithms
- [ ] Implement case filtering by evidence mode
- [ ] Implement relevance scoring
- [ ] Create matching engine
- [ ] Integration with profiler
- [ ] Create analyser CLI commands

**Note:** Requires specification and profiler completion.

---

## Dependencies & Prerequisites

### External Dependencies:

1. **API Keys Required:**
   - Anthropic Claude API key (for Steps 1, 3, 4)
   - Web search API key (Google Custom Search / SerpAPI)

2. **Python Packages:**
   - Already in `pyproject.toml`: ✅
   - May need additional packages for search API

3. **Infrastructure:**
   - GitHub repository (✅ done)
   - CI/CD setup (GitHub Actions - to be added)

### Internal Dependencies:

- Phase 1 → Phase 2 (pipeline must exist before CLI)
- Phase 2 → Phase 3 (data persistence needed for validation)
- Phase 3 → Phase 4 (system must work before comprehensive testing)

---

## Risk Management

### High-Risk Areas:

1. **AI API Reliability**
   - **Risk:** API failures, rate limits, cost overruns
   - **Mitigation:** Robust retry logic, rate limiting, cost monitoring

2. **Content Extraction Quality**
   - **Risk:** Poor extraction from complex websites
   - **Mitigation:** Multiple extraction methods, fallbacks, extensive testing

3. **Claim Extraction Accuracy**
   - **Risk:** AI misses claims or extracts incorrectly
   - **Mitigation:** Human validation workflow, iterative prompt improvement

4. **Timeline Overruns**
   - **Risk:** Complex steps take longer than estimated
   - **Mitigation:** Prioritize MVP, defer nice-to-have features

### Medium-Risk Areas:

1. **Schema Evolution**
   - **Risk:** Need to change schemas as requirements evolve
   - **Mitigation:** Version schemas, migration tools

2. **Performance at Scale**
   - **Risk:** Slow processing for large cases
   - **Mitigation:** Benchmark early, optimize bottlenecks

---

## Success Metrics

### Phase 1 Success:
- ✅ Can process a case end-to-end (organisation + topic → case file)
- ✅ Pipeline success rate >80%
- ✅ All steps have unit tests

### Phase 2 Success:
- ✅ CLI is user-friendly and functional
- ✅ Cases can be saved and loaded reliably
- ✅ All CLI commands work

### Phase 3 Success:
- ✅ Reviewers can efficiently validate cases
- ✅ Review data is tracked accurately

### Phase 4 Success:
- ✅ Test coverage >80%
- ✅ Zero critical bugs
- ✅ Code quality meets standards

### Overall Success:
- ✅ System can process real-world cases
- ✅ Documentation is complete
- ✅ Ready for production use (with human validation)

---

## Timeline Summary

| Phase | Weeks | Cumulative |
|-------|-------|------------|
| Phase 1: Core Pipeline | 5 weeks | 5 weeks |
| Phase 2: Data & CLI | 3 weeks | 8 weeks |
| Phase 3: Validation | 2 weeks | 10 weeks |
| Phase 4: Testing | 2 weeks | 12 weeks |
| **Total (MVP)** | **12 weeks** | |

**MVP Timeline:** 12 weeks (3 months)  
**With Buffer:** 14-16 weeks (3.5-4 months)

---

## Next Steps

1. **Review this plan** with stakeholders
2. **Prioritize phases** based on business needs
3. **Set up development environment:**
   - Install dependencies
   - Set up API keys
   - Configure logging
4. **Start Phase 1.1** (Content Extraction)
5. **Set up project tracking** (GitHub Projects, issues)

---

## Notes

- This plan assumes a single developer working full-time
- Timeline can be compressed with multiple developers
- Some phases can be parallelized (e.g., testing while building)
- Phases 5-6 are future work and not included in MVP timeline
- Regular reviews and adjustments recommended

---

**Last Updated:** 2026-01-19  
**Owner:** Development Team  
**Status:** Ready for Review
