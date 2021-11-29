class Person:
    MIN_AGE = 0
    MAX_AGE = 150

    def __init__(self, first_name, last_name, age):
        # invalid tests: None, not a string, wrong length
        # valid tests: all is valid
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_info(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old'

    @classmethod
    def __validate_age(cls, value):
        if value < cls.MIN_AGE or cls.MAX_AGE < value:
            raise ValueError(f'Age must be between {cls.MIN_AGE} and {cls.MAX_AGE}')
