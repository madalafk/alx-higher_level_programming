#!/usr/bin/python3
# 1-write_file.py

""" This module that contains a function that writes string to a text file
"""


def write_file(filename="", text=""):
    """ Function that writes to a text file

    Args:
        filename: filename to read from
        text: text to write

    Raises:
        Exception: if file cannot be pened

    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
