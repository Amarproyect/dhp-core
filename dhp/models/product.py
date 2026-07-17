from dataclasses import dataclass


@dataclass
class Product:
    id: int
    reference: str
    name: str
    price: float
    ean13: str
    active: bool
