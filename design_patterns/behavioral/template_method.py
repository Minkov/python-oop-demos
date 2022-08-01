import abc


class Sorter(abc.ABC):
    # template method
    @abc.abstractmethod
    def key_func(self, value):
        pass

    def sort(self, elements):
        return sorted(elements, key=self.key_func)


class NaturalSorter(Sorter):
    def key_func(self, value):
        return value


class ByDivisionRemainderSorter(Sorter):
    def __init__(self, base):
        self.base = base

    def key_func(self, value):
        return value % self.base, value


ns = NaturalSorter()
bdrs = ByDivisionRemainderSorter(3)

values = [1, 6, 3, 4, 2]

print(ns.sort(values))
print(bdrs.sort(values))
