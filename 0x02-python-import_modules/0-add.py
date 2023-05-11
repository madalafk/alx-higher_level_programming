#!/usr/bin/python3

""" add integers, where:
    arg : a = ist int, 2 = 2nd int
    Returns: sum a,b
"""

if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
