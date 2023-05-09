#!/usr/bin/python3

# function that creates a copy of the string, removes character
# position n (not the Python way, the “C array index”)

def remove_char_at(string, n):
    if n < 0 or n >= len(string):
        return string

    new_string = ""
    for i in range(len(string)):
        if i != n:
            new_string += string[i]

    return new_string
