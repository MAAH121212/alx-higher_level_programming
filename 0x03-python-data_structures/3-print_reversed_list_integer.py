#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    for i in range(length):
        i += 1
    while i > 0:
        print("{:d}".format(i))
        i -= 1
