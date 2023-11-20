# Function to add two numbers.
def add(number_one, number_two):
    return number_one + number_two


# Function to divide two numbers. Raises a ValueError if the divisor is zero.
def divide(number_one, number_two):
    if number_two == 0:
        raise ValueError
    return number_one / number_two
