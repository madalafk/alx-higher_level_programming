#!/usr/bin/python3

# this function will print out  a string in uppercase followed by a new line

def uppercase(str):
    for char in str:
        uppercase_char = chr(ord(char) - 32) if 97 <= ord(char) <= 122 else char
        print("{}".format(uppercase_char), end="")
    print()
