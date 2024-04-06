#!/usr/bin/python3

"""Defines a class Square."""


class Square:
    """Represents a square.
    Attributes:
        size (int) : the size of the square.
        
    Methods:
        __init__(size=0): initialize the square size , default value is 0.
        area(): Return the area of the square.
    """

    def __init__(self, size=0):
        """
        Initialize square object (size).

        Args:
            size (int) : the size of the square.

        Raises:
            TypeError: if size isn't an int.
            ValueError: if the size value is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
    def area(self):
        """Calculates and returns the area of the square.
        
        Returns:
            int: the area of the square
        """
        return (self.__size ** 2)
