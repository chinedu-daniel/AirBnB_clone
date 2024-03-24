#!/usr/bin/python3
"""
Test suits for city
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Tests for city
    """

    def setUp(self):
        """
        Set up for the tests
        """
        self.city = City()
        self.city.name = "California"

    def tearDown(self):
        """
        Clean up after each test
        """
        del self.city

    def test_name_attribute_exists(self):
        """
        Test if the name attribute is present in the city instance
        """
        self.assertTrue(hasattr(self.city, 'name'),
                        "city instance lacks a 'name' attribute")

    def test_name_assignment(self):
        """
        Test assignment of the name attribute
        """
        self.assertEqual(self.city.name, "California",
                         "city.name has incorrect value.")

    def test_name_type(self):
        """
        Test the type of the name attribute
        """
        self.assertIsInstance(self.city.name, str,
                              "city.name is not of type 'str'.")

    def test_new_name_assignment(self):
        """
        Test updating the name attribute
        """
        self.city.name = "Nevada"
        self.assertEqual(self.city.name, "Nevada",
                         "city.name did not update correctly.")


if __name__ == '__main__':
    unittest.main()
