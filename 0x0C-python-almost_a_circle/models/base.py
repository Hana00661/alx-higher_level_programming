#!/usr/bin/python3
"""the Base class"""

import json
import os


class Base:
    """the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """function to create an instance of Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """function to returns the JSON string to list_dictionaries"""
        return "[]" if list_dictionaries is None \
            else json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """function to writes the JSON string of list_objs to a file"""

        filename = f"{cls.__name__}.json"
        with open(filename, 'w', encoding='utf-8') as file:
            if list_objs is None:
                return file.write(cls.to_json_string(None))
            liste = [i.to_dictionary() for i in list_objs]
            make_string = cls.to_json_string(liste)
            return file.write(make_string)

    @staticmethod
    def from_json_string(json_string):
        """function to returns the list of the JSON string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """function to return an instance with all attributes"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """function """
        filename = f"{cls.__name__}.json"
        if os.path.exists(filename) is False:
            return []
        with open(filename, "r") as file:
            liste = cls.from_json_string(file.read())
            for i in range(len(liste)):
                liste[i] = cls.create(**liste[i])
        return liste
