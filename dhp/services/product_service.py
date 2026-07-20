from dhp.models.product import Product


class ProductService:

    def __init__(self, provider):
        self.api = provider

    def count(self):
        return self.api.product_count()

    def list(self):
        data = self.api.products()["products"]

        products = []

        for item in data:
            try:
                products.append(self.get(item["id"]))
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

        return Product(
            id=data.get("id"),
            reference=data.get("reference", ""),
            name=data.get("name", ""),
            price=float(data.get("price", 0)),
            ean13=data.get("ean13", ""),
            active=data.get("active") == "1",
        )

    def exists(self, product_id):
        try:
            self.get(product_id)
            return True
        except Exception:
            return False