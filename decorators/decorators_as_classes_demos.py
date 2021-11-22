import functools


class call_count:
    # decorator
    def __init__(self, func):
        self.func = func
        self.count = 0
        functools.update_wrapper(self, func)

    # wrapper
    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


class cache:
    def __init__(self, func):
        self.func = func
        self.cache_dict = {}

    def __call__(self, *args, **kwargs):
        cache_key = tuple(args) + tuple(kwargs.items())
        if cache_key not in self.cache_dict:
            self.cache_dict[cache_key] = self.func(*args, **kwargs)
        return self.cache_dict[cache_key]


@call_count
def fibonacci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    return result


print(fibonacci)
print(fibonacci(15))
print(fibonacci.count)
