from category import Category
from products import Product
class Iter:
    def __init__(self, category: Category):
        """Принимает объект класса Category"""
        self.category = category
        self.stop = len(category)

    def __iter__(self):
        self.current_val = -1
        return self

    def __next__(self):
        if self.current_val + 1 < self.stop:
            self.current_val += 1
            return self.category.all_products[self.current_val]
        else:
            raise StopIteration


# prod_1 = Product('orange', 'very testy', 35, 20)
# prod_2 = Product('apple', 'so fresh', 730, 21)
#
# cat_1 = Category('test', 'test_test', [prod_2, prod_1])
#
# r = Iter(cat_1)
#
# print(list(r))