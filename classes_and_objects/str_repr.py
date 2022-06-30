class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}; Age: {self.age}'

    def __repr__(self):
        return f'Person("{self.name}", {self.age})'


ss = 'Doncho'

print(str(ss))
print(repr(ss))
print(eval(repr(ss)))

p = Person('Doncho', 19)
print(str(p))
print(repr(p))
print(eval(repr(p)))
