#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for eachList in matrix:
        if not all(isinstance(number, (int, float)) for number in eachList):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(eachList) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = [round(number / div, 2) for number in eachList]
        new_matrix.append(new_row)
    return new_matrix
