class Command:
    def execute(self):
        pass


class SumCommand(Command):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def execute(self):
        return self.x + self.y


commands = [
    SumCommand(2, 3),
    SumCommand(3, 7),
    SumCommand(5, 7),
]

for c in commands:
    print(c.execute())


class AddCommand(Command):
    def __init__(self, ll, value):
        self.value = value
        self.ll = ll

    def execute(self):
        self.ll.append(self.value)


class PrintCommand(Command):
    def __init__(self, ll):
        self.ll = ll

    def execute(self):
        print(self.ll)
        return self.ll


ll = []
commands = [
    AddCommand(ll, 3),
    AddCommand(ll, 7),
    PrintCommand(ll),
    AddCommand(ll, -7),
    PrintCommand(ll),
    AddCommand(ll, 11),
]

[c.execute() for c in commands]


class GenericCommand(Command):
    def __init__(self, func):
        self.func = func

    def execute(self):
        return self.func()


ll = []
commands = [
    # AddCommand(ll, 3),
    # AddCommand(ll, 7),
    # PrintCommand(ll),
    # AddCommand(ll, -7),
    # PrintCommand(ll),
    # AddCommand(ll, 11),
    GenericCommand(lambda: ll.append(3)),
    GenericCommand(lambda: ll.append(7)),
    GenericCommand(lambda: print(ll)),
    GenericCommand(lambda: ll.append(-7)),
    GenericCommand(lambda: print(ll)),
    GenericCommand(lambda: ll.append(11)),
    GenericCommand(lambda: print(ll)),

]

[c.execute() for c in commands]
