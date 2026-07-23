"""
DHP Kernel - Plugin Manager
"""

from __future__ import annotations

from .dependency_resolver import DependencyResolver
from .plugin_loader import PluginLoader
from .registry import Registry


class PluginManager:

    def __init__(
        self,
        registry: Registry,
    ):

        self.registry = registry

        self.loader = PluginLoader()

        self.resolver = DependencyResolver()

        self.plugins = []

    # --------------------------------------------------

    def discover(
        self,
        package: str,
    ) -> int:

        plugins = self.loader.discover(package)

        plugins = self.resolver.resolve(plugins)

        self.plugins = plugins

        command_bus = self.registry.get_service(
            "command_bus"
        )

        for plugin in plugins:

            self.registry.register_plugin(plugin)

            for capability in plugin.metadata.capabilities:

                self.registry.register_capability(
                    capability,
                    plugin,
                )

            for handler in plugin.command_handlers():

                command_bus.register(handler)

        return len(plugins)

    # --------------------------------------------------

    def start(self) -> None:

        for plugin in self.plugins:

            plugin.start()

    # --------------------------------------------------

    def stop(self) -> None:

        for plugin in reversed(self.plugins):

            plugin.stop()