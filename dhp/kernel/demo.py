"""
Pequeña prueba del Kernel DHP.
"""

from __future__ import annotations

from .config_plugin import ConfigPlugin
from .plugin_manager import PluginManager
from .registry import Registry


from .test_plugin import TestPlugin


def main() -> None:
    registry = Registry()

    logger = registry.get_service("logger")

    logger.info("Kernel iniciado")

    manager = PluginManager(registry)

    manager.register(ConfigPlugin())
    manager.register(TestPlugin())

    logger.debug("Plugins registrados correctamente")

    print()

    print("Plugins registrados:")
    print(list(registry.plugins.keys()))

    print()

    manager.start_all()

    print()

    manager.stop_all()

    print()

    logger.info("Kernel detenido")


if __name__ == "__main__":
    main()