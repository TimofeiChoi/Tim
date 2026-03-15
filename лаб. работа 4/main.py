from abc import ABC, abstractmethod
from typing import Union

class Vehicle(ABC):
    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Args:
            brand: Марка транспортного средства
            model: Модель транспортного средства
            year: Год выпуска
        """
        self._brand = brand
        self._model = model
        self._year = year
        self._is_engine_running = False

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def model(self) -> str:
        return self._model

    @property
    def year(self) -> int:
        return self._year

    @property
    def is_engine_running(self) -> bool:
        return self._is_engine_running

    def start_engine(self) -> str:
        """
        Запуск двигателя.
        Returns:
            str: Сообщение о результате запуска
        """
        if self._is_engine_running:
            return "Двигатель уже запущен"

        self._is_engine_running = True
        return f"Двигатель {self._brand} {self._model} запущен"

    def stop_engine(self) -> str:
        """
        Остановка двигателя.
        Returns:
            str: Сообщение о результате остановки
        """
        if not self._is_engine_running:
            return "Двигатель уже остановлен"

        self._is_engine_running = False
        return f"Двигатель {self._brand} {self._model} остановлен"

    @abstractmethod
    def move(self) -> str:
        """
        Абстрактный метод, который описывает движение транспортного средства.
        """
        pass

    def __str__(self) -> str:
        """
        Пользовательское строковое представление.
        """
        return f"{self._brand} {self._model} ({self._year} г.)"

    def __repr__(self) -> str:
        """
        Строковое представление для разработчиков.
        """
        return f'{self.__class__.__name__}(brand="{self._brand}", model="{self._model}", year = {self._year})'


class Car(Vehicle):
    def __init__(self, brand: str, model: str, year: int, doors_count: int, body_type: str) -> None:
        """
        Args:
            brand: Марка автомобиля
            model: Модель автомобиля
            year: Год выпуска
            doors_count: Количество дверей
            body_type: Тип кузова
        """
        super().__init__(brand, model, year)
        self.doors_count = doors_count  #Используем сеттер для проверки
        self._body_type = body_type

    @property
    def doors_count(self) -> int:
        return self._doors_count

    @doors_count.setter
    def doors_count(self, value: int) -> None:
        """
        Args:
            value: Количество дверей
        Raises:
            TypeError: Если значение не целое число
            ValueError: Если количество дверей не в диапазоне 2-5
        """
        if not isinstance(value, int):
            raise TypeError("Количество дверей должно быть целым числом")
        if value < 2 or value > 5:
            raise ValueError("Количество дверей должно быть от 2 до 5")
        self._doors_count = value

    @property
    def body_type(self) -> str:
        return self._body_type

    def move(self) -> str:
        """
        Переопределение абстрактного метода move для легкового автомобиля.
        Причина перегрузки: специфика движения легкового авто отличается от грузового (более высокая скорость, маневренность).
        Returns:
            str: Описание движения
        """
        if not self._is_engine_running:
            return f"{self} не может ехать - сначала запустите двигатель"
        return f"{self} едет по дороге с комфортной скоростью"

    def __str__(self) -> str:
        """
        Перегрузка метода str для добавления специфической информации.
        Причина перегрузки: для легкового авто важно указать тип кузова и количество дверей в пользовательском представлении.
        """
        return f"Легковой: {super().__str__()}, {self._body_type}, {self._doors_count} дв."


class Truck(Vehicle):
    def __init__(self, brand: str, model: str, year: int, capacity_kg: float, has_trailer: bool = False) -> None:
        """
        Args:
            brand: Марка автомобиля
            model: Модель автомобиля
            year: Год выпуска
            capacity_kg: Грузоподъемность в кг
            has_trailer: Наличие прицепа
        """
        super().__init__(brand, model, year)
        self.capacity_kg = capacity_kg  #Используем сеттер для проверки
        self._has_trailer = has_trailer
        self._current_load_kg = 0.0  #Текущая загрузка

    @property
    def capacity_kg(self) -> float:
        return self._capacity_kg

    @capacity_kg.setter
    def capacity_kg(self, value: Union[int, float]) -> None:
        """
        Args:
            value: Грузоподъемность в кг
        Raises:
            TypeError: Если значение не число
            ValueError: Если грузоподъемность не положительная
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Грузоподъемность должна быть числом")
        if value <= 0:
            raise ValueError("Грузоподъемность должна быть положительной")
        self._capacity_kg = float(value)

    @property
    def has_trailer(self) -> bool:
        return self._has_trailer

    @property
    def current_load_kg(self) -> float:
        return self._current_load_kg

    def load_cargo(self, weight_kg: float) -> str:
        """
        Загрузка груза.
        Инкапсуляция: изменение текущей загрузки только через этот метод с проверкой на превышение грузоподъемности.
        """