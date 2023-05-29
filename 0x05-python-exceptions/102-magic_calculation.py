def magic_calculation(a, b):
    """
    Performs magic calculation.

    Args:
        a: An int representing 1st parameter.
        b: An int representing 2nd parameter.

    Returns:
        result from magic calculation.

    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += a ** b / i
        except Exception:
            result = b + a
            break
    return (result)
