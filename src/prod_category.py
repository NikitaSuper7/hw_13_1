import json
from config import operations_path


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
        self.label = label
        self.description = description
        self.products = products

        add_to_products = [Category.products.append(product) for product in self.products]
        Category.labels.add(self.label)
        Category.count_uniq_labels = len(Category.labels)
        Category.cnt_products = len(products)

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

def make_products(path):
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

