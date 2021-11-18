def custom_range(start, end):
    for x in range(start, end):
        yield x


# for x in custom_range(1, 5):
#     print(f'From loop: {x}')


iter1 = custom_range(1, 6)

print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))

#
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def __iter__(self):
#         for c in self.name:
#             yield c
#
#
# for x in Person('Doncho'):
#     print(x)
