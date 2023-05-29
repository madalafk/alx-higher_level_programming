#!/usr/bin/python3

def safe_print_integer_err(value):
    """
    Prints int and handles the potential exceptions.

    Args:
        value: value to print

    Returns:
        True if  value is int and has been printed successfully, else  False
    """
    import sys
    try:
        print("{:d}".format(value))
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return (False)
    else:
        return (True)
