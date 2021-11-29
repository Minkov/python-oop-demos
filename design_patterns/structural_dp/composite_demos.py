import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass


class Rect(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return self.radius * self.radius * math.pi


class ComplexShape(Shape):
    def __init__(self, shapes: list[Shape]):
        self.shapes = shapes

    @property
    def area(self):
        return sum(s.area for s in self.shapes)


shapes = [
    Rect(2, 5),
    Circle(1),
    ComplexShape([Rect(2, 5), Circle(1)])
]

for s in shapes:
    print(s.area)
