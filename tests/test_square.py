# Import necessary modules for testing.
import pytest
import src.shapes as shapes


@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (6, 36), (7, 49), (8, 64), (9, 81)])
def test_multiple_square_areas(side_length, expected_area):
    """
    Test function to check the calculation of the area for multiple square instances.

    Parameters:
    - side_length: Length of the square's side.
    - expected_area: Expected area of the square.
    """
    # Create a square instance with the specified side length and check if the area matches the expected value.
    assert shapes.Square(side_length=side_length).area() == expected_area


@pytest.mark.parametrize("side_length, expected_perimeter", [(3, 12), (4, 16), (5, 20), (6, 24), (7, 28)])
def test_multiple_square_perimeter(side_length, expected_perimeter):
    """
    Test function to check the calculation of the perimeter for multiple square instances.

    Parameters:
    - side_length: Length of the square's side.
    - expected_perimeter: Expected perimeter of the square.
    """
    # Create a square instance with the specified side length and check if the perimeter matches the expected value.
    assert shapes.Square(side_length=side_length).perimeter() == expected_perimeter
