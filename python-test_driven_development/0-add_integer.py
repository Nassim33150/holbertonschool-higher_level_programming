#!/usr/bin/python3
"""
    Add two integers or floats.

    Args:
        a (int, float): The first number.
        b (int, float): The second number. Defaults to 98.

    Raises:
        TypeError: If either 'a' or 'b' is not an integer or float.

    Returns:
        int: The sum of 'a' and 'b', after
        converting them to integers if they are floats.
    """


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
