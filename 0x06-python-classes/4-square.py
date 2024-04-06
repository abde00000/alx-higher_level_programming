#!/usr/bin/python3

"""Defines a square class."""


class Square:
    """Represents a square class."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    @property
    def size(self):
        """Returns the size value of the square."""
        return self.__size
    
    @size.setter
    def size(self, value):
        """set the new size value of the sqaure.
        
        Args:
            value (int): the new size value.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
