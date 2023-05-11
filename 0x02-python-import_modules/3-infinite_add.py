#!/usr/bin/python3

def add_arg(argv):
    n = len(argv) - 1
    if n == 0:
        print("{:d}".format(n))
        return
    else:
        i = 1
        add = 0
        while i <= n:
            add += int(argv[i])
            i += 1
        print("{:d}".format(add))

if __name__ == "__main__":
    '''
    Program that prints the result of the addition of all arguments.
    '''
    import sys
    add_arg(sys.argv)
