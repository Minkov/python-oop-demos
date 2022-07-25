def print_list(ll):
    pass


def increment_list_values(ll):
    return [x + 1 for x in ll]


def apply_func_for_list_values(ll, func):
    return [func(x) for x in ll]


print(
    apply_func_for_list_values([1, 2, 3], lambda x: x + 2)
)


def f(x):
    def f_internal(y):
        return x + y  # f_internal makes **closure** with `x`

    return f_internal  # no `()`


f1 = f(2)
print(f1)
print(f1(3))  # 2 + 3
print(f1(4))  # 2 + 4
print(f1(2))  # 2 + 2

f.some_prop = 42  # monkey typing
print(f.some_prop)
