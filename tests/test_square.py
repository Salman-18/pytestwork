import pytest
import src.shapes as shapes

@pytest.mark.parametrize("side_length, expected_area", [(5,25), (6,36), (7,49), (8,64), (9,81)])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length=side_length).area() == expected_area
    
    
@pytest.mark.parametrize("side_length, expected_perimeter", [(3,12), (4,16), (5,20), (6,24),(7,28)])
def test_multiple_square_perimeter(side_length,expected_perimeter):
    assert shapes.Square(side_length=side_length).perimeter() == expected_perimeter