# Variant 1 - Best
class Parent:
    _possible_drinks = ['beer', 'wine']


class Child(Parent):
    _possible_drinks = ['beer', 'wine', 'vodka']


# Variant 2 - Ok
class Child2(Parent):
    def __init__(self):
        self._possible_drinks = super()._possible_drinks + ['vodka']


# Variant 3 - Wrong
class Child3(Parent):
    _possible_drinks = Parent._possible_drinks + ['vodka']
