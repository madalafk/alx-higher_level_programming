#!/usr/bin/python3
# 1-my_list.py
"""This function defines an inherited list class 'MyList'."""


class MyList(list):
    """Inherits from the built-in 'lis' class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
