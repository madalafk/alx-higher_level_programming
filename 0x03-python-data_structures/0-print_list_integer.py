#!/usr/bin/python3

'''
A program that imports all functions from the file calculator_1.py
and handles basic operations.
'''

def print_list_integer(my_list=[]):
    for number in range(len(my_list)):
        print("{:d}".format(my_list[number]))
