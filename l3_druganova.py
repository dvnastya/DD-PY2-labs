class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):
    """ Дочерний класс книги. """
    def __init__(self, name: str, author: str, pages: int):

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целочисленной")

        if not pages > 0:
            raise ValueError("Количество страниц должно быть положительной")

        self.pages = pages
        super().__init__(name, author)

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """ Дочерний класс книги. """
    def __init__(self, name: str, author: str, duration: float):

        if not isinstance(duration, float):
            raise TypeError("Длительность должна быть числом с плавающей запятой")

        if not duration > 0:
            raise ValueError("Длительность должна быть положительной")

        self.duration = duration

        super().__init__(name, author)

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}. Длительность {self.duration} часов"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

