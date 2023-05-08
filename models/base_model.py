#!/usr/bin/env python3
"""This module contains the base class"""
import uuid
from datetime import datetime


class BaseModel:
    """The BaseModel class"""
    def __init__(self) -> None:
        """Initializes a BaseModel instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """Returns a string representation of a BaseModel instance"""
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self) -> None:
        """Updates the updated_at attribute of an instance"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the instance"""
        ins_dict = self.__dict__
        ins_dict["__class__"] = type(self).__name__
        ins_dict["created_at"] = self.created_at.isoformat()
        ins_dict["updated_at"] = self.updated_at.isoformat()
