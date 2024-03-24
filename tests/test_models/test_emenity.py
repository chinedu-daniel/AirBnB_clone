#!/usr/bin/python3
"""
Tests for the amenity
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Tests for amenity
    """

    def setUp(self):
        """
        Set up for the tests
        """
        self.amenity = Amenity()
        self.amenity.name = "California"

    def tearDown(self):
        """
        Clean up after each test
        """
        del self.amenity

    def test_name_attribute_exists(self):
        """
        Test if the name attribute is present in the amenity instance
        """
        self.assertTrue(hasattr(self.amenity, 'name'),
                        "amenity instance lacks a 'name' attribute")

    def test_name_assignment(self):
        """
        Test assignment of the name attribute
        """
        self.assertEqual(self.amenity.name, "California",
                         "amenity.name has incorrect value.")

    def test_name_type(self):
        """
        Test the type of the name attribute
        """
        self.assertIsInstance(self.amenity.name, str,
                              "amenity.name is not of type 'str'.")

    def test_new_name_assignment(self):
        """
        Test updating the name attribute
        """
        self.amenity.name = "Nevada"
        self.assertEqual(self.amenity.name, "Nevada",
                         "amenity.name did not update correctly.")


if __name__ == '__main__':
    unittest.main()
