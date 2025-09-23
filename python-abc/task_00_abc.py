#!/usr/bin/python3

"""
Module qui permet de travailler sur les class
abstraites ainsi que les sous class.
"""

from abc import ABC, abstractmethod


class Animal(ABC):

    """
    Création de la class Animal en tant que class abstraite.
    """

    @abstractmethod
    def sound(self):

        """
        Méthode de type abc pour définir une action.
        """

        pass


class Dog(Animal):

    """
    Dog est une sous class de Animal.
    """

    def sound(self):

        """
        Méthode pour définir une action
        """

        return ("Bark")


class Cat(Animal):

    """
    Cat est une sous class de Animal.
    """

    def sound(self):

        """
        Méthode pour définir une action
        """

        return ("Meow")
