from dhp.models.product import Product


class ProductService:

    FIELDS = ["id", "reference", "name", "price", "ean13", "active"]

    def __init__(self, provider):
        self.api = provider

    def list(self):
        data = self.api.products(display=self.FIELDS)["products"]

        products = []

        for item in data:
            try:
                products.append(self._to_product(item))
            except Exception:
                pass

        return products

    def search(self, text):

        text = text.lower()

        return [
            p for p in self.list()
            if text in p.name.lower()
            or text in p.reference.lower()
        ]

    def get(self, product_id):

        data = self.api.product(product_id)["product"]

        return self._to_product(data)

    @staticmethod
    def _to_product(data):
        return Product(
            id=data.get("id"),
            reference=data.get("reference", ""),
            name=data.get("name", ""),
            price=float(data.get("price", 0)),
            ean13=data.get("ean13", ""),
            active=data.get("active") == "1",
        )
