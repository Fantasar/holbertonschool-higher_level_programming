#!/usr/bin/env python3
"""
Module qui permet de construire des class abstraite, d'afficher l'aire
ainsi que le périmètre d'une forme géométrique.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):

    """
    Création d'une class abstraite Shape,avec la méthode abc
    """

    @abstractmethod
    def area(self):
        """
        Définition d'une méthode pour l'air d'une forme géométrique.
        """
        pass

    @abstractmethod
    def perimeter(self):

        """
        Définition d'une méthode pour le périmètre d'une forme géométrique
        """
        pass


class Circle(Shape):
    """
    Création d'une sous class de Shape, nommer Circle.
    """

    def __init__(self, radius):
        """
        Construction d'une méthode qui prends en paramètre le rayon.
        """
        self.radius = radius

    def area(self):
        """
        Création de la méthode pour caluler l'air
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Création de la méthode pour calculer le périmètre.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Création d'une sous class de Shape, nommer Rectangle.
    """

    def __init__(self, width, height):
        """
        Construction d'une méthode qui prends la hauteur et la largeur.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Methode pour calculer l'air d'un rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Methode pour calculer le périmètre d'un rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):

    """
    Affiche l'aire et le périmètre d'une forme
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
