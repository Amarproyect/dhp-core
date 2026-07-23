"""
DHP HERMES

Punto de entrada principal.
"""

from __future__ import annotations

from .kernel.boot import Boot


def main() -> None:

    boot = Boot()

    boot.initialize()

    #
    # Descubrimiento automático
    #
    boot.discover("dhp.kernel")

    boot.start()

    boot.stop()


if __name__ == "__main__":
    main()