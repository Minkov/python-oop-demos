# SRP violation - calculate area for both triangle and rect
#  Solved by splitting into multiple classes
import os


class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_triangle_area(self):
        return self.width * self.height / 2


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_rectangle_area(self):
        return self.width * self.height


class ComplexShape:
    def __init__(self, shapes):
        self.shapes = shapes

    def get_complex_shape_area(self):
        total_area = 0
        for shape in self.shapes:
            if shape is Triangle:
                total_area += shape.get_triangle_area()
            elif shape is Rectangle:
                total_area += shape.get_rectangle_area()
        return total_area


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
cs = ComplexShape([tr, rect])

printer.print(tr.get_triangle_area())
printer.print('-' * 10)
printer.print(rect.get_rectangle_area())
printer.print('-' * 10)
printer.print(cs.get_complex_shape_area())
