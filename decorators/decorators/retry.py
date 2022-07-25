import time
from functools import wraps


def retry(count, timeout_in_seconds=1):
    DEFAULT_COUNT = 1

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            the_exception = None
            for i in range(count):
                try:
                    return func(*args, **kwargs)
                except Exception as ex:
                    print(f'Try {i + 1} failed. Retrying...')
                    the_exception = ex
                    time.sleep(timeout_in_seconds)

            raise the_exception

        return wrapper

    func = count if callable(count) else None
    count = count if not callable(count) else DEFAULT_COUNT

    if func:  # @log
        return decorator(func)
    else:  # @log(...)
        return decorator
