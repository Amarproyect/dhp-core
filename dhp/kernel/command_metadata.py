"""
DHP Kernel - Command Metadata
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class CommandMetadata:

    name: str

    description: str = ""

    plugin: str = ""

    version: str = "1.0"

    permissions: list[str] = field(default_factory=list)

    tags: list[str] = field(default_factory=list)