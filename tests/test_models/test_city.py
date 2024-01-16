#!/usr/bin/python3
"""Unittest user module"""

import unittest
import pycodestyle
from datetime import datetime
from models.base_model import BaseModel
from models.city import City
from time import sleep

class TestCity(unittest.TestCase):
    """Test City class"""

    def setUp(self):
        """Set up for the test"""
        self.city = City()
        self.city.state_id = "123"
        self.city.name = "San Francisco"

    def tearDown(self):
        """Tear down after the test"""
        del self.city

    def test_instance_attributes(self):
        """Test instance attributes"""
        self.assertEqual(self.city.state_id, "123")
        self.assertEqual(self.city.name, "San Francisco")

    def test_to_dict_method(self):
        """Test to_dict method of City class"""
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['state_id'], "123")
        self.assertEqual(city_dict['name'], "San Francisco")
        self.assertTrue('id' in city_dict)
        self.assertTrue('created_at' in city_dict)
        self.assertTrue('updated_at' in city_dict)
        self.assertTrue('__class__' in city_dict)

    def test_save_method(self):
        """Test save method of City class"""
        original_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(original_updated_at, self.city.updated_at)

    def test_str_method(self):
        """Test str method of City class"""
        expected_str = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected_str)

    def test_create_instance_with_dict(self):
        """Test creating an instance with a dictionary"""
        city_dict = {
            'id': '456',
            'created_at': '2024-01-16T20:53:57.830067',
            'updated_at': '2024-01-16T20:53:57.830067',
            '__class__': 'City',
            'state_id': '456',
            'name': 'Los Angeles'
        }
        new_city = City(**city_dict)
        self.assertEqual(new_city.state_id, '456')
        self.assertEqual(new_city.name, 'Los Angeles')
        self.assertEqual(new_city.id, '456')
        self.assertIsInstance(new_city.created_at, datetime)
        self.assertIsInstance(new_city.updated_at, datetime)

if __name__ == '__main__':
    unittest.main()