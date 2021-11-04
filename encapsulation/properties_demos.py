import hashlib
import uuid
from base64 import encode


class Person:
    def __init__(self, name, age, nickname=None):
        self.name = name
        self.age = age
        self.nickname = nickname

    def say_name(self):
        print(self.name)

    def get_info(self):
        return f'Name: {self.name}, Age: {self.age}, Nickname: {self.nickname}'

    @property
    def is_adult(self):
        return self.age >= 18

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if not new_age:
            raise ValueError('Age cannot be None')
        self.__age = new_age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not new_name:
            raise ValueError('Name cannot be None')

        if any([not x.isalpha() for x in new_name]):
            raise ValueError('Name can contain only letters')

        self.__name = new_name

    @property
    def nickname(self):
        return self.__nickname

    @nickname.setter
    def nickname(self, value):
        if self.is_adult:
            raise ValueError('Nickname can only be changed for non-adults')
        self.__nickname = value


#
# p = Person('Gosho', 17)
# print(p.age)
# print(p.get_info())
# p.nickname = 'Tigara'
# print(p.get_info())
# print(p.nickname)
# p.age = 18
# p.nickname = 'Golemiq tigar'
# print(p.nickname)


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def password(self):
        return self.__password_hash

    @password.setter
    def password(self, value):
        salt = uuid.uuid4().hex
        # self.__password_hash = hashlib.sha512((value + salt).encode()).hexdigest()
        self.__password_hash = f'---{value}---'


for _ in range(5):
    user1 = User('user1', '12345qwe')
    print(user1.password)
