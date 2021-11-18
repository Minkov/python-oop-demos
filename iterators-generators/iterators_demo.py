class Person:
    def __init__(self, name):
        self.name = name

    # return an object with a method `__next__`
    def __iter__(self):
        return PersonIterator(self)


class PersonIterator:
    def __init__(self, person):
        self.person = person
        self.index = 0

    def __next__(self):
        if self.index == len(self.person.name):
            raise StopIteration

        value = self.person.name[self.index]
        self.index += 1
        return value


gosho = Person('Gosho')
for x in gosho:
    print(x)

iter1 = iter(gosho)
iter2 = iter(gosho)
print(iter1)

print('Iter 1: ' + next(iter1))
print('Iter 1: ' + next(iter1))
print('Iter 1: ' + next(iter1))

print('Iter 2: ' + next(iter2))

print('Iter 1: ' + next(iter1))

print('Iter 2: ' + next(iter2))
