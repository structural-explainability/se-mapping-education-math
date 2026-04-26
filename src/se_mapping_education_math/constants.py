"""constants.py - Shared constants for SE education math mapping repositories.

Keep aligned with
se-mapspec/data/alignment/alignment-schema.toml.
"""

from se_mapping_education.constants import (
    ALLOWED_METHODS,
    ALLOWED_RELATIONS,
    DEFAULT_DATA_DIR,
    DEFAULT_MAPPINGS_DIR,
    DEFAULT_MATRIX_OUTPUT,
)

MATH_DOMAIN = "math"

__all__ = [
    "ALLOWED_METHODS",
    "ALLOWED_RELATIONS",
    "DEFAULT_DATA_DIR",
    "DEFAULT_MAPPINGS_DIR",
    "DEFAULT_MATRIX_OUTPUT",
    "MATH_DOMAIN",
]
