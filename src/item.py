import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all = self.all.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(\'{self.__name}\', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        """
        Оставляет первые 10 символов наименования товара.
        """
        self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, csvpath='../src/items.csv'):
        """
        Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_
        """
        cls.all.clear()
        with open(csvpath, 'r', encoding='windows-1251') as file:
            data = csv.DictReader(file)
            for row in data:
                cls(row['name'], float(row['price']), cls.string_to_number(row['quantity']))

    @staticmethod
    def string_to_number(value: str) -> int:
        """
        Возвращает число из числа-строки
        """
        return int(float(value))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
