import pytest
from src.products import Product
from src.category import Category
from config import operations_path
from src.main import make_products


@pytest.fixture
def make_prod():
    make_1 = make_products(operations_path)
    return make_1

def test_make_prod(make_prod):
    assert make_products(operations_path)[0].name == 'Смартфоны'
    assert make_products(operations_path)[1].name == 'Телевизоры'
    assert make_products(operations_path)[
               1].description == 'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником'
