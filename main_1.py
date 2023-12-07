import doctest

class Website:
    def __init__(self, kolichestvo_registr: int, zahod: int):
        """
        Создание и подготовка к работе объекта "Вебсайт"
        : kolichestvo_registr - количество регистраций на сайте
        : zahod - количество просмотров сайта

    Пример: website=Website(1000,200) #инициализация экземпляров класса
    """
        if not isinstance(kolichestvo_registr, (int, float)):
            raise TypeError("Количество регистраций должно быть типа int или float")
        if kolichestvo_registr <= 0:
            raise ValueError("Количество регистраций должно быть положительным числом")
        self.kolichestvo_registr = kolichestvo_registr

        if not isinstance(zahod, int):
            raise TypeError("Количество просмотров быть int")
        if zahod <= 0:
            raise ValueError("Количество просмотров должно быть положительным числом")
        self.zahod = zahod
    def add_chel(self,plus_chel:int)->None
        """
        Добавление посетитиелей на сайт
        :plus_chel: Количество людей

        :raise ValueError: Если количество людей отрицательно, вызываем ошибку
        Пример:
        >>> website=Website(1000,200)
            website.add_chel(5) 
        """
        if not isinstance(plus_chel, int):
            raise TypeError("Количество добавления посетителей должно быть типа Int")
        if plus_chel<0
            raise ValueError("количество добавления людей должно быть положительным")
        
     def users_in_day(self) -> float:
        """
        Определение среднего количества пользователей в день

        :return: Среднее кол-во пользователей в день

        Примеры:
        >>> website = Website(7, 490)
        >>> website.users_in_day()
        """
        
class Rocket:
    def __init__(self, payload_weigth: float, max_range: float):
        """
        Создание и подготовка к работе объекта "Ракета"

        :param payload_weigth: Масса полезной нагрузки
        :param max_range: Максимальная дальность полета

        Примеры:
        >>> rocket = Rocket(2000, 10000)  # инициализация экземпляра класса
        """
        if not isinstance(payload_weigth, (int, float)):
            raise TypeError("Масса полезной нагрузки должна быть типа int или float")
        if payload_weigth <= 0:
            raise ValueError("Масса полезной нагрузки должна быть положительным числом")
        self.payload_weigth = payload_weigth

        if not isinstance(max_range, (int, float)):
            raise TypeError("Максимальная дальность полета должна быть int или float")
        if max_range <= 0:
            raise ValueError("Максимальная дальность полета должна быть положительным числом")
        self.max_range = max_range

    def add_mass_to_rocket(self, plus_mass: float) -> None:
        """
        Добавление массы в полезную нагрузку.
        :param plus_mass: Объем добавляемой массы

        :raise ValueError: Если количество добавляемой массы отрицательно, вызываем ошибку

        Примеры:
        >>> rocket = Rocket(2000, 10000)
        >>> rocket.add_mass_to_rocket(200)
        """
        if not isinstance(plus_mass, (int, float)):
            raise TypeError("Добавляемая масса должна быть типа int или float")
        if plus_mass < 0:
            raise ValueError("Добавляемая масса должна положительным числом")
        ...

    def remove_mass_from_rocket(self, minus_mass: float) -> None:
        """
        Уменьшения массы полезной нагрузки.

        :param minus_mass: отбираемая масса
        :raise ValueError: Если уменьшение масса превышает текущую массу, вызываем ошибку

        :return: Уменьшенная масса

        Примеры:
        >>> rocket = Rocket(2000, 10000)
        >>> rocket.remove_mass_from_rocket(500)
        """
        ...
        
class Target:
    def __init__(self, shoots: int, hits: int):
        """
        Создание и подготовка к работе объекта "Мишень"

        :param shoots: Количество выстрелов
        :param hits: Количество попаданий

        Примеры:
        >>> target = Target(10, 7)  # инициализация экземпляра класса
        """
        if not isinstance(shoots, int):
            raise TypeError("Количество выстрелов должно быть типа int")
        if shoots <= 0:
            raise ValueError("Количество выстрелов должно быть больше нуля")
        self.shoots = shoots

        if not isinstance(hits, int):
            raise TypeError("Количество попаданий должно быть int")
        if hits < 0:
            raise ValueError("Количество попаданий не может быть отрицательным числом")
        self.hits = hits

    def misses(self) -> int:
        """
        Функция определяет количество промахов

        :return: Количество промахов

        Примеры:
        >>> target = Target(10, 7)
        >>> target.misses()
        """
        ...

    def extra_points(self, points) -> None:
        """
        Добавление очков за прошлые попытки.
        :param points: Количество добавляемых очков

        :raise ValueError: Если количество очков отрицательно, то вызываем ошибку

        Примеры:
        >>> target = Target(12, 5)
        >>> target.extra_points(3)
        """
        if not isinstance(points, int):
            raise TypeError("Добавляемые очки должны быть типа int")
        if points < 0:
            raise ValueError("Добавляемые очки должны быть не отрицательным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
