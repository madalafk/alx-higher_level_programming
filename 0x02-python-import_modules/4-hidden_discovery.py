#!/usr/bin/python3

if __name__ == "__main__":
    '''
    Program that prints all the names defined by the compiled module hidden_4.pyc
    '''

    import hidden_4

    # Print sorted name from directory
    for name in sorted(dir(hidden_4)):
        # Print only names that do not start with __
        if name[:2] != '__':
            print("{}".format(name))
