class StudentTaxes:
    def __init__(self, name, semester_tax, average_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.average_grade = average_grade

    def get_discount(self):
        if self.average_grade > 5:
            return self.semester_tax * 0.3
        return 0


class AdditionalDiscount(StudentTaxes):
    def get_discount(self):
        if 5.5 <= self.average_grade < 6:
            return self.semester_tax * 0.8
        elif 4 < self.average_grade <= 5:
            return self.semester_tax * 0.2
        return super().get_discount()


class NoDiscount(StudentTaxes):
    # Violation of OCP
    def get_discount(self):
        return 0

    # Violation of LSP
    # def get_discount(self):
    #     pass


st = [
    StudentTaxes('Doncho', 1000, 4.5),
    StudentTaxes('Pesho', 1000, 5.5),
    AdditionalDiscount('Maria', 1000, 4.5),
    AdditionalDiscount('Stamat', 1000, 5.5),
]

[print(s.get_discount()) for s in st]

# Regular day
yordan = StudentTaxes('Yordan', 1000, 4.5)

# Promotion day
yordan2 = AdditionalDiscount('Yordan', 1000, 4.5)
