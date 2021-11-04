class Person:
    def __init__(self, name, age):
        # private/non-visible, accessible only from within this class
        self.set_name(name)
        # protected, accessible from within this class and inheritors
        self.set_age(age)

    # public/visible
    def say_name(self):
        print(self.get_name())

    def get_info(self):
        return f'Name: {self.get_name()}, Age: {self.get_age()}'

    def is_adult(self):
        return self.get_age() >= 18

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if not new_age:
            raise ValueError('Age cannot be None')
        self._age = new_age

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if not new_name:
            raise ValueError('Name cannot be None')

        if any([not x.isalpha() for x in new_name]):
            raise ValueError('Name can contain only letters')

        self.__name = new_name


class SoftwareDeveloper(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


p = SoftwareDeveloper('Doncho', 11)

print(p.get_info())
p.say_name()
print(p.get_name())
p.set_name('Donch')

print(p.get_name())

print(p.is_adult())

print(p.is_adult())
