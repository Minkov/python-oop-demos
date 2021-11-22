import functools


def log(func):
    @functools.wraps(func)
    def wrapper():
        print(f'{func.__name__} executed')
        return func()

    return wrapper


@log
def f1():
    return 5


print(f1())


def f2():
    return 5


f2 = log(f2)
print(f2())
