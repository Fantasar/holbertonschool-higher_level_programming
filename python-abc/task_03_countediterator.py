#!/usr/bin/python3

"""
Création d'un modules pour itinérer un compteur en utilisant
la commande spécial __iter__
"""


class CountedIterator:

    """
    Création d'une class qui va itinérer de + 1 conserver la
    valeur dans un compteur
    """

    def __init__(self, iterable):

        """
        Méthode pour construire un itérateur
        """

        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):

        """
        Méthode pour itinérer notre compteurs.
        """

        valeur = next(self.iterator)
        self.count += 1

        return valeur

    def get_count(self):

        """
        Méthode pour retourner le compteur à l'écran
        """

        return self.count
