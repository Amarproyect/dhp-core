"""
DHP Kernel - Command Result
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class CommandResult:

    success: bool = True

    data: Any = None

    message: str = ""

    metadata: dict[str, Any] = field(default_factory=dict)