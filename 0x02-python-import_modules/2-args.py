#!/usr/bin/python3

if __name__ == "__main__":
    '''
    This program prints the number of and the list of its arguments.
    '''
    import sys

    arg = sys.argv
    num_elements = len(arg) - 1

    if num_elements > 1:
        print("{} arguments:".format(num_elements))
        for i in range(1, num_elements + 1):
            print("{}: {}".format(i, arg[i]))

    elif num_elements == 0:
        print("{} arguments.".format(num_elements))

    else:
        print("{} argument:".format(num_elements))
        print("{}: {}".format(num_elements, arg[1]))
