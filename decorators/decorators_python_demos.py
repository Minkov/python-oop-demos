from functools import wraps


def uppercase(func):  # The **Decorator**
    @wraps(func)
    # @functools.wraps(func)
    def wrapper():
        result = func()
        return result.upper()

    return wrapper


# syntax sugar for `get_shopping_list = uppercase(get_shopping_list)`
@uppercase
def get_shopping_list():
    return 'eggs, milk, sugar'


@uppercase
def get_name():
    """
    Very complex function
    """
    return 'Doncho Minkov'


print(get_name)
print(get_name.__name__)
print(get_name.__doc__)
print(f'I am {get_name()}')
print(f'I have to buy {get_shopping_list()}')
print(f'I am {get_name()}')

#
# print(uppercase(get_shopping_list))
# print(uppercase(get_name))
