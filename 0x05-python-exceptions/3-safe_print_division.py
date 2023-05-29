#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Divides two int and print the result.

    Args:
        a (int): The dividend.
        b (int): The divisor.

    Returns:
        value of the division if successful, else None.
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
