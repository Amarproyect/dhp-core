"""
DHP Kernel - Command Handler
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from .command import Command
from .command_metadata import CommandMetadata
from .command_result import CommandResult


class CommandHandler(ABC):

    @property
    @abstractmethod
    def metadata(self) -> CommandMetadata:
        ...

    @property
    def command(self) -> str:

        return self.metadata.name

    @abstractmethod
    def execute(
        self,
        command: Command,
    ) -> CommandResult:
        ...