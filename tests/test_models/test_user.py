#!/usr/bin/python3
"""Unittest user module"""

import unittest
import pycodestyle
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from time import sleep


class TestUser(unittest.TestCase):
    """Test User

    Args:
        unittest (_type_): _description_
    """
    def test_user_inheritance(self):
        """Test if User inherits from BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_user_attributes(self):
        """Test User attributes"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertTrue(hasattr(user, 'first_name'))

    def test_user_attribute_types(self):
        """Test User attribute types"""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.last_name, str)
        self.assertIsInstance(user.first_name, str)

    def test_user_string_representation(self):
        """Test the __str__ method of User"""
        user = User()
        string_repr = str(user)
        self.assertIn("[User]", string_repr)
        self.assertIn("'id':", string_repr)
        self.assertIn("'created_at':", string_repr)
        self.assertIn("'updated_at':", string_repr)

    def test_user_to_dict_method(self):
        """Test the to_dict method of User
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn('__class__', user_dict)
        self.assertIn('email', user_dict)
        self.assertIn('password', user_dict)
        self.assertIn('last_name', user_dict)
        self.assertIn('first_name', user_dict)"""

    def test_user_created_at_updated_at(self):
        """Test if User has attributes created_at and updated_at"""
        user = User()
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)

    def test_user_save_method(self):
        """Test the save method of User"""
        user = User()
        old_updated_at = user.updated_at
        sleep(1)  # Ensure there is a time difference when saving
        user.save()
        self.assertNotEqual(old_updated_at, user.updated_at)


if __name__ == '__main__':
    unittest.main()
