# Import necessary modules for testing.
import pytest
import src.my_functions as my_function
import time

# Define test functions for different functionalities.

def test_add():
    """
    Test function to check the 'add' function with integer inputs.
    """
    result = my_function.add(number_one=1, number_two=4)
    assert result == 5

def test_add_string():
    """
    Test function to check the 'add' function with string inputs.
    """
    result = my_function.add(number_one="I love ", number_two="Sindh")  
    assert result == "I love Sindh"

def test_divide():
    """
    Test function to check the 'divide' function with normal division.
    """
    result = my_function.divide(number_one=10, number_two=5)
    assert result == 2

def test_divide_by_zero():
    """
    Test function to check if the 'divide' function raises a ValueError when dividing by zero.
    """
    with pytest.raises(ValueError):
        my_function.divide(number_one=10, number_two=0)

@pytest.mark.slow
def test_very_slow():
    """
    Test function marked as slow to simulate a slow-running test.
    """
    time.sleep(2)
    result = my_function.divide(number_one=10, number_two=5)
    assert result == 2

@pytest.mark.skip(reason="This feature is broken for now")
def test_new_add():
    """
    Test function marked as skipped with a reason.
    """
    assert my_function.add(number_one=1, number_two=2) == 3

@pytest.mark.xfail(reason="We cannot divide by zero")
def test_divide_by_zero_broken():
    """
    Test function marked as xfail to denote an expected failure.
    """
    my_function.divide(number_one=4, number_two=0)
