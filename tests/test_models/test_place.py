#!/usr/bin/python3
"""
Test suits for amenities
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Tests for place
    """

    def setUp(self):
        """
        Set up for the tests
        """
        self.place = Place()
        self.place.name = "California"

    def tearDown(self):
        """
        Clean up after each test
        """
        del self.place

    def test_name_attribute_exists(self):
        """
        Test if the name attribute is present in the place instance
        """
        self.assertTrue(hasattr(self.place, 'name'),
                        "place instance lacks a 'name' attribute")

    def test_name_assignment(self):
        """
        Test assignment of the name attribute
        """
        self.assertEqual(self.place.name, "California",
                         "place.name has incorrect value.")

    def test_name_type(self):
        """
        Test the type of the name attribute
        """
        self.assertIsInstance(self.place.name, str,
                              "place.name is not of type 'str'.")

    def test_new_name_assignment(self):
        """
        Test updating the name attribute
        """
        self.place.name = "Nevada"
        self.assertEqual(self.place.name, "Nevada",
                         "place.name did not update correctly.")


if __name__ == '__main__':
    unittest.main()
