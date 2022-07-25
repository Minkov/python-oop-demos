def uppercase_basic(func_to_decorate):
    result = func_to_decorate()
    return result.upper()


def uppercase(func_to_decorate):  # The **Decorator**
    def func_wrapper():
        result = func_to_decorate()
        return result.upper()

    return func_wrapper


def get_shopping_list():
    return 'eggs, milk, sugar'


def get_name():
    """
    Very complex function
    :return:
    """
    return 'Doncho Minkov'


get_name = uppercase(get_name)  # The **Decorating** of `get_name`
get_shopping_list = uppercase(get_shopping_list)

print(f'I am {get_name()}')
print(f'I have to buy {get_shopping_list()}')
print(f'I am {get_name()}')

#
# print(uppercase(get_shopping_list))
# print(uppercase(get_name))
