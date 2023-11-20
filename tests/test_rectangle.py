# Import pytest for testing functionality.
import pytest


def test_area(my_rectangle):
    """
    Test function to check if the 'area' method of a rectangle calculates the correct area.
    """
    assert my_rectangle.area() == 10 * 20


@pytest.mark.slow
def test_perimeter(my_rectangle):
    """
    Test function to check if the 'perimeter' method of a rectangle calculates the correct perimeter.
    """
    assert my_rectangle.perimeter() == (10 * 2) + (20 * 2)


def test_not_equal(my_rectangle, other_rectangle):
    """
    Test function to check if two rectangles are not equal.
    """
    assert my_rectangle != other_rectangle
