#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
        return
    max_width = 0
    for row in matrix:
        for num in row:
            width = len(str(num))
            if width > max_width:
                max_width = width

    for row in matrix:
        for num in row:
            print("{:>{}}".format(num, max_width), end=" ")
        print()
