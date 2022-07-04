class X:
    def __init__(self, name):
        self.name = name

    def fx(self):
        print(f'I am X: Name: {self.name}')

    def f(self):
        print('I am f() from X')


class Y:
    def __init__(self, age):
        self.age = age

    def fy(self):
        print(f'I am Y; Age: {self.age}')

    def f(self):
        print('I am f() from Y')


class XY(X, Y):
    def __init__(self, name, age):
        X.__init__(self, name)
        Y.__init__(self, age)


xy = XY('Doncho', 17)
print(XY.mro())
xy.f()
xy.fy()
