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

    root = ET.Element("root")
    data = ET.SubElement(root, "data")

    ET.SubElement(data, 'name').text = str(dictionary['name'])
    ET.SubElement(data, 'age').text = str(dictionary['age'])
    ET.SubElement(data, 'city').text = str(dictionary['city'])

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

        for data in root.findall("data"):
            name = data.find("name").text if data.find("name")
            is not None else "N/A"
            age = data.find("age").text if data.find("age")
            is not None else "N/A"
            city = data.find("city").text if data.find("city")
            is not None else "N/A"

            return ("name: {}, age: {}, city: {}".format(name, age, city))

    except ET.ParseError as e:
        print(f"Erreur de parsing XML : {e}")
    except Exception as e:
        print(f"Une Erreur est survenue : {e}")
