def genrange(start, end):
    value = start

    while value < end + 1:
        yield value
        value += 1


print(list(genrange(1, 10)))
