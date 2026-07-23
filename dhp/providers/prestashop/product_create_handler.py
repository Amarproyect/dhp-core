"""
Prestashop Product Create Handler
"""

from __future__ import annotations

from dhp.kernel.command import Command
from dhp.kernel.command_handler import CommandHandler
from dhp.kernel.command_metadata import CommandMetadata
from dhp.kernel.command_result import CommandResult


class ProductCreateHandler(CommandHandler):

    @property
    def metadata(self) -> CommandMetadata:

        return CommandMetadata(

            name="product.create",

            description="Crear un producto en Prestashop",

            plugin="prestashop",

            permissions=[

                "products.write",

            ],

            tags=[

                "products",

                "prestashop",

            ],

        )

    def execute(
        self,
        command: Command,
    ) -> CommandResult:

        print("Creando producto...")

        print(command.payload)

        return CommandResult(

            success=True,

            message="Producto creado correctamente.",

            data=command.payload,

        ) 