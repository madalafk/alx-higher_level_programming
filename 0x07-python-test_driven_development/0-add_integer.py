#!/usr/bin/python3
"""

This module module defines an addition function.

"""


def add_integer(a, b=98):
    """ This Function adds two integer or float numbers

    Args:
        a: first num
        b: second num

    Returns:
        addition of the two given numbers

    Raises:
        TypeError: If a or b aren't integer and/or float numbers

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
