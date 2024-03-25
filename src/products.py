
class Product:
    """product that we have in our store."""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __repr__(self):
        return f"product_class_{self.name}"

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
        return self.__price * self.quantity + other.__price * other.quantity

    def __str__(self):
        return f"{self.name}, стоимость - {self.price} руб.,Остаток - {self.quantity}"