
from abc import ABC, abstractmethod
import math

# Abstract class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


# Circle class
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Rectangle class
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Main program
circle1 = Circle(7)
rectangle1 = Rectangle(10, 5)

print("Area of Circle:", round(circle1.area(), 2))
print("Area of Rectangle:", rectangle1.area())
