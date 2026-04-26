"""types.py - Shared types for SE education math mapping repositories.

Keep aligned with
se-mapspec/data/alignment/alignment-schema.toml.
"""

from typing import TypedDict

from se_mapping_education.types import (
    Alignment,
    ContextRef,
    MappingFile,
    Method,
    Relation,
)


class NorScope(TypedDict, total=False):
    """NOR scope metadata."""

    domain: str
    grade: str
    grade_band: str
    focus: str


class Acu(TypedDict):
    """Education mathematics unit inside NOR."""

    id: str
    label: str
    description: str


class NorFile(TypedDict, total=False):
    """Parsed NOR file."""

    nor: NorScope
    acu: list[Acu]


__all__ = [
    "Alignment",
    "ContextRef",
    "MappingFile",
    "Method",
    "Relation",
    "NorScope",
    "Acu",
    "NorFile",
]
