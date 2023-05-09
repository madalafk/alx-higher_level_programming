#!/usr/bin/python3

# prints out all the possible different combinations of two digits

for dt1 in range(0, 10):
    for dt2 in range(dt1 + 1, 10):
        print("{}{}".format(dt1, dt2), end=", ")
print("09")
