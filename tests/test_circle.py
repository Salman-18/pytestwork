# Import the 'pytest' module for writing and executing tests.
# Import the 'shapes' module that contains the shapes classes for testing.
# Import the 'math' module for mathematical operations.
import pytest
import src.shapes as shapes
import math


class TestCircle:
    """
    Test class for the 'Circle' shape.
    """

    def setup_method(self, method):
        """
        Fixture setup method to create an instance of the 'Circle' class before each test method.
        """
        print(f"Setting up method {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        """
        Fixture teardown method to delete the instance of the 'Circle' class after each test method.
        """
        print(f"Tear down method {method}")
        del self.circle

    @pytest.mark.slow
    def test_area(self):
        """
        Test method to check if the 'area' method of the 'Circle' class calculates the area correctly.
        """
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        """
        Test method to check if the 'perimeter' method of the 'Circle' class calculates the perimeter correctly.
        """
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected

    def test_not_same_area_rectangle(self, my_rectangle):
        """
        Test method to ensure that the area of a circle is not equal to the area of a rectangle.
        Uses the 'my_rectangle' fixture for testing.
        """
        assert self.circle.area() != my_rectangle.area()
