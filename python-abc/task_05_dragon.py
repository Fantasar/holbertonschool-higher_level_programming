#!/usr/bin/python3

"""
Module qui permet d'animer une intéraction avec un dragon
"""


class SwimMixin:

    """
    Création d'une Mixin de class avec la méthode pour nager.
    """

    def swim(self):

        """
        Méthodes pour pouvoir faire l'action de nager
        """

        print("The creature swims!")


class FlyMixin:

    """
    Création d'une Mixin de class avec la méthode pour
    pouvoir voler.
    """

    def fly(self):

        """
        Méthodes pour pouvoir faire l'action voler.
        """

        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):

    """
    Création de la class dragon qui est enfant de
    SwimMixin et Flymixin
    """

    def roar(self):

        """
        Méthode pour pouvoir réaliser l'action de crier
        """

        print("The dragon roars!")
