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


class Rectangle(BaseGeometry):

    """
    Création d'une classe fille de BaseGeometry.
    """

    def __init__(self, width, height):

        """
        Initialisation d'une méthode qui prends en paramètre
        la largeur et la hauteur.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
    
    def area(self):

        """
        Méthode d'instance pour calculer l'air du Rectangle.
        """

        return str(self.__width * self.__height)
    
    def __str__(self):
        
        """
        Retourne une string représentant Réctangle
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
