import pytest
import src.my_functions as my_function

def test_add():
    result = my_function.add(number_one=1, number_two=4)
    assert result == 5

def test_add_string():
    result = my_function.add(number_one="I love ", number_two="Sindh")  
    assert result == "I love Sindh"
def test_divide():
    result = my_function.divide(number_one=10, number_two=5)
    assert result == 2
    
def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_function.divide(number_one=10, number_two=0)