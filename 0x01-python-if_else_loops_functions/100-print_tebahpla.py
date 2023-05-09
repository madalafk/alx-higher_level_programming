#!/usr/bin/python3

# prints the ASCII alphabet, in reverse code

for c in range(ord('z'), ord('a') - 1, -1):
    print("{}{}".format(chr(c), chr(c - 32)), end="")
