# Import the 'pytest' module for writing and executing tests.
# Import the 'shapes' module that contains the shapes classes for testing.

import pytest
import src.shapes as shapes


# This is a conftest file, serving as a common place for fixtures and other configurations.

# Fixture to create an instance of the 'Rectangle' class with specific length and width.
# The 'my_rectangle' fixture is used for testing.


@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(length=10, width=20)

# Fixture to create another instance of the 'Rectangle' class with different length and width.
# The 'other_rectangle' fixture is used for additional testing.


@pytest.fixture
def other_rectangle():
    return shapes.Rectangle(length=5, width=6)
