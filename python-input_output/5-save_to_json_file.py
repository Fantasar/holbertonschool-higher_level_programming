#!/usr/bin/python3

"""
Module qui permet de travailler sur les intéractions avec l'utilisateur,
en utilisant les "Input" et des "Output"
"""

import json


def save_to_json_file(my_obj, filename):

    """
    Méthode d'instance pour écrire dans un fichier texte,
    un objet en utilisant commande JSON
    """

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
