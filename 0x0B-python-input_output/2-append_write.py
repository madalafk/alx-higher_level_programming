#!/usr/bin/python3

"""This  Module contains a function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """ Function that appends a string to a text file

    Args:
        filename: filename to write to 
        text: text to write

    Raises
        Exception: None

    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
