from abc import ABC, abstractmethod

from project.utils import is_positive


class BakedFood(ABC):
    __INVALID_NAME_MESSAGE = 'Name cannot be empty string or white space!'

    # Bad practice, only for the exam
    @abstractmethod
    def __init__(self, name: str, portion: float, price: float):
        self.name = name
        self.portion = portion
        self.price = price

    @classmethod
    def __validate_name(cls, value):
        if not value or not value.strip():
            raise ValueError(cls.__INVALID_NAME_MESSAGE)

    @classmethod
    def __validate_price(cls, value):
        if not is_positive(value):
            raise ValueError('Price cannot be less than or equal to zero!')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__validate_price(value)
        self.__price = value

    def __repr__(self):
        return f' - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv'
