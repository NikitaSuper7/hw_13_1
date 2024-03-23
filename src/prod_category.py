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


    def pud_products(self, products):
        """Добавляет продукты в атрибут класса - products."""
        for product in products:
            product = {'name': product.name,
                       'description': product.description,
                       'price': product.price,
                       'quantity': product.amount}
            self.__products.append(product)
            Category.count_products += 1
        return self.__products

    @property
    def all_products(self):
        information = []
        for product in self.__products:
            information.append(f"{product['name']}, стоимость - {product['price']} руб.,Остаток - {product['quantity']}")
        return information

    def __repr__(self):
        return f"category_class - {self.name}"


class Product:
    """product that we have in our store."""
    name: str
    description: str
    price: float
    amount: int

    def __init__(self, name, description, price, amount):
        self.name = name
        self.description = description
        self.__price = price
        self.amount = amount

    def __repr__(self):
        return f"product_class - {self.name}"

    @classmethod
    def build_product(cls, dictionary: dict):
        """Создает объект класса Product из словаря.
        ключи:
        name - название продукта (str)
        description - описание (str).
        price - цена (float),.
        amount - количество (int)"""
        return cls(**dictionary)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > self.__price and new_price is float:
            self.__price = new_price
        elif new_price <= self.__price:
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
    products = []
    for category in json_file:
        categories.append(category['name'])
        categories[-1] = Category(category['name'], category['description'], category['products'])
        for product in category['products']:
            products.append(product['name'])
            products[-1] = Product(product['name'], product['description'], product['price'], product['quantity'])
    categories = list(dict.fromkeys(categories))  # возвращает уникальные элементы списка, сохраняя порядок.

    return (categories, products)
