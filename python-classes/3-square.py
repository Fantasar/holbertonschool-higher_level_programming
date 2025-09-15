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

        self._Square__size = size

        if not isinstance(self._Square__size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Method instance for calculs area a square
        """
        return self._Square__size ** 2
