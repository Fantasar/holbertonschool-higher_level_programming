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

        Args:
        size: is int of longs square

        Raise:
        TypeError: is not type int for size.
        ValueError: size is > 0.
        """

        self.size = size

    @property
    def size(self):
        """
        This methode return Square
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        This instance methode assigned and controls value of size.
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
        return self.size ** 2
