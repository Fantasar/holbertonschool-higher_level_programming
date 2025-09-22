#!/usr/bin/python3

"""
Le modules permet de s'entrainer sur la création de class et de ces filles.
"""


def is_same_class(obj, a_class):

    """
    Méthode qui va vérifier si le type de l'objet rentrer en instance.
    Renvoie vraie ou faux.
    """
    return type(obj) is a_class
