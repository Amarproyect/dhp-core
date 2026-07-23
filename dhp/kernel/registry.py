"""
DHP Kernel - Registry

Registro central del Kernel.
"""

from __future__ import annotations

from typing import Any

from .config_service import ConfigService
from .logger_service import LoggerService
from .exceptions import (
    CapabilityNotFoundError,
    DuplicateCapabilityError,
    DuplicatePluginError,
    PluginNotFoundError,
)
from .plugin import Plugin
from .service_container import ServiceContainer


class Registry:
    """
    Registro central del Kernel.
    """

    def __init__(self) -> None:
        self._plugins: dict[str, Plugin] = {}
        self._capabilities: dict[str, Plugin] = {}

        self._services = ServiceContainer()

        # Servicios nativos del Kernel
        self._services.register(
            "config",
            ConfigService(),
        )

        self._services.register(
            "logger",
            LoggerService(),
        )

    # ---------------------------------------------------------
    # Plugins
    # ---------------------------------------------------------

    def register_plugin(self, plugin: Plugin) -> None:
        plugin_id = plugin.metadata.id

        if plugin_id in self._plugins:
            raise DuplicatePluginError(plugin_id)

        self._plugins[plugin_id] = plugin

    def get_plugin(self, plugin_id: str) -> Plugin:
        if plugin_id not in self._plugins:
            raise PluginNotFoundError(plugin_id)

        return self._plugins[plugin_id]

    @property
    def plugins(self) -> dict[str, Plugin]:
        return self._plugins

    # ---------------------------------------------------------
    # Capabilities
    # ---------------------------------------------------------

    def register_capability(
        self,
        capability: str,
        plugin: Plugin,
    ) -> None:
        if capability in self._capabilities:
            raise DuplicateCapabilityError(capability)

        self._capabilities[capability] = plugin

    def get_capability(
        self,
        capability: str,
    ) -> Plugin:
        if capability not in self._capabilities:
            raise CapabilityNotFoundError(capability)

        return self._capabilities[capability]

    # ---------------------------------------------------------
    # Services
    # ---------------------------------------------------------

    def register_service(
        self,
        name: str,
        service: Any,
    ) -> None:
        self._services.register(name, service)

    def get_service(
        self,
        name: str,
    ) -> Any:
        return self._services.get(name)

    @property
    def services(self) -> ServiceContainer:
        return self._services