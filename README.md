# AI Value Realiser

**A systematic, evidence-based approach to identifying, evaluating, and committing to AI initiatives that deliver measurable business value.**

Joint initiative by [Goal Atlas](https://goalatlas.com) and [weareCrank](https://wearecrank.com).

---

## The Problem

Most organisations know AI could create value, but struggle to connect that potential to their specific context. Leadership teams face three persistent challenges:

1. They can't easily find examples relevant to their industry, functions, or scale
2. They lack a rigorous process to evaluate which initiatives deserve commitment
3. They struggle to build business cases that link AI capabilities to specific P&L impact

The result is **pilot purgatory** — endless experimentation without the conviction to scale.

## The Solution

The AI Value Realiser addresses these challenges through three integrated components:

| Component | Purpose |
|-----------|---------|
| **AI Case Library** | Evidence-backed database of AI value creation cases, with verified claims |
| **Company Profiler** | Builds structured understanding of client context (sector, functions, scale) |
| **Opportunity Analyser** | Matches organisational profiles to relevant cases |

These feed into a four-stage **Value Realisation Process**: Scope → Explore → Commit → Adopt.

---

## Repository Structure

```
ai-value-realiser/
├── case_library/           # AI Case Library
│   ├── schemas/            # Pydantic data models (v1.5)
│   ├── pipeline/           # 5-step provenance pipeline + persistence, casefile export
│   ├── viewer/             # Browse UI (hardwired path; run viewer.server)
│   ├── ontology/           # Mechanism/Outcome/Cognitive Depth taxonomy
│   ├── OLD_cases_enriched/  # Legacy seeds (reference only)
│   └── out/                 # Rebuilt library (case_library/out by default; build.json, claims.json, casefile.md per case)
│
├── profiler/               # Company Profiler (products, financials, functions)
│
├── opportunity_analyser/   # Matching engine
│
├── docs/
│   ├── specs/              # Component specifications
│   └── architecture/       # Architecture briefs
│
├── tools/                  # CLI tools, scripts
│
└── tests/                  # Test suites
```

---

## Quick Start

```bash
# Clone
git clone git@github.com:goalatlas/ai-value-realiser.git
cd ai-value-realiser

# Set up environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -e ".[dev]"

# Run tests
pytest
```

---

## Components

### AI Case Library

A curated collection of **202 cases** (rebuilt from legacy with full provenance) showing how organisations have created value through AI. Each case has verified value claims, context claims, captured sources, and a human-readable `casefile.md`.

**Key features:**
- **Evidence level:** outcome / adoption / method (three-tier; outcome = quantified business result)
- **Application type:** Capability Enhancement vs Capability Creation
- **Ontology:** Mechanism, Outcome, Cognitive Depth (v1.0)
- **Value attribution:** Direct, Contributing, Contextual
- **Human validation:** Tier 1/2/3 (data recording in place; review UI pending)

**Pipeline:** Steps 1 (discovery) → 2 (extraction) → 3 (claim extraction, Anthropic) → 4 (verification) → 5 (human validation). Output per case: `build.json`, `claims.json`, `sources/text/*.txt`, `casefile.md`.

**Run migration (already done for 202 cases):**
```bash
python -m case_library.run_legacy_cases --out case_library/out --limit 9999   # full run
python -m case_library.run_legacy_cases --out case_library/out --resume       # resume after stop
```

**Browse the library:**
```bash
python -m case_library.viewer.server   # then open http://127.0.0.1:8765/
```
Library path is hardwired (`case_library/out` by default; override with `CASE_LIBRARY_PATH`).

📄 [Full Specification](docs/specs/AI_CASE_LIBRARY_SPECIFICATION_v1_5.md) · [Development Notes](docs/DEVELOPMENT_NOTES_CASE_LIBRARY.md) · [Migration Estimate](docs/MIGRATION_ESTIMATE.md)

### Company Profiler

*Coming soon* — Builds structured profiles of client organisations for case matching.

### Opportunity Analyser

*Coming soon* — Matches organisation profiles to relevant cases from the library.

---

## Value Realisation Process

| Stage | Purpose | Case Library Mode |
|-------|---------|-------------------|
| **Scope** | Define search space, surface relevant cases | Exploratory |
| **Explore** | Understand value potential through guided question flows | Standard |
| **Commit** | Build business case with bulletproof evidence | Strict |
| **Adopt** | Scale and realise value | Standard |

---

## Ontology v1.0

### Mechanism (How does AI create value?)
`automation` · `augmentation` · `optimization` · `innovation`

### Outcome (What business result?)
`velocity` · `experience` · `cost_reduction` · `revenue_lift` · `risk_avoidance` · `cost_erosion` · `business_growth`

### Cognitive Depth (What AI sophistication?)
`descriptive` · `diagnostic` · `predictive` · `prescriptive` · `generative` · `autonomous`

---

## Development

### Prerequisites

- Python 3.11+
- Git

### Setup

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install with dev dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=case_library --cov-report=html
```

---

## Documentation

- [AI Case Library Specification](docs/specs/AI_CASE_LIBRARY_SPECIFICATION_v1_5.md)
- [Case Library Development Notes](docs/DEVELOPMENT_NOTES_CASE_LIBRARY.md) — Current status, pipeline, persistence, viewer, migration
- [Migration Estimate](docs/MIGRATION_ESTIMATE.md) — API cost and time for rebuilding the 202-case library
- [Work Plan](docs/WORK_PLAN.md) — Implementation roadmap
- [Work Plan Summary](docs/WORK_PLAN_SUMMARY.md) — Quick reference
- [Architecture Brief](docs/architecture/VALUE_REALISER_ARCHITECTURE_BRIEF.md) *(coming soon)*

---

## Contributing

This is currently a private repository for Goal Atlas and weareCrank. Contact mike@goalatlas.com for access.

---

## License

Proprietary. © 2026 Goal Atlas Ltd.
