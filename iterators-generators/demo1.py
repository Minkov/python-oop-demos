ll = [1, 2, 3, 4, 5]

for x in ll:
    print(x)

print([x + 1 for x in ll])


class Person:
    def __init__(self, name):
        self.name = name


pp = Person('Gosho')

for x in pp:
    print(x)

print([x + 1 for x in pp])
