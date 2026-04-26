"""types.py - Shared types for SE education math mapping repositories.

Keep aligned with
se-mapspec/data/alignment/alignment-schema.toml.
"""

from typing import Literal, NotRequired, TypedDict

Relation = Literal["equivalent", "narrower", "broader", "overlaps", "none"]

Method = Literal[
    "manual",
    "expert_review",
    "llm_assisted",
    "rule_based",
    "imported",
]


class ContextRef(TypedDict):
    """Minimal context reference."""

    id: str


class Alignment(TypedDict):
    """A single source-to-target mapping assertion."""

    source_id: str
    target_id: str
    relation: Relation
    confidence: float
    method: Method
    human_validated: bool
    source_text: NotRequired[str]
    note: NotRequired[str]
    evidence: NotRequired[list[str]]


class MappingFile(TypedDict, total=False):
    """Parsed TOML structure for a mapping file."""

    ctx: ContextRef
    alignment: list[Alignment]


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
