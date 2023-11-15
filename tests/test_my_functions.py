import pytest
import src.my_functions as my_function
import time


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
    
@pytest.mark.slow    
def test_very_slow():
    time.sleep(2)
    result = my_function.divide(number_one=10, number_two=5)
    assert result == 2
    
@pytest.mark.skip(reason="This feature is broken for now")
def test_new_add():
    assert my_function.add(number_one=1, number_two=2) == 3
    
@pytest.mark.xfail(reason= " We cannot divide by zero ")
def test_divide_by_zero_broken():
    my_function.divide(number_one=4, number_two=0)