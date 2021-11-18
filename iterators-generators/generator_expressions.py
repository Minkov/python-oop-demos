def gen(iterable):
    for x in iterable:
        yield x


ll = [1, 5, 17, 102]
g1 = (x / 2 for x in ll)

print([x / 2 for x in ll])
print(g1)
print(gen(ll))
