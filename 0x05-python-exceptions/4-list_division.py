#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    does Division of element / element from the two lists.

    Args:
        my_list_1 (list): 1st list.
        my_list_2 (list): 2nd list.
        list_length (int): desired length from the resulting list.

    Returns:
        new list of length (list_length) having all the divisions.
    """
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)

    return (new_list)
