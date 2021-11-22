import functools

from logger_demos import log


def uppercase(func_to_be_decorated):
    @functools.wraps(func_to_be_decorated)
    def wrapper_uppercase():
        result = func_to_be_decorated()
        return str(result).upper()

    return wrapper_uppercase


@log
@uppercase
def say_hi():
    return 'Hello, Doncho!'


def say_bye():
    return 'Bye, Doncho!'


def my_sum():
    return 1 + 2


# say_hi = uppercase(say_hi)
print(say_hi)
# say_bye = uppercase(say_bye)
# my_sum = uppercase(my_sum)

print(say_hi())
print(say_hi())
print(say_hi())
print(say_bye())
print(my_sum())
