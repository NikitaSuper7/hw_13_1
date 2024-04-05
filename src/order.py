from src.abstract_category import AbstractCategory
from src.products import Product


class Order(AbstractCategory):
    def __init__(self, order: Product):
        self.name = order.name
        self.description = order.description
        self.price = order.price
        self.quantity = order.quantity
        self.color = order.color

    def pud_products(self, new_prod: Product):
        """Кладет продукт в заказ. При наличие в заказе продукта, заменяет его на новый."""
        self.name = new_prod.name
        self.description = new_prod.description
        self.price = new_prod.price
        self.quantity = new_prod.quantity
        self.color = new_prod.color


# prod_1 = Product('apple', 'very testy', 20.5, 3)
# prod_2 = Product('orange', 'very healthy', 32.5, 5)
# prod_3 = Product('banana', 'huge banana', 145, 20)
#
# order_1 = Order(prod_1)
# print(order_1.name)
#
# order_1.pud_products(prod_2)
# print(order_1.name)
