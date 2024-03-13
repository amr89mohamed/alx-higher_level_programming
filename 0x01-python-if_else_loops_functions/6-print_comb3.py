#!/usr/bin/python3
for num in range(10):
    for num_2 in range(num + 1, 10):
        if num == 8 and num_2 == 9:
            print("{:d}{:d}".format(num, num_2))
        else:
            print("{:d}{:d}, ".format(num, num_2), end='')
