import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @property
    @abstractmethod
    def dimensions(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        return f'{self.color} shape with area: {self.area()} and perimeter: {self.perimeter()}'


class Rect(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

    @property
    def dimensions(self):
        return (self.width, self.height)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, side, height, color):
        super().__init__(color)
        self.side = side
        self.height = height

    @property
    def dimensions(self):
        return (self.side, self.height)

    def area(self):
        return self.side * self.height / 2

    def perimeter(self):
        pass
        # return math.sqrt()


shapes = [
    Rect(1, 2, 'black'),
    Rect(3, 2, 'green'),
    Rect(4, 5, 'yellow'),
    Triangle(6, 3, 'red'),
    # Shape(),
]

for s in shapes:
    print(s)
    print(s.dimensions)
