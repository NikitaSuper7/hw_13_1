from src.products import Product

class AddProductException(Exception):
    """Исключение добавление пустого продукта."""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Невозвожно добавить продукт с нулевым количеством'

    def __str__(self):
        return self.message


class ScriptException:
    def __init__(self, product: Product):
        if product.quantity <= 0:
            raise AddProductException()

