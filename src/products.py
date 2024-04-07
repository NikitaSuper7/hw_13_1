from src.abstract_product import AbstrProduct
from src.mixin_name import MixinName


class Product(AbstrProduct, MixinName):
    """product that we have in our store."""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int, color: str = None):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color

    @classmethod
    def build_product(cls, dictionary: dict):
        """Создает объект класса Product из словаря.
        ключи:
        name - название продукта (str)
        description - описание (str).
        price - цена (float),.
        quantity - количество (int)"""
        return cls(**dictionary)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > self.__price and new_price > 0:
            self.__price = new_price
        elif 0 < new_price <= self.__price:
            question = input("Are you sure that you want to reduce a price?(y/n) ").strip().lower()
            if question == 'y':
                self.__price = new_price
        else:
            print("You put incorrect price")

    def __add__(self, other):
        if type(self) == type(other):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError('Можно складывать только товары принадлежащие к одному классу.')

    def __str__(self):
        return f"{self.name}, стоимость - {self.price} руб.,Остаток - {self.quantity}"
