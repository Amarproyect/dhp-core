"""
DHP Kernel - Command Registry Demo
"""

from __future__ import annotations

from dhp.kernel.command_bus import CommandBus

from dhp.providers.prestashop.product_create_handler import (
    ProductCreateHandler,
)


def main():

    bus = CommandBus()

    bus.register(
        ProductCreateHandler()
    )

    print()

    print("======================================")
    print("COMANDOS REGISTRADOS")
    print("======================================")

    for metadata in bus.commands().values():

        print(f"Nombre      : {metadata.name}")
        print(f"Descripción : {metadata.description}")
        print(f"Plugin      : {metadata.plugin}")
        print(f"Permisos    : {metadata.permissions}")
        print(f"Tags        : {metadata.tags}")
        print("--------------------------------------")


if __name__ == "__main__":

    main()