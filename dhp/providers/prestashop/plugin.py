"""
Prestashop Plugin
"""

from __future__ import annotations

from dhp.kernel.plugin import Plugin
from dhp.kernel.plugin import PluginMetadata

from .product_create_handler import ProductCreateHandler


class PrestashopPlugin(Plugin):

    def __init__(self):

        super().__init__(

            PluginMetadata(

                id="prestashop",

                name="Prestashop Provider",

                version="1.0.0",

                priority=100,

                dependencies=[

                    "config",

                ],

                capabilities=[

                    "product.create",

                ],

            )

        )

    def command_handlers(self):

        return [

            ProductCreateHandler(),

        ]

    def install(self):

        print("PrestashopPlugin: install")

    def start(self):

        print("PrestashopPlugin: start")

    def stop(self):

        print("PrestashopPlugin: stop")

    def uninstall(self):

        print("PrestashopPlugin: uninstall")