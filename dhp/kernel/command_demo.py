"""
Demo CommandBus
"""

from __future__ import annotations

from dhp.kernel.command import Command
from dhp.kernel.command_bus import CommandBus
from dhp.kernel.logger_middleware import LoggerMiddleware

from dhp.providers.prestashop.product_create_handler import (
    ProductCreateHandler,
)


def main():

    bus = CommandBus()

    bus.add_middleware(
        LoggerMiddleware()
    )

    bus.register(
        ProductCreateHandler()
    )

    result = bus.execute(

        Command(

            "product.create",

            {

                "reference": "ABC001",

                "name": "Producto",

                "price": 19.95,

            },

        )

    )

    print(result)


if __name__ == "__main__":

    main()