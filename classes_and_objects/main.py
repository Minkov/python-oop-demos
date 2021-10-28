# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.grades = []
#
#     def fullname(self):
#         return f'{self.first_name} {self.last_name}'
#
#     def add_grade(self, subject, grade):
#         self.grades.append((subject, grade))
#
#     def print_grades(self):
#         print(self.grades)
#
#
# pesho = Person('Pesho', 'Goshov', 19)
#
# print(pesho)
# print(pesho.first_name)
# print(pesho.fullname())
# print(Person.fullname)
# print(Person.fullname(pesho))
# print(Person.fname)

'''
1/2 + 3/4 = (1*4 + 3*2) /(2*4)
'''


class Fraction:
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator

    def __add__(self, other):
        nominator = self.nominator * other.denominator + \
                    other.nominator * self.denominator

        denominator = self.denominator * other.denominator
        return Fraction(nominator, denominator)

    def __eq__(self, other):
        return self.nominator == other.nominator \
               and self.denominator == other.denominator

    def __hash__(self):
        return hash(self.nominator / self.denominator)

    def __str__(self):
        return f'{self.nominator}/{self.denominator}'


f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
print(f1 + f2)  # __add__(f1, f2)

print(Fraction(1, 2) == Fraction(1, 2))
print(Fraction(1, 2) == Fraction(1, 3))

''' 3* (1/2) =3/2'''

print(3 / 2)
print(3 // 2)

print(hash(Fraction(1, 2)))

print(f1.__dict__)
