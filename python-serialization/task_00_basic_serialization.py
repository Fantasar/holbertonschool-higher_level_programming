#!/usr/bin/python3

"""
Module basic_serialization permet de construire et déconstruire un fichier de
format Json.
"""


import json


def serialize_and_save_to_file(data, filename):

    """
    Méthode d'instance serialisation qui permet de un construire
    un objet en mémoire.
    """

    with open(filename, "w", encoding="utf-8") as fichier:
        json.dump(data, fichier)


def load_and_deserialize(filename):

    """
    Méthode d'instance déserialiser un octet de mémoire en
    objet pour une fonctions.
    """

    with open(filename, "r", encoding="utf-8") as fichier:
        conteneur = json.load(fichier)

    print("{}".format(conteneur))
