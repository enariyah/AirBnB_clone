#!/usr/bin/python3
"""Tests for serialization and deserialization methods"""
import json
import os
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Tests for serialization and deserialization"""
    def test_type(self):
        test_storage = FileStorage()
        self.assertIsInstance(test_storage, FileStorage)
        self.assertEqual(test_storage._FileStorage__file_path, "file.json")
        # self.assertEqual(test_storage._FileStorage__objects, {})

    def test_storage_all(self):
        """Tests retrieval of stored objects"""
        self.assertIsInstance(storage.all(), dict)
        self.assertIs(storage.all(), storage._FileStorage__objects)

    def test_storage_new(self):
        """Tests serialization of instances"""
        prev_size = len(storage.all())
        obj = BaseModel()
        storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key], obj)
        self.assertEqual(len(storage.all()), prev_size + 1)

    def test_storage_save(self):
        """Tests that json serialization is correctly stored in file"""
        obj = BaseModel()
        key = f"{obj.__class__.__name__}.{obj.id}"
        storage.save()
        with open("file.json", "r", encoding="utf-8") as f:
            json_dict = json.load(f)
        self.assertIn(key, json_dict)
        self.assertEqual(json_dict[key], obj.to_dict())
        objects_dict = {}
        for key, val in storage._FileStorage__objects.items():
            objects_dict[key] = val.to_dict()
        self.assertEqual(json_dict, objects_dict)
    
    def test_storage_reload_exists(self):
        """Tests that deserialization happens correctly"""
        if os.path.exists("../file.json"):
            storage.reload()
        else:
            base = BaseModel()
            base.save()
            storage.reload()
        with open("file.json", "r", encoding="utf-8") as f:
            json_dict = json.load(f)
        for key, val in json_dict.items():
            self.assertIn(key, storage._FileStorage__objects)
            self.assertEqual(val, storage._FileStorage__objects[key].to_dict())

    def test_storage_reload_nonexistent(self):
        if os.path.exists("../file.json"):
            os.remove("../file.json")
        self.assertEqual(storage.reload(), None)
