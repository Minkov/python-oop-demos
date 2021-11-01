class Person:
    def __init__(self, name):
        self.name = name


class SoftwareDeveloper(Person):
    def __init__(self, name, tech_stack):
        super().__init__(name)
        self.tech_stack = tech_stack


class TechnicalLead(SoftwareDeveloper):
    def __init__(self, name, tech_stack, team_size):
        super().__init__(name, tech_stack)
        self.team_size = team_size


tl = TechnicalLead('Gosho', ['python', 'react'], 15)

print(isinstance(tl, TechnicalLead))
print(isinstance(tl, SoftwareDeveloper))
print(isinstance(tl, Person))
print(tl)