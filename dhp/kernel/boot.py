"""
DHP Kernel - Boot
"""

from __future__ import annotations

from .logger_service import LoggerService
from .plugin_manager import PluginManager
from .registry import Registry


class Boot:
    """
    Punto de entrada del Kernel DHP.
    """

    def __init__(self) -> None:

        self.registry = Registry()

        self.manager = PluginManager(self.registry)

        self.logger: LoggerService = self.registry.get_service("logger")

    # ---------------------------------------------------------
    # Inicialización
    # ---------------------------------------------------------

    def initialize(self) -> None:

        self.logger.info("=" * 60)
        self.logger.info("DHP HERMES BOOT")
        self.logger.info("=" * 60)

        self.logger.info("Inicializando Registry...")
        self.logger.info("Registry OK")

        self.logger.info("Inicializando servicios...")

        self.logger.info("Servicio cargado: config")
        self.logger.info("Servicio cargado: logger")

        self.logger.info("Kernel inicializado correctamente")

    # ---------------------------------------------------------
    # Plugins
    # ---------------------------------------------------------

    def discover(self, package: str) -> None:

        self.logger.info(f"Buscando plugins en {package}...")

        total = self.manager.discover(package)

        for plugin in self.registry.plugins.values():
            self.logger.info(f"Plugin encontrado: {plugin.name}")

        self.logger.info(f"{total} plugins encontrados")

    # ---------------------------------------------------------
    # Ciclo de vida
    # ---------------------------------------------------------

    def start(self) -> None:

        self.logger.info("Iniciando plugins...")

        self.manager.start_all()

        self.logger.info("Plugins iniciados")

    def stop(self) -> None:

        self.logger.info("Deteniendo plugins...")

        self.manager.stop_all()

        self.logger.info("Plugins detenidos")

        self.logger.info("Kernel detenido")