#!/usr/bin/python3
"""
La fonction permet de découper un texte au totem de ponctuation.

"""


def text_indentation(text):

    """
    Args:
    La variable text contient le texte à découper 

    Raise:
    TypeError : Si jamais la variable n'est pas une string.

    """
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    idx = 0

    while idx < len(text):
        print("{}".format(text[idx]), end="")

        if text[idx] in ".:?":
            print("\n")
            idx += 1
            while idx < len(text) and text[idx] == " ":
                idx += 1
            continue
        idx += 1
