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

    def area(self):
        """Calculate the Rectangle area."""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - "\
            f"{self.width}/{self.height}"

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """assigns an argument to each attribute"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """updating the public method def update(self, *args):
        by changing the prototype to update(self, *args, **kwargs)
        that assigns a key/value argument to attributes"""
        if args:
            self.__update(*args)
        if kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        to_dic = {'id': self.id,
                   'width': self.width,
                   'height': self.height,
                   'x': self.x,
                   'y': self.y
                   }
        return to_dic