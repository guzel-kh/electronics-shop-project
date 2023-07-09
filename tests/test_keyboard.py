import pytest


from src.keyboard import Keyboard


@pytest.fixture
def kb_test():
    return Keyboard('Dark Project KD87A', 9600, 5)


# TestCase #1 Инициализация
def test_init(kb_test):
    assert kb_test.name == 'Dark Project KD87A'
    assert kb_test.price == 9600
    assert kb_test.quantity == 5
    assert kb_test.language == "EN"


# TestCase #2 Change language
def test_change_lang(kb_test):
    kb_test.change_lang
    assert kb_test.language == 'RU'
    kb_test.change_lang.change_lang
    assert kb_test.language == 'RU'
    with pytest.raises(ValueError):
        kb_test.language = "CH"
