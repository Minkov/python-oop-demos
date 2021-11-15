class StrAllAttributesMixin:
    def __str__(self):
        parts = [f'{key}={value}' for (key, value) in self.__dict__.items()]
        return ';'.join(parts)


class Person(StrAllAttributesMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age
