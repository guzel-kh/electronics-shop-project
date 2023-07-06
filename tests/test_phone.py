import pytest

from src.phone import Phone


@pytest.fixture
def phone_test():
    return Phone("iPhone 14", 120_000, 5, 2)


# TestCase #1 Инициализация
def test_init(phone_test):
    assert phone_test.name == "iPhone 14"
    assert phone_test.price == 120_000
    assert phone_test.quantity == 5
    assert phone_test.number_of_sim == 2
    with pytest.raises(ValueError):
        Phone("iPhone 14", 120_000, 5, 0)


# TestCase #2 Str
def test_str(phone_test):
    assert str(phone_test) == 'iPhone 14'


# TestCase #3 Repr
def test_repr(phone_test):
    assert repr(phone_test) == "Phone('iPhone 14', 120000, 5, 2)"
