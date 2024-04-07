import pytest
from src.category import Category
from src.products import Product
from src.add_exception import AddProductException, ScriptException


@pytest.fixture
def products():
    prod_1 = Product('apple', 'very testy', 20.5, 3)
    prod_2 = Product('orange', 'very healthy', 33, 5)
    prod_3 = Product('banana', 'huge banana', 145, 20)
    all_prod = [prod_1, prod_2, prod_3]
    return all_prod


@pytest.fixture
def category(products):
    cat_1 = Category('Fruits', 'sweet fruits', products)
    return cat_1


@pytest.fixture
def add_incorrect_prod():
    prod_1 = Product('meat', 'Very fresh', 25_000, 45)
    prod_2 = Product('fish', 'Not fresh', 2_000, 15)
    test_1 = Category('food', 'all about food', [prod_1, prod_2])
    test_no = 'test_str'
    return test_1, test_no


@pytest.fixture
def pud_0_prod():
    prod_3 = Product('fish', 'Not fresh', 2_000, 0)
    prod_2 = Product('fish', 'Not fresh', 2_000, 15)
    test_1 = Category('food', 'all about food', [prod_2])
    return test_1, prod_3, prod_2

@pytest.fixture
def pud_product(category):
    prod_2 = Product('fish', 'Not fresh', 2_000, 15)
    category.pud_products(prod_2)
    return category


def test_category(category):
    assert category.name == 'Fruits'
    assert category.description == 'sweet fruits'


def test_pud_prod(add_incorrect_prod):
    assert add_incorrect_prod[0].all_products == ['meat, стоимость - 25000 руб.,Остаток - 45',
                                        'fish, стоимость - 2000 руб.,Остаток - 15']


def test_raise_pud_product(pud_0_prod):
    with pytest.raises(AddProductException) as e:
        test_1 = ScriptException(pud_0_prod[1])

def test_pud_product_2(pud_product):
    assert pud_product.all_products == ['apple, стоимость - 20.5 руб.,Остаток - 3',
 'orange, стоимость - 33 руб.,Остаток - 5',
 'banana, стоимость - 145 руб.,Остаток - 20',
 'fish, стоимость - 2000 руб.,Остаток - 15']


def test_avg_price(category):
    cat_test = Category('test', 'test', [])
    assert cat_test.average_price() == 0
    assert category.average_price() == 66.2
