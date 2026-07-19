# Demonstrate abstraction using ABC

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


circle = Circle(5)
rectangle = Rectangle(10, 6)

print("Circle Area:", circle.area())
print("Rectangle Area:", rectangle.area())
