#!/usr/bin/python3
"""Module for the Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """Representation of the Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.integer_validation("width", value, False)
        self.__width = value

    @property
    def height(self):
        """height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.integer_validation("height", value, False)
        self.__height = value

    @property
    def x(self):
        """x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.integer_validation("x", value)
        self.__x = value

    @property
    def y(self):
        """y of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.integer_validation("y", value)
        self.__y = value

    def integer_validation(self, name, value, eq=True):
        """ validation of all setter methods and instantiation"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if not eq and value <= 0:
            raise ValueError(f"{name} must be > 0")
        if eq and value < 0:
            raise ValueError(f"{name} must be >= 0")
