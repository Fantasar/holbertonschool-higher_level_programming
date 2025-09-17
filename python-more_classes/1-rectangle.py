#!/usr/bin/python3
"""
Write and define a Rectangle.
"""


class Rectangle:
    """
    Represent class Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        methods for attribut width and height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Method for return width rectangle
        """
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """
        Methods for controls and attribute width values

        Raise:
        TypeError : Is not int values
        ValueError : Is < at 0

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Methods for return height rectangle
        """
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """
        Methods for controls and attribut values of height rectangle

        Raise:
        TypeError : Is not int values
        ValueError : Is < at 0

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
