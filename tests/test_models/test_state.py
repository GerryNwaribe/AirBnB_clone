#!/usr/bin/python3
"""Unittest user module"""

import unittest
import pycodestyle
from datetime import datetime
from models.base_model import BaseModel
from models.state import State
from time import sleep


class TestUser(unittest.TestCase):
    """Test User

    Args:
        unittest (_type_): _description_
    """