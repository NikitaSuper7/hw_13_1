from src.category import Category
from src.products import Product
from src.class_iterator import Iter
import pytest

@pytest.fixture
def products():
    prod_1 = Product('apple', 'very testy', 20.5, 3)
    prod_2 = Product('orange', 'very healthy', 32.5, 5)
    prod_3 = Product('banana', 'huge banana', 145, 20)
    all_prod = [prod_1, prod_2, prod_3]
    return all_prod

@pytest.fixture
def category(products):
    category_1 = Category('food', 'fresh food', products)
    return category_1

@pytest.fixture
def iteration(category):
    test_1 = Iter(category)
    return test_1

def test_iter(iteration):
    assert list(iteration) == ['apple, стоимость - 20.5 руб.,Остаток - 3',
 'orange, стоимость - 32.5 руб.,Остаток - 5',
 'banana, стоимость - 145 руб.,Остаток - 20']