# DoD
class C0:
    def __init__(self, value):
        self.value = value

    def f1(self):
        print('C0')


class C1(C0):
    def __init__(self):
        super().__init__('C1')


class C2(C0):
    def __init__(self):
        super().__init__('C2')


class C12(C1, C2):
    def __init__(self):
        super().__init__()
        # C2.__init__(self)


print(C1().value)
print(C2().value)

ins = C12()
ins.f1()
print(ins.value)
