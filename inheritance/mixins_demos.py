class StrDicMixin:
    def __str__(self):
        key_values = ', '.join(
            f'{key}: {value}' for (key, value) in self.__dict__.items()
        )

        return f'{self.__class__.__name__} ({key_values})'


class Animal(StrDicMixin):
    def __init__(self, name):
        self.name = name


class Dog(Animal, StrDicMixin):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


class Robot(StrDicMixin):
    def __init__(self, programs_count):
        self.programs_count = programs_count


class DogRobot(Dog, Robot):
    def __init__(self, name, age, programs_count):
        Dog.__init__(self, name, age)
        Robot.__init__(self, programs_count)


# name: Gosho, hobbies: [...]
class Person(StrDicMixin):
    age = 11  # shared for all persons

    def __init__(self, name):
        if not name:
            raise ValueError('Person name cannot be None or empty string')
        self.name = name  # only for this person instance
        self.hobbies = set()

    def add_hobby(self, hobby):
        self.hobbies.add(hobby)


class Employee(Person):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company


class SoftwareDeveloper(Person):
    def __init__(self, name):
        super().__init__(name)
        self.add_hobby('Lego')
        self.add_hobby('Cats')


print(Person('Gosho'))
print(SoftwareDeveloper('Gosho'))
print(Employee('Maria', 'SoftUni'))
print(Dog('Sharo', 2))
print(DogRobot('Sharo', 3, 7))
