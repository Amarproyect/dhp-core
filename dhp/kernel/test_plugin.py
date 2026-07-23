"""
Test Plugin
"""

from __future__ import annotations

from .plugin import Plugin, PluginMetadata


class TestPlugin(Plugin):

    def __init__(self) -> None:
        super().__init__(
            PluginMetadata(
                id="test",
                name="Test Plugin",
                version="1.0.0",
                priority=1,
                dependencies=[
                    "config",
                ],
            )
        )

    def install(self) -> None:
        pass

    def start(self) -> None:
        print("TestPlugin: start")

    def stop(self) -> None:
        print("TestPlugin: stop")

    def uninstall(self) -> None:
        pass