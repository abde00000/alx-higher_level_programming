#!/usr/bin/python3

"""
defines a square class

Attributes:
    __size (int): the size of the square.

Methods:
    __init__(size): initialize a square size.
 """
class Square:

    def __init__(self, size=0):
        """
        initializes the size object.

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
