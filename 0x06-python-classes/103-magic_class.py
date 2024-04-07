#!/usr/bin/python3

import math


class MagicClass:
    """
    Represents a magical class with radius-based calculations.

    Attributes:
        __radius (float): The radius of the magical object.
    """

    def __init__(self, radius):
        """
        Initializes a MagicClass object with a given radius.

        Args:
            radius (float): The radius of the magical object.
        Raises:
            TypeError: If the radius is not a number.
        """
        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the magical object.

        Returns:
            float: The area of the magical object.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate the circumference of the magical object.

        Returns:
            float: The circumference of the magical object.
        """
        return 2 * math.pi * self.__radius
