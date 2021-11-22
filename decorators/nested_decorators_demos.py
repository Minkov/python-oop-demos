from logger_demos import log
from simple_decorators_demos import uppercase


@log
@uppercase
def say_hi():
    return 'Hello, Doncho!'


def say_by():
    return 'Bye, Doncho!'


say_by = log(uppercase(say_by))
