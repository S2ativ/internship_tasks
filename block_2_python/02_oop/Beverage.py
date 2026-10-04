class Beverage:
    """Класс газировки для всех видов.

    Args:
        name (str): Название газировки.
        size (float | int): Объем газировки.
        price (int): Цена газировки.
    """

    def __init__(self, name, size, price):
        self._name = name
        self._size = size
        self._price = price

    def get_name(self):
        """Возвращает название газировки.

        Returns:
            str: Название газировки.
        """
        return self._name

    def get_size(self):
        """Возвращает объем газировки.

        Returns:
            float | int: Объем газировки.
        """
        return self._size

    def get_price(self):
        """Возвращает цену газировки.

        Returns:
            int: Цена газировки.
        """
        return self._price

    def set_price(self, price):
        """Устанавливает новую цену на газировку.

        Args:
            price (int): Новая цена газировки.
        """
        self._price = price

    def describe(self):
        """Возвращает текстовое описание газировки.

        Returns:
            str: Описание газировки со всеми параметрами.
        """
        return f'{self._size} л газировки "{self._name}" стоит {self._price} руб'


class Soda(Beverage):
    """Представляет обычную газировку с добавлением вкуса.

    Args:
        name (str): Название газировки.
        size (float | int): Объем газировки.
        price (int): Цена газировки.
        flavor (str): Вкус газировки.
    """

    def __init__(self, name, size, price, flavor):
        super().__init__(name, size, price)
        self._flavor = flavor

    def get_flavor(self):
        """Возвращает вкус газировки.

        Returns:
            str: Вкус газировки.
        """
        return self._flavor

    def describe(self):
        """Возвращает текстовое описание газировки со вкусом.

        Returns:
            str: Описание газировки со всеми параметрами, включая вкус.
        """
        return f'{self._size} л газировки "{self._name}" со вкусом "{self._flavor}" стоит {self._price} руб.'


class DietSoda(Soda):
    """Представляет диетическую газировку (без сахара).

    Args:
        name (str): Название газировки.
        size (float | int): Объем газировки.
        price (int): Цена газировки.
        flavor (str): Вкус газировки.
    """

    def __init__(self, name, size, price, flavor):
        super().__init__(name, size, price, flavor)

    def describe(self):
        """Возвращает текстовое описание диетической газировки (без сахара).

        Returns:
            str: Описание газировки со всеми параметрами, включая указание, что она диетическая.
        """
        return f'{self._size} л диетической газировки "{self._name}" со вкусом "{self._flavor}" стоит {self._price} руб. '


regular_soda = Soda("Sprite", 0.33, 45, "лимон")
print(regular_soda.describe())

diet_soda = DietSoda("Mirinda", 0.33, 50, "мандарин")
print(diet_soda.describe())

regular_soda = Soda("Буратино", 1.5, 65, "дюшес")
print(regular_soda.describe())