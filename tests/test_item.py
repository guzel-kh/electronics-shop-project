"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item_test():
    return Item("Ноутбук", 20000, 5)


# TestCase#1  Total Price
def test_calculate_total_price(item_test):
    assert item_test.calculate_total_price() == 100000


# TestCase#3 Apply Discount
def test_apply_discount(item_test):
    Item.pay_rate = 0.5
    item_test.apply_discount()
    assert 20000 * Item.pay_rate == item_test.price
    assert item_test.price == 10000
