#!/usr/bin/python3

# prints out all the possible different combinations of two digits

for dt1 in range(0, 10):
    for dt2 in range(dt1, 10):
        if dt1 != dt2:
            print("{}{}".format(dt1, dt2), end=", " if not (dt1 == 8 and dt2 == 9) else "\n")
