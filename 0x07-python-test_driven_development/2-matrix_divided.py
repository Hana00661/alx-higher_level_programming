#!/usr/bin/python3
"""
function matrix_divided
"""


def matrix_divided(matrix, div):
    """
    function that returns a new matrix divided by 2

    Args:
        matrix : the matrix
        div : the divider

    Returns:
        the new matrix
    """
    if isinstance(matrix, list) is False:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    for element in matrix:
        if isinstance(element, list) is False:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        new = []
        size = len(matrix[0])
        for i in range(len(matrix)):
            if len(matrix[i]) != size:
                raise TypeError("Each row of the matrix must have the same \
size")
            new.append([])
            for j in range(len(matrix[i])):
                if isinstance(matrix[i][j], (int, float)) is False:
                    raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
                new[i].append(round(matrix[i][j] / div, 2))
        return new
