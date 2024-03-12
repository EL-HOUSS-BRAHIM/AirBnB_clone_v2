#!/usr/bin/python3
"""Test module for the Amenity class"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import unittest


class test_Amenity(test_basemodel):
    """Test class for Amenity"""

    def setUp(self):
        """Set up for test"""
        super().setUp()
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test the name attribute of Amenity"""
        new = self.value(name="name")
        self.assertEqual(type(new.name), str)


if __name__ == '__main__':
    unittest.main()
