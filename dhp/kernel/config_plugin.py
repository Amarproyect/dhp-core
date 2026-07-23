"""
DHP Kernel - Config Plugin

Plugin encargado de exponer la configuración global del sistema.
"""

from __future__ import annotations

from .plugin import Plugin
from .plugin import PluginMetadata


class ConfigPlugin(Plugin):
    """
    Plugin que registra la configuración del sistema.
    """

    def __init__(self) -> None:
        super().__init__(
            PluginMetadata(
                id="config",
                name="Configuration Plugin",
                version="1.0.0",
            )
        )

    def install(self) -> None:
        print("ConfigPlugin: install")

    def start(self) -> None:
        print("ConfigPlugin: start")

    def stop(self) -> None:
        print("ConfigPlugin: stop")

    def uninstall(self) -> None:
        print("ConfigPlugin: uninstall")