class Items:
    def __init__(self, *args):
        self._items = list(args)

    def add_item(self, value):
        self._items.append(value)

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __add__(self, other):
        result = Items()
        [result.add_item(x) for x in self._items]
        [result.add_item(x) for x in other._items]
        return result

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError('Items can be multiplied only by integers')

        result = Items()
        [result.add_item(x) for x in self._items * other]
        return result

    def __eq__(self, other):
        return self._items == other._items



i1 = Items(1, 2, 3)

print(len('asd'))
print(len([1, 2, 3, 4]))
print(len((1, 2, 3, 4, 5)))
print(len({1: 2, 3: 4}))
print(len(i1))

i2 = Items(-1)

i3 = Items(10, 11)

print(f'{i1} + {i2} = {i1 + i2}')
print(i1 + i2 + i3)  # (i1 + i2) + i3

print([1, 2] * 5)
print(i1 * 3)

print(Items(1, 2, 3) == Items(1, 2, 3))
print(Items(1, 2, 3) != Items(1, 2, 3))
print([1, 2, 3] == [1, 2, 3])
