"""
DHP Kernel - Plugin Loader

Descubrimiento automático de plugins.
"""

from __future__ import annotations

import importlib
import inspect
import pkgutil
from types import ModuleType
from typing import Iterable

from .plugin import Plugin


class PluginLoader:
    """
    Descubre automáticamente plugins dentro de un paquete.
    """

    def __init__(self) -> None:
        self._plugins: list[Plugin] = []
        self._loaded_ids: set[str] = set()

    @property
    def plugins(self) -> list[Plugin]:
        return self._plugins

    def clear(self) -> None:
        self._plugins.clear()
        self._loaded_ids.clear()

    def discover(self, package_name: str) -> list[Plugin]:
        """
        Busca todos los plugins dentro de un paquete.
        """

        self.clear()

        package = importlib.import_module(package_name)

        for module in self._walk(package):
            self._discover_module(module)

        self._plugins.sort(
            key=lambda plugin: plugin.metadata.priority
        )

        return self._plugins

    # ---------------------------------------------------------
    # Descubrimiento
    # ---------------------------------------------------------

    def _walk(
        self,
        package: ModuleType,
    ) -> Iterable[ModuleType]:

        yield package

        if not hasattr(package, "__path__"):
            return

        for module_info in pkgutil.walk_packages(
            package.__path__,
            package.__name__ + ".",
        ):
            try:
                yield importlib.import_module(module_info.name)
            except Exception:
                continue

    def _discover_module(
        self,
        module: ModuleType,
    ) -> None:

        for _, obj in inspect.getmembers(module, inspect.isclass):

            if obj is Plugin:
                continue

            if not issubclass(obj, Plugin):
                continue

            if inspect.isabstract(obj):
                continue

            try:
                instance = obj()
            except Exception:
                continue

            #
            # Evitar plugins duplicados
            #
            if instance.id in self._loaded_ids:
                continue

            self._loaded_ids.add(instance.id)
            self._plugins.append(instance)