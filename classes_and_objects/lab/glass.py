class Glass:
    initial_content = 0
    capacity = 250

    def __init__(self):
        self.content = self.initial_content

    def fill(self, ml):
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


glass = Glass()
glass2 = Glass()

print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
