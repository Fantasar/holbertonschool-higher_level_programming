#!/usr/bin/python3

"""
Module pour construire une class poisson-volant, le principe va être de
travailler sur l'héritage de deux class l'oiseau et le poisson.
"""


class Fish:

    """
    Création de la class Fish avec les attribut de pourvoir nager,
    ainsi que son habitat naturelle
    """

    def swim(self):

        """
        Méthode pour pouvoir nager
        """

        print("The fish is swimming")

    def habitat(self):

        """
        Méthode pour définir son habitât
        """

        print("The fish lives in water")


class Bird:

    """
    Création de la class Bird avec les méthodes de pouvoir voler,
    ainsi que son habitat naturelle
    """

    def fly(self):

        """
        Méthode pour pouvoir voler
        """

        print("The bird is flying")

    def habitat(self):

        """
        Methode pour définir son habitat naturelle.
        """

        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):

    """
    Création de la sous class Poisson-volant : c'est le mélange
    de Fish et Bird.
    """

    def fly(self):

        """
        Méthode pour définir le vol du poisson-volant
        """

        print("The flying fish is soaring!")

    def swim(self):

        """
        Méthode pour définir la nage du poisson-volant
        """

        print("The flying fish is swimming!")

    def habitat(self):

        """
        Méthode pour définir l'habitat du poisson-volant
        """

        print("The flying fish lives both in water and the sky!")
