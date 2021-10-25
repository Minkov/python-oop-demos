class Phone:
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        # print(f'{self.color} {self.size} turned on!')

    def turn_off(self):
        self.is_on = False

    def get_self(self):
        return self


p1 = Phone('green', 4.7)
p2 = Phone('red', 5.1)

print(p1.get_self())
print(p2.get_self())

print(p1.is_on)
print(p2.is_on)
p1.turn_on()
print(p1.is_on)
print(p2.is_on)
p1.turn_off()
print(p1.is_on)
print(p2.is_on)


# p2.turn_on()


class Battery:
    pass


b1 = Battery()
print(b1)
print(isinstance(b1, Battery))
