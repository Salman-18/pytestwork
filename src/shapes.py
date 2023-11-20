# Import the math module for mathematical operations.
import math
# Define an abstract class 'Shape' with methods 'area' and 'perimeter'.


class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass

# Define a class 'Circle' inheriting from 'Shape'.


class Circle(Shape):

    def __init__(self, radius) -> None:
        # Initialize with the radius.
        self.radius = radius
   
    def area(self):
        # Calculate the area of the circle.
        return math.pi * self.radius **2


    def perimeter(self):
        # Calculate the perimeter (circumference) of the circle.
        return 2 * math.pi * self.radius

# Define a class 'Rectangle' inheriting from 'Shape'.


class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        # Initialize with length and width.
        self.length = length
        self.width = width

    def __eq__(self, other):

        # Compare equality of two rectangles.
        if not isinstance(other, Rectangle):
            return False

        return self.width == other.width and self.length == other.length


    def area(self):
        # Calculate the area of the rectangle.
        return self.length * self.width

    def perimeter(self):
        # Calculate the perimeter of the rectangle.
        return (self.length * 2) + (self.width * 2)

# Define a class 'Square' inheriting from 'Rectangle'.
class Square(Rectangle):
    def __init__(self, side_length):
        # Call the __init__ method of the parent class (Rectangle).
        super().__init__(side_length, side_length)
