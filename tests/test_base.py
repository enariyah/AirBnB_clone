#!/usr/bin/python3
"""Tests for the BaseModel class"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """Class for BaseModel test cases"""
    def test_init_types(self):
        """Tests the initilisation types of a BaseModel instance"""
        base = BaseModel()
        self.assertEqual(type(base), BaseModel)
        self.assertEqual(type(base.id), str)
        self.assertEqual(type(base.created_at), datetime)
        self.assertEqual(type(base.updated_at), datetime)

    def test_init_kwargs(self):
        """Test the initilisation using kwargs argument"""
        base = BaseModel()
        base_dict = base.to_dict()
        base_copy = BaseModel(**base_dict)
        self.assertEqual(type(base_copy.created_at), datetime)
        self.assertEqual(type(base_copy.updated_at), datetime)
        self.assertEqual(base_dict, base_copy.to_dict())
        self.assertFalse(base_copy is base)

    def test_save(self):
        """Tests the instance method save"""
        base = BaseModel()
        old_time = base.updated_at
        base.name = "My First Model"
        base.save()
        self.assertTrue("name" in base.__dict__)
        self.assertTrue(base.updated_at > old_time)
    
    def test_to_dict(self):
        """Tests the to_dict instance method of BaseModel class"""
        base = BaseModel()
        base.my_number = 89
        base_dict = base.to_dict()
        self.assertEqual(type(base_dict), dict)
        self.assertEqual(type(base_dict['id']), str)
        self.assertEqual(type(base_dict['created_at']), str)
        self.assertEqual(type(base_dict['updated_at']), str)
        self.assertTrue("__class__" in base_dict)
        self.assertTrue("my_number" in base_dict)

    def test_print(self):
        """Tests the __str__ method of the BaseModel class"""
        base = BaseModel()
        expected_output = f"[{type(base).__name__}] ({base.id}) {base.__dict__}"
        self.assertEqual(base.__str__(), expected_output)
