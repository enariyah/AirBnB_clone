#!/usr/bin/python3
"""Tests for the BaseModel class"""
import os
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class TestBase(unittest.TestCase):
    """Class for BaseModel test cases"""
    def test_init_types(self):
        """Tests the initilisation types of a BaseModel instance"""
        base = BaseModel()
        self.assertEqual(type(base), BaseModel)
        self.assertEqual(type(base.id), str)
        self.assertEqual(type(base.created_at), datetime)
        self.assertEqual(type(base.updated_at), datetime)

    def test_ids_not_equal(self):
        """Tests that each object has a unique id"""
        base = BaseModel()
        base_1 = BaseModel()
        self.assertNotEqual(base.id, base_1.id)

    def test_init_no_args(self):
        """Tests that the init method does not use args"""
        self.assertRaises(TypeError, BaseModel("I shouldn't be here", True))

    def test_init_kwargs(self):
        """Test the initilisation using kwargs argument"""
        base = BaseModel()
        base_dict = base.to_dict()
        base_copy = BaseModel(**base_dict)
        self.assertIn('__class__', base_dict)
        self.assertNotIn('__class__', base_copy.__dict__)
        self.assertIsInstance(base_copy.created_at, datetime)
        self.assertIsInstance(base_copy.updated_at, datetime)
        self.assertEqual(base_dict, base_copy.to_dict())
        self.assertFalse(base_copy is base)

    def test_save(self):
        """Tests the instance method save"""
        base = BaseModel()
        old_time = base.updated_at
        base.name = "My First Model"
        base.save()
        self.assertTrue("name" in base.__dict__)
        self.assertNotEqual(base.updated_at, old_time)
        self.assertTrue(base.updated_at > old_time)

    def test_to_dict(self):
        """Tests the to_dict instance method of BaseModel class"""
        base = BaseModel()
        base.my_number = 89
        base_dict = base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict['id'], base.id)
        self.assertIsInstance(base_dict['created_at'], str)
        date = datetime.fromisoformat(base_dict['created_at'])
        self.assertEqual(date, base.created_at)
        self.assertIsInstance(base_dict['updated_at'], str)
        date = datetime.fromisoformat(base_dict['updated_at'])
        self.assertEqual(date, base.updated_at)
        self.assertIn("__class__", base_dict)
        self.assertIn("my_number", base_dict)

    def test_print(self):
        """Tests the __str__ method of the BaseModel class"""
        base = BaseModel()
        expected_output = f"[{type(base).__name__}] ({base.id})"
        expected_output += f" {base.__dict__}"
        self.assertEqual(base.__str__(), expected_output)

    def test_storage_all(self):
        """Tests retrieval of stored objects"""
        self.assertEqual(type(storage.all()), dict)
        self.assertEqual(len(storage.all()) % 7, 0)

    def test_storage_new(self):
        """Tests serialization of a BaseModel instance"""
        prev_size = len(storage.all())
        base = BaseModel()
        key = f"{base.__class__.__name__}.{base.id}"
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], base)
        self.assertEqual(len(storage.all()), prev_size + 1)

    def test_storage_reload_nonexistent(self):
        if os.path.exists("../file.json"):
            os.remove("../file.json")
        self.assertEqual(storage.reload(), None)
