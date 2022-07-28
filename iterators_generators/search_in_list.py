class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getitem__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]
        return None


def get_person_by_name(people, name):
    people_found = [p for p in people if p.name == name]
    if people_found:
        return people_found[0]
    return None


people = [
    Person('Doncho', 19),
    Person('Pesho', 38),
    Person('Maria', 53),
    Person('Gancho', 17),
    Person('Stamat', 91),
]

print(get_person_by_name(people, 'Doncho'))
print(get_person_by_name(people, 'Stamat'))
print(get_person_by_name(people, 'Stamat2'))

print(people[0]['name'])
