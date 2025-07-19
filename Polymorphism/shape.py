from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return f"{self.width + self.height:.2f}"
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"{math.pi * self.radius ** 2:.2f}"
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    

# duck typing
def calculate_area(shape):
    return shape.area()


shapes = [Rectangle(2, 3), Circle(3), Triangle(3, 4)]

for shape in shapes:
    print(calculate_area(shape))

