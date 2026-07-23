"""
Plugin de prueba para validar el Kernel.
"""

from __future__ import annotations

from .plugin import Plugin, PluginMetadata


class TestPlugin(Plugin):
    """Plugin de prueba."""

    def __init__(self) -> None:
        super().__init__(
            PluginMetadata(
                id="test",
                name="Test Plugin",
                version="1.0.0",
            )
        )

    def install(self) -> None:
        print("TestPlugin: install")

    def start(self) -> None:
        print("TestPlugin: start")

    def stop(self) -> None:
        print("TestPlugin: stop")

    def uninstall(self) -> None:
        print("TestPlugin: uninstall")