# tests/test_smoke.py
"""Smoke tests for se_mapping_education_math."""

from se_mapping_education_math.cli import main
from se_mapping_education_math.constants import (
    ALLOWED_METHODS,
    ALLOWED_RELATIONS,
    MATH_DOMAIN,
)
from se_mapping_education_math.types import Acu


def test_constants_present():
    assert "equivalent" in ALLOWED_RELATIONS
    assert "expert_review" in ALLOWED_METHODS
    assert MATH_DOMAIN == "math"


def test_math_specific_types():
    acu: Acu = {"id": "acu.a", "label": "Test", "description": "A test ACU"}
    assert acu["id"] == "acu.a"


def test_cli_no_args_returns_error():
    assert main([]) == 1


def test_cli_unknown_command_returns_error():
    assert main(["unknown"]) == 1
