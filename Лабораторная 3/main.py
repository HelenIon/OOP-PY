class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(_name={self._name!r}, _author={self._author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = None
        self.set_pages(pages)

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. " \
               f"Количество страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(_name={self._name!r}, _author={self._author!r}, " \
               f"_pages={self._pages!r})"

    def set_pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError("Число страниц должно иметь целочисленный тип (int)")
        if pages < 1:
            raise ValueError("Число страниц должно быть больше 0")
        self._pages = pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = None
        self.set_duration(duration)

    def __str__(self):
        return f"Аудиокнига {self._name}. Автор {self._author}. " \
               f"Продолжительность: {self._duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(_name={self._name!r}, _author={self._author!r}, " \
               f"_duration={self._duration!r})"

    def set_duration(self, duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError("Продолжительность должна иметь тип числа с плавающей точкой (float)")
        if duration <= 0:
            raise ValueError("Число страниц должно быть больше 0")
        self._duration = duration
