import abc
import math
import os


class Shape(abc.ABC):
    @abc.abstractmethod
    def get_area(self):
        pass


class Triangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height / 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.radius * self.radius * math.pi


class ComplexShape(Shape):
    def __init__(self, shapes):
        self.shapes = shapes

    def get_area(self):
        # Violation of LSP
        return [sh.get_area() for sh in self.shapes]


class StdPrinter:
    def print(self, obj):
        print(obj)


class FilePrinter:
    def __init__(self, filename):
        self.filename = filename

    def print(self, obj):
        with open(self.filename, 'a') as file:
            file.write(str(obj))
            file.write(os.linesep)


printer = StdPrinter()
# printer = FilePrinter('./result.txt')

tr = Triangle(10, 5)
rect = Rectangle(10, 5)
circle = Circle(10)
cs = ComplexShape([
    tr,
    rect,
    circle,
])

shapes = [
    tr,
    rect,
    circle,
    cs,
]

[printer.print(sh.get_area()) for sh in shapes]
