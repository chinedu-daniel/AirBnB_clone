#!/usr/bin/python3
"""Class to represent the file storage"""

import json
from models.base_model import BaseModel


class FileStorage:
    """
    File Storage class
    Attributes:
        __file_path: path to the file
        __objects: dictionary of objects
    Methods:
        all(self): returns the dictionary objects
        new(self, obj): sets in __objects the obj
        save(self): save to file by serializing __objects to json
        reload(self): deserializes the JSON to file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Dictionary representation of all objects
        """
        return self.__objects

    def new(self, obj):
        """
        write a new object
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes an object to a JSON file
        """
        with open(self.__file_path, '+w') as f:
            obj_dict = {key: obj.to_dict()
                        for key, obj in self.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as f:
                dict_ = json.load(f)
                for value in dict_.values():
                    class_name = value['__class__']
                    self.new(eval(class_name)(**value))

        except FileNotFoundError:
            pass
