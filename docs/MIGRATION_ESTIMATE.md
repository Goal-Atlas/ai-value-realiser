# Migration estimate (OLD_cases_enriched → new library)

**Status:** Migration has been run; 202 cases are written to `case_library/out` (or your `--out` path). Progress is in `migration_progress.json`.

**Scope:** 202 cases (seeds from `case_library/OLD_cases_enriched`).  
**Anthropic usage:** Step 3 (claim extraction) only — 1 API call per case (plus up to 2 retries on malformed JSON or 1 on zero claims in rare cases). Step 1 (discovery) and Step 4 (verification) do not call the API.

## Per-case assumptions

| Item | Value |
|------|--------|
| LLM calls per case | 1 (occasionally 2–3 if retries) |
| Input per request | ~8k–15k tokens (system + prompt + sources; sources truncated to 10k chars each; avg 3 sources) |
| Output per request | ~1.5k–4k tokens (JSON value_claims + context_claims) |
| Model (default) | claude-3-5-sonnet-20240620 |

## Totals (202 cases)

| Metric | Low | High |
|--------|-----|------|
| API calls | 202 | ~250 |
| Input tokens | ~1.6M | ~2.5M |
| Output tokens | ~300k | ~800k |

## Cost (Anthropic list pricing; check [anthropic.com/pricing](https://www.anthropic.com/pricing) for current rates)

Example **Claude 3.5 Sonnet** (approximate):

- Input: **$3–6 per million tokens**
- Output: **$15–30 per million tokens**

Rough total for 202 cases:

- **Low:** ~1.6M in × $3 + ~0.4M out × $15 ≈ **$4.80 + $6 ≈ $11**
- **High:** ~2.5M in × $6 + ~0.8M out × $30 ≈ **$15 + $24 ≈ $39**

So **about $10–40** for the full migration, depending on actual token counts and pricing tier. Batch API (if you use it) can cut cost by ~50%.

## Time

- **Step 2 (extraction):** ~2–10 s per case (HTTP fetch + trafilatura/pypdf). 202 cases ≈ 7–35 min.
- **Step 3 (LLM):** ~15–45 s per request. 202 cases ≈ 50–150 min.
- **Step 4 (verification):** In-process only, seconds per case.

**Total wall-clock:** about **1.5–3 hours** if run sequentially. Use `--resume` if you stop and restart.

## How to run

```bash
# From project root (ai-value-realiser)
# Full migration (202 cases), progress saved under case_library/out
python -m case_library.run_legacy_cases --out case_library/out --limit 9999

# Or process in batches and resume later, e.g. first 50:
python -m case_library.run_legacy_cases --out case_library/out --limit 50
# Later: next 50 (use --resume to skip the first 50)
python -m case_library.run_legacy_cases --out case_library/out --limit 100 --resume
# etc.
```

Progress is stored in `case_library/out/migration_progress.json`; you see “Migration: X/Y complete, Z to process” at start and “N/M — case_id done” after each case.
