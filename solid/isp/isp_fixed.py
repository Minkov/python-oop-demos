from abc import ABC, abstractmethod


class Validator(ABC):
    @abstractmethod
    def validate(self, value):
        pass


class MinStringLengthValidator(Validator):
    def __init__(self, min_length):
        self.min_length = min_length

    def validate(self, value):
        if len(value) < self.min_length:
            raise ValueError(f'Value must be at least {self.min_length} characters long')


class MaxStringLengthValidator(Validator):
    def __init__(self, max_length):
        self.max_length = max_length

    def validate(self, value):
        if self.max_length < len(value):
            raise ValueError(f'Value must be at most {self.max_length} characters long')


class Person:
    name_validators = (
        MinStringLengthValidator(2),
        MaxStringLengthValidator(15),
    )

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        [validator.validate(value) for validator in self.name_validators]
        self.__name = value


class Teacher(Person):
    name_validators = (
        MinStringLengthValidator(6),
        MaxStringLengthValidator(19),
    )
