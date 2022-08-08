class ListInternal:
    def __init__(self):
        self.__values = []

    def append(self, value):
        self.__values.append(value)
        return self

    def remove(self, index):
        self.__validate_index(index)
        return self.__values.pop(index)

    def get(self, index):
        self.__validate_index(index)
        return self.__values[index]

    def extend(self, iterable):
        [self.append(v) for v in iterable]
        return self

    def insert(self, index, value):
        self.__validate_index(index, min_index=-self.size() - 1, max_index=self.size() + 1)

        self.__values.insert(index, value)

        return self

    def pop(self):
        return self.__values.pop()

    def clear(self):
        self.__values.clear()

    def index(self, value):
        return self.__values.index(value)

    def count(self, value):
        return self.__values.count(value)

    def reverse(self):
        return self.list_with_values(self.__values[::-1])

    def copy(self):
        return self.list_with_values(self.__values)

    def size(self):
        return len(self.__values)

    def add_first(self, value):
        self.insert(0, value)

    def dictionize(self):
        """
        Returns the list as a dictionary:
            - The keys will be each value on an even position
            - The values will be each value on an odd position
            - If the last value is on an even position, it’s value will be " " (space)
        """
        dict_values = self.__values.copy()
        if len(dict_values) % 2 == 1:
            dict_values.append(' ')

        return {dict_values[index]: dict_values[index + 1] for index in range(0, len(dict_values), 2)}

    def move(self, count):
        """
            Move the first `count` of values to the end of the list
            :returns the list.
        """
        if count == 0:
            return self
        if count < 0 or self.size() < count:
            raise IndexError('Invalid move count')

        self.__values = self.__values[count:] + self.__values[:count]

        return self

    def sum(self):
        return sum(self.__values)

    def underbound(self):
        fixed_values = [self.__get_compare_value(x) for x in self.__values]
        value = min(fixed_values)
        return fixed_values.index(value)

    def overbound(self):
        fixed_values = [self.__get_compare_value(x) for x in self.__values]
        value = max(fixed_values)
        return fixed_values.index(value)

    def __validate_index(self, index, min_index=None, max_index=None):
        if not min_index:
            min_index = -self.size()
        if not max_index:
            max_index = self.size()
        if not isinstance(index, int):
            raise TypeError('Index should be an integer')

        if index < min_index or max_index <= index:
            raise IndexError('Index is out of bounds')

    @staticmethod
    def __get_compare_value(value):
        if isinstance(value, int):
            return value
        if hasattr(value, '__len__'):
            return len(value)

        raise ValueError('Invalid value')

    @classmethod
    def list_with_values(cls, values):
        ll = cls()
        [ll.append(v) for v in values]
        return ll

    def __len__(self):
        return self.size()

    def __getitem__(self, item):
        return self.get(item)

    def __iter__(self):
        for value in self.__values:
            yield value
