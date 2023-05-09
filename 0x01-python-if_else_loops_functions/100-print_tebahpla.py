#!/usr/bin/python3

# prints the ASCII alphabet, in reverse code

for c in range(ord('Z'), ord('A') - 1, -1):
    print("{}{}".format(chr(c + 32), chr(c)), end="")
