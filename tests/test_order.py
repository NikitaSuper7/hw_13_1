import pytest
from src.order import Order
from src.products import Product
from src.add_exception import AddMuchProductException, AddProductException, ScriptException, MyException


@pytest.fixture
def product():
    prod_1 = Product('apple', 'very testy', 20.5, 3)
    prod_2 = Product('orange', 'very healthy', 32.5, 5)
    return prod_1, prod_2


@pytest.fixture
def order(product):
    order_1 = Order(product[0], 1)
    return order_1


@pytest.fixture
def pud_products_order(order, product):
    order.pud_products(product[1], 1)
    return order


@pytest.fixture
def product_0_quan():
    product_1 = Product('apple', 'very testy', 20.5, 0)
    return product_1


def test_orders(order):
    assert order.count == 1
    assert order.price == 20.5


def test_pud_products(pud_products_order):
    assert pud_products_order.count == 1
    assert pud_products_order.price == 32.5


def test_rais_0_quan(product_0_quan):
    with pytest.raises(AddProductException):
        Order(product_0_quan, 1)


def test_rais_to_much_prod(product, order):
    with pytest.raises(AddMuchProductException):
        order.pud_products(product[0], 125)
