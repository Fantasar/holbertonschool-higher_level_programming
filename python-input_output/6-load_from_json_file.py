#!/usr/bin/python3

"""
Module qui permet de travailler sur les intéractions avec l'utilisateur,
en utilisant les "Input" et des "Output"
"""

import json


def load_from_json_file(filename):

    """
    Méthode d'instance qui va lire un fichier de type json et le
    retourner à l'utilisateur en type python.
    """

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
