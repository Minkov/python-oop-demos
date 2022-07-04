# class Person(object):  # `Person` is extended by `Teacher`
class Person:  # `Person` is extended by `Teacher`
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}; Age: {self.age}'


class Teacher(Person):  # `Teacher` extends `Person`
    def teach(self):
        print(f'mr. {self.name} is teaching')


t = Teacher('Doncho', 47)

print(t.name)
print(t.age)
t.teach()
print(t)

p = Person('Maria', 19)
p.teach()
