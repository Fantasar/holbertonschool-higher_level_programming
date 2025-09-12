#!/usr/bin/python3
"""
This module provides a function to add two integers,
ensuring that both inputs are integers or floats.
If inputs are floats, they are cast to integers before addition.
"""


def add_integer(a, b=98):

    """
    Adds two integers.

    Args:
        a (int, float): The first number.
        b (int, float, optional): The second number. Defaults to 98.

    Returns:
        int: The sum of a and b, after casting floats to integers.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float) and (math.isnan(a) or math.isinf(a)):
        raise ValueError("a cannot be NaN or infinity")
    if isinstance(b, float) and (math.isnan(b) or math.isinf(b)):
        raise ValueError("b cannot be NaN or infinity")
    
    return int(a) + int(b)
