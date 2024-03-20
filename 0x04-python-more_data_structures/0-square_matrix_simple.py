#!/usr/bin/python3
def square_matrix_simple(matrix=None):
    if matrix is None:
        return []
    new_matrix = []
    sq = lambda x: x ** 2
    for row in matrix:
        new_matrix.append(list(map(sq, row)))
    return new_matrix
