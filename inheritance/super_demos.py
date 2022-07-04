'''
`self` means this instance
`super()` means this instance as the `Parent` class
    - Call it when in the same method (98% of the times)
'''


class Person:  # `Person` is extended by `Teacher`
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return {
            'name': self.name,
            'age': self.age,
        }

    def __str__(self):
        return f'Name: {self.name}; Age: {self.age}'


class AdultPerson(Person):
    def get_info(self):
        return {
            **Person.get_info(self),
            'is_adult': True,
        }


class Teacher(AdultPerson):
    def __init__(self, name, age, subject, title='mr'):
        # self.name = name
        # self.age = age
        super().__init__(name, age)  # More abstract, not a concrete reference to the parent class
        # super(Teacher, self).__init__(name, age) # Old python versions
        self.subject = subject
        self.title = title

    def get_info(self):
        # parent_info = super().get_info()
        # parent_info['title'] = self.title
        # parent_info['subject'] = self.subject
        # return parent_info
        return {
            # **Person.get_info(self), # Correct, but concrete. Use `super()`
            **super().get_info(),  # reference to parent method `get_info`
            'title': self.title,
            'subject': self.subject,
        }

    def teach(self):
        print(f'{self.title.capitalize()}. {self.name} is teaching "{self.subject}"')

    # def __str__(self):
    #     parent_str = super().__str__()
    #     return f'{parent_str}; Subject: Python OOP'

    def __str__(self):
        parent_str = super().__str__()
        #     parent_str = self.__str__() # Recursion
        return f'{parent_str}; Subject: Python OOP'


#
t1 = Teacher('Doncho', 47, 'Python OOP')
t2 = Teacher('Maria', 32, 'C# Design Patterns', 'ms')
t1.teach()
t2.teach()
print(t1.get_info())
print(t2.get_info())
# print(str(Teacher('Doncho', 47)))
