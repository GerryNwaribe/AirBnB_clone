#!/usr/bin/python3
"""Unittest user module"""

import unittest
import pycodestyle
from datetime import datetime
from models.base_model import BaseModel
from models.state import State
from time import sleep


class TestState(unittest.TestCase):
    """Test State class"""

    def setUp(self):
        """Set up for the test"""
        self.state = State()
        self.state.name = "California"

    def tearDown(self):
        """Tear down after the test"""
        del self.state

    def test_instance_attributes(self):
        """Test instance attributes"""
        self.assertEqual(self.state.name, "California")

    def test_to_dict_method(self):
        """Test to_dict method of State class"""
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['name'], "California")
        self.assertTrue('id' in state_dict)
        self.assertTrue('created_at' in state_dict)
        self.assertTrue('updated_at' in state_dict)
        self.assertTrue('__class__' in state_dict)

    def test_save_method(self):
        """Test save method of State class"""
        original_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(original_updated_at, self.state.updated_at)

    def test_str_method(self):
        """Test str method of State class"""
        expected_str = "[State] ({}) {}".format(
            self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), expected_str)

    def test_create_instance_with_dict(self):
        """Test creating an instance with a dictionary"""
        state_dict = {
            'id': '123',
            'created_at': '2024-01-16T20:53:57.830067',
            'updated_at': '2024-01-16T20:53:57.830067',
            '__class__': 'State',
            'name': 'New York'
        }
        new_state = State(**state_dict)
        self.assertEqual(new_state.name, 'New York')
        self.assertEqual(new_state.id, '123')
        self.assertIsInstance(new_state.created_at, datetime)
        self.assertIsInstance(new_state.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
