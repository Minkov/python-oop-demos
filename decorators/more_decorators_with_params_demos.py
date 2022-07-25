from random import random

from decorators.retry import retry


@retry
def fail(chance):
    value = random()  # 0 <= random() < 1

    if value < chance:
        raise Exception('It fails')
    return 'It works'


print(fail(0.1))
