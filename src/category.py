from src.products import Product
from src.abstract_category import AbstractCategory
from src.add_exception import AddProductException, ScriptException


class Category(AbstractCategory):
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

    def pud_products(self, product):
        """Добавляет один продукт, только если принадлежит классу Product."""
        try:
            prod_test = ScriptException(product)
        except AddProductException as e:
            print(e)
            print("You have to enter quantity > 0")
        else:
            if isinstance(product, Product):
                self.__products.append(product)
                Category.count_products += 1
                print("Product added successfully")
            else:
                raise TypeError("You cant pud this product")
        finally:
            print("The procedure 'add product' has finished")



    def average_price(self):
        """Возвращает среднюю стоимость товаров"""
        sum_price = 0
        for product in self.__products:
            sum_price += product.price

        try:
            result = sum_price / len(self.__products)
        except ZeroDivisionError:
            return 0
        else:
            return round(result, 1)

    @property
    def all_products(self):
        information = []
        for product in self.__products:
            information.append(
                f"{product.name}, стоимость - {product.price} руб.,Остаток - {product.quantity}")
        return information  # '\n'.join(information)

    def __repr__(self):
        return f"category_class_{self.name}"

    def __len__(self):
        return len(self.__products)

    def __str__(self):
        return f"{self.name}, количество продуктов - {self.__len__()}"


# if __name__ == '__main__':
#     cat_1 = Category('test', 'teast', [])
#     prod_1 = Product('test_p', 'test_p', 255, 1)
#
#     cat_1.pud_products(prod_1)

