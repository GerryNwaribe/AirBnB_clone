#!/usr/bin/python3
"""Unittest user module"""

import unittest
import pycodestyle
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review
from time import sleep

class TestReview(unittest.TestCase):
    """Test Review class"""
    
    def test_pycodestyle(self):
        """Test that the code follows pycodestyle guidelines"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
    
    def setUp(self):
        """Set up for the test"""
        self.review = Review()
        self.review.place_id = "123"
        self.review.user_id = "456"
        self.review.text = "Great experience!"

    def tearDown(self):
        """Tear down after the test"""
        del self.review

    def test_instance_attributes(self):
        """Test instance attributes"""
        self.assertEqual(self.review.place_id, "123")
        self.assertEqual(self.review.user_id, "456")
        self.assertEqual(self.review.text, "Great experience!")

    def test_to_dict_method(self):
        """Test to_dict method of Review class"""
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['place_id'], "123")
        self.assertEqual(review_dict['user_id'], "456")
        self.assertEqual(review_dict['text'], "Great experience!")

    def test_save_method(self):
        """Test save method of Review class"""
        original_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(original_updated_at, self.review.updated_at)

    def test_str_method(self):
        """Test str method of Review class"""
        expected_str = "[Review] ({}) {}".format(self.review.id, self.review.__dict__)
        self.assertEqual(str(self.review), expected_str)

    def test_create_instance_with_dict(self):
        """Test creating an instance with a dictionary"""
        review_dict = {
            'id': '789',
            'created_at': '2024-01-16T20:53:57.830067',
            'updated_at': '2024-01-16T20:53:57.830067',
            '__class__': 'Review',
            'place_id': '123',
            'user_id': '456',
            'text': 'Great experience!'
        }
        new_review = Review(**review_dict)
        self.assertEqual(new_review.place_id, '123')
        self.assertEqual(new_review.user_id, '456')
        self.assertEqual(new_review.text, 'Great experience!')

if __name__ == '__main__':
    unittest.main()