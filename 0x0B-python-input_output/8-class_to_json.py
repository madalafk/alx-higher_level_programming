#!/usr/bin/python3
"""This  Modul has a function tha returns the dictionary description with a simple
data structure for a JSON serialization of an object
"""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
