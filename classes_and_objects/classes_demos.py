class Person:
    min_age = 0  # property/field (data attribute)

    # `self` is `this` in C#, Java, JS, C++, ...
    def __init__(self, name: str, age: int):  # method (function attribute)
        self.name = name  # property/field (data attribute)
        self.age = age  # property/field (data attribute)

    def print_info(self):  # method (func attribute)
        print(f'I am {self.name} and I am {self.age}-years-old')

    def equals(self, other):  # method (func attribute)
        print(self == other)
    #
    # def __str__(self):
    #     return f'Name: {self.name}; Age: {self.age}'

    def __str__(self):
        return '; '.join(f'{key}={value}' for key, value in self.__dict__.items())



p1 = Person('Doncho', 19)
p2 = Person('Maria', 24)
p1.print_info()
p2.print_info()
print(p1.name)
print(p2.name)
p1.equals(p2)  # False
p1.equals(p1)  # True
p2.equals(p1)  # False
p2.equals(p2)  # True

p1.print_info()
Person.print_info(p1)  # Don't do this
print(p1)
print(p2)

people_list = [p1, p2]
people_list_strings = [str(p) for p in people_list]
print(p1 == 'Name: Doncho; Age: 19')
print(str(p1) == 'Name: Doncho; Age: 19')

print(p1 in people_list)
print(p2 in people_list)
print(Person('Doncho', 19) in people_list)
