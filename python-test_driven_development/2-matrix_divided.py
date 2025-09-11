#!/usr/bin/python3
"""
Le module produit une fonction qui divise deux valeurs,
les valeurs peuvent être des floats ou des entiers.
"""


def matrix_divided(matrix, div):

    """
    Divise toutes les valeurs d'une matrice.

    argument
        matrix (list de list en int, float): Une listes de nombres.
        div (int, float): Valeur pour la division.

    Retours
        une nouvelle lists: Elle contient les valeurs de la division
        matrix.

    Raises:
        TypeError: Si matrix contient des valeurs qui ne sont pas des entiers
        ou des floats ou si les lignes n'ont pas la même taille.
        TypeError: Si div n'est pas un nombre.
        ZeroDivisionError: Si div est égal à 0.

    Exemples:
        >>> matrix_divided([[1, 2], [3, 4]], 2)
        [[0.5, 1.0], [1.5, 2.0]]
        >>> matrix_divided([[1, 2], [3, 4]], 0)
        Traceback (most recent call last):
        ZeroDivisionError: division by zero
    """
    if not isinstance(matrix, list) or not all(isinstance(temp, list) for temp in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    longeur = len(matrix[0])
    for temp in matrix:
        if len(temp) != longeur:
            raise TypeError("Each row of the matrix must have the same size")

        for idx in temp:
            if not isinstance(idx, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    return [[round(idx / div, 2) for idx in temp] for temp in matrix]
