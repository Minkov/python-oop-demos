from dataclasses import dataclass


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


@dataclass(eq=False)
class Person2:
    name: str
    age: int


p1 = Person2(name='Gosho', age=5)
p2 = Person2(name='Gosho', age='5')
print(p1 == p2)
