#!/usr/bin/python3

output = ""
for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        output += "{}".format(chr(letter))
print(output, end="")
