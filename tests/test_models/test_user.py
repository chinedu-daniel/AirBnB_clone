#!/usr/bin/python3
"""
Tests for the user
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Tests for user
    """

    def setUp(self):
        """
        Set up for the tests
        """
        self.user = User()
        self.user.first_name = "California"

    def tearDown(self):
        """
        Clean up after each test
        """
        del self.user

    def test_first_name_attribute_exists(self):
        """
        Test if the first_name attribute is present in the user instance
        """
        self.assertTrue(hasattr(self.user, 'first_name'),
                        "user instance lacks a 'first_name' attribute")

    def test_first_name_assignment(self):
        """
        Test assignment of the first_name attribute
        """
        self.assertEqual(self.user.first_name, "California",
                         "user.first_name has incorrect value.")

    def test_first_name_type(self):
        """
        Test the type of the first_name attribute
        """
        self.assertIsInstance(self.user.first_name, str,
                              "user.first_name is not of type 'str'.")

    def test_new_first_name_assignment(self):
        """
        Test updating the first_name attribute
        """
        self.user.first_name = "Nevada"
        self.assertEqual(self.user.first_name, "Nevada",
                         "user.first_name did not update correctly.")


if __name__ == '__main__':
    unittest.main()
