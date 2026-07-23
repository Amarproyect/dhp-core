"""
DHP Kernel - Configuration Service
"""

from __future__ import annotations

from typing import Any


class ConfigService:
    """
    Servicio central de configuración del Kernel.
    """

    def __init__(self) -> None:
        self._config: dict[str, Any] = {}

    def set(self, key: str, value: Any) -> None:
        self._config[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    def has(self, key: str) -> bool:
        return key in self._config

    def remove(self, key: str) -> None:
        if key in self._config:
            del self._config[key]

    def clear(self) -> None:
        self._config.clear()

    @property
    def values(self) -> dict[str, Any]:
        return self._config.copy()