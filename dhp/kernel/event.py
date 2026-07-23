"""
DHP Kernel - Event

Define la estructura base de cualquier evento intercambiado entre
plugins del sistema.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass(slots=True)
class Event:
    """
    Representa un evento interno del Kernel.
    """

    name: str
    payload: dict[str, Any] = field(default_factory=dict)
    source: str = ""

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )