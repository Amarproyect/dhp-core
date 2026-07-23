"""
DHP Kernel - Plugin Manager
"""

from __future__ import annotations

from .plugin import Plugin
from .registry import Registry


class PluginManager:
    """
    Gestiona el ciclo de vida de todos los plugins.
    """

    def __init__(self, registry: Registry):
        self.registry = registry

    def register(self, plugin: Plugin) -> None:
        self.registry.register_plugin(plugin)

    def start_all(self) -> None:
        for plugin in self.registry.plugins.values():
            plugin.start()

    def stop_all(self) -> None:
        for plugin in self.registry.plugins.values():
            plugin.stop()