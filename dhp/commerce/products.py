from dhp.services.product_service import ProductService


class Products:

    def __init__(self):
        self.service = ProductService()

    def list(self):

        print()
        print(f"{'ID':<10} {'REF':<12} {'PRECIO':>10}   NOMBRE")
        print("-" * 80)

        for p in self.service.list():
            print(f"{p.id:<10} {p.reference:<12} {p.price:>10.2f}   {p.name}")

        print()

    def get(self, product_id):

        p = self.service.get(int(product_id))

        print()
        print(f"ID         : {p.id}")
        print(f"Referencia : {p.reference}")
        print(f"Nombre     : {p.name}")
        print(f"Precio     : {p.price:.2f} €")
        print(f"EAN13      : {p.ean13}")
        print(f"Activo     : {'Sí' if p.active else 'No'}")
        print()
