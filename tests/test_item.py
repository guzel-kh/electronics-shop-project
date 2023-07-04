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


# TestCase#4 Name length
def test_name(item_test):
    assert len(item_test.name) <= 10
    item_test.name = 'СуперСмартфон'
    assert item_test.name == 'СуперСмарт'


# TestCase#5 object from csv
def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item1 = Item.all[4]
    assert item1.name == 'Клавиатура'
    assert item1.price == 75
    assert item1.quantity == 5


# TestCase#6 String to number
def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.6') == 5
