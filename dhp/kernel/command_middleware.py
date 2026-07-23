"""
DHP Kernel - Command Middleware
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from .command import Command
from .command_result import CommandResult


class CommandMiddleware(ABC):

    @abstractmethod
    def handle(
        self,
        command: Command,
        next_handler,
    ) -> CommandResult:
        ...