BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id: int, name: str, pages: int):
        self.id = id  # идентификатор книги
        self.name = name  # название книги
        self.pages = pages  # количество страниц в книге

    def __str__(self):
        return f'Книга(id={self.id}, name="{self.name}", pages={self.pages})'

    def __repr__(self):
        return f'Book(id={self.id}, name="{self.name}", pages={self.pages})'


class Library:
    def __init__(self, books=None):
        self.books = books or []

    def get_next_book_id(self):
        """Возвращает идентификатор для добавления новой книги в библиотеку."""
        if not self.books:
            return 1  # возвращаем 1 тк нет книг
        else:
            return max(book.id for book in self.books) + 1  # возвращаем id последней книги + 1

    def get_index_by_book_id(self, book_id):
        """Возвращает индекс книги в списке по её идентификатору."""
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index  # возвращаем индекс, если книга найдена
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

