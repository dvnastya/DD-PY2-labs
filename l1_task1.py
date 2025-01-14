# TODO Написать 3 класса с документацией и аннотацией типов
class Arm:
    def __init__(self, diameter: int, length: float):
        if diameter <= 0:
            raise ValueError("Diameter must be a positive integer.")
        if length <= 0:
            raise ValueError("Length must be a positive float.")
        self.diameter = diameter
        self.length = length

    def get_dimensions(self) -> str:
        """
        Получение размеров арматуры.
        :return: Размеры арматуры
        """

    def is_empty_arm(self) -> bool:
        """
        Функция которая проверяет есть ли арматура
        :return: Есть ли арматура
        """


class Student:
    def __init__(self, name: str, age: int):
        if age < 0:
            raise ValueError("Age must be a non-negative integer.")
        self.name = name
        self.age = age

    def introduce(self) -> str:
        """
        Представление студента.
        :return: Строка с представлением студента.
        """

    def take_exam(self, subject: str):
        """
        Сдает экзамен по заданному предмету.
        :return: Сдает ли студент экзамен.
        """


class Car:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def get_description(self) -> str:
        """
        Получение описания автомобиля.
        :return: Описание автомобиля.
        """

    def refuel(self, liters: float):
        """
        Заправляет автомобиль указанным количеством литров топлива.
        :return: Объем топлива .
        """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    pass

