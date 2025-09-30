#!/usr/bin/python3

"""
Module qui permet de travailler sur les intéractions avec l'utilisateur,
en utilisant les "Input" et des "Output"
"""


class Student:
    """
    Création d'une class Student qui contient:
     - Le nom de l'élève.
     - Le prénom de l'élève.
     - L'âge de l'élève.

    """

    def __init__(self, first_name, last_name, age):

        """
        Création d'une méthode de construction pour contenir
        les information de l'élève
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):

        """
        Création de la méthode json pour afficher les information
        de l'élève comme un dictionnaire.
        """

        return self.__dict__
