from abc import ABC, abstractmethod


class SortStrategy(ABC):
    @abstractmethod
    def sort(self, ll):
        pass


class AscendingSortStrategy(SortStrategy):
    def sort(self, ll):
        ll.sort()


class DescendingSortStrategy(SortStrategy):
    def sort(self, ll):
        ll.sort(reverse=True)


class ModuleByDivisorSortStrategy(SortStrategy):
    def __init__(self, divisor):
        self.divisor = divisor

    def sort_by_key(self, x):
        return (x % self.divisor, x)

    def sort(self, ll):
        ll.sort(key=self.sort_by_key)


class CountInListSortStrategy(SortStrategy):
    def sort_by_key_func(self, ll):
        counts_dict = {}
        for x in ll:
            if x not in counts_dict:
                counts_dict[x] = 0
            counts_dict[x] += 1

        def sort_by_key(x):
            return counts_dict[x]

        return sort_by_key

    def sort(self, ll):
        ll.sort(key=self.sort_by_key_func(ll))


class ListHandler:
    __sort_strategy: SortStrategy = AscendingSortStrategy()

    def __init__(self, ll: list):
        self.internal_list = ll
        self.sort()

    @property
    def sort_strategy(self):
        return self.__sort_strategy

    @sort_strategy.setter
    def sort_strategy(self, value):
        self.__sort_strategy = value
        self.sort()

    def sort(self):
        self.sort_strategy.sort(self.internal_list)

    def print(self):
        print(self.internal_list)


lh = ListHandler([1, 5, 1, 1, 1, 1, 2, 2, 45, 2, 3, 45, ])
lh.print()
lh.sort_strategy = DescendingSortStrategy()
lh.print()
lh.sort_strategy = ModuleByDivisorSortStrategy(3)
lh.print()
lh.sort_strategy = CountInListSortStrategy()
lh.print()
