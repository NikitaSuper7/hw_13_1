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


@pytest.fixture
def pud_products(make_prod):
    make_prod[0][0].pud_products()
    make_prod[0][1].pud_products()
    return Category.products


@pytest.fixture
def prod_price_setter(make_prod):
    make_prod[1][0].product_price = 200_000
    make_prod[1][1].product_price = 5
    return make_prod[1][0].price, make_prod[1][1].price


def test_products(products):
    assert products[0].label == 'apple'
    assert products[1].description == 'very healthy'
    assert products[2].label == 'banana'
    assert products[2].amount == 20


def test_category(category):
    assert category.label == 'Fruits'
    assert category.description == 'sweet fruits'
    assert category.count_uniq_labels == 3


def test_make_prod(make_prod):
    assert make_products(operations_path)[0][0].label == 'Смартфоны'
    assert make_products(operations_path)[0][1].label == 'Телевизоры'
    assert make_products(operations_path)[1][1].label == 'Iphone 15'
    assert make_products(operations_path)[0][1].count_uniq_labels == 3


def test_prod_price(prod_price_setter):
    assert prod_price_setter[0] == 200_000
    assert prod_price_setter[1] == 5


def test_pud_prod(pud_products):
    assert pud_products == [{'description': '256GB, Серый цвет, 200MP камера',
                             'name': 'Samsung Galaxy C23 Ultra',
                             'price': 180000.0,
                             'quantity': 5},
                            {'description': '512GB, Gray space',
                             'name': 'Iphone 15',
                             'price': 210000.0,
                             'quantity': 8},
                            {'description': '1024GB, Синий',
                             'name': 'Xiaomi Redmi Note 11',
                             'price': 31000.0,
                             'quantity': 14},
                            {'description': 'Фоновая подсветка',
                             'name': '55" QLED 4K',
                             'price': 123000.0,
                             'quantity': 7}]
