#!/usr/bin/python3
"""Module containing the matrix_divided function."""


def matrix_divided(matrix, div):
    """the function divides all elements of a matrix."""
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    len_row = len(matrix[0])
    new_matrix = []
    for row in matrix:
        new_row = []
        if len(row) != len_row:
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not (isinstance(i, int) or isinstance(i, float)):
                type_err = "matrix must be a matrix (list of lists) "
                type_err += "of integers/floats"
                raise TypeError(type_err)
            new_row.append(round((i / div), 2))
        new_matrix.append(new_row)
    return new_matrix
