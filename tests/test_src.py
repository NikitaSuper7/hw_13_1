import pytest
from src.prod_category import Product, Category, make_products
from config import operations_path


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
def make_prod():
    make_1 = make_products(operations_path)
    return make_1


@pytest.fixture
def pud_prod(make_prod):
    prod_1 = Product('meat', 'Very fresh', 25_000, 45)
    prod_2 = Product('fish', 'Not fresh', 2_000, 15)
    test_1 = make_prod
    test_2 = make_prod
    test_1[0][0].pud_products([prod_2, prod_1])
    test_2[0][1].pud_products([prod_1])
    return test_1[0][0].all_products, test_2[0][1].all_products


@pytest.fixture
def prod_price_setter(make_prod):
    make_prod[1][0].product_price = 200_000
    make_prod[1][1].product_price = 5
    return make_prod[1][0].price, make_prod[1][1].price


def test_products(products):
    assert products[0].name == 'apple'
    assert products[1].description == 'very healthy'
    assert products[2].name == 'banana'
    assert products[2].amount == 20


def test_category(category):
    assert category.name == 'Fruits'
    assert category.description == 'sweet fruits'


def test_make_prod(make_prod):
    assert make_products(operations_path)[0][0].name == 'Смартфоны'
    assert make_products(operations_path)[0][1].name == 'Телевизоры'
    assert make_products(operations_path)[1][1].name == 'Iphone 15'


def test_prod_price(prod_price_setter):
    assert prod_price_setter[0] == 180000
    assert prod_price_setter[1] == 210_000


def test_pud_prod(pud_prod):
    assert pud_prod[0] == [
        'Samsung Galaxy C23 Ultra, стоимость - 180000.0 руб.,Остаток - 5',
        'Iphone 15, стоимость - 210000.0 руб.,Остаток - 8',
        'Xiaomi Redmi Note 11, стоимость - 31000.0 руб.,Остаток - 14',
        'fish, стоимость - 2000 руб.,Остаток - 15',
        'meat, стоимость - 25000 руб.,Остаток - 45',
    ]
