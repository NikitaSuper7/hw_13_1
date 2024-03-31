import pytest
from src.category import Category
from src.products import Product


@pytest.fixture
def products():
    prod_1 = Product('apple', 'very testy', 20.5, 3)
    prod_2 = Product('orange', 'very healthy', 32.5, 5)
    prod_3 = Product('banana', 'huge banana', 145, 20)
    all_prod = [prod_1, prod_2, prod_3]
    return all_prod


@pytest.fixture
def category(products):
    cat_1 = Category('Fruits', 'sweet fruits', products)
    return cat_1


@pytest.fixture
def pud_prod():
    prod_1 = Product('meat', 'Very fresh', 25_000, 45)
    prod_2 = Product('fish', 'Not fresh', 2_000, 15)
    test_1 = Category('food', 'all about food', [prod_1, prod_2])
    test_1.pud_products(prod_2)
    return test_1.all_products


def test_category(category):
    assert category.name == 'Fruits'
    assert category.description == 'sweet fruits'


def test_pud_prod(pud_prod):
    assert pud_prod == ['meat, стоимость - 25000 руб.,Остаток - 45', 'fish, стоимость - 2000 руб.,Остаток - 15',
                        'fish, стоимость - 2000 руб.,Остаток - 15']
