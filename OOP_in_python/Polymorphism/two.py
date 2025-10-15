#########################################################################################
# Create a class Shape with a method calculate_area. Derive classes Circle and Rectangle
# from Shape with their own implementations of calculate_area.
#########################################################################################
import math

class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return f"Area of circle :{math.pi}* {self.radius ** 2}"

class Rectange(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return f"Area of rectangle :{self.width * self.height}"


def main():
    circle = Circle(20)
    print(circle.calculate_area())
    rectangle = Rectange(10, 50)
    print(rectangle.calculate_area())

if __name__ := '__main__':
    main()
