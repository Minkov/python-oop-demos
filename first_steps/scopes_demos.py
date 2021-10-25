x = 5
y = -1
ll = []


def f1():
    print(f'From f1: {x}')


def f2():
    global x
    global ll
    x = 6
    ll.append(2)
    ll = []
    print(f'From f2: {x}')


def f3():
    x = 7

    def f31():
        print(f'From f31: {x}')
        print(f'From f31: y={y}')

    def f32():
        nonlocal x
        x = 8
        print(f'From f32: {x}')

    f31()
    f32()
    print(f'From f3: {x}')


f1()
f2()
f3()
print(f'From global: {x}')


# def sum_partial(x):
#     def sum_second(y):
#         return x + y
#
#     return sum_second
#
#
# s = sum_partial(1)
# print(s(2))
# print(s(3))
