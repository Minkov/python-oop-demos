class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def increase_age(self):
        self.age += 1

    def __str__(self):
        return ';'.join(f'{key}={value}'
                        for key, value in self.__dict__.items())


class Employee(Person):  # `Employee` can use everything from `Person`
    def __init__(self, name, age, field):
        self.field = field
        super().__init__(name, age)  # `super()` means `Person`

    def work(self):
        print(f'{self.name} is working in {self.field}')


# `Teacher` can use everything from `Employee`
# including from their parents
class Teacher(Employee):
    def __init__(self, name, age, field, subject):
        super().__init__(name, age, field)  # `super()` means `Employee`
        self.subject = subject

    def teach(self):
        print(f'Mr. {self.name} is teaching {self.subject}')


t = Teacher('Doncho', 47, 'Education', 'Python OOP')
print(t)
t.teach()
t.work()
t.increase_age()

print(t)
