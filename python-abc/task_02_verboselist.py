#!/usr/bin/python3

"""
Module qui permet de construire des class list qui affiche
les notifications.
"""


class VerboseList(list):

    """
    Création de la class VerboseList pour gérer les opérations
    de la list
    """

    def append(self, list):

        """
        Création de la méthode, qui ajoute un élément à une liste
        """

        super().append(list)
        print("Added [{}] to the list.".format(list))

    def extend(self, list):

        """
        Création de la méthode, qui ajoute étend d'un
        nombres définis élément à une liste
        """

        super().extend(list)
        print("Extended the list with [{}] items.".format(len(list)))

    def remove(self, list):

        """
        Création de la méthode, qui suprime un élément à une liste
        """

        super().remove(list)
        print("Removed [{}] from the list.".format(list))

    def pop(self, index=-1):

        """
        Création de la méthode, qui fait popper un élément à une liste
        """

        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
