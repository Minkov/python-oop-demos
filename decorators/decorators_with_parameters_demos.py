import functools


def repeat(count=1):
    # def repeat(func=None, count=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(count):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator
    # if func:
    #     return decorator(func)
    # else:
    #     return decorator


@repeat(count=14)
def say_hi():
    print('Hi, Doncho!')


# @repeat
def say_bye():
    print('Bye, Doncho!')


say_hi()
say_bye()
