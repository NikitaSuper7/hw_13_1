
import pytest
from src.phone import Phone

@pytest.fixture
def phone():
    phone_1 = Phone('iphone_15', 'the future of phones', 125_000, 112, 'green',
                    255, '15_pro', 512)

    phone_2 = Phone('honor_50', 'usual phone', 50_000, 11, 'blue',
                    115, 'honor_50_bfx', 128)

    return phone_1, phone_2

def test_phone(phone):
    assert phone[0].name == 'iphone_15'
    assert phone[1].color == 'blue'
    assert phone[1].ram == 128


