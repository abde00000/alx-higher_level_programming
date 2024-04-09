#!/usr/bin/python3

"""writing an empty class."""


class Rectangle:
    """Represents the Rectangle  class."""
    def __init__(self, width=0, height=0):
        """Initialize the rectangle class.

        Args:
            width: the width of the rectangle.
            height: the height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width."""
        return self.__width

    @property
    def height(self):
        """Set the instance height."""
        return self.__height

    @width.setter
    def width(self, value):
        """Set the instance width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """Set the instance height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Calculates and Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and Return the area of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """return a string that prints the rectangle."""
        rec_str = ""
        if self.__width == 0 or self.__height == 0:
            return rec_str
        for row in range(self.__height):
            rec_str += "#" * self.__width + "\n"
        return rec_str
