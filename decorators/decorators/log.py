import sys
from functools import wraps


def log(filepath='./logs.txt'):
    DEFAULT_FILEPATH = './logs.txt'

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            stdout_original = sys.stdout
            with open(filepath, 'a') as file:
                sys.stdout = file
                result = func(*args, **kwargs)
            sys.stdout = stdout_original
            return result

        return wrapper

    func = filepath if callable(filepath) else None
    filepath = filepath if not callable(filepath) else DEFAULT_FILEPATH

    if func:  # @log
        return decorator(func)
    else:  # @log(...)
        return decorator

