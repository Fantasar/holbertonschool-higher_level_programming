#!/usr/bin/python3
"""
Fontion qui imprime un carré avec comme motif #.

"""


def print_square(size):

    """
    Args:
        Size est la longeur et largeur en entier du carré.

    Raise:
        TypeError: Si jamais size est un float ou une string.
        ValueError: Si jamais size est plus petit que 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for longeur in range(size):
        for largeur in range(size):
            print("#", end="")
        print()
