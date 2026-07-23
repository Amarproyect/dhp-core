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

    manager = PluginManager(registry)

    manager.register(ConfigPlugin())
    manager.register(TestPlugin())

    print("Plugins registrados:")
    print(list(registry.plugins.keys()))

    manager.start_all()

    manager.stop_all()


if __name__ == "__main__":
    main()