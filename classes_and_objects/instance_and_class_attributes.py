class Person:
    min_age = 0  # class properties/attributes
    max_age = 150  # class properties/attributes

    def __init__(self, name, age):
        self.name = name  # instance properties/attributes
        self.age = age  # instance properties/attributes

    def __str__(self):
        return f'Name: {self.name}; Age: {self.age};' \
               f' Min age: {self.min_age}; Max age: {self.max_age}'


people_list = [
    Person('Doncho', 19),
    Person('Maria', 24),
]

[print(p) for p in people_list]

Person.max_age = 160  # Don't do this!

[print(p) for p in people_list]

people_list[0].max_age = 165  # this creates instance attribute `max_age`

[print(p) for p in people_list]  # print() calls `str(obj)` internally

people_list[0].name = 'Doncho 2'  # Not great
