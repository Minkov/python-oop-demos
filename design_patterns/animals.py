class Cat:
    kind = 'cat'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Simple factory
    @classmethod
    def without_age(cls, name):
        return cls(name, None)


class Dog:
    kind = 'dog'

    def __init__(self, name):
        self.name = name
