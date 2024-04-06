#!/usr/bin/python3

"""Defines a class Square."""


class Square:
    """Represents a square."""
    
    def __init__(self, size=0):
        """
        Initialize square object (size).

        Args:
            size(int) : the size of the square.

        Raises:
            TypeError: if size isn't an int.
            ValueError: if the size value is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
