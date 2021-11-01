class Person:
    age = 11  # shared for all persons

    def __init__(self, name):
        if not name:
            raise ValueError('Person name cannot be None or empty string')
        self.name = name  # only for this person instance
        self.hobbies = set()

    def add_hobby(self, hobby):
        # validate if None
        # validate name
        # validate if hobby already exists

        self.hobbies.add(hobby)

    def __str__(self):
        if self.hobbies:
            return f'{self.name} has hobbies: {self.hobbies}'
        else:
            return f'{self.name} has no hobbies'


class Employee(Person):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

    # Wrong
    # def __init__(self, name, company):
    #     self.name = name
    #     self.company = company
    #     self.hobbies = set()


class SoftwareDeveloper(Person):
    def __init__(self, name):
        super().__init__(name)
        self.add_hobby('Lego')
        self.add_hobby('Cats')


class Teacher(Person):
    def __init__(self, name):
        # same as Person.__init__(self, name), but not abstract
        super().__init__(name)
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)
        self.add_hobby(subject)

    def __str__(self):
        # same as Person.__str(self), but not abstract
        super_str = super().__str__()

        if self.subjects:
            subjects = f' and subjects: {self.subjects}'
        else:
            subjects = ' and no subjects'

        return super_str + subjects


class Driver(Person):
    def drive(self):
        return f'{self.name} is driving...'


mrGeorge = Teacher('mr. George')
pesho = SoftwareDeveloper('Pesho')
maria = Employee('Maria', 'SoftUni')
marto = Driver('Marto')
print(marto.drive())

print(mrGeorge)
print(pesho)
print(maria)

mrGeorge.add_hobby('Tennis')  # From person
mrGeorge.add_subject('Math')  # From teacher

maria.add_hobby('Jogging')

print(mrGeorge)
print(maria)
# pesho = SoftwareDeveloper('Pesho')
# gosho = SoftwareDeveloper('Gosho')
#
# # pesho.hobbies.append('Biking')  # violates encapsulation and abstraction
# pesho.add_hobby('Biking')

'''
every square in rect, but not every rect in square 
'''

print(SoftwareDeveloper.mro())
