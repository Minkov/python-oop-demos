from app.validators import name_validator


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        name_validator.validate_name(value)
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        name_validator.validate_name(value)
        self.__last_name = value

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def get_info(self):
        return f'My name is {self.fullname} and I am {self.age}-years-old!'
