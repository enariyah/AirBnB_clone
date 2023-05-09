#!/usr/bin/python3
"""This module contains the base class"""
import uuid
from datetime import datetime


class BaseModel:
    """The BaseModel class"""
    def __init__(self, *args, **kwargs) -> None:
        """Initializes a BaseModel instance"""
        if len(kwargs) > 0:
            for key in kwargs:
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    self.__setattr__(key, datetime.fromisoformat(kwargs[key]))
                else:
                    self.__setattr__(key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self) -> str:
        """Returns a string representation of a BaseModel instance"""
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self) -> None:
        """Updates the updated_at attribute of an instance"""
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """Returns a dictionary representation of the instance"""
        ins_dict = self.__dict__.copy()
        ins_dict["__class__"] = type(self).__name__
        ins_dict["created_at"] = self.created_at.isoformat()
        ins_dict["updated_at"] = self.updated_at.isoformat()

        return (ins_dict)
