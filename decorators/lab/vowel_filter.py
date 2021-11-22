import functools
from functools import wraps


def is_vowel(ch):
    return ch in ('eyuoai' + 'eyuoai'.upper())


def vowel_filter(func):
    @wraps(func)
    def wrapper():
        result = func()
        return [c for c in result if is_vowel(c)]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


@vowel_filter
def say_hi():
    return 'Hello, Doncho!'


@vowel_filter
def say_bye():
    return 'Bye, Doncho!'


print(get_letters())  # ["a", "e"]
print(say_hi())
print(say_bye())
