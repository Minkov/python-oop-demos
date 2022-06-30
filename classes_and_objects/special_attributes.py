# Functions and classes in Python are first-class citizens
# i.e. they can have behavior and state

class Glass:
    """Creates a glass object

Properties:
    `content` - keeps the content of the glass

Methods:
    `fill(ml)`:
        - If enough space, adds ml to content
        - If not enough space, does not add to content
    """
    initial_content = 0
    capacity = 250

    def __init__(self):
        self.content = self.initial_content

    def fill(self, ml):
        """
`fill(ml)`:
    - If enough space, adds ml to content
    - If not enough space, does not add to content

:param ml: milliliters to add
:return: message as described above
        """
        space_left = self.calculate_space_left()
        # defensive programming:
        # 1. Check invalid cases first
        if space_left < ml:
            return f'Cannot add {ml} ml'

        # 2. Then continue
        self.content += ml
        return f'Glass filled with {ml} ml'

    def empty(self):
        self.content = 0
        return 'Glass is now empty'

    def info(self):
        space_left = self.calculate_space_left()
        return f'{space_left} ml left'

    def calculate_space_left(self):
        return self.capacity - self.content

    def __str__(self):
        return '; '.join(f'{key}={value}' for key, value in self.__dict__.items())


class_list = [
    Glass,
    list,
    set,
]

print(Glass.fill.__name__)
[print(klass.__name__) for klass in class_list]
[print(klass.__dict__) for klass in class_list]
[print(klass.__module__) for klass in class_list]

print(Glass.__doc__)
print(Glass.fill.__doc__)

gl = Glass()
print(gl.__dict__)
gl.fill(100)
print(gl.__dict__)
print(gl)
print(Glass.empty.__dict__)
