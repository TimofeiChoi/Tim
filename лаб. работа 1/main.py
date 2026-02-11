# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from abc import ABC, abstractmethod

class Wall(ABC):
        """
        Абстрактный класс, описывающий стену.

        :param material (str): Материал стены
        :param height (float): Высота стены в метрах
        :param width (float): Ширина стены в метрах
        :param color (str): Цвет стены
        """
        def __init__(self, material: str, height: float, width: float, color: str = "white"):
            """
            Создание стены.
            >>> wall = Wall("concrete", 2.5, 4.0)
            >>> wall.material
            'brick'
            >>> Wall("", 2.5, 4.0)
            Traceback (most recent call last):
            ValueError: Материал не может быть пустым
            >>> Wall("brick", -1.0, 4.0)
            Traceback (most recent call last):
            ValueError: Высота и ширина должны быть положительными числами
            """
            self.material = material.strip()
            self.height = height
            self.width = width
            self.color = color

            if not isinstance(material, str) or not material.strip():
                raise ValueError("Материал не может быть пустым")
            if height <= 0 or width <= 0:
                raise ValueError("Высота и ширина должны быть положительными числами")

        @abstractmethod
        def paint(self, new_color: str) -> str:
            """
            Покрасить стену в новый цвет.
            :param new_color: Название цвета
            :return str: Сообщение о покраске

            >>> wall = Wall("concrete", 3.0, 5.0, "gray")
            >>> wall.paint("blue")
            'Стена покрашена в синий'
            >>> wall.color
            'синий'
            """
            ...

        @abstractmethod
        def calculate_the_area(self, height: float, width: float) -> float:
            """
            Рассчитать площадь стены.
            :param height
            :param width
            :return float: Площадь стены в квадратных метрах

            >>> wall = Wall("wood", 2.5, 4.0)
            >>> wall.calculate_the_area()
            10.0
            """
            ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()


class Smartphone(ABC):
    """
    Абстрактный класс, описывающий телефон.

    :param model (str): Модель телефона
    :param height (float): Высота телефона в см
    :param width (float): Ширина телефона в см
    :param weight (float): Масса телефона в г
    """

    def __init__(self, model: str, height: float, width: float, weight: float):
        """
        Создание телефона
        >>> phone = Smartphone("Samsung", 16.0, 7.5, 200)
        >>> Smartphone("Samsung", -16.0, 7.5, -200)
        Traceback (most recent call last):
            ValueError: Длина, ширина или вес телефона не соответствуют действительности
        """
        self.model = model.strip()
        self.height = height
        self.width = width
        self.weight = weight
        if height <= 0 or width <= 0 or weight <= 0:
            raise ValueError("Длина, ширина или вес телефона быть положительными числами")

    @abstractmethod
    def use_the_case(self, height: float, width: float, color: str) -> bool:
        """
        Надеть чехол
        :param height: Высота чехла
        :param width: Ширина чехла
        :param color: Цвет чехла
        :return str: Успешно надет
        >>> phone = Smartphone("Samsung", 16.0, 7.5, 200)
        >>> phone.use_the_case(16.0, 7.5, "black")
        True
        """
        ...
    @abstractmethod
    def buy_smartphone(self, money: float, price: float) -> bool:
        """
        :param money
        :param price
        :return Успешная покупка or Недостаточно средств
        >>> phone = Smartphone("Samsung", 16.0, 7.5, 200)
        >>> phone.buy_smartphone(30000.0, 20000.0)
        True
        """
        ...



class Music(ABC):
    """
    Абстрактный класс, описывающий любимую музыку.

    :param genre (str): Жанр музыки
    :param name (float): Название музыки
    """
    def __init__(self, genre: str, name: str):
        """
        Создание телефона
        >>> music = Music("", "")
        Traceback (most recent call last):
            ValueError: Напишите жанр или название предпочитаемой музыки
        """
        self.genre = genre.strip()
        self.name = name.strip()
        if (not isinstance(genre, str) or not genre.strip()) or\
                (not isinstance(name, str) or not name.strip()):
            raise ValueError("Напишите жанр или название предпочитаемой музыки")
        g = genre.replace("-", "")
        n = name.replace("-", "")
        if g.isdigit() or n.isdigit():
            raise ValueError("Введите корректное название для жанра или музыки")
    @abstractmethod
    def find_new_music(self, genre: str) -> list:
        """
        Поиск музыки схожего жанра
        :param genre:Название музыки
        :return: Вот похожая музыка: ....
        >>> music = Music("Classic", "Moonlight sonata")
        >>> music.find_new_music("Classic")
        Вот эту музыку стоит послушать: ....
        """
        ...
    @abstractmethod
    def where_to_listen_to_music(self, name: str) -> list:
        """
        :param name: Название музыки
        :return: Здесь ее можно послушать: ....
        >>> music = Music("Classic", "Moonlight sonata")
        >>> music.where_to_listen_to_music("Moonlight sonata")
        Здесь ее можно послушать: ...
        """
        ...