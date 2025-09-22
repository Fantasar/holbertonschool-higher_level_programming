#!/usr/bin/python3

def is_same_class(obj, a_class):

    """
    Méthode qui va vérifier si le type de l'objet rentrer en instance.
    Renvoie vraie ou faux.
    """
    return type(obj) is a_class
