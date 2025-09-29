#!/usr/bin/python3
import json

"""
Module qui permet de travailler sur les intéractions avec l'utilisateur,
en utilisant les "Input" et des "Output"
"""


def from_json_string(my_str):

    """
    Méthode d'instance qui retourne un objet représenter en json string.
    """

    return json.loads(my_str)
