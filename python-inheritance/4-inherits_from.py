#!/usr/bin/python3

"""
Le modules permet de s'entrainer sur la création de class et de ces filles.
"""


def inherits_from(obj, a_class):

    """
    Méthodes qui permet de renvoyer vraie ou faux dans le cas si l'objet
    est un héritier direct ou non d'une class
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
