class Person:
    def __init__(self, salary):
        self.salary = salary

    def __str__(self):
        return str(self.salary)

    def __bool__(self):
        return self.salary > 1000

    def __int__(self):
        return self.salary


p1 = Person(120)
p2 = Person(1200)

if p1:
    print(p1)
if p2:
    print(p2)

print(2 + int(p1))
