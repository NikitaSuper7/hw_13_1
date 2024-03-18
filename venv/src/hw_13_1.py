import json
from venv.config import operations_path


def main():
    class Category:
        """Product category of our store."""
        labels: set
        description: str
        products: list

        products = []
        labels = set()

        @classmethod
        def uniq_products(cls):
            return len(cls.products)

        @classmethod
        def count_labels(cls):
            return len(cls.labels)

        def __init__(self, label, description, products):
            self.label = label
            self.description = description
            self.products = products

            add_to_products = [Category.products.append(product) for product in self.products]
            Category.labels.add(self.label)

        def __repr__(self):
            return f"category class - {self.label}"

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
            return f"product class - {self.label}"

    def make_products():
        with open(operations_path, encoding='utf-8') as f:
            content = f.read()
            json_file = json.loads(content)
        # test_1 = json_file[0]['products']
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


if __name__ == '__main__':
    main()
