#!/usr/bin/python3
"""
Create a square Class and define it with the attribute size.

Attributes:
    __size: the size of the square
Methodes:
    __init__(size): Initialize size attribute with the value size.
"""
class square:
    """
        represents a new square object.

        Args:
            size: the size of the square
    """
    def __init__(self, size):
        """
        Initialize the square object size.
        Args:
        size: the size of the square
        """
        self.__size = size
