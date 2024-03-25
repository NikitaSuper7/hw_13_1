import json
from config import operations_path
from category import Category
from products import Product

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
