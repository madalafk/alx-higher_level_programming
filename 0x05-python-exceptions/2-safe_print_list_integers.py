#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints int from a list using "{:d}".format().

    Args:
        my_list (list): list to print int from.
        x (int): number of int to print.

    Returns:
        number of int successfully printed.
    """
    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            count += 1

    print()
    return (count)
