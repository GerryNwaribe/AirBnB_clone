#!/usr/bin/python3
"""Unittest test_base_model module"""

import unittest
import pycodestyle
from datetime import datetime
from models.base_model import BaseModel
from time import sleep


class TestBaseModel(unittest.TestCase):
    """Test Case"""

    """def test_pycodestyle(self):
        _s = pycodestyle.StyleGuide(quiet=True)
        _r = _s.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
        "Found code style errors (and warnings).")

    def test_doc(self):
        import models.base_model
        self.assertIsNotNone(models.base_model.__doc__)

    def test_doc(self):
        self.assertIsNotNone(BaseModel.__doc__)

    def test_doc(self):
        self.assertIsNotNone(BaseModel.__init__.__doc__)"""

    def test_doc(self):
        self.assertIsNotNone(BaseModel.__str__.__doc__)

    def test_doc(self):
        self.assertIsNotNone(BaseModel.save.__doc__)

    def test_doc(self):
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_string(self):
        """Test Case"""
        gerry = BaseModel()
        expected_output = f"[BaseModel] ({gerry.id}) {gerry.__dict__}"
        self.assertEqual(str(gerry), expected_output)

    def test_initializer(self):
        """Test Case"""
        gerry = BaseModel()
        self.assertIsInstance(gerry, BaseModel)
        self.assertIsInstance(gerry.id, str)
        self.assertIsInstance(gerry.created_at, datetime)
        self.assertIsInstance(gerry.updated_at, datetime)

    def test_todict(self):
        """Self explain"""
        gerry = BaseModel()
        self.assertIn("id", gerry.to_dict())
        self.assertIn("created_at", gerry.to_dict())
        self.assertIn("updated_at", gerry.to_dict())
        self.assertIn("__class__", gerry.to_dict())

    def test_todict_values(self):
        """Self explain"""
        gerry = BaseModel()
        self.assertEqual(gerry.to_dict()["id"], gerry.id)

    def test_updating_time(self):
        """Test Case"""
        gerry = BaseModel()
        old_time = gerry.updated_at
        sleep(0.1)
        gerry.save()
        new_time = gerry.updated_at
        self.assertNotEqual(old_time, new_time)
