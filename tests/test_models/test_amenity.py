#!/usr/bin/python3
"""Unittest user module"""

import unittest
import pycodestyle
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
from time import sleep


class TestAmenity(unittest.TestCase):
    """Test Amenity class"""

    def test_pycodestyle(self):
        """Test that the code follows pycodestyle guidelines"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def setUp(self):
        """Set up for the test"""
        self.amenity = Amenity()
        self.amenity.name = "California"

    def tearDown(self):
        """Tear down after the test"""
        del self.amenity

    def test_instance_attributes(self):
        """Test instance attributes"""
        self.assertEqual(self.amenity.name, "California")

    def test_to_dict_method(self):
        """Test to_dict method of amenity class"""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['name'], "California")
        self.assertTrue('id' in amenity_dict)
        self.assertTrue('created_at' in amenity_dict)
        self.assertTrue('updated_at' in amenity_dict)
        self.assertTrue('__class__' in amenity_dict)

    def test_save_method(self):
        """Test save method of amenity class"""
        original_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(original_updated_at, self.amenity.updated_at)

    def test_str_method(self):
        """Test str method of amenity class"""
        expected_str = "[Amenity] ({}) {}".format(
            self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)

    def test_create_instance_with_dict(self):
        """Test creating an instance with a dictionary"""
        amenity_dict = {
            'id': '123',
            'created_at': '2024-01-16T20:53:57.830067',
            'updated_at': '2024-01-16T20:53:57.830067',
            '__class__': 'amenity',
            'name': 'New York'
        }
        new_amenity = Amenity(**amenity_dict)
        self.assertEqual(new_amenity.name, 'New York')
        self.assertEqual(new_amenity.id, '123')
        self.assertIsInstance(new_amenity.created_at, datetime)
        self.assertIsInstance(new_amenity.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
