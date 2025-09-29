#!/usr/bin/python3

"""
Module qui permet de travailler sur les intéractions avec l'utilisateur,
en utilisant les "Input" et des "Output"
"""


def read_file(filename=""):

    """
    Méthode d'instance qui va afficher à l'écran le contenue d'un fichier
    en utilisant la commande "with"
    """

    with open(filename, "r", encoding="utf-8") as f:
        contenue = f.read()

        print("{}".format(contenue), end="")
