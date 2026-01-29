"""
Runtime configuration utilities.

Central place for:
- Loading environment variables from `.env` when present
- Sanitizing secrets used in HTTP headers (Anthropic API key)
- Creating injected callables (e.g. Step 3 LLM function)
"""

from __future__ import annotations

import os
from typing import Callable, Optional


def load_env() -> None:
    """Load environment variables from `.env` if python-dotenv is installed."""
    try:
        from dotenv import load_dotenv  # type: ignore

        load_dotenv()
    except Exception:
        # Missing dependency or any dotenv parsing issue: fall back to normal env vars
        return


_SMART_QUOTES = "\u201c\u201d\u2018\u2019"


def sanitize_header_value(value: Optional[str]) -> str:
    """
    Sanitize a value that will be used in HTTP headers.

    httpx encodes header values as ASCII; smart quotes (common from copy/paste)
    will raise UnicodeEncodeError.
    """
    if not value:
        return ""
    s = value.strip().strip(_SMART_QUOTES)
    # Fail fast if still not ASCII — better than sending a mangled API key.
    s.encode("ascii")
    return s


def get_env(name: str, default: Optional[str] = None) -> str:
    """Fetch and sanitize an env var intended for headers."""
    return sanitize_header_value(os.getenv(name, default))


LLMFn = Callable[[str], str]


def build_anthropic_llm_fn(
    *,
    max_tokens: int = 8192,
    temperature: float = 0.2,
) -> tuple[LLMFn, str]:
    """
    Create a Claude-backed llm_fn using the `anthropic` Python SDK.

    Returns:
      (llm_fn, model_name)
    """
    import anthropic

    load_env()

    api_key = (
        get_env("ANTHROPIC_API_KEY")
        or get_env("ANTHROPIC_APIKEY")
        or get_env("ANTHROPIC_API_KEY_V1")
    )
    if not api_key:
        raise RuntimeError(
            "No Anthropic API key found. Please set ANTHROPIC_API_KEY (or ANTHROPIC_APIKEY). "
            "If using .env, use plain ASCII quotes (not smart quotes)."
        )

    model_name = get_env("ANTHROPIC_MODEL", "claude-3-5-sonnet-20240620")
    client = anthropic.Anthropic(api_key=api_key)

    def llm_fn(prompt: str) -> str:
        response = client.messages.create(
            model=model_name,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": (
                                "You are an AI value case extraction engine. "
                                "Given the following document content, extract VALUE CLAIMS and CONTEXT CLAIMS "
                                "according to the AI Case Library specification v1.5.\n\n"
                                "CRITICAL: You MUST respond with VALID JSON ONLY.\n"
                                "- Use double quotes for all strings. Never put raw newlines inside a string; use \\n.\n"
                                "- Keep source_quote and claim_description under 400 characters each.\n"
                                "- Escape quotes and backslashes inside strings.\n"
                                "- Do NOT include markdown code fences (```) or prose.\n"
                                "- Return ONLY the JSON object, starting with '{' and ending with '}'.\n\n"
                                "The JSON must have this structure:\n"
                                "{\n"
                                '  "model": "string",\n'
                                '  "extraction_confidence": 0.0-1.0,\n'
                                '  "value_claims": [ /* array */ ],\n'
                                '  "context_claims": [ /* array */ ]\n'
                                "}\n\n"
                                f"{prompt}"
                            ),
                        }
                    ],
                }
            ],
        )

        parts = [getattr(p, "text", None) for p in getattr(response, "content", [])]
        parts = [p for p in parts if isinstance(p, str) and p.strip()]
        if not parts:
            raise RuntimeError("Claude response contained no text content")

        raw = parts[0].strip()

        # Strip leading/trailing markdown code fences if present
        if raw.startswith("```"):
            lines = raw.splitlines()
            if lines:
                lines = lines[1:]  # drop ``` or ```json
            if lines and lines[-1].strip().startswith("```"):
                lines = lines[:-1]
            raw = "\n".join(lines).strip()

        # If there is surrounding prose, extract substring between first '{' and last '}'.
        if raw and not raw.lstrip().startswith(("{", "[")):
            start = raw.find("{")
            end = raw.rfind("}")
            if start != -1 and end != -1 and end > start:
                raw = raw[start : end + 1].strip()

        return raw

    return llm_fn, model_name

