from faker import Faker
from faker.providers.python import TEnum
import time

class Fake:
    """
    Класс для генерации случайных тестовых данных с использованием библиотеки Faker.
    """
    def __init__(self, faker: Faker):
        """
        :param faker: Экземпляр класса Faker, который будет использоваться для генерацуии данных.
        """
        self.faker = faker

    def enum(self, value: type[TEnum]) -> TEnum:
        """
        Выбирает случайное значение из enum-типа.

        :param value: Enum-класс для генерации значения.
        :return: Случайное значение из перечисления.
        """
        return self.faker.enum(value)

    def email (self) -> str:
        """
        Генеиррует случайный email.

        Будет использован случайный домен, если он не указан явно.
        :return: Случайный email.
        """
        return f"{time.time()}.{self.faker.email()}"
    
    def category(self) -> str:
        """
        Генерирует случайную категорию покупки из предопределённого списка.

        Используется для имитации категории покупки в системах, 
        моделирующих пользовательские транзакции.

        :return: Случайная категория из перечисленных ('gas', 'taxi' и т.д.).
        """
        return self.faker.random_element([
            "gas",
            "taxi",
            "tolls",
            "water",
            "beauty",
            "mobile",
            "travel",
            "parking",
            "catalog",
            "internet",
            "satellite",
            "education",
            "government",
            "healthcare",
            "restaurants",
            "electricity",
            "supermarkets",
        ])
    
    def last_name(self) -> str:
        """
        Генерирует случайную фамилию.

        :return: Случайная фамилия.
        """
        return self.faker.last_name()
    
    def first_name(self) -> str:
        """
        Генерирует случайное имя.

        :return: Случайное имя.
        """
        return self.faker.first_name()
    
    def middle_name(self) -> str:
        """
        Генерирует случайное отчество/среднее имя/его аналог.

        :return: Случайное отчество.
        """
        return self.faker.first_name()
    
    def phone_number(self) -> str:
        """
        Генерирует случайный номер телефона.

        :return: Случайный номер телефона.
        """
        return self.faker.phone_number()
    
    def float(self, start: int = 1, end: int = 1000) -> float:
        """
        Генерирует случайное число с плавающей запятой в указанном диапазоне.

        :param start: Начало диапазона (включительно).
        :param end: Конец диапазона (включительно).
        :return: Случайное число с плавающей запятой.
        """
        return self.faker.pyfloat(min_value=start, max_value=end, right_digits=2)
    
    def amount(self) -> float:
        """
        Генерирует случайную сумму денежных средств

        :return: Сумма от 1 до 1000
        """
        return self.float(1, 1000)

fake = Fake(faker=Faker())
