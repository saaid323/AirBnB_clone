#!/usr/bin/python3
"""that serializes instances to a JSON file and
deserializes JSON file to instances"""


import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """serializes instances to a JSON file and deserializes
    JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        data = {}
        for obj in FileStorage.__objects.keys():
            data[obj] = FileStorage.__objects[obj].to_dict()
        try:
            with open(FileStorage.__file_path, mode="r") as f:
                existing_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = {}

        data.update(existing_data)

        with open(FileStorage.__file_path, mode="w+") as f:
            json.dump(data, f, indent=4)

    def reload(self):
        """deserializes the JSON file If the file doesn’t exist, no exception
        should be raised"""
        try:
            if os.path.getsize(FileStorage.__file_path) == 0:
                return
            with open(FileStorage.__file_path, "r") as f:
                objdict = json.load(f)

                for objects in objdict.values():
                    cls_name = objects["__class__"]
                    objects.pop("__class__")
                    self.new(eval(cls_name)(**objects))
        except (FileNotFoundError, json.JSONDecodeError):
            return
