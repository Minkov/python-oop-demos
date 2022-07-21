class custom_range:
    def __init__(self, n):
        self.next_value = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_value == self.n:
            raise StopIteration

        value_to_return = self.next_value
        self.next_value += 1
        return value_to_return


class custom_range_with_generator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        value = 1
        while value < self.n:
            yield value  # `yield` is a keyword
            value += 1


def first_n(n):
    """
    Get an iterator for the numbers from 1 to n, exclusive
    """
    value = 1
    while value < n:
        yield value
        value += 1


iter1 = iter(custom_range_with_generator(10))
iter2 = iter(custom_range_with_generator(10))

print(iter1 == iter2)
print(iter1)
print(iter2)

print('iter1', next(iter1))
print('iter1', next(iter1))
print('iter1', next(iter1))

print('iter2', next(iter2))

print('iter1', next(iter1))
print('iter1', next(iter1))
#
# for x in custom_range(10):
#     print(x)
#
# for x in first_n(10):
#     print(x)
#
# print(custom_range(10))
# print(first_n(10))
