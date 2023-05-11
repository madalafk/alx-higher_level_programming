#!/usr/bin/python3

def add(a, b):
    return a + b
""" add integers, where:
    arg : a = ist Int, 2 = 2nd Int
    Returns: sum a,b
"""
if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
