"""
DHP Kernel - Resolver

Resuelve qué plugin implementa una capability.
"""

from __future__ import annotations

from .exceptions import CapabilityNotFoundError
from .plugin import Plugin
from .registry import Registry


class Resolver:
    """
    Resuelve capabilities utilizando el Registry.
    """

    def __init__(self, registry: Registry):

        self._registry = registry

    def resolve(self, capability: str) -> Plugin:
        """
        Devuelve el plugin que implementa una capability.
        """

        plugin = self._registry.get_capability(capability)

        if plugin is None:
            raise CapabilityNotFoundError(capability)

        return plugin