#!/usr/bin/python3

"""
Module qui permet d'utiliser la méthode pickles sur une classe de la sérialiser
et désérialiser.
"""


import pickle


class CustomObject:

    """
    Construction d'une class qui prends en compte les éléments :
        name = string
        age = int
        student = boolean
    """

    def __init__(self, name, age, is_student):

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):

        """
        Méthode d'instance qui permet d'afficher un objet.
        """

        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):

        """
        Méthode d'instance qui permet de sérialiser un fichier en utilisant
        la méthode pickle
        """

        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):

        """
        Méthode d'instance de class qui permet de désérialiser une classe
        """

        with open(filename, "rb") as f:
            conteneur = pickle.load(f)
            return conteneur
