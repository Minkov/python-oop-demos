import functools
from dataclasses import dataclass


def singleton(cls):
    instances = []

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if not instances:
            instances.append(cls(*args, **kwargs))
        return instances[0]

    return wrapper


@singleton
@dataclass
class Person:
    name: str
    age: int


p1 = Person('Doncho', 19)
p2 = Person('Pesho', 21)

print(p1)
print(p2)
