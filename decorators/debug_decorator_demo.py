# FUNC_NAME(arg1, arg2, arg3, kwarg1_key=kwarg1_value...) = RESULT
import functools

from cache_demos import cache


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        params = [
            ', '.join(str(x) for x in args),
            ', '.join(f'{key}={value}' for key, value in kwargs.items())
        ]

        params_string = ', '.join(params)

        print(f'{func.__name__}({params_string}) = {result}')

        return result

    return wrapper


@debug
@cache
def my_sum(x, y):
    return x + y


@debug
def my_sum_three(x, y, z):
    return x + y + z


print(my_sum)

print(my_sum(1, y=3))
print(my_sum(1, 3))
print(my_sum_three(1, 3, z=7))
