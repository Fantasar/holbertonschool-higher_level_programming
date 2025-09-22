#!/usr/bin/python3

"""
Module pour contrôler une forme de géométrie de base
"""


class BaseGeometry:

    """
    Création de la class BaseGeometry
    """

    def area(self):

        """
        Méthode pour contrôler l'air d'une forme géométrique;

        Raise:
        Exception lorsequ'il n'est pas possible de le calculer
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """
        Methode pour intégrer une valeur.

        Raise:
        TypeError : La valeur n'est pas un entier.
        ValueError : La valeur est inférieur à 0.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
