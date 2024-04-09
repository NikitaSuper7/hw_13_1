from src.abstract_category import AbstractCategory
from src.products import Product
from src.add_exception import AddMuchProductException, AddProductException, ScriptException


class Order(AbstractCategory):
    def __init__(self, product: Product, count: int):
        try:
            ScriptException(product, count=count)
        except AddProductException as e:
            print(e)
            print("You have to enter quantity > 0")
            raise AddProductException()
        except AddMuchProductException as e:
            print(e)
            print(f"Please order this product in quantity <= {product.quantity}")
            raise AddMuchProductException()
        else:
            self.product = product # ссылка на то, какой товар был куплен
            self.price = product.price * count  # итоговая стоимость
            self.count = count  # количество купленного товара
            print("Product added successfully")
        finally:
            print("The procedure 'add product' has finished")

    def pud_products(self, new_prod: Product, count):
        """Кладет продукт в заказ. При наличие в заказе продукта, заменяет его на новый."""
        try:
            ScriptException(new_prod, count=count)
        except AddProductException as e:
            print(e)
            print("You have to enter quantity > 0")
            raise AddProductException()
        except AddMuchProductException as e:
            print(e)
            print(f"Please order this product in quantity <= {new_prod.quantity}")
            raise AddMuchProductException()
        else:
            self.product = new_prod  # ссылка на то, какой товар был куплен
            self.price = new_prod.price * count  # итоговая стоимость
            self.count = count  # количество купленного товара
            print("Product added successfully")
        finally:
            print("The procedure 'add product' has finished")


# if __name__ == '__main__':
#     prod_1 = Product('apple', 'very testy', 20.5, 3)
#     prod_2 = Product('orange', 'very healthy', 32.5, 0)
#     prod_3 = Product('banana', 'huge banana', 145, 20)
#
#     order_1 = Order(prod_2, 2)

