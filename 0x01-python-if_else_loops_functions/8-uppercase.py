#!/usr/bin/python3

# this function will print out  a string in uppercase followed by a new line

def uppercase(str):
    uppercase_str = ""
    for c in str:
        uppercase_c = c
        if 97 <= ord(c) <= 122:
            uppercase_c = chr(ord(c) - 32)
        uppercase_str += uppercase_c
    print("{}".format(uppercase_str))
