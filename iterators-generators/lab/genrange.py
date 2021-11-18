def genrange(start, end):
    return (x for x in range(start, end + 1))


def genrange_wrong(start, end):
    r = [x for x in range(start, end + 1)]
    return (x for x in r)


print(list(genrange(1, 10)))
