#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for x in my_list:
        if my_list[x] % 2 == 0:
            return True, my_list[x]
    return False
