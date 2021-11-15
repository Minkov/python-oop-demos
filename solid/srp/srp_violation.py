# Single responsibility principle

"""
You are given a list of shapes.
Calculate the sum of their ares.
And print it
"""
import math

from shapes import Rect, Circle


class ShapesController:
    def _calc_shape_area(self, shape):
        if isinstance(shape, Rect):
            return shape.width * shape.height
        elif isinstance(shape, Circle):
            return shape.radius * shape.radius * math.pi

    # Violation of SRP, 2 responsibilities:
    # - Calc of area sum
    # - Printing the sum
    def print_areas_sum(self, shapes):
        area_sum = sum(self._calc_shape_area(s) for s in shapes)
        print(f'Area sum of shapes is :{area_sum}')


shapes = [
    Circle(10),  # area = 10 * 10 * 3.14 ~ 314.XYZ
    Rect(4, 5),  # area = 4 * 5 = 20
]  # area_sum = 314.XYZ + 20 ~ 334.XYZ

ShapesController().print_areas_sum(shapes)















