#!/usr/bin/python3

"""
Module qui permet de travailler sur les intéractions avec l'utilisateur,
en utilisant les "Input" et des "Output"
"""


def append_write(filename="", text=""):

    """
    Méthode d'instance qui ajoute une chaine de caractère à la fin d'un
    fichier et retourne le nombre de caractère.
    """

    with open(filename, "a+", encoding="utf-8") as f:
        return f.write(text)
