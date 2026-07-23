"""
DHP Kernel - Plugin Manager
"""

from __future__ import annotations

from .dependency_resolver import DependencyResolver
from .plugin import Plugin
from .plugin_loader import PluginLoader
from .registry import Registry


class PluginManager:

    def __init__(self, registry: Registry):

        self.registry = registry

        self.loader = PluginLoader()

        self.resolver = DependencyResolver()

    def discover(self, package: str) -> int:

        plugins = self.loader.discover(package)

        plugins = self.resolver.resolve(plugins)

        for plugin in plugins:

            self.registry.register_plugin(plugin)

        return len(plugins)

    def start_all(self) -> None:

        for plugin in self.registry.plugins.values():

            plugin.start()

    def stop_all(self) -> None:

        for plugin in reversed(
            list(self.registry.plugins.values())
        ):

            plugin.stop()