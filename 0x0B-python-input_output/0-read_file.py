#!/usr/bin/python3
# 0-read_file.py
""" This module contains a function that reads a text file (UTF8)
and prints it to stdout
"""


def read_file(filename=""):
    """ Function that reads from file

    Args:
        filename: filename to read from

    Raises:
        Exception: file opened

    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')

