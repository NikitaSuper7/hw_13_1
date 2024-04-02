from src.products import Product


class Phone(Product):
    """продукты категории 'Смартфоны'. """
    name: str
    description: str
    price: float
    quantity: int
    performance: float
    ram: int
    model: str
    color: str

    def __init__(self, name: str, description: str, price: int, quantity: int, color: str, performance: float,
                 model: str, ram: int):
        super().__init__(name, description, price, quantity, color)

        self.performance = performance
        self.ram = ram
        self.model = model

