from abc import ABC, abstractmethod


class Book(ABC):
    """Абстрактный класс для всех типов книг.

    Args:
        title (str): Название книги.
        author (str): Автор книги.
    """

    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def get_summary(self):
        """Выводит краткое описание книги.

        Обязателен к переопределению во всех дочерних классах.
        """
        pass


class Fiction(Book):
    """Представляет художественную литературу."""

    def get_summary(self):
        """Выводит описание художественной книги."""
        print(
            f'"{self.title}" - роман в стиле исторический фикшн, автор - {self.author}'
        )


class NonFiction(Book):
    """Представляет научно-популярную литературу."""

    def get_summary(self):
        """Выводит описание научно-популярной книги."""
        print(f'"{self.title}" - книга в стиле нон-фикшн, автор - {self.author}')


class Poetry(Book):
    """Представляет поэзию.

    Класс является абстрактным, т.к. метод get_summary не переопределен.
    """

    pass


# Проверка работы:
fiction_book = Fiction("Террор", "Дэн Симмонс")
nonfiction_book = NonFiction("Как писать книги", "Стивен Кинг")

fiction_book.get_summary()
nonfiction_book.get_summary()