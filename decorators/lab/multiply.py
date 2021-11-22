import functools


def multiply(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * times

        return wrapper

    return decorator


@multiply(4)
def add_ten(number):
    return number + 10


print(add_ten(3))  # 39


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))  # 80
