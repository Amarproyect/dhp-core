"""
DHP Kernel Lifecycle

Define el ciclo de vida estándar que deben implementar
todos los plugins del sistema.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class Lifecycle(ABC):
    """
    Contrato de ciclo de vida para todos los plugins.
    """

    @abstractmethod
    def install(self) -> None:
        """Instala el componente."""

    @abstractmethod
    def start(self) -> None:
        """Inicia el componente."""

    @abstractmethod
    def stop(self) -> None:
        """Detiene el componente."""

    @abstractmethod
    def uninstall(self) -> None:
        """Desinstala el componente."""