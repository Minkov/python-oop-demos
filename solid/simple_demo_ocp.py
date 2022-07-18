import abc


class Validator(abc.ABC):
    @abc.abstractmethod
    def validate(self, value):
        pass


class NumbersValidator(Validator):
    min_value = 0
    max_value = 1024

    def validate(self, value):
        if value < self.min_value or self.max_value < value:
            raise ValueError(f'Value is outside the range [{self.min_value}, {self.max_value}]')


class NegativeNumbersValidator(NumbersValidator):
    min_value = -1024
    max_value = 0


class DynamicNumbersValidator(NumbersValidator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value


validators = [
    NumbersValidator(),
    NegativeNumbersValidator(),
    DynamicNumbersValidator(-1, 1),
]

numbers = [1, -1]
for validator in validators:
    for number in numbers:
        try:
            validator.validate(number)
            print(f'{number} is valid')
        except:
            print(f'{number} is invalid')
