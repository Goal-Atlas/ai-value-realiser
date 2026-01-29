# Work Plan - Quick Reference

**Full Plan:** See [WORK_PLAN.md](WORK_PLAN.md)

---

## 🎯 Goal

Transform AI Value Realiser from foundation (schemas ✅) to fully functional system.

---

## 📅 Current state (as of 2026-01)

**Case Library:** Pipeline (Steps 1–5), persistence, casefile.md export, migration progress tracking, and browse viewer are implemented. **Migration complete:** 202 cases rebuilt from `OLD_cases_enriched` into `case_library/out`. Step 5 (human validation) has data recording only; review UI is not yet built.

---

## 📅 Timeline: 12 Weeks (MVP)

| Phase | Focus | Duration | Status |
|-------|-------|----------|--------|
| **Phase 1** | Core Pipeline (Steps 2→1→3→4) + orchestration | 5 weeks | ✅ Done |
| **Phase 2** | Data Persistence, migration, viewer | 3 weeks | ✅ Done |
| **Phase 3** | Human Validation Workflow (UI) | 2 weeks | 🟡 Data only; UI pending |
| **Phase 4** | Testing & Quality | 2 weeks | 🟡 Tests in place; coverage can grow |

**Total:** 12 weeks (3 months) for MVP

---

## 🚀 Phase 1: Core Pipeline (CRITICAL PATH)

### Week 1: Step 2 - Content Extraction
**Why First:** Deterministic, no AI, testable immediately

- [ ] HTTP client with retry logic
- [ ] PDF extraction (pypdf)
- [ ] HTML extraction (trafilatura + BeautifulSoup)
- [ ] Multi-page detection
- [ ] Tests

**Deliverable:** Can extract content from any URL

---

### Week 2: Step 1 - Source Discovery
**Why Second:** Requires AI but simpler than claim extraction

- [ ] Web search integration
- [ ] AI source selection (Claude API)
- [ ] Source quality assessment
- [ ] Retry & error handling
- [ ] Tests

**Deliverable:** Returns 5-10 prioritized URLs

---

### Week 3: Step 3 - Claim Extraction
**Why Third:** Most complex AI step

- [ ] AI claim extraction (value + context)
- [ ] Attribution assignment
- [ ] Claim structuring
- [ ] Batch processing
- [ ] Tests

**Deliverable:** Extracts claims from content

---

### Week 4: Step 4 - Verification & Categorisation
**Why Fourth:** Requires AI + deterministic logic

- [ ] Quote verification
- [ ] Ontology classification
- [ ] Evidence type assignment
- [ ] Metric extraction
- [ ] Verification summary
- [ ] Tests

**Deliverable:** Verified, classified claims

---

### Week 5: Pipeline Orchestration
**Goal:** Wire everything together

- [ ] Pipeline runner
- [ ] Build log management
- [ ] Case file generation
- [ ] Basic CLI integration
- [ ] End-to-end tests

**Deliverable:** Full pipeline works end-to-end

---

## 💾 Phase 2: Data & CLI (3 weeks)

### Week 6: Data Persistence
- [ ] Case file I/O (JSON/YAML)
- [ ] File structure management
- [ ] Case management utilities
- [ ] Tests

### Week 7: CLI Implementation
- [ ] `case list` command
- [ ] `case build` command
- [ ] `case validate` command
- [ ] `ontology show` command
- [ ] CLI enhancements (progress bars, colors)

### Week 8: Configuration
- [ ] Settings system
- [ ] API key management
- [ ] Logging framework

---

## 👤 Phase 3: Human Validation (2 weeks)

### Week 9: Review Interface
- [ ] Review queue management
- [ ] `case review` CLI command
- [ ] Review tracking
- [ ] Tests

### Week 10: Tier 2/3 Support (Optional)
- [ ] Blind extraction workflow
- [ ] Calibration tools

---

## ✅ Phase 4: Testing & Quality (2 weeks)

### Week 11: Test Coverage
- [ ] Integration tests
- [ ] Test data & fixtures
- [ ] Performance tests
- [ ] CI/CD setup

### Week 12: Code Quality
- [ ] Linting & formatting
- [ ] Type checking
- [ ] Documentation
- [ ] Code review

---

## 📋 Next Steps (Immediate)

1. **Set up environment:**
   ```bash
   # Install dependencies
   pip install -e ".[dev]"
   
   # Set up API keys
   export ANTHROPIC_API_KEY="your-key"
   export GOOGLE_SEARCH_API_KEY="your-key"
   ```

2. **Start Phase 1.1:**
   - Create `case_library/pipeline/extraction.py`
   - Implement HTTP client
   - Implement content extraction

3. **Create GitHub issues:**
   - One issue per week/task
   - Link to full work plan
   - Track progress

---

## 🎯 Success Criteria

### Phase 1 Complete When:
- ✅ Can process case: `organisation + topic → case file`
- ✅ Pipeline success rate >80%
- ✅ All steps have tests

### MVP Complete When:
- ✅ Full pipeline functional
- ✅ CLI is user-friendly
- ✅ Cases can be saved/loaded
- ✅ Test coverage >80%
- ✅ Ready for production use

---

## ⚠️ Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| AI API failures | Robust retry logic, rate limiting |
| Poor extraction quality | Multiple methods, fallbacks |
| Low claim accuracy | Human validation workflow |
| Timeline overruns | Prioritize MVP, defer nice-to-haves |

---

## 📊 Progress Tracking

- [x] Phase 1.1: Content Extraction (Step 2)
- [x] Phase 1.2: Source Discovery (Step 1)
- [x] Phase 1.3: Claim Extraction (Step 3)
- [x] Phase 1.4: Verification (Step 4)
- [x] Phase 1.5: Orchestration + casefile export + migration progress
- [x] Phase 2.1: Data Persistence (build.json, claims.json, casefile.md, sources/text)
- [x] Phase 2.2: Migration runner (--out, --resume) + viewer (hardwired path)
- [ ] Phase 2.3: CLI (optional; runners are `run_legacy_cases`, `viewer.server`)
- [x] Phase 3.1: Step 5 data recording
- [ ] Phase 3.2: Human validation UI
- [x] Phase 4.1: Unit tests (pipeline, schemas, persistence, step5)
- [ ] Phase 4.2: Integration / E2E as needed

---

**Last Updated:** 2026-01-28  
**See Full Plan:** [WORK_PLAN.md](WORK_PLAN.md) · **Status detail:** [DEVELOPMENT_NOTES_CASE_LIBRARY.md](DEVELOPMENT_NOTES_CASE_LIBRARY.md)
