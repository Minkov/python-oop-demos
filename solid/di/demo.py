# Open-close principle

"""
You are given a list of shapes.
Calculate the sum of their ares.
And print it
"""
import math

from shapes import Rect, Circle, Triangle, Square, MyShape


class ShapesCalculator:
    def _calc_shape_area(self, shape):
        return shape.area()

    def calculate_areas_sum(self, shapes):
        return sum(self._calc_shape_area(s) for s in shapes)

    # Adding this is not a violation to OCP
    def calculate_perimeter_sum(self, shapes):
        pass


class StdinPrinter:
    def print(self, message):
        print(message)


class FilePrinter:
    def __init__(self, filename):
        self.filename = filename

    def print(self, message):
        with open(self.filename, 'a') as file:
            file.writelines([message])


class ShapesController:
    def __init__(self, printer, area_calculator):
        self.printer = printer
        self.area_calculator = area_calculator

    def print_areas_sum(self, shapes):
        area_sum = self.area_calculator.calculate_areas_sum(shapes)
        self.printer.print(f'Area sum of shapes is: {area_sum}')


shapes = [
    Circle(10),  # area = 10 * 10 * 3.14 ~ 314.XYZ
    Rect(4, 5),  # area = 4 * 5 = 20
    Triangle(2, 5),  # area = 2 * 5 / 2 = 5
    Square(4),  # area = 4*4 = 16
    MyShape(),
]  # area_sum = 314.XYZ + 20 + 5 + 16 ~ 355.XYZ

sc = ShapesController()
sc.printer = FilePrinter('sd')
sc.print_areas_sum(shapes)

sc.printer = StdinPrinter()
sc.print_areas_sum(shapes)
# IoC
