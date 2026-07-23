"""
DHP Kernel - Command Bus
"""

from __future__ import annotations

from .command import Command
from .command_handler import CommandHandler
from .command_metadata import CommandMetadata
from .command_middleware import CommandMiddleware
from .command_result import CommandResult


class CommandBus:

    def __init__(self):

        self._handlers: dict[str, CommandHandler] = {}

        self._middlewares: list[CommandMiddleware] = []

    # --------------------------------------------------

    def register(
        self,
        handler: CommandHandler,
    ) -> None:

        self._handlers[handler.command] = handler

    # --------------------------------------------------

    def add_middleware(
        self,
        middleware: CommandMiddleware,
    ) -> None:

        self._middlewares.append(middleware)

    # --------------------------------------------------

    def execute(
        self,
        command: Command,
    ) -> CommandResult:

        if command.name not in self._handlers:

            raise RuntimeError(
                f"No existe handler para '{command.name}'."
            )

        handler = self._handlers[command.name]

        def call(index: int, cmd: Command):

            if index == len(self._middlewares):

                return handler.execute(cmd)

            return self._middlewares[index].handle(
                cmd,
                lambda c: call(index + 1, c),
            )

        return call(0, command)

    # --------------------------------------------------

    def commands(
        self,
    ) -> dict[str, CommandMetadata]:

        return {

            name: handler.metadata

            for name, handler in self._handlers.items()

        }