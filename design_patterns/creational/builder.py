class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '; '.join(f'{key}={value}' for key, value in self.__dict__.items())


class PersonBuilder:
    # Optional parameters outside the `Person` class
    person_attrs = {
        'name': 'John Doe',
        'age': 0,
    }

    def set_name(self, name):
        self.person_attrs['name'] = name

    def set_age(self, age):
        self.person_attrs['age'] = age

    def build(self):
        # Create external for person validation
        return Person(**self.person_attrs)


builder = PersonBuilder()
builder.set_age(19)
builder.set_name('Doncho')
print(builder.build())
