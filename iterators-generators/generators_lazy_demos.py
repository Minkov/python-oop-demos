# def fibonacci(n):
#     fib = [0, 1]
#     for _ in range(2, n + 1):
#         fib.append(fib[-1] + fib[-2])
#     return fib
#
#
# def fibonacci_gen():
#     x = 0
#     y = 1
#     yield x
#     while True:
#         x, y = y, x + y
#         yield x
#
#
# print(fibonacci(5))
# print(fibonacci(11))
# print(fibonacci(17))
#
# fibonacci_iter = fibonacci_gen()
# for i in range(6):
#     print(next(fibonacci_iter))
#
# for i in range(6):
#     print(next(fibonacci_iter))
from time import time


def increase_by_1_v1(iterable):
    result = [x + 1 for x in iterable]
    for x in result:
        yield x


def increase_by_1_v2(iterable):
    for x in iterable:
        yield x + 1


def increase_by_1_v3(iterable):
    return (x + 1 for x in iterable)


ll = list(range(2 ** 25))

start = time()

# iter1 = increase_by_1_v1(ll)
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
for x in increase_by_1_v1(ll):
    y = x + 1

end = time()

print(f'V1: {end - start}')

start = time()

# iter1 = increase_by_1(ll)
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
for x in increase_by_1_v2(ll):
    y = x + 1
end = time()

print(f'V2: {end - start}')
