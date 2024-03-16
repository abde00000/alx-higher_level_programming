#!/usr/bin/python3
def print_matrix_integer(matrix=None):
    if matrix is None:
        matrix = []
    for list_1 in matrix:
        for num in list_1:
            print("{:d}".format(num), end=" ")
        print()
