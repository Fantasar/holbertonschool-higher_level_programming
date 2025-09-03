#!/usr/bin/python3
def uppercase(str):
    resultat = ""
    for count in str:
        val = ord(count)
        if 'a' <= count <= 'z':
            valeur = val - 32
            resultat += chr(valeur)
        else:
            resultat += count
    print("{}".format(resultat))
