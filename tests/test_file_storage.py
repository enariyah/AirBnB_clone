#!/usr/bin/python3
"""Tests for serialization and deserialization methods"""
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests for serialization and deserialization"""
    def test_type(self):
        test_storage = FileStorage()
        self.assertEqual(type(test_storage), FileStorage)
