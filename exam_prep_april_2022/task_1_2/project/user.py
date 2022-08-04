import os

from project.utils.validators import validate_non_empty_string, validate_greater_than_value


class User:
    MIN_AGE = 6

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__validate_username(value)
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value

    @staticmethod
    def __validate_username(username):
        validate_non_empty_string(username, 'Invalid username!')

    def __validate_age(self, age):
        validate_greater_than_value(age, self.MIN_AGE, f'Users under the age of {self.MIN_AGE} are not allowed!')

    def __str__(self):
        # TODO: Extract into a method
        movies_liked_str = 'No movies liked.'
        if self.movies_liked:
            movies_liked_str = os.linesep.join(m.details() for m in self.movies_liked)
        # `linesep` is `\n` for Unix/Linux and `\n\r` for Windows

        # TODO: Extract into a method
        movies_owned_str = 'No movies owned.'
        if self.movies_owned:
            movies_owned_str = os.linesep.join(m.details() for m in self.movies_owned)

        return f'''Username: {self.username}, Age: {self.age}
Liked movies:
{movies_liked_str}
Owned movies:
{movies_owned_str}'''
