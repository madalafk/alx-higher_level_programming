#!/usr/bin/python3

def safe_print_integer(value):
    """Print an int with "{:d}".format().

    Args:
        value: The value to be print.

    Returns:
        True if the value is an int and has been correctly printed,
        otherwise False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
