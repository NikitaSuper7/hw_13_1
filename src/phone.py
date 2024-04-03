from src.products import Product
from src.mixin_name import MixinName


class Phone(Product, MixinName):
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


test_1 = Phone('iphone_15', 'best_one', 125_000, 14, 'blue', 255,
               'test_x_1', 512)
print(repr(test_1))
