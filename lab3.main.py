class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Класс для бумажной книги. """

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.set_pages(pages)

    def set_pages(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def get_pages(self):
        return self._pages

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Страниц: {self.get_pages()}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.get_pages()})"


class AudioBook(Book):
    """ Класс для аудиокниги. """

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.set_duration(duration)

    def set_duration(self, value: float):
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError("Длительность должна быть положительным числом.")
        self._duration = float(value)

    def get_duration(self):
        return self._duration

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}. Длительность: {self.get_duration()} часов"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.get_duration()})"


# Пример использования
try:
    paper_book = PaperBook("Kafka on the Shore", "Haruki Murakami", 428)
    audio_book = AudioBook("It", "Stephen King", 13.5)

    print(paper_book)  # Информация о бумажной книге
    print(audio_book)  # Информация об аудиокниге

    # Проверка методов repr
    print(repr(paper_book))
    print(repr(audio_book))

except ValueError as e:
    print(e)
