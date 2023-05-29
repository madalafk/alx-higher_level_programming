#!/usr/bin/python3

def raise_exception_msg(message=""):
    """
    Raises a name exception with a specified message.

    Args:
        message (str): message to be included in the exception.

    Raises:
        NameError: will raise a NameError with specified message Always.
    """
    raise NameError(message)
