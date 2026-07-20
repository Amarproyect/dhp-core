from abc import ABC, abstractmethod


class ProductProvider(ABC):

    @abstractmethod
    def products(self):
        """Return all products."""
        raise NotImplementedError

    @abstractmethod
    def product(self, product_id):
        """Return a single product."""
        raise NotImplementedError

    def product_count(self):
        return len(self.products()["products"])