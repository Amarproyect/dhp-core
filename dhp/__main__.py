"""
DHP HERMES

Punto de entrada principal.
"""

from __future__ import annotations

from .kernel.boot import Boot
from .kernel.config_plugin import ConfigPlugin
from .kernel.test_plugin import TestPlugin


def main() -> None:
    boot = Boot()

    boot.initialize()

    boot.register_plugin(ConfigPlugin())
    boot.register_plugin(TestPlugin())

    boot.start()

    boot.stop()


if __name__ == "__main__":
    main()