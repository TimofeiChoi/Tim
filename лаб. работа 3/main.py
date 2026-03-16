class Book:
    def __init__(self, name, author):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f'"{self.name}" {self.author}'

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name}", author="{self.author}")'


class PaperBook(Book):

    def __init__(self, name, author, pages):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = value

    def __str__(self):
        return f'"{self.name}" {self.author} - {self.pages} стр.'

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name}", author="{self.author}", pages = {self.pages})'


class AudioBook(Book):
    def __init__(self, name, author, duration):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительной")
        self._duration = float(value)

    def __str__(self):
        hours = int(self.duration // 60)
        minutes = int(self.duration % 60)
        if hours > 0:
            return f'"{self.name}" {self.author} - {hours}ч {minutes}мин'
        else:
            return f'"{self.name}" {self.author} - {minutes}мин'

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name}", author="{self.author}", duration = {self.duration})'


if __name__ == '__main__':
    paper = PaperBook("1984", "Книга 1", 328)
    audio = AudioBook("1984", "Озвучка книги 1", 495)
    print(paper)
    print(audio)
