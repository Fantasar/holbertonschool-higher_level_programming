#!/usr/bin/python3
import json


"""
Module qui permet de travailler sur les intéractions avec l'utilisateur,
en utilisant les "Input" et des "Output"
"""


def to_json_string(my_obj):

    """
    Méthode d'instance pour utiliser la représentation d'un objet
    dans le format JSON.
    """

    return json.dumps(my_obj)
