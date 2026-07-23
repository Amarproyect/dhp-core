"""
DHP Kernel - Service Container

Contenedor de servicios del Kernel.
"""

from __future__ import annotations

from typing import Any

from .exceptions import KernelError


class ServiceAlreadyRegisteredError(KernelError):
    """Se intenta registrar un servicio ya existente."""


class ServiceNotFoundError(KernelError):
    """Se solicita un servicio inexistente."""


class ServiceContainer:
    """
    Contenedor central de servicios.

    Permite registrar y recuperar servicios compartidos
    por cualquier plugin del Kernel.
    """

    def __init__(self) -> None:
        self._services: dict[str, Any] = {}

    def register(self, name: str, service: Any) -> None:
        if name in self._services:
            raise ServiceAlreadyRegisteredError(
                f"Service '{name}' already registered."
            )

        self._services[name] = service

    def get(self, name: str) -> Any:
        if name not in self._services:
            raise ServiceNotFoundError(
                f"Service '{name}' not found."
            )

        return self._services[name]

    def has(self, name: str) -> bool:
        return name in self._services

    def remove(self, name: str) -> None:
        if name not in self._services:
            raise ServiceNotFoundError(
                f"Service '{name}' not found."
            )

        del self._services[name]

    def clear(self) -> None:
        self._services.clear()

    @property
    def services(self) -> dict[str, Any]:
        return self._services