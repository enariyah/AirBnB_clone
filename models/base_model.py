#!/usr/bin/python3
"""This module contains the base class"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """The BaseModel class"""
    def __init__(self, *args, **kwargs) -> None:
        """Initializes a BaseModel instance"""
        if len(kwargs) > 0:
            for key in kwargs:
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.fromisoformat(kwargs[key]))
                else:
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        """Returns a string representation of a BaseModel instance"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self) -> None:
        """Updates the updated_at attribute of an instance"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self) -> dict:
        """Returns a dictionary representation of the instance"""
        ins_dict = {}
        ins_dict['__class__'] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                ins_dict[key] = val.isoformat()
            else:
                ins_dict[key] = val

        return (ins_dict)
