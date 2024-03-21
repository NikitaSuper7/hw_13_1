import json
from config import operations_path # - Здесь находится файл с продуктами


class Category:
    """Product category of our store."""
    labels: set
    description: str
    products: list

    products = []
    labels = set()

    cnt_products = len(products)

    count_uniq_labels = len(labels)


    def __init__(self, label, description, products):
        """Инициализирует объект класса Category."""
        self.label = label
        self.description = description
        self.__products = products

        # add_to_products = [Category.products.append(product) for product in self.products]
        Category.labels.add(self.label)
        Category.count_uniq_labels = len(Category.labels)
        Category.cnt_products = len(Category.products)

    def pud_products(self):
        """Добавляет продукты в атрибут класса - products."""
        for product in self.__products:
            Category.products.append(product)
            Category.count_uniq_labels = len(Category.labels)
            Category.cnt_products = len(Category.products)
        return Category.products

    @property
    def all_products(self):
        for product in Category.products:
            print(f"Продукт - {product['name']}.\nЦена - {product['price']}.\nОстаток - {product['quantity']}")
        return Category.products

    def __repr__(self):
        return f"category_class - {self.label}"

class Product:
    """product that we have in our store."""
    label: str
    description: str
    price: float
    amount: int

    def __init__(self, label, description, price, amount):
        self.label = label
        self.description = description
        self.price = price
        self.amount = amount

    def __repr__(self):
        return f"product_class - {self.label}"

    @classmethod
    def build_product(cls, string: str):
        """Создает объект класса Product из строки формата - 'название-описание-стоимость-остаток'"""
        label, description, price, amount = string.split('-')
        amount = int(amount)
        price = float(price)
        return cls(label, description, price, amount)

    @property
    def product_price(self):
        return f"Название - {self.label}, Стоимость товара - {self.price}"

    @product_price.setter
    def product_price(self, new_price):
        while new_price < 0 and new_price is not float:
            print("You put incorrect price, please enter new price")
            new_price = float(input("enter new price in float format: "))
        if new_price < self.price:
            answer = input("Are you sure that you want to reduce cost?(y/n):").strip().lower()
            if answer == 'y':
                self.price = new_price
                return self.price
            else:
                return self.price
        else:
            self.price = new_price
        return self.price



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

test_1 = make_products(operations_path)


