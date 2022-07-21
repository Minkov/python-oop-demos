# [ -> literal for list comprehension
# { -> literal for set or dict comprehension
# ( -> literal for generator expression

'''
Generators are syntax sugar for iterators
Generator expressions are syntax sugar for generators
'''


def print_from_iter(values_iter):
    print(values_iter)
    for value in values_iter:
        print(value)


def gen_func(n):
    for x in range(n):
        yield x


print_from_iter(
    gen_func(5)
)

print_from_iter(
    (x for x in range(5))
)
