#!/usr/bin/env python3
"""
Module qui permet de construire des class abstraite, d'afficher l'aire
ainsi que le périmètre d'une forme géométrique.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Classe abstraite représentant une forme géométrique."""

    @abstractmethod
    def area(self):
        """Calcule l'aire de la forme géométrique."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calcule le périmètre de la forme géométrique."""
        pass


class Circle(Shape):
    """Classe représentant un cercle."""

    def __init__(self, radius):
        """Initialise un cercle avec son rayon."""
        self.radius = radius

    def area(self):
        """Calcule l'aire du cercle."""
        return math.pi * abs(self.radius ** 2)

    def perimeter(self):
        """Calcule le périmètre (circonférence) du cercle."""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Classe représentant un cercle."""

    def __init__(self, width, height):
        """Calcule l'aire du cercle."""
        self.width = width
        self.height = height

    def area(self):
        """Calcule le périmètre (circonférence) du cercle."""
        return self.width * self.height

    def perimeter(self):
        """Calcule le périmètre du rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Affiche l'aire et le périmètre d'une forme (duck typing)."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
