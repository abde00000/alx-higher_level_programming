#!/usr/bin/python3
"""Module for Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Representing the Square Class."""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - "\
            f"{self.width}"

    @property
    def size(self):
        """size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.integer_validation("size", value)
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """updates the attributes of the class square."""
        if id is not None:
            self.id = id
        if size is not None:
            self.width = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """assigns attributes."""
        if args:
            self.__update(*args)
        if kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        to_dic = {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
        return to_dic
