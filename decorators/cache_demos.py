import functools


def cache(func):
    cache_dict = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = tuple(args) + tuple(kwargs.items())
        if cache_key not in cache_dict:
            cache_dict[cache_key] = func(*args, **kwargs)

        return cache_dict[cache_key]

    return wrapper


def call_count(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)

    wrapper.call_count = 0
    return wrapper


@call_count
@cache
def fibonacci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    # print(f'fib({n}) = {result}')
    return result


@call_count
@cache
def f(x, y, z):
    result = 0
    for i in range(1, x):
        result += f(x - i, y, z)
        for j in range(1, y):
            result += f(x, y - j, z)
            for k in range(1, z):
                result += f(x, y, z - k)
    return result


print(fibonacci(n=20))
print(fibonacci(20))
print(fibonacci(15))
print(f'Fibonacci count: {fibonacci.call_count}')

# f(3, 5, 3)
print(f.call_count)
