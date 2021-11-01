class C1:
    def __init__(self, c1_value):
        self.c1_value = c1_value

    def f1(self):
        print('I am from C1')


class C2:
    def __init__(self, c2_value):
        self.c2_value = c2_value

    def f2(self):
        print('I am from C2')


class C12(C1, C2):
    def __init__(self, c1_value, c2_value):
        C1.__init__(self, c1_value)
        C2.__init__(self, c2_value)

    def f1(self):
        print('-- From c12 --')
        super().f1()

    def f2(self):
        print('-- From c12 --')
        super().f2()


instance = C12('1', '2')
instance.f1()
instance.f2()
print(instance.c1_value)
print(instance.c2_value)

print(C12.mro())
