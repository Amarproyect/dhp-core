"""
Configuration Plugin
"""

from __future__ import annotations

from .plugin import Plugin, PluginMetadata


class ConfigPlugin(Plugin):

    def __init__(self) -> None:
        super().__init__(
            PluginMetadata(
                id="config",
                name="Configuration Plugin",
                version="1.0.0",
                priority=10,
                dependencies=[],
            )
        )

    def install(self) -> None:
        pass

    def start(self) -> None:
        print("ConfigPlugin: start")

    def stop(self) -> None:
        print("ConfigPlugin: stop")

    def uninstall(self) -> None:
        pass