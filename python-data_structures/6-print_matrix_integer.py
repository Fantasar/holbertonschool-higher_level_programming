#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    longeur = len(matrix)
    index = 0
    while index < longeur:
        largeur = len(matrix[index])
        position = 0

        while position < largeur:
            print("{:d}".format(matrix[index][position]), end=" ")
            position += 1

        print("")
        index += 1
