# wrong
def squares_wrong(n):
    s = [x * x for x in range(1, n + 1)]
    for x in s:
        yield x


# correct v1
def squares_v1(n):
    for x in range(1, n + 1):
        yield x * x


# correct v2
def squares_v2(n):
    return (x * x for x in range(1, n + 1))


print(list(squares(5)))
