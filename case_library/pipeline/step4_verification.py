"""
Step 4: Verification (quote + substantiation)

Primary verification is against the **captured extracted text** in
`sources/text/*.txt` (spec v1.5 §6.5.1). Re-fetching the live URL is optional
and only used to flag divergence; it is not required for a claim to be
considered verified "against extraction".

This module focuses on:
- Finding claim `source_quote` in captured source text
- Recording match offsets into `BuildLog.VerificationAttempt`
- Setting claim verification statuses to reflect match outcomes
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable, List, Optional, Tuple

from case_library.schemas import (
    BuildLog,
    ContextClaim,
    ContextVerificationStatus,
    SourceExtraction,
    ValueClaim,
    VerificationStatus,
)


@dataclass(frozen=True)
class QuoteMatch:
    matched: bool
    method: str
    confidence: float
    start: Optional[int] = None
    end: Optional[int] = None


_QUOTE_CHARS = "\"\u201c\u201d"
_APOSTROPHE_CHARS = "'\u2018\u2019"
_DASH_CHARS = "-\u2013\u2014"


def _build_quote_regex(quote: str) -> re.Pattern[str]:
    """
    Build a regex that matches a quote with:
    - Flexible whitespace (spaces/newlines/tabs)
    - Curly/straight quote equivalence
    - Hyphen/en-dash/em-dash equivalence
    """
    parts: List[str] = []
    for ch in quote:
        if ch.isspace():
            parts.append(r"\s+")
            continue
        if ch in _QUOTE_CHARS:
            parts.append(rf"[{re.escape(_QUOTE_CHARS)}]")
            continue
        if ch in _APOSTROPHE_CHARS:
            parts.append(rf"[{re.escape(_APOSTROPHE_CHARS)}]")
            continue
        if ch in _DASH_CHARS:
            parts.append(rf"[{re.escape(_DASH_CHARS)}]")
            continue
        parts.append(re.escape(ch))
    return re.compile("".join(parts), flags=re.MULTILINE)


def find_quote_in_text(text: str, quote: str) -> QuoteMatch:
    """
    Find the quote in text, attempting progressively more tolerant matches.

    Returns offsets into `text` when a match is found.
    """
    if not text or not quote:
        return QuoteMatch(False, method="empty_input", confidence=0.0)

    # 1) Exact substring match
    idx = text.find(quote)
    if idx != -1:
        return QuoteMatch(True, method="exact", confidence=1.0, start=idx, end=idx + len(quote))

    # 2) Regex-normalized match (whitespace/punctuation variants)
    rx = _build_quote_regex(quote)
    m = rx.search(text)
    if m:
        s, e = m.span()
        return QuoteMatch(True, method="regex_normalized", confidence=0.75, start=s, end=e)

    return QuoteMatch(False, method="not_found", confidence=0.0)


def _index_sources_by_id(sources: Iterable[SourceExtraction]) -> dict[str, SourceExtraction]:
    return {s.source_id: s for s in sources}


def verify_value_claims_against_sources(
    value_claims: Iterable[ValueClaim],
    sources: Iterable[SourceExtraction],
) -> Tuple[List[ValueClaim], List[BuildLog.VerificationAttempt]]:
    """
    Verify value-claim quotes against captured source text.

    Sets:
    - VERIFIED if quote matched in any referenced source text
    - NEEDS_REVIEW otherwise
    """
    sources_by_id = _index_sources_by_id(sources)
    attempts: List[BuildLog.VerificationAttempt] = []
    verified_claims: List[ValueClaim] = []

    for claim in value_claims:
        best_match: Optional[QuoteMatch] = None
        best_source: Optional[str] = None

        for source_id in claim.source_ids:
            src = sources_by_id.get(source_id)
            if not src or not (src.content or "").strip():
                attempts.append(
                    BuildLog.VerificationAttempt(
                        claim_id=claim.id,
                        source_id=source_id,
                        method="missing_source_text",
                        result="no_text",
                        char_offset_start=None,
                        char_offset_end=None,
                        match_confidence=0.0,
                        ai_explanation=None,
                    )
                )
                continue

            match = find_quote_in_text(src.content or "", claim.source_quote)
            attempts.append(
                BuildLog.VerificationAttempt(
                    claim_id=claim.id,
                    source_id=source_id,
                    method=match.method,
                    result="matched" if match.matched else "not_found",
                    char_offset_start=match.start,
                    char_offset_end=match.end,
                    match_confidence=match.confidence,
                    ai_explanation=None,
                )
            )
            if match.matched and (best_match is None or match.confidence > best_match.confidence):
                best_match = match
                best_source = source_id

        # Update verification_status based on best match
        updated = claim.model_copy(deep=True)
        if best_match and best_match.matched:
            updated.verification_status = VerificationStatus.VERIFIED
            # If quote_location is missing, add a lightweight pointer
            if not updated.quote_location and best_source and best_match.start is not None:
                updated.quote_location = f"{best_source}@{best_match.start}:{best_match.end}"
        else:
            updated.verification_status = VerificationStatus.NEEDS_REVIEW

        verified_claims.append(updated)

    return verified_claims, attempts


def verify_context_claims_against_sources(
    context_claims: Iterable[ContextClaim],
    sources: Iterable[SourceExtraction],
) -> Tuple[List[ContextClaim], List[BuildLog.VerificationAttempt]]:
    """
    Verify context-claim quotes against captured source text.

    Rules:
    - If verification_status is INFERRED, we do not attempt quote matching.
    - Otherwise, VERIFIED if quote matched in any referenced source text,
      UNVERIFIED if not.
    """
    sources_by_id = _index_sources_by_id(sources)
    attempts: List[BuildLog.VerificationAttempt] = []
    verified_claims: List[ContextClaim] = []

    for claim in context_claims:
        updated = claim.model_copy(deep=True)

        if updated.verification_status == ContextVerificationStatus.INFERRED:
            verified_claims.append(updated)
            continue

        quote = (updated.source_quote or "").strip()
        best_match: Optional[QuoteMatch] = None
        best_source: Optional[str] = None

        for source_id in updated.source_ids:
            src = sources_by_id.get(source_id)
            if not src or not (src.content or "").strip():
                attempts.append(
                    BuildLog.VerificationAttempt(
                        claim_id=updated.id,
                        source_id=source_id,
                        method="missing_source_text",
                        result="no_text",
                        char_offset_start=None,
                        char_offset_end=None,
                        match_confidence=0.0,
                        ai_explanation=None,
                    )
                )
                continue

            match = find_quote_in_text(src.content or "", quote) if quote else QuoteMatch(
                False, method="no_quote_provided", confidence=0.0
            )
            attempts.append(
                BuildLog.VerificationAttempt(
                    claim_id=updated.id,
                    source_id=source_id,
                    method=match.method,
                    result="matched" if match.matched else "not_found",
                    char_offset_start=match.start,
                    char_offset_end=match.end,
                    match_confidence=match.confidence,
                    ai_explanation=None,
                )
            )
            if match.matched and (best_match is None or match.confidence > best_match.confidence):
                best_match = match
                best_source = source_id

        if best_match and best_match.matched:
            updated.verification_status = ContextVerificationStatus.VERIFIED
            if not updated.source_quote and best_source and best_match.start is not None:
                updated.source_quote = quote
        else:
            updated.verification_status = ContextVerificationStatus.UNVERIFIED

        verified_claims.append(updated)

    return verified_claims, attempts


def run_step4_verification(
    *,
    value_claims: Iterable[ValueClaim],
    context_claims: Iterable[ContextClaim],
    sources: Iterable[SourceExtraction],
    model_name: Optional[str] = None,
) -> Tuple[List[ValueClaim], List[ContextClaim], BuildLog.Step4VerificationLog]:
    """
    Run Step 4 verification for all claims against captured source text.

    Returns updated claims plus a Step4VerificationLog with per-attempt details.
    """
    updated_value, value_attempts = verify_value_claims_against_sources(value_claims, sources)
    updated_context, context_attempts = verify_context_claims_against_sources(context_claims, sources)

    log = BuildLog.Step4VerificationLog(
        model=model_name,
        verification_attempts=[*value_attempts, *context_attempts],
        verification_summary=None,
    )
    return updated_value, updated_context, log


__all__ = [
    "QuoteMatch",
    "find_quote_in_text",
    "run_step4_verification",
    "verify_value_claims_against_sources",
    "verify_context_claims_against_sources",
]

