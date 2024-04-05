import pytest
from src.order import Order
from src.products import Product


@pytest.fixture
def product():
    prod_1 = Product('apple', 'very testy', 20.5, 3)
    prod_2 = Product('orange', 'very healthy', 32.5, 5)
    return prod_1, prod_2


@pytest.fixture
def order(product):
    order_1 = Order(product[0])
    return order_1
@pytest.fixture
def pud_products_order(order, product):
    order.pud_products(product[1])
    return order

def test_orders(order):
    assert order.name == 'apple'
    assert order.price == 20.5

def test_pud_products(pud_products_order):
    assert pud_products_order.name == 'orange'
    assert pud_products_order.price == 32.5

