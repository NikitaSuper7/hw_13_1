from src.products import Product


class GreenGrass(Product):
    """Класс для продуктов категории 'Трава зеленая'."""

    name: str
    description: str
    price: float
    quantity: int
    color: str
    country: str
    period: float

    def __init__(self, name: str, description: str, price: float, quantity: int, color: str, country: str,
                 period: float):
        super().__init__(name, description, price, quantity, color)

        self.period = period
        self.country = country
