def len2(obj):
    # if not hasattr(obj, '__len__'):
    #     raise TypeError('Must have __len__')
    return obj.__len__()


class Items:
    def __init__(self, *args):
        self._items = list(args)

    def __len__(self):
        return len(self._items)


print(len2(Items(1, 2, 3)))
print(len2([1, 2, 3, 4]))
print(hasattr(Items(), '_items'))
print(len2(1))
