class Fraction:
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator

    # fraction1 + fraction 2
    def __add__(self, other):
        nominator = self.nominator * other.denominator + \
                    other.nominator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(nominator, denominator)

    def __str__(self):
        return f'{self.nominator}/{self.denominator}'


f1_2 = Fraction(1, 2)
print(f'{f1_2.nominator}/{f1_2.denominator}')
print(f1_2)
print(Fraction(3, 4))
print(Fraction(1, 2) + Fraction(3, 4))
