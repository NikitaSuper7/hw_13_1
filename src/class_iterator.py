from src.category import Category
from src.products import Product
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

