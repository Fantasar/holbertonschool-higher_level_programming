#!/usr/bin/python3

"""
Module pour construire une classe ansi que sa fille
"""


class MyList(list):

    """
    Construction de la class MyList
    """

    def print_sorted(self):

        """
        Méthodes d'instance qui imprime une listes triés
        """

        print(sorted(self))
