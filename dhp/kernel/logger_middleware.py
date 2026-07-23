"""
Logger Middleware
"""

from __future__ import annotations

from .command import Command
from .command_middleware import CommandMiddleware
from .command_result import CommandResult


class LoggerMiddleware(CommandMiddleware):

    def handle(
        self,
        command: Command,
        next_handler,
    ) -> CommandResult:

        print(f"[COMMAND] {command.name}")

        result = next_handler(command)

        print(f"[RESULT ] {result.success}")

        return result