#!/usr/bin/python3
"""Unittest user module"""

import unittest
import pycodestyle
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place
from time import sleep

class TestPlace(unittest.TestCase):
    """Test Place class"""
    
    def setUp(self):
        """Set up for the test"""
        self.place = Place()
        self.place.city_id = "123"
        self.place.user_id = "456"
        self.place.name = "Cozy Cabin"
        self.place.description = "A beautiful cabin in the woods"
        self.place.number_rooms = 2
        self.place.number_bathrooms = 1
        self.place.max_guest = 4
        self.place.price_by_night = 100
        self.place.latitude = 42.123
        self.place.longitude = -71.456
        self.place.amenity_ids = ["789", "012"]

    def tearDown(self):
        """Tear down after the test"""
        del self.place

    def test_instance_attributes(self):
        """Test instance attributes"""
        self.assertEqual(self.place.city_id, "123")
        self.assertEqual(self.place.user_id, "456")
        self.assertEqual(self.place.name, "Cozy Cabin")
        self.assertEqual(self.place.description, "A beautiful cabin in the woods")
        self.assertEqual(self.place.number_rooms, 2)
        self.assertEqual(self.place.number_bathrooms, 1)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 42.123)
        self.assertEqual(self.place.longitude, -71.456)
        self.assertEqual(self.place.amenity_ids, ["789", "012"])

    def test_to_dict_method(self):
        """Test to_dict method of Place class"""
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict['city_id'], "123")
        self.assertEqual(place_dict['user_id'], "456")
        self.assertEqual(place_dict['name'], "Cozy Cabin")
        self.assertEqual(place_dict['description'], "A beautiful cabin in the woods")
        self.assertEqual(place_dict['number_rooms'], 2)
        self.assertEqual(place_dict['number_bathrooms'], 1)
        self.assertEqual(place_dict['max_guest'], 4)
        self.assertEqual(place_dict['price_by_night'], 100)
        self.assertEqual(place_dict['latitude'], 42.123)
        self.assertEqual(place_dict['longitude'], -71.456)
        self.assertEqual(place_dict['amenity_ids'], ["789", "012"])

    def test_save_method(self):
        """Test save method of Place class"""
        original_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(original_updated_at, self.place.updated_at)

    def test_str_method(self):
        """Test str method of Place class"""
        expected_str = "[Place] ({}) {}".format(self.place.id, self.place.__dict__)
        self.assertEqual(str(self.place), expected_str)

    def test_create_instance_with_dict(self):
        """Test creating an instance with a dictionary"""
        place_dict = {
            'id': '789',
            'created_at': '2024-01-16T20:53:57.830067',
            'updated_at': '2024-01-16T20:53:57.830067',
            '__class__': 'Place',
            'city_id': '123',
            'user_id': '456',
            'name': 'Cozy Cabin',
            'description': 'A beautiful cabin in the woods',
            'number_rooms': 2,
            'number_bathrooms': 1,
            'max_guest': 4,
            'price_by_night': 100,
            'latitude': 42.123,
            'longitude': -71.456,
            'amenity_ids': ["789", "012"]
        }
        new_place = Place(**place_dict)
        self.assertEqual(new_place.city_id, '123')
        self.assertEqual(new_place.user_id, '456')
        self.assertEqual(new_place.name, 'Cozy Cabin')
        self.assertEqual(new_place.description, 'A beautiful cabin in the woods')
        self.assertEqual(new_place.number_rooms, 2)
        self.assertEqual(new_place.number_bathrooms, 1)
        self.assertEqual(new_place.max_guest, 4)
        self.assertEqual(new_place.price_by_night, 100)
        self.assertEqual(new_place.latitude, 42.123)
        self.assertEqual(new_place.longitude, -71.456)
        self.assertEqual(new_place.amenity_ids, ["789", "012"])

if __name__ == '__main__':
    unittest.main()