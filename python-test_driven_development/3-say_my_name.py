#!/usr/bin/python3

"""
Le module de cette fonction permet d'afficher un nom et un prénom,
rentrer par l'utilisateur.

"""


def say_my_name(first_name, last_name=""):
    """
    Args :
        first_name : string qui contient le prénom.
        last_name : string qui contient le nom de famille.

    Raise:
        TypeError :
        Si jamais first_name ou last_name est un int ou un float

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
