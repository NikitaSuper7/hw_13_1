import pytest
from src.grass import GreenGrass


@pytest.fixture
def phone():
    phone_1 = GreenGrass('grass_1', 'premier', 100, 250, 'orange',
                         'Spain', 3)

    phone_2 = GreenGrass('grass_2', 'first_class', 250, 170, 'blue',
                         'Russia', 1)

    return phone_1, phone_2


def test_phone(phone):
    assert phone[0].name == 'grass_1'
    assert phone[0].period == 3
    assert phone[1].description == 'first_class'
    assert phone[1].country == 'Russia'
