"""
DHP Kernel - Capability
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Capability:

    name: str

    description: str = ""