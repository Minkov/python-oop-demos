def dec(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@dec
def x():
    pass


# decorator factory
def dec_with_params(params):
    def dec(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return dec


@dec_with_params(params='asd')
def y():
    pass
