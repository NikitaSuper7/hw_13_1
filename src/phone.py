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
        self.color = color
        self.ram = ram


emp_1 = Product('test_1', 'test_1', 255, 2)
phone_1 = Phone('iphone_15', 'the future of phones', 125_000, 112, 'green',
                255, '15_pro', 512)

print(type(emp_1))
print(type(phone_1))