"""Tests for BankForge guardrails."""

from common.guardrails import validate_policy


def test_validate_policy_accepts_name():
    result = validate_policy("kyc_check")
    assert result.allowed is True


def test_validate_policy_requires_name():
    result = validate_policy("")
    assert result.allowed is False
