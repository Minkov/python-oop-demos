from decorators.cache import cache
from decorators.measure_time import measure_time

'''
@measure_time
@cache
def fibonacci(n):
    ...
=> fibonacci = measure_time(cache(fibonacci))

@cache
@measure_time
def fibonacci(n):
    ...
=> fibonacci = cache(measure_time(fibonacci))

'''


@cache
@measure_time
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(5))  # = 5
print(fibonacci(6))  # = 8
print(fibonacci(30))  # = 8
print(fibonacci(30))  # = 8
print(fibonacci(n=36))  # = 8
