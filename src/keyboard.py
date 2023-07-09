from src.item import Item


class KeyboardMixin:
    """
    Класс-миксин для хранения и изменения раскладки клавиатуры
    """
    def __init__(self) -> None:
        self.__language = "EN"

    @property
    def language(self) -> None:
        return self.__language

    @property
    def change_lang(self):
        """
        Меняет язык на другой из двух доступных(RU и EN)
        Возвращает self
        """
        if self.language == "EN":
            self.__language = "RU"
        elif self.language == "RU":
            self.__language = "EN"
        return self


class Keyboard(Item, KeyboardMixin):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        KeyboardMixin.__init__(self)
