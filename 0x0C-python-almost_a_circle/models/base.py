"""Module for the Base Class."""
import json
from pathlib import Path


class Base:
    """represent our Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the object with an optional ID. If no ID is provided, it assigns a unique ID."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries=None):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string."""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            n1 = Rectangle(1, 1)
        elif cls is Square:
            n1 = Square(1)
        else:
            n1 = None
        n1.update(**dictionary)
        return n1

    @classmethod
    def load_from_file(cls):
        filename = f"{cls.__name__}.json"
        file_path = Path(filename)
        if file_path.exists():
            with open(filename, "r", encoding="utf-8") as f:
                new_dict = f.read()
            return [cls.create(**d) for d in cls.from_json_string(new_dict)]
        return []
