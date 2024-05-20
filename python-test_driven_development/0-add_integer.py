#!/usr/bin/python3
"""

This module is composed by a function that adds two numbers

"""


def add_integer(a, b=98):
    """
    Adds two integers.
    Args:
        a: The first number, must be an integer or float.
        b: The second number, must be an integer or float (default is 98).
    Returns:
        The sum of a and b as an integer.
    Raises:
        TypeError: If a or b are not integers or floats.
    """
    # Check if a is an integer or a float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast both a and b to integers if they are floats
    a = int(a)
    b = int(b)

    return a + b
