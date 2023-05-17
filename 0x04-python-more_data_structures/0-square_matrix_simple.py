#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for ind1, row in enumerate(new_matrix):
        for ind2, col in enumerate(new_matrix):
            new_matrix[ind1][ind2] = row[ind2] ** 2
    return new_matrix
