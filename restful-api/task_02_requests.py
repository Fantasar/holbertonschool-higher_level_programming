#!/usr/bin/python3

"""
Modules qui permet de travailler sur les HTTP request des API, ainsi que sur
l'impression à l'écran des information en format CSV ou Jason.
"""


import requests
import csv


def fetch_and_print_posts():

    """
    Méthode d'instance qui imprime à l'écran le code erreur ainsi
    que du texte en format json
    """

    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    if r.status_code == 200:
        posts = r.json()
        print("Status Code:", r.status_code)
        for post in posts:
            print(post["title"])

    else:
        print("Erreur", r.status_code)


def fetch_and_save_posts():

    """
    Méthodes d'instance qui permet d'imprimer un code erreur en cas de
    réussite ou d'échecs.
    Ainsi que la création d'un tableaux en format CSV dans lequels vont
    être stocker les information avec les ID
    """

    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    if r.status_code == 200:
        posts = r.json()
        data = [{"id": p["id"], "title": p["title"], "body": p["body"]}
                for p in posts]

        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)

        print("Fichiers posts.csv créer avec succès")
    else:
        print("Erreur", r.status_code)
