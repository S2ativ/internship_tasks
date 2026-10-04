class Book:
    """Представляет книгу в библиотечной системе.

    Args:
        title (str): Название книги.
        author (str): Автор книги.
        isbn (str): Уникальный международный номер книги (ISBN).
    """

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False

    def check_out(self):
        """Выдает книгу абоненту, если она доступна."""
        if self.checked_out:
            print("Книга находится у абонента.")
        else:
            self.checked_out = True
            print("Выдаем книгу абоненту.")

    def check_in(self):
        """Принимает книгу обратно от абонента."""
        if not self.checked_out:
            print("Книга в наличии.")
        else:
            self.checked_out = False
            print("Принимаем книгу в библиотеку.")


# Проверка работы:
book1 = Book("Война и мир", "Л.Н. Толстой", "978-0743273565")

book1.check_out()
book1.check_out()

book1.check_in()
book1.check_in()
