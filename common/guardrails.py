"""Guardrails utilities for account and compliance policies."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class GuardrailResult:
    allowed: bool
    reason: str = ""
    metadata: dict[str, Any] | None = None


def validate_policy(name: str, payload: dict[str, Any] | None = None) -> GuardrailResult:
    """Return a simple allow-by-default guardrail result for scaffolding."""
    payload = payload or {}
    if not name:
        return GuardrailResult(False, "Policy name is required.", payload)
    return GuardrailResult(True, "Policy accepted.", payload)
