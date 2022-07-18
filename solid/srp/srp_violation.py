class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # SRP violation - calculate area for both triangle and rect
    def print_triangle_area(self):
        area = self.width * self.height / 2
        print(area)  # SRP Violation - calculation and printing

    # SRP violation - calculate area for both triangle and rect
    def print_rectangle_area(self):
        area = self.width * self.height
        print(area)  # SRP Violation - calculation and printing


tr = Shape(10, 5)
rect = Shape(10, 5)

tr.print_triangle_area()
print('-' * 100)
rect.print_rectangle_area()
