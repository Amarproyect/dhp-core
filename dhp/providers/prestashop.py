import requests

from dhp.providers.provider import Provider
from dhp.providers.base import ProductProvider


class PrestaShop(Provider, ProductProvider):

    def __init__(self, url, api_key):
        super().__init__(url, api_key)

    def _get(self, resource, display=None):
        base = self.url.rstrip("/")
        if not base.endswith("/api"):
            base += "/api"
        params = {}
        if display:
            params["display"] = f"[{','.join(display)}]"
        r = requests.get(
            f"{base}/{resource}",
            params=params,
            auth=(self.api_key, ""),
            headers={"Output-Format": "JSON"},
            timeout=20,
        )

        r.raise_for_status()
        return r.json()

    def products(self, display=None):
        return self._get("products", display=display)

    def product(self, product_id):
        return self._get(f"products/{product_id}")
