#!/usr/bin/python3
# 5-text_indentation.py
"""This module defines text-indentation function."""

def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    y = 0
    while y < len(text) and text[y] == ' ':
        y += 1

    while y < len(text):
        if text[y] == '.' or text[y] == '?' or text[y] == ':':
            print(text[y])
            print()
        else:
            print(text[y], end='')

        y += 1
