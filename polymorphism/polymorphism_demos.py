import math


class Shape:
    def area(self):
        pass


class Rect(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi


def print_area(shape: Shape):
    # if isinstance(shape, Rect):
    #     print(shape.rect_area())
    # elif isinstance(shape, Circle):
    #     print(shape.circle_area())
    print(shape.area())
    # print(shape.width, shape.height)


r = Rect(2, 5)
c = Circle(3)
shapes: list[Shape] = [
    r,
    c,
]

[print_area(s) for s in shapes]

print(isinstance(r, Rect))
print(isinstance(r, Circle))
print(isinstance(r, Shape))
# print_area(2)
print(Rect.mro())


class Person:
    def say_hello(self):
        print("Hello! 1")

    def say_hello(self):
        print("Hello! 2")


Person().say_hello()
