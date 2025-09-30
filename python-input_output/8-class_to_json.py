#!/usr/bin/python3

"""
Module qui permet de travailler sur les intéractions avec l'utilisateur,
en utilisant les "Input" et des "Output"
"""


def class_to_json(obj):

    """
    Méthode qui return une description simple en format Json,
    d'un dictionnaire stocker dans une class.
    """

    return obj.__dict__
