from debug_decorator_demo import debug


class Person:
    @debug
    def __init__(self, name, age):
        self.name = name
        self.age = age


Person('Doncho', 19)
