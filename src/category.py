from src.products import Product

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

    def pud_products(self, products: Product):
        """Добавляет один продукт."""
        self.__products.append(products)
        Category.count_products += 1

    @property
    def all_products(self):
        information = []
        for product in self.__products:
            information.append(
                f"{product.name}, стоимость - {product.price} руб.,Остаток - {product.quantity}")
        return information#'\n'.join(information)

    def __repr__(self):
        return f"category_class_{self.name}"

    def __len__(self):
        return len(self.__products)

    def __str__(self):
        return f"{self.name}, количество продуктов - {self.__len__()}"