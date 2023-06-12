#!/usr/bin/python3
# 101-add_attribute.py
"""Defines a function that adds attributes to objects if possible."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object.
    Args:
        obj (any): Object to add an attribute to.
        att (str): Name of the attribute to add to obj.
        value (any): value of attribute.
    Raises:
        TypeError: If the attr cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
