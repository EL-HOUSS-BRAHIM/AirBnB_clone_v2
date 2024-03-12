#!/usr/bin/python3
"""Test module for the Review class"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import unittest


class test_review(test_basemodel):
    """Test class for Review"""

    def setUp(self):
        """Set up for test"""
        super().setUp()
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test the place_id attribute of Review"""
        new = self.value(place_id="some_place_id")
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Test the user_id attribute of Review"""
        new = self.value(user_id="some_user_id")
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Test the text attribute of Review"""
        new = self.value(text="some review text")
        self.assertEqual(type(new.text), str)


if __name__ == '__main__':
    unittest.main()
