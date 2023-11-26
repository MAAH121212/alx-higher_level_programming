#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not all(isinstance(row, list) and
               all(isinstance(elem, (int, float))
                   for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                "of integers/floats")
    row_length = len(matrix[0])
    for i in matrix:
        if len(i) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    divide_matrix = [
            [round(element / div, 2) for element in i] for i in matrix]
    return divide_matrix
