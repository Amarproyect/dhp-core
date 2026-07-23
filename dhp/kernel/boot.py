"""
DHP Kernel - Boot
"""

from __future__ import annotations

from .command import Command
from .command_bus import CommandBus
from .logger_middleware import LoggerMiddleware
from .plugin_manager import PluginManager
from .registry import Registry


class Boot:

    def __init__(self):

        self.registry = Registry()

        self.command_bus = CommandBus()

        self.command_bus.add_middleware(
            LoggerMiddleware()
        )

        self.registry.register_service(
            "command_bus",
            self.command_bus,
        )

        self.manager = PluginManager(
            self.registry,
        )

    # --------------------------------------------------

    def discover(
        self,
        package: str,
    ) -> int:

        return self.manager.discover(package)

    # --------------------------------------------------

    def start(self):

        self.manager.start()

    # --------------------------------------------------

    def stop(self):

        self.manager.stop()

    # --------------------------------------------------

    def execute(
        self,
        command: str,
        payload: dict | None = None,
    ):

        if payload is None:

            payload = {}

        return self.command_bus.execute(

            Command(

                name=command,

                payload=payload,

            )

        )