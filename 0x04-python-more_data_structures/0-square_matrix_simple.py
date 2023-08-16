#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    ''' Function to square a matrix '''
    new_matrix = []
    for i in matrix:
        temp = []
        for x in range(len(i)):
            temp.append(i[x] ** 2)
        new_matrix.append(temp)
    return (new_matrix)
