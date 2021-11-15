class Validator:
    def validate_not_none(self, value):
        pass

    def validate_positive_number(self, value):
        pass

    def validate_min_string_length(self, value, min_length):
        pass

    def validate_max_string_length(self, value, max_length):
        pass


class Person:
    validator = Validator()

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.validator.validate_min_string_length(value, 2)
        self.validator.validate_max_string_length(value, 15)
        self.__name = value
