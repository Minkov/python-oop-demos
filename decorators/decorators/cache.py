from functools import wraps


def cache(func):
    cached_values = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = args + tuple(kwargs.items())
        if key not in cached_values:
            cached_values[key] = func(*args, **kwargs)

        return cached_values[key]

    return wrapper
