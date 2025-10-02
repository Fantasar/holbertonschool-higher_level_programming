#!/usr/bin/python3


"""
Module qui contient renvoie le contenue d'un dictionnaire, la data est stocker
dans une class et on utilise la méthode csv pour renvoyer les informations.
"""

import csv
import json


def convert_csv_to_json(filename):

    """
    Méthode instance pour convertir un fichier de type csv en json
    """

    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
            data = list(csv.DictReader(csvfile))

        with open('data.json', mode='w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)
            return True

    except Exception as e:

        return False
