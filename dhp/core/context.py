from dhp.core.config import settings
from dhp.providers.prestashop import PrestaShop
from dhp.services.product_service import ProductService


class DHP:
    def __init__(self):
        provider = PrestaShop(
            url=settings.prestashop_url,
            api_key=settings.prestashop_api_key,
        )

        self.products = ProductService(provider)