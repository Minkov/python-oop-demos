def custom_range_1(n):
    value = 1
    while value < n:
        yield value
        value += 1


def custom_range_2(n):
    values = list(range(1, n))  # Creates a list of n elements
    for value in values:
        yield value


n = 1024 * 1024  # * 1024

cr1 = custom_range_1(n)
cr2 = custom_range_2(n)

print(next(cr1))
print(next(cr2))
