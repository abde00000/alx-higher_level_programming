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
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Gets the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the instance width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Set the instance height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the instance height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
