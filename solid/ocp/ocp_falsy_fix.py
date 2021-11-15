# Open-close principle

"""
You are given a list of shapes.
Calculate the sum of their ares.
And print it
"""
import math

from shapes import Rect, Circle, Triangle, Square


class ShapesAreaCalculator:
    def _calc_shape_area(self, shape):
        if isinstance(shape, Rect):
            return shape.width * shape.height
        elif isinstance(shape, Circle):
            return shape.radius * shape.radius * math.pi

    def calculate_areas_sum(self, shapes):
        return sum(self._calc_shape_area(s) for s in shapes)


class ShapesAreaCalculatorWithTriangle(ShapesAreaCalculator):
    def _calc_shape_area(self, shape):
        if isinstance(shape, Triangle):
            return shape.height * shape.side / 2
        return super()._calc_shape_area(shape)


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
    shapes_area_calculator = ShapesAreaCalculatorWithTriangle()
    # printer = FilePrinter('./output.txt')
    printer = StdinPrinter()

    def print_areas_sum(self, shapes):
        area_sum = self.shapes_area_calculator.calculate_areas_sum(shapes)
        self.printer.print(f'Area sum of shapes is: {area_sum}')


shapes = [
    Circle(10),  # area = 10 * 10 * 3.14 ~ 314.XYZ
    Rect(4, 5),  # area = 4 * 5 = 20
    Triangle(2, 5),  # area = 2 * 5 / 2 = 5
]  # area_sum = 314.XYZ + 20 + 5~ 339.XYZ

ShapesController().print_areas_sum(shapes)
