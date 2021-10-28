class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def get_space_left(self):
        return self.capacity - self.content

    def fill(self, ml):
        """
            Fills water in the glass
            If no space for ml, nothing is filled in the glass
        """
        if self.get_space_left() < ml:
            return f'Cannot add {ml} ml'

        self.content += ml
        return f'Glass filled with {ml} ml'

    def empty(self):
        self.content = 0
        return 'Glass is now empty'

    def info(self):
        return f'{self.get_space_left()} ml left'


def print_func_name_decorator(func):
    def internal_func(*args, **kwargs):
        print(f'****Called {func.__name__} ****')
        return func(*args, **kwargs)

    return internal_func


print(' --- Glass.__dict__ ---')
for key, value in Glass.__dict__.items():
    if callable(value):
        setattr(Glass, key, print_func_name_decorator(value))

g = Glass()
print(g.fill(100))
print(g.fill.__doc__)
print(g.fill(200))
print(g.empty())
print(g.fill(200))
print(g.info())

print(Glass.__dict__['info'](g))
print(Glass.info(g))
