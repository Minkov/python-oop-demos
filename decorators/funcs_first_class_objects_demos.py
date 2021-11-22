# cache
def f(x):
    # cache_dict
    z = 7 + x

    # wrapper
    def internal_f(y):
        return z + y

    internal_f.initial_value = x

    return internal_f


f1 = f(1)
print(f1)
print(f1(2))
print(f1(3))
print(f1(4))

f2 = f(2)
print(f2)
print(f2(2))
print(f2(3))
print(f2(4))
print(f1.initial_value)
print(f2.initial_value)
