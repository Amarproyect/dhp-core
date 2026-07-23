"""
DHP Kernel - Boot

Punto de arranque del Kernel.
"""

from __future__ import annotations

from .plugin_manager import PluginManager
from .registry import Registry


class Boot:
    """
    Inicializa y detiene el Kernel.
    """

    def __init__(self) -> None:
        self.registry = Registry()
        self.plugin_manager = PluginManager(self.registry)

    @property
    def logger(self):
        return self.registry.get_service("logger")

    def initialize(self) -> None:
        """
        Inicializa todos los servicios del Kernel.
        """

        self.logger.info("=" * 60)
        self.logger.info("DHP HERMES BOOT")
        self.logger.info("=" * 60)

        self.logger.info("Inicializando Registry...")
        self.logger.info("Registry OK")

        self.logger.info("Inicializando servicios...")

        for service in self.registry.services.services.keys():
            self.logger.info(f"Servicio cargado: {service}")

        self.logger.info("Kernel inicializado correctamente")

    def register_plugin(self, plugin) -> None:
        self.plugin_manager.register(plugin)

    def start(self) -> None:
        self.logger.info("Iniciando plugins...")
        self.plugin_manager.start_all()
        self.logger.info("Plugins iniciados")

    def stop(self) -> None:
        self.logger.info("Deteniendo plugins...")
        self.plugin_manager.stop_all()
        self.logger.info("Plugins detenidos")
        self.logger.info("Kernel detenido")