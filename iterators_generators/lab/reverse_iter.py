# Full implementation
class reverse_iter:
    def __init__(self, values):
        self.values = list(values)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < -len(self.values):
            raise StopIteration

        value_to_return = self.values[self.index]
        self.index -= 1
        return value_to_return


class reverse_iter2:
    def __init__(self, values):
        self.values = reversed(values)

    def __iter__(self):
        return iter(self.values)


for item in reverse_iter2([1, 2, 3, 4]):
    print(item)

for item in reverse_iter2({1, 2, 3, 4}):
    print(item)
