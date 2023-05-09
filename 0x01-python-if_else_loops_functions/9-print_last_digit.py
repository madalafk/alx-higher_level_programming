#!/usr/bin/python3

# this function will print the last digit of a number

def print_last_digit(number):
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit
