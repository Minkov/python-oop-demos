import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rect:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def area(self):
        return self.width * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi


class Triangle:
    def __init__(self, side, height):
        self.side = side
        self.height = height

    def area(self):
        return self.side * self.height / 2


class Square(Rect):
    def __init__(self, side):
        super().__init__(side, side)


class MyShape:
    def area(self):
        return 3.13 * 7.3
