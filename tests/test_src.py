import pytest
from src.prod_category import Product, Category, make_products
from config import operations_path


@pytest.fixture
def products():
    prod_1 = Product('apple', 'very testy', 20.5, 3)
    prod_2 = Product('orange', 'very healthy', 32.5, 5)
    prod_3 = Product('banana', 'huge banana', 145, 20)
    return prod_1, prod_2, prod_3

@pytest.fixture
def category(products):
    cat_1 = Category('Fruits', 'sweet fruits', products)
    return cat_1

@pytest.fixture
def make_prod():
    make_1 = make_products(operations_path)
    return make_1

def test_products(products):
    assert products[0].label == 'apple'
    assert products[1].description == 'very healthy'
    assert products[2].label == 'banana'
    assert products[2].amount == 20

def test_category(category):
    assert category.label =='Fruits'
    assert category.description == 'sweet fruits'
    assert category.count_uniq_labels == 1

def test_make_prod(make_prod):
    assert make_products(operations_path)[0][0].label == 'Смартфоны'
    assert make_products(operations_path)[0][1].label == 'Телевизоры'
    assert make_products(operations_path)[1][1].label == 'Iphone 15'
    assert make_products(operations_path)[0][1].count_uniq_labels == 3
