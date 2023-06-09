#!/usr/bin/python3
# 4-print_square.py
"""This module defines a square-printing function."""


def print_square(size):
    """Prints a square with the character #.
    
    Args:
        size (int): Length of the square.
        
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0.
    """
    if not isinstance(size, int):
        if isinstance(size, float) and size.is_integer():
            size = int(size)
        else:
            raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
