import pytest
from src.products import Product
from src.phone import Phone

@pytest.fixture
def products():
    prod_1 = Product('apple', 'very testy', 20.5, 3)
    prod_2 = Product('orange', 'very healthy', 32.5, 5)
    prod_3 = Product('banana', 'huge banana', 145, 20)
    all_prod = [prod_1, prod_2, prod_3]
    return all_prod

@pytest.fixture
def prod_price_setter():
    prod_1 = Product('orange', 'so tasty', 75, 12)
    prod_2 = Product('apple', 'green sort', 32, 5)
    prod_1.price = 80
    prod_2.price = 30
    return prod_1.price, prod_2.price

@pytest.fixture
def add_method():
    prod_1 = Product('apple', 'very testy', 20.5, 3)
    prod_2 = Product('apple', 'green sort', 32, 5)
    phone_1 = Phone('honor_50', 'usual phone', 50_000, 11, 'blue',
                    115, 'honor_50_bfx', 128)
    return prod_1, phone_1, prod_2

def test_products(products):
    assert products[0].name == 'apple'
    assert products[1].description == 'very healthy'
    assert products[2].name == 'banana'
    assert products[2].quantity == 20


def test_prod_price(prod_price_setter):
    assert prod_price_setter[0] == 80
    assert prod_price_setter[1] == 32

def test_add_method(add_method):
    assert add_method[0] + add_method[2] == 221.5
    with pytest.raises(TypeError):
        add_method[0] + add_method[1]
