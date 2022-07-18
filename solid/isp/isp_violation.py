import math


class ShapeCalculator:
    def get_circle_area(self, radius):
        return radius * radius * math.pi

    def get_rectangle_area(self, width, height):
        return width * height

    def get_rectangle_perimeter(self, width, height):
        return width * 2 + height * 2

    def get_triangle_area(self, width, height):
        return width * height / 2


sizes = [
    (10,),  # Circle
    (4, 2,),  # Rect
    (5, 4,),  # Triangle
]
