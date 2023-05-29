#!/usr/bin/python3

def safe_function(fct, *args):
    """
    safely executes a function

    Args:
        fct: function to executed.
        *args: Variable num of argS passed to the function.

    Returns:
        result function execution.
        If exception occurs on execution process, returns None 
	and prints the err to stderr preceded by "Exception:".

    """
    import sys
    try:
        result = fct(*args)
    except Exception as error:
        sys.stderr.write("Exception: {}\n".format(error))
        result = None

    return (result)
