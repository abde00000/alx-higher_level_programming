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
        self.integer_validation("size", self.width)
        self.width = value
        self.height = value