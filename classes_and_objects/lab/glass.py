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

    # Don't do this, prefer defensive programming
    # def fill(self, ml):
    #     if ml <= self.get_space_left():
    #         self.content += ml
    #         return f'Glass filled with {ml} ml'
    #
    #     return f'Cannot add {ml} ml'

    def empty(self):
        self.content = 0
        return 'Glass is now empty'

    def info(self):
        return f'{self.get_space_left()} ml left'


glass = Glass()
print(glass.fill(100))
print(glass.fill.__doc__)
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())

print(' --- glass.__dict__ ---')
for key, value in glass.__dict__.items():
    print(key, value)


def print_name(func):
    def internal_func(*args, **kwargs):
        print(f'****Called {func.__name__} ****')
        return func(*args, **kwargs)

    return internal_func


print(' --- Glass.__dict__ ---')
for key, value in Glass.__dict__.items():
    if callable(value):
        setattr(Glass, key, print_name(value))

g = Glass()
print(g.fill(100))
print(g.fill.__doc__)
print(g.fill(200))
print(g.empty())
print(g.fill(200))
print(g.info())