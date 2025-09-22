#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Méthode qui va vérifier si l'objet fait partie d'une instance de classe.
    Renvoie vraie ou faux.
    """
    return type(obj) is a_class
