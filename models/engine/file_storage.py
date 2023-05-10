#!/usr/bin/python3
"""
This module contains the class and method that handle
serialization and desrilization of python objects
"""
import json


class FileStorage:
    """Contains methods for serilization and desirilization"""
    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """Returns __objects"""
        return FileStorage.__objects

    def new(self, obj) -> None:
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self) -> None:
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json_dict = {}
            for k, v in FileStorage.__objects.items():
                json_dict[k] = v.to_dict()
            json.dump(json_dict, f)

    def reload(self) -> dict:
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; otherwise, do nothing.
        If the file doesn't exist, no exception should be raised)
        """
        from models.base_model import BaseModel
        from models.user import User
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                json_dict = {}
                for k, v in json.load(f).items():
                    if v['__class__'] == 'BaseModel':
                        json_dict[k] = BaseModel(**v)
                    elif v['__class__'] == 'User':
                        json_dict[k] = User(**v)
                FileStorage.__objects = json_dict
        except FileNotFoundError:
            pass
