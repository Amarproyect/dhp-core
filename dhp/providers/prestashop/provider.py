import requests

from dhp.providers.provider import Provider
from dhp.providers.base import ProductProvider


class PrestaShop(Provider, ProductProvider):

    def __init__(self, url, api_key):
        super().__init__(url, api_key)

    def _get(self, resource):
        r = requests.get(
            f"{self.url}/webservice/dispatcher.php",
            params={"url": resource},
            auth=(self.api_key, ""),
            headers={
                "Host": "82.70.94.106",
                "Output-Format": "JSON",
            },
            timeout=20,
        )

        r.raise_for_status()
        return r.json()

    def products(self):
        return self._get("products")

    def product(self, product_id):
        return self._get(f"products/{product_id}")