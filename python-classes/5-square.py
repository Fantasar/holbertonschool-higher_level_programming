#!/usr/bin/python3
"""
Is modules for print géométrique cube.
"""


class Square:
    """
    Square is class for cube.
    """
    def __init__(self, size=0):
        """
        Is function for controls size of square.
        """
        self.size = size

    @property
    def size(self):
        """
        This methode return Square
        """
        return _self.size

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

        self._size = value

    def area(self):
        """
        Method instance for calculs area a square
        """
        return self.size * self.size

    def my_print(self):
        """
        Method instance for print square.

        Args :
        idx & pos : int for loops
        """
        idx = 0
        pos = 0

        if self._size == 0:
            print("")

        for idx in range(self._size):
            for pos in range(self._size):
                print("{}".format('#'), end="")
            print("")
