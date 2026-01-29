"""
Step 5: Human Validation (data recording only).

Implements §6.6 / §7 of the AI Case Library spec:

- Input: casefile (claims) from Step 4 + human verdicts
- Action: Record reviewer verdicts (valid | invalid | unclear) per claim,
  missed claims count, time taken, and optional Tier 2 precision/recall
- Output: Updated BuildLog.step_5_human_validation and claim-level
  human_validation fields on ValueClaim and ContextClaim

This module does not provide a UI; it provides the API to record
human validation results so they can be persisted to build.json and claims.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Iterable, List

from case_library.schemas import (
    BuildLog,
    ContextClaim,
    ReviewerVerdict,
    ValidationTier,
    ValueClaim,
)


def _parse_verdict(s: str) -> ReviewerVerdict | None:
    """Normalize string to ReviewerVerdict."""
    if not s:
        return None
    v = str(s).strip().lower()
    if v in ("valid", "v", "y", "yes", "1"):
        return ReviewerVerdict.VALID
    if v in ("invalid", "inv", "n", "no", "0"):
        return ReviewerVerdict.INVALID
    if v in ("unclear", "?", "u"):
        return ReviewerVerdict.UNCLEAR
    return None


def record_human_validation(
    build_log: BuildLog,
    value_claims: Iterable[ValueClaim],
    context_claims: Iterable[ContextClaim],
    *,
    tier: ValidationTier,
    reviewer_id: str | None = None,
    verdicts: dict[str, str] | None = None,
    time_taken_minutes: int | None = None,
    missed_claims_added: int = 0,
    precision_score: float | None = None,
    recall_score: float | None = None,
    review_date: datetime | None = None,
) -> tuple[BuildLog, list[ValueClaim], list[ContextClaim]]:
    """
    Record human validation results and attach Step 5 log to BuildLog.

    verdicts: map claim_id -> "valid" | "invalid" | "unclear" (case-insensitive).
    Claims not in verdicts keep their existing human_validation; claims in
    verdicts get human_validation updated (reviewed=True, reviewer_verdict,
    review_date, reviewer_id).

    Returns (build_log with step_5_human_validation set, updated value_claims,
    updated context_claims). Input build_log and claim lists are not mutated;
    copies are returned.
    """
    verdicts = verdicts or {}
    review_date = review_date or datetime.now(timezone.utc)
    value_list = list(value_claims)
    context_list = list(context_claims)

    # Build verdict map (claim_id -> ReviewerVerdict)
    verdict_map: dict[str, ReviewerVerdict] = {}
    for claim_id, raw in verdicts.items():
        v = _parse_verdict(raw)
        if v is not None:
            verdict_map[claim_id] = v

    def apply_validation_vc(claim: ValueClaim) -> ValueClaim:
        data = claim.model_dump(mode="json")
        hv = dict(data.get("human_validation") or {})
        if claim.id in verdict_map:
            hv["reviewed"] = True
            hv["reviewer_verdict"] = verdict_map[claim.id].value
            hv["review_date"] = review_date.isoformat()
            hv["reviewer_id"] = reviewer_id
        data["human_validation"] = hv
        return ValueClaim.model_validate(data)

    def apply_validation_cc(claim: ContextClaim) -> ContextClaim:
        data = claim.model_dump(mode="json")
        hv = dict(data.get("human_validation") or {})
        if claim.id in verdict_map:
            hv["reviewed"] = True
            hv["reviewer_verdict"] = verdict_map[claim.id].value
            hv["review_date"] = review_date.isoformat()
            hv["reviewer_id"] = reviewer_id
        data["human_validation"] = hv
        return ContextClaim.model_validate(data)

    updated_value = [apply_validation_vc(c) for c in value_list]
    updated_context = [apply_validation_cc(c) for c in context_list]

    claims_reviewed = len(verdict_map)
    step5_log = BuildLog.Step5HumanValidationLog(
        tier=tier,
        reviewer_id=reviewer_id,
        review_date=review_date,
        time_taken_minutes=time_taken_minutes,
        claims_reviewed=claims_reviewed if claims_reviewed else None,
        verdicts=verdicts,
        missed_claims_added=missed_claims_added,
        precision_score=precision_score,
        recall_score=recall_score,
    )

    # Copy build_log and set step_5
    log_data = build_log.model_dump()
    log_data["step_5_human_validation"] = step5_log.model_dump(mode="json")
    updated_log = BuildLog.model_validate(log_data)

    return updated_log, updated_value, updated_context
