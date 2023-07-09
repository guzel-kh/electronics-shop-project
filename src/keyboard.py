from src.item import Item


class KeyboardMixin:
    """
    Класс-миксин для хранения и изменения раскладки клавиатуры
    """
    SUPPORTED_LANGUAGES = ('EN', 'RU')

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, value) -> None:
        if value not in self.SUPPORTED_LANGUAGES:
            raise ValueError('Unsupported language')
        self.__language = value

    @property
    def change_lang(self):
        """
        Меняет язык на следующий из поддерживаемых
        Возвращает self
        """
        current_language_index = self.SUPPORTED_LANGUAGES.index(self.__language)
        next_lang_index = (current_language_index + 1) % len(self.SUPPORTED_LANGUAGES)
        self.language = self.SUPPORTED_LANGUAGES[next_lang_index]
        return self


class Keyboard(Item, KeyboardMixin):
    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name=name, price=price, quantity=quantity)
        self.language = language
