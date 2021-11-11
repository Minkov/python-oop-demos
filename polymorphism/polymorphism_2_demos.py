class Person:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f'{self.name} is eating...'


class Employee(Person):
    pass


class Teacher(Employee):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def teaching(self):
        return f'{self.name} is teaching {self.subject}'

    def eat(self):
        return super().eat() + 'FAST!'


class Engineer(Person):
    def __init__(self, name, speciality):
        super().__init__(name)
        self.speciality = speciality

    def craft(self):
        return f'{self.name} is crafting something {self.speciality}'


class Animal:
    def eat(self):
        return 'The animal is eating...'


items = [
    Teacher('Mr. George', 'Math'),
    Teacher('Ms. Maria', 'History'),
    Engineer('Baj Gosho', 'Stroitelstvo'),
    Animal(),
]

for p in items:
    print(p.eat())
    print(p.sleep())
