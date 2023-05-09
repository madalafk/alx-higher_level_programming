#!/usr/bin/python3

# prints out all the possible different combinations of two digits

for digit1 in range(0, 10):
    for digit2 in range(digit1, 10):
        if digit1 != digit2:
            print("{}{}".format(digit1, digit2), end=", " if not (digit1 == 8 and digit2 == 9) else "\n")
