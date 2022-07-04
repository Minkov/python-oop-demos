class X:
    def __init__(self, name):
        print(f'X.__init__({name})')
        self.name = name

    def fx(self):
        print(f'I am X: Name: {self.name}')

    def f(self):
        print('I am f() from X')


class Y:
    def __init__(self, age):
        print(f'Y.__init__({age})')
        self.age = age

    def fy(self):
        print(f'I am Y; Age: {self.age}')

    def f(self):
        print('I am f() from Y')


class XY(X, Y):
    def __init__(self, name, age):
        X.__init__(self, name)
        Y.__init__(self, age)
        # super().__init__(name)
        # super().__init__(age)


xy = XY('Doncho', 17)
xy.fx()
xy.fy()
xy.f()

print(xy)

'''
class X

class X1 inherits X
class X2 inherits X
class X12 inherits (X1, X2)  

'''
