#!/usr/bin/python3
"""Tests for serialization and deserialization methods"""
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests for serialization and deserialization"""
    def test_type(self):
        test_storage = FileStorage()
        self.assertIsInstance(test_storage, FileStorage)
        self.assertEqual(test_storage._FileStorage__file_path, "file.json")
        # self.assertEqual(test_storage.all(), {})
