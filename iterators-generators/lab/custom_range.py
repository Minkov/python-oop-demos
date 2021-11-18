class custom_range_iterator:
    def __init__(self, custom_range):
        # self.custom_range = custom_range
        self.start = custom_range.start
        self.end = custom_range.end
        self.step = custom_range.step
        self.current_number = self.start

    def __next__(self):
        if self.step > 0 and self.current_number > self.end:
            raise StopIteration
        if self.step < 0 and self.current_number < self.end:
            raise StopIteration

        value_to_return = self.current_number
        self.current_number += self.step

        return value_to_return


# Break until 19:10

class custom_range:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.current_number = self.start

    # return an object with a method `__next__`
    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0 and self.current_number > self.end:
            raise StopIteration
        if self.step < 0 and self.current_number < self.end:
            raise StopIteration

        value_to_return = self.current_number
        self.current_number += self.step

        return value_to_return


one_to_ten = custom_range(1, 5, 3)
for num in one_to_ten:
    print(num)

one_to_ten = custom_range(5, 1, -1)
for num in one_to_ten:
    print(num)

#
# for x in one_to_ten:
#     print(f' --- Outer loop - {x} ---')
#     for y in one_to_ten:
#         print(f' --- Inner loop - {y} ---')
#
# print('-' * 20)
# r = range(1, 4)
#
# for x in r:
#     print(f' --- Outer loop - {x} ---')
#     for y in r:
#         print(f' --- Inner loop - {y} ---')
