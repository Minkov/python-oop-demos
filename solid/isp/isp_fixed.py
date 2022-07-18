import abc
import math


class ShapeCalculator(abc.ABC):
    @abc.abstractmethod
    def get_area(self, *args):
        pass

    @abc.abstractmethod
    def get_perimeter(self, *args):
        pass


class CircleCalculator(ShapeCalculator):
    def get_area(self, radius):
        return radius * radius * math.pi

    def get_perimeter(self, radius):
        return 2 * radius * math.pi


class RectangleCalculator(ShapeCalculator):
    def get_area(self, width, height):
        return width * height

    def get_perimeter(self, width, height):
        return width * 2 + height * 2


sizes = [
    (10,),  # Circle
    (4, 2,),  # Rect
    (5, 4,),  # Triangle
]
