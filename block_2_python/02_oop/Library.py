class Book:
    """Представляет книгу в библиотеке.

    Args:
        title (str): Название книги.
        author (str): ФИО автора книги.
    """

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._status = True  # защищенный атрибут: инкапсуляция статуса книги

    def __str__(self):
        """Возвращает текстовое описание книги с её текущим статусом.

        Returns:
            str: Строка с информацией о книге и её доступности.
        """
        # полиморфизм: print(book) сам выбирает этот метод, вместо стандартного __str__
        if self._status:
            text = f"Книга «{self.title}» от автора {self.author} доступна"
        else:
            text = f"Книга «{self.title}» от автора {self.author} выдана"
        return text


class Reader:
    """Представляет читателя библиотеки.

    Args:
        num_ticket (int): Номер читательского билета.
    """

    def __init__(self, num_ticket):
        self.num_ticket = num_ticket
        self._history = []  # защищенный список взятых книг(инкапсуляция)


class Library:
    """Класс библиотеки для управления всеми книгами и читателями."""

    def __init__(self):
        self.__books = []  # приватный список книг(инкапсуляция)
        self.__readers = []  # приватный список читателей(инкапсуляция)

    def add_book(self, book):
        """Добавляет книгу в базу библиотеки.

        Args:
            book (Book): Объект добавляемой книги.
        """
        self.__books.append(book)

    def register_reader(self, reader):
        """Регистрирует нового читателя в системе.

        Args:
            reader (Reader): Объект регистрируемого читателя.
        """
        self.__readers.append(reader)

    def give_book(self, book, reader):
        """Выдает книгу читателю, если она свободна и есть в базе.

        Args:
            book (Book): Запрашиваемая книга.
            reader (Reader): Читатель, запрашивающий книгу.
        """
        if book in self.__books and book._status:
            if reader in self.__readers:
                reader._history.append(book)
                book._status = False
                print(f"Книга «{book.title}» успешно выдана.")
            else:
                print("Читатель не зарегистрирован")
        else:
            print(f"Книги «{book.title}» нет в наличии.")

    def take_book(self, book, reader):
        """Принимает книгу обратно от читателя.

        Args:
            book (Book): Возвращаемая книга.
            reader (Reader): Читатель, сдающий книгу.
        """
        if book in reader._history:
            reader._history.remove(book)
            book._status = True
            print(f"Книга «{book.title}» принята.")
        else:
            print(f"Ошибка: Читатель не брал книгу «{book.title}».")

    def list_books(self):
        """Печатает все книги с номерами и статусом"""
        print("\nСписок книг:")
        num = 1
        for book in self.__books:
            print(f"{num} {book}")
            num += 1

    def get_book_index(self, index):
        """Возвращает книгу по номеру
        
        Args:
            index (int): Номер книги, который ввёл пользователь.

        Returns:
            Book | None: Книга или None, если такого номера нет.
        """
        position = index - 1
        if position < 0:
            return None
        elif position >= len(self.__books):
            return None
        else:
            return self.__books[position]


# Консольное меню:

library = Library()

book1 = Book("Преступление и наказание", "Ф.М. Достоевский")
book2 = Book("Капитанская дочка", "А.С. Пушкин")
reader1 = Reader(1)

library.add_book(book1)
library.add_book(book2)
library.register_reader(reader1)


while True:
    print("\n----- Меню управления библиотекой ----")
    print("1) Выдать книгу читателю")
    print("2) Принять книгу у читателя")
    print("3) Показать статус книг")
    print("4) Выход")

    choice = input("Выберите действие (1-4): ").strip()

    if choice == "1" or choice == "2":
        library.list_books()
        num = input("Номер книги: ")

        if not num.isdigit():
            print("Нужно ввести число!")
            continue

        book = library.get_book_index(int(num))
        if book is None:
            print("Нет книги с таким номером")
            continue

        if choice == "1":
            library.give_book(book, reader1)
        else:
            library.take_book(book, reader1)

    elif choice == "3":
        library.list_books()

    elif choice == "4":
        print("Завершение работы программы. До свидания!")
        break

    else:
        print("Неизвестная команда. Попробуйте снова.")
