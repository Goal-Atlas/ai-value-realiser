# Quick Start Checklist

Use this checklist to get started with implementation immediately.

---

## ✅ Pre-Development Setup

- [ ] Review [WORK_PLAN.md](WORK_PLAN.md) - Understand the full roadmap
- [ ] Review [WORK_PLAN_SUMMARY.md](WORK_PLAN_SUMMARY.md) - Quick reference
- [ ] Set up development environment:
  ```bash
  cd ai-value-realiser
  python -m venv .venv
  source .venv/bin/activate  # or .venv\Scripts\activate on Windows
  pip install -e ".[dev]"
  ```
- [ ] Verify tests run: `pytest tests/`
- [ ] Set up API keys (create `.env` file):
  ```bash
  ANTHROPIC_API_KEY=your-key-here
  GOOGLE_SEARCH_API_KEY=your-key-here  # or SERPAPI_KEY
  ```
- [ ] Create GitHub issues for Phase 1 tasks (one per week)

---

## 🚀 Phase 1.1: Content Extraction (Week 1)

### Day 1-2: HTTP Client
- [ ] Create `case_library/pipeline/extraction.py`
- [ ] Implement HTTP client with `httpx`
- [ ] Add retry logic (3× exponential backoff: 1s, 2s, 4s)
- [ ] Handle status codes correctly
- [ ] Write unit tests for retry logic
- [ ] Test with real URLs

### Day 3-4: Content Extraction
- [ ] Implement PDF extraction using `pypdf`
- [ ] Implement HTML extraction using `trafilatura`
- [ ] Add BeautifulSoup fallback for complex HTML
- [ ] Handle encoding issues
- [ ] Add minimum content validation (200 chars)
- [ ] Write unit tests for each method
- [ ] Test with various URL types

### Day 5: Multi-Page Detection
- [ ] Create `case_library/pipeline/multipage.py`
- [ ] Implement pagination pattern detection
- [ ] Implement chapter/part detection
- [ ] Implement series detection
- [ ] Add URL relationship classification
- [ ] Write unit tests
- [ ] Test with multi-page content

### End of Week 1 Deliverable:
```bash
# Should be able to run:
python -c "from case_library.pipeline.extraction import extract_content; result = extract_content('https://example.com'); print(result.content[:200])"
```

---

## 📝 Implementation Notes

### File Structure to Create:
```
case_library/pipeline/
├── __init__.py          # Already exists
├── extraction.py        # NEW - HTTP + content extraction
└── multipage.py         # NEW - Multi-page detection
```

### Key Functions to Implement:

**`extraction.py`:**
- `fetch_url(url: str, retries: int = 3) -> httpx.Response`
- `extract_pdf(content: bytes) -> str`
- `extract_html(html: str, url: str) -> str`
- `extract_content(url: str) -> SourceExtraction`

**`multipage.py`:**
- `detect_multi_page(content: str, base_url: str) -> MultiPageDetection`
- `has_pagination_pattern(content: str) -> bool`
- `extract_pagination_links(content: str, base_url: str) -> list[RelatedUrl]`

### Testing Strategy:
1. Start with unit tests for individual functions
2. Add integration tests with real URLs (use test fixtures)
3. Test edge cases (empty content, malformed HTML, etc.)

---

## 🎯 Week 1 Success Criteria

- [ ] Can extract content from PDFs
- [ ] Can extract content from HTML pages
- [ ] Retry logic works correctly
- [ ] Multi-page detection identifies patterns
- [ ] All functions have unit tests
- [ ] Tests pass: `pytest tests/test_extraction.py -v`

---

## 📚 Resources

- **httpx docs:** https://www.python-httpx.org/
- **trafilatura docs:** https://trafilatura.readthedocs.io/
- **pypdf docs:** https://pypdf.readthedocs.io/
- **BeautifulSoup docs:** https://www.crummy.com/software/BeautifulSoup/bs4/doc/

---

## 🐛 Common Issues & Solutions

**Issue:** HTTP 429 (Rate Limited)
- **Solution:** Implement exponential backoff, respect Retry-After header

**Issue:** Encoding errors
- **Solution:** Detect encoding from headers/content, use chardet if needed

**Issue:** JavaScript-rendered content
- **Solution:** Note limitation, may need Selenium/Playwright later (out of scope for MVP)

**Issue:** PDF extraction fails
- **Solution:** Try multiple PDF libraries, handle encrypted PDFs gracefully

---

## 🔄 Daily Workflow

1. **Morning:** Review yesterday's progress, plan today's tasks
2. **Development:** Implement features, write tests
3. **Afternoon:** Run tests, fix issues, commit changes
4. **End of day:** Update progress, note blockers

---

## 📊 Progress Tracking

Track your progress here:

**Week 1 Progress:**
- [ ] Day 1: HTTP client
- [ ] Day 2: HTTP retry logic
- [ ] Day 3: PDF extraction
- [ ] Day 4: HTML extraction
- [ ] Day 5: Multi-page detection

**Blockers/Notes:**
- _Add any blockers or important notes here_

---

**Next:** After Week 1, move to [Phase 1.2: Source Discovery](WORK_PLAN.md#12-step-1-source-discovery-week-2)
