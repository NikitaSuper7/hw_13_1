import json
from config import operations_path  # - Здесь находится файл с продуктами


class Category:
    """Product category of our store."""
    names: str
    description: str
    products: list
    categories = set()
    count_categories = 0
    count_products = 0

    def __init__(self, name: str, description: str, products: list):
        """Инициализирует объект класса Category."""
        self.name = name
        self.description = description
        self.__products = products
        Category.categories.add(self.name)

        Category.count_categories = len(Category.categories)
        Category.count_products += len(self.__products)

    def pud_products(self, products: list):
        """Добавляет продукты в атрибут класса - products."""
        for product in products:
            self.__products.append(product)

    @property
    def all_products(self):
        information = []
        for product in self.__products:
            information.append(
                f"{product.name}, стоимость - {product.price} руб.,Остаток - {product.quantity}")
        return '\n'.join(information)

    def __repr__(self):
        return f"category_class_{self.name}"

    def __str__(self):
        return f"{self.name}"


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
        if new_price > self.__price and new_price is float:
            self.__price = new_price
        elif 0 < new_price <= self.__price:
            question = input("Are you sure that you want to reduce a price?(y/n) ").strip().lower()
            if question == 'y':
                self.__price = new_price
        else:
            print("You put incorrect price")


def make_products(path):
    """Создает объекты классов Category и Products из файла json."""
    with open(path, encoding='utf-8') as f:
        content = f.read()
        json_file = json.loads(content)
    categories = []
    for category_info in json_file:
        products = []
        for product_info in category_info['products']:
            product = Product.build_product(product_info)
            products.append(product)
        category = Category(category_info['name'], category_info['description'], products)
        categories.append(category)
    return categories





