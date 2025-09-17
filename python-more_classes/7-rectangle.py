#!/usr/bin/python3
"""
Write and define a Rectangle.
"""


class Rectangle:
    """
    Represent class Rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        methods for attribut width and height.
        """
        Rectangle.number_of_instances += 1
        self._Rectangle__width = width
        self._Rectangle__height = height

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
        if not isinstance(self._Rectangle__width, int):
            raise TypeError("width must be an integer")
        if self._Rectangle__width < 0:
            raise ValueError("width must be >= 0")

        self._Rectangle__width = value

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
        if not isinstance(self._Rectangle__height, int):
            raise TypeError("height must be an integer")
        if self._Rectangle__height < 0:
            raise ValueError("height must be >= 0")

        self._Rectangle__height = value

    def area(self):
        """
        Methode instance for calculs area
        """
        return self._Rectangle__height * self._Rectangle__width

    def perimeter(self):
        """
        Methode instance for calculs perimeter
        """
        if self._Rectangle__height == 0 or self._Rectangle__width == 0:
            return 0
        return 2 * (self._Rectangle__height + self._Rectangle__width)

    def __str__(self):
        """
        Methode for print a rectangle with str
        """
        if self.height == 0 or self.width == 0:
            return ""

        chaine = ""
        for idx in range(self.height):
            chaine += str(self.print_symbol) * self.width
            if idx != self.height - 1:
                chaine += "\n"
        return chaine

    def __repr__(self):
        """
        Methode for print object
        """
        return ("Rectangle({}, {})".format
                (self._Rectangle__width, self._Rectangle__height))

    def __del__(self):
        """
        Methode for delete instance rectangle
        """
        if not Rectangle.number_of_instances <= 0:
            Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
