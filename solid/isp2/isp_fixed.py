import abc


class Validator(abc.ABC):
    @abc.abstractmethod
    def validate(self, value):
        pass


class InRangeValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value):
        if value < self.min_value or self.max_value < value:
            raise ValueError()


class GreaterThanValidator(Validator):
    def __init__(self, min_value):
        self.min_value = min_value

    def validate(self, value):
        if value <= self.min_value:
            raise ValueError()


in_range_validator = InRangeValidator(3, 5)
in_range_validator.validate(3)
in_range_validator.validate(4)

greater_than_validator = GreaterThanValidator(3)

greater_than_validator.validate(4)
greater_than_validator.validate(3)
