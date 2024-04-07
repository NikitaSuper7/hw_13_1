from src.products import Product


class MyException(Exception):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Script error'

    def __str__(self):
        return self.message


class AddProductException(MyException):
    """Исключение добавление пустого продукта."""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'You cannot add product with 0 quantity'

    def __str__(self):
        return self.message


class AddMuchProductException(MyException):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'You order more product then we have'

    def __str__(self):
        return self.message


class ScriptException:
    def __init__(self, product: Product, count=0):
        if product.quantity <= 0:
            raise AddProductException()
        elif product.quantity <= count:
            raise AddMuchProductException()
