def func():
    pass


# Class names are always PascalCase
class Person:
    # constructor
    def __init__(self, name, age):  # `self` is `this` in C#, Java, JS, ...
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age}-years-old'

    def increase_age(self):
        self.age += 1


p1 = Person('Doncho', 20)  # `p1` is instance of `Person`
p2 = Person('Pesho', 11)  # `p2` is instance of `Person`
print(p1)
print(p2)
p1.increase_age()
print(p1)
