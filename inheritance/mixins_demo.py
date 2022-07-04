class StrMixin:
    str_delimeter = ';'

    def __str__(self):
        return self.str_delimeter.join(f'{key}={value}' for key, value in self.__dict__.items())


class EqualsMixin:
    def __eq__(self, other):
        self_dict = self.__dict__
        other_dict = other.__dict__

        for key, value in self_dict.items():
            if key not in other_dict or other_dict[key] != value:
                return False
        return True


class Person(StrMixin, EqualsMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Building(StrMixin):
    str_delimeter = ', '

    def __init__(self, name, address):
        self.name = name
        self.address = address


print(Person('Doncho', 17))
print(Person('Doncho', 17) == Person('Doncho', 17))
print(Building('SoftUni', 'Aleksander Malinov 33'))
