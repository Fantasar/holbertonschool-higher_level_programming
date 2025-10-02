#!/usr/bin/python3

"""
Module qui convertie un fichier XML en Json.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):

    """
    Méthode d'instance qui sérialise un fichier xml.
    Les élèments stocker sont :
    Le nom.
    L'age.
    La ville.
    """

    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):

    """
    Méthode d'instance qui permet de déserialiser un fichier xml vers du
    Json.

    Les cas erreurs possible :
    - Une erreur de transformation sur le XML.
    - Une autres erreurs gérer par Exception.
    """

    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text

        return result

    except ET.ParseError as e:
        print(f"Erreur de parsing XML : {e}")
    except Exception as e:
        print(f"Une Erreur est survenue : {e}")
