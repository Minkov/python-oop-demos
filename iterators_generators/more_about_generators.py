def gen_func(n):
    print('The start')
    for x in range(n):
        yield x


def norm_func(n):
    for x in range(n):
        return x


print(norm_func(5))
gf = gen_func(5)
print(next(gf))
