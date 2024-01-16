#!/usr/bin/python3
"""Unittest test_base_model module"""

import unittest
import pycodestyle
from datetime import datetime
from models.base_model import BaseModel
from time import sleep


class TestBaseModel(unittest.TestCase):
    """Test Basemodel"""

    def setUp(self):
        """Set up a BaseModel instance for testing"""
        self.my_model = BaseModel()

    def tearDown(self):
        """Clean up after each test"""
        del self.my_model

    def test_init(self):
        """Test the __init__ method of BaseModel"""
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))

    def test_str(self):
        """Test the __str__ method of BaseModel"""
        expected_str = "[BaseModel] ({}) {}".format(
            self.my_model.id, self.my_model.__dict__)
        self.assertEqual(str(self.my_model), expected_str)

    def test_save(self):
        """Test the save method of BaseModel"""
        original_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(original_updated_at, self.my_model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel"""
        obj_dict = self.my_model.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'],
                         self.my_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'],
                         self.my_model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
