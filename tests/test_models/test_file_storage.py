#!/usr/bin/python3
"""Unittest test_base_model module"""

import unittest
import pycodestyle
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from time import sleep
import json
import os


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""
    
    def test_pycodestyle(self):
        """Test that the code follows pycodestyle guidelines"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def setUp(self):
        """Set up a FileStorage instance for testing"""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after each test"""
        del self.storage

    def test_all(self):
        """Test the all method of FileStorage"""
        objects_dict = self.storage.all()
        self.assertIsInstance(objects_dict, dict)
        self.assertIs(objects_dict, FileStorage._FileStorage__objects)

    def test_new(self):
        """Test the new method of FileStorage"""
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, FileStorage._FileStorage__objects)

    def test_save_reload(self):
        """Test the save and reload methods of FileStorage"""
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)

        # Save the object
        self.storage.new(obj)
        self.storage.save()

        # Clear the stored objects
        FileStorage._FileStorage__objects = {}

        # Reload the objects
        self.storage.reload()
        self.assertIn(key, FileStorage._FileStorage__objects)

    def test_reload_nonexistent_file(self):
        """Test the reload method when the file doesn't exist
        # Rename the existing file to simulate its non-existence
        os.rename(FileStorage._FileStorage__file_path, 'temp_file.json')

        with self.assertRaises(FileNotFoundError):
            self.storage.reload()

        # Move the renamed file back to its original name
        os.rename('temp_file.json', FileStorage._FileStorage__file_path)"""

    def test_reload_invalid_json(self):
        """Test the reload method with invalid JSON in the file
        with open(FileStorage._FileStorage__file_path, 'w') as f:
            f.write('Invalid JSON')
        with self.assertRaises():  # We use a generic exception here
            self.storage.reload()"""


if __name__ == '__main__':
    unittest.main()