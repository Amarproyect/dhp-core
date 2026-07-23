"""
DHP Kernel - Plugin

Clase base para cualquier componente extensible de DHP.
"""

from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from .lifecycle import Lifecycle


class PluginState(Enum):
    """Estado del ciclo de vida de un plugin."""

    INSTALLED = "installed"
    LOADING = "loading"
    STARTED = "started"
    STOPPED = "stopped"
    DISABLED = "disabled"
    ERROR = "error"
    UNINSTALLED = "uninstalled"


@dataclass(slots=True)
class PluginMetadata:
    """Metadatos del plugin."""

    id: str
    name: str
    version: str

    author: str = ""
    description: str = ""

    homepage: str = ""
    license: str = ""

    api_version: str = "1.0"

    priority: int = 100

    tags: list[str] = field(default_factory=list)

    dependencies: list[str] = field(default_factory=list)

    capabilities: list[str] = field(default_factory=list)

    publishes: list[str] = field(default_factory=list)

    subscribes: list[str] = field(default_factory=list)

    config: dict[str, Any] = field(default_factory=dict)


class Plugin(Lifecycle):
    """
    Clase base de todos los plugins del sistema.
    """

    def __init__(self, metadata: PluginMetadata):

        self.metadata = metadata
        self.state = PluginState.INSTALLED

    @property
    def id(self) -> str:
        return self.metadata.id

    @property
    def name(self) -> str:
        return self.metadata.name

    @property
    def version(self) -> str:
        return self.metadata.version

    def is_started(self) -> bool:
        return self.state == PluginState.STARTED

    def is_enabled(self) -> bool:
        return self.state != PluginState.DISABLED

    def is_running(self) -> bool:
        return self.state == PluginState.STARTED

    @abstractmethod
    def install(self) -> None:
        ...

    @abstractmethod
    def start(self) -> None:
        ...

    @abstractmethod
    def stop(self) -> None:
        ...

    @abstractmethod
    def uninstall(self) -> None:
        ...