#!/usr/bin/python3
"""
Is modules for print géométrique cube.
"""


class Square:
    """
    Square is class for cube.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Is function for controls size of square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        This methode return Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This instance methode assigned and controls value of size.

        Raise:
        TypeError: Is not int.
        ValueError: value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Methode position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        method position controls:
        Raise:
        TypeError : Is not int in tuples
        ValueError : If values is < 0
        """

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2 or not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Method instance for calculs area a square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Method instance for print square.

        Args :
        idx & pos : int for loops
        """
        if self.__size == 0:
            print("")
            return

        for vide in range(self.__position[1]):
            print("")
        for longeur in range(self.__size):
            for espace in range(self.__position[0]):
                print(" ", end="")
            for colonne in range(self.__size):
                print("{}".format('#'), end="")
            print("")
