#!/usr/bin/python3

"""
Module qui retourne un triangle Pascal
"""


def pascal_triangle(n):

    """
    Retourne une liste d'entier qui représente un triangle
    de caractère n
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for idx in range(1, n):
        prev_row = triangle[-1]
        row = [1]

        for idx2 in range(1, i):
            row.append(prev_row[idx2 - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle
