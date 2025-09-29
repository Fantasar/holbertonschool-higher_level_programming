#!/usr/bin/python3

"""
Module qui permet de travailler sur les intéractions avec l'utilisateur,
en utilisant les "Input" et des "Output"
"""


def write_file(filename="", text=""):

    """
    Méthode d'instance qui permet de construire un fichier text
    avec une phrase.
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
