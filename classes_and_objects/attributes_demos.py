import math


class Circle:
    # class attribute, class variable
    pi = math.pi

    def __init__(self, radius):
        # object attribute, instance attribute, instance variable
        self.radius = radius

    def calc_area(self):
        return self.radius * self.radius * self.pi


print(Circle(10).calc_area())

c1 = Circle(10)
c2 = Circle(100)
print(c1.pi)
print(c2.pi)

Circle.pi = 1  # changed for all instances
print(c1.pi)
print(c2.pi)




# class Person:
#     first_name = models.CharField(max_length=20)