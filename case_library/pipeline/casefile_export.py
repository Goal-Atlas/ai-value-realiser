"""
Generate casefile.md (YAML frontmatter + markdown body) from pipeline output.

Aligns with §5.2 of the AI Case Library spec: one file per case with identity,
sources, value_claims, context_claims, verification_summary, status, and a
readable markdown body (Executive Summary, Key Findings, Sources).
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from case_library.schemas import (
    BuildLog,
    ContextClaim,
    ValueClaim,
)


CASEFILE_MD = "casefile.md"


def _enum_value(x: Any) -> str:
    if x is None:
        return ""
    return getattr(x, "value", str(x))


def _verification_summary_from_claims(
    value_claims: list[ValueClaim],
    context_claims: list[ContextClaim],
) -> dict[str, Any]:
    vc_total = len(value_claims)
    vc_verified = sum(1 for v in value_claims if _enum_value(v.verification_status) == "verified")
    vc_needs_review = sum(1 for v in value_claims if _enum_value(v.verification_status) == "needs_review")
    vc_rejected = sum(1 for v in value_claims if _enum_value(v.verification_status) == "rejected")
    by_attr: dict[str, int] = {}
    for v in value_claims:
        a = _enum_value(v.ai_attribution)
        by_attr[a] = by_attr.get(a, 0) + 1
    cc_total = len(context_claims)
    cc_verified = sum(1 for c in context_claims if _enum_value(c.verification_status) == "verified")
    cc_unverified = sum(1 for c in context_claims if _enum_value(c.verification_status) == "unverified")
    cc_inferred = sum(1 for c in context_claims if _enum_value(c.verification_status) == "inferred")
    return {
        "value_claims": {
            "total": vc_total,
            "verified": vc_verified,
            "needs_review": vc_needs_review,
            "rejected": vc_rejected,
            "by_attribution": by_attr,
        },
        "context_claims": {
            "total": cc_total,
            "verified": cc_verified,
            "unverified": cc_unverified,
            "inferred": cc_inferred,
        },
        "all_value_verified": vc_total > 0 and vc_needs_review == 0 and vc_rejected == 0,
        "all_context_verified": cc_total == 0 or (cc_unverified == 0 and cc_inferred == 0),
    }


def _sources_from_build_log(build_log: BuildLog) -> list[dict[str, Any]]:
    out = []
    step2 = build_log.step_2_extraction
    if not step2:
        return out
    for s in step2.sources:
        out.append({
            "id": s.source_id,
            "title": s.url[:80] + ("..." if len(s.url) > 80 else ""),
            "url": s.url,
            "raw_file": s.raw_file or "",
            "text_file": s.text_file or f"sources/text/{s.source_id}.txt",
            "extraction_method": s.extraction_method or "unknown",
            "extraction_quality": s.extraction_quality or "high",
            "is_multi_page": getattr(s, "is_multi_page", False),
            "related_urls": [],
        })
    return out


def write_casefile_md(
    case_dir: Path,
    *,
    case_id: str,
    organisation: str,
    title: str,
    build_log: BuildLog,
    value_claims: list[ValueClaim],
    context_claims: list[ContextClaim],
) -> Path:
    """
    Write casefile.md (YAML frontmatter + markdown body) to case_dir.

    organisation and title typically come from the seed (SeedEntry).
    """
    case_dir = Path(case_dir)
    case_dir.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    verification = _verification_summary_from_claims(value_claims, context_claims)
    sources = _sources_from_build_log(build_log)

    # Human validation summary from build_log if Step 5 was run
    hv_summary: dict[str, Any] | None = None
    if build_log.step_5_human_validation:
        s5 = build_log.step_5_human_validation
        hv_summary = {
            "reviewed": True,
            "review_date": s5.review_date.isoformat() if s5.review_date else None,
            "reviewer_id": s5.reviewer_id,
            "validation_tier": _enum_value(s5.tier) if s5.tier else "tier_1",
            "value_claims": {"valid": 0, "invalid": 0, "unclear": 0, "missed": s5.missed_claims_added or 0},
            "context_claims": None,
            "precision_score": s5.precision_score,
            "recall_score": s5.recall_score,
        }
        # Count verdicts from step 5 if stored
        verdicts = getattr(s5, "verdicts", None) or {}
        for v in value_claims:
            verdict = verdicts.get(v.id, "")
            if verdict in ("valid", "Valid"):
                hv_summary["value_claims"]["valid"] += 1
            elif verdict in ("invalid", "Invalid"):
                hv_summary["value_claims"]["invalid"] += 1
            elif verdict in ("unclear", "Unclear"):
                hv_summary["value_claims"]["unclear"] += 1

    status = "complete" if verification["all_value_verified"] else "needs_review"
    if not value_claims:
        status = "in_progress"

    front = {
        "case_id": case_id,
        "organisation": organisation,
        "title": title,
        "date_created": now,
        "date_updated": now,
        "sources": sources,
        "value_claims": [v.model_dump(mode="json") for v in value_claims],
        "context_claims": [c.model_dump(mode="json") for c in context_claims],
        "verification_summary": verification,
        "human_validation_summary": hv_summary,
        "status": status,
        "confidence": "high" if value_claims else "low",
        "review_flags": [],
        "ontology_metadata": {
            "version_used": "1.0",
            "tagged_date": now,
            "needs_retagging": False,
        },
    }

    # Markdown body: Executive Summary, Key Findings, Sources
    body_lines = [
        f"# {title}",
        "",
        "## Executive Summary",
        "",
        organisation + ": " + (value_claims[0].claim_title if value_claims else title) + ".",
        "",
        "## Key Findings",
        "",
    ]
    for v in value_claims:
        body_lines.append(f"- **{v.claim_title}** — {_enum_value(v.verification_status) or '—'} ({_enum_value(v.evidence_level) or '—'})")
        if v.source_quote:
            quote_label = f"Quote (from {v.quote_source_id}): " if v.quote_source_id else "Quote: "
            body_lines.append(f"  - {quote_label}\"{v.source_quote[:200]}{'...' if len(v.source_quote) > 200 else ''}\"")
        body_lines.append("")
    body_lines.append("## Sources")
    body_lines.append("")
    for s in sources:
        body_lines.append(f"- **{s['id']}**: {s['url']}")
    body_lines.append("")

    yaml_block = yaml.dump(front, default_flow_style=False, allow_unicode=True, sort_keys=False)
    content = "---\n" + yaml_block.strip() + "\n---\n\n" + "\n".join(body_lines)
    path = case_dir / CASEFILE_MD
    path.write_text(content, encoding="utf-8")
    return path
