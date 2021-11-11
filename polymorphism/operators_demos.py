class Person:
    def __init__(self, salary):
        self.salary = salary

    # self > other
    def __gt__(self, other):
        return self.salary > other.salary

    # self >= other
    def __ge__(self, other):
        return self.salary >= other.salary

    def __str__(self):
        return f'Salary: {self.salary}'


def compare_lt(x, y):
    print(f'{x} < {y} -> {x < y}')


def compare_gt(x, y):
    print(f'{x} > {y} -> {x > y}')


def compare_le(x, y):
    print(f'{x} <= {y} -> {x <= y}')


def compare_ge(x, y):
    print(f'{x} >= {y} -> {x >= y}')


def compare_eq(x, y):
    print(f'{x} == {y} -> {x == y}')


def compare_ne(x, y):
    print(f'{x} != {y} -> {x != y}')


p1 = Person(1200)
p2 = Person(6000)
p3 = Person(1200)

people = [p1, p2, p3]

for x in people:
    for y in people:
        compare_lt(x, y)
        compare_le(x, y)
        compare_gt(x, y)
        compare_ge(x, y)
        compare_eq(x, y)
        compare_ne(x, y)

print(str('123'))
print(repr('123'))
