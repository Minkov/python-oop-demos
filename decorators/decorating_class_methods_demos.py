from decorators.cache import cache
from decorators.measure_time import measure_time


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @cache
    @measure_time
    def get_age_after_years(self, years):
        return self.age + years


p1 = Person('Doncho', 19)
p2 = Person('Doncho', 19)

print(p1.get_age_after_years(10))
print(p2.get_age_after_years(10))
print(p1)
print(p2)
