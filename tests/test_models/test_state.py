#!/usr/bin/python3
"""
Tests for state
"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Tests for the State class.
    """

    def setUp(self):
        """
        Set up for the tests
        """
        self.state = State()
        self.state.name = "California"

    def tearDown(self):
        """
        Clean up after each test
        """
        del self.state

    def test_name_attribute_exists(self):
        """
        Test if the name attribute is present in the State instance
        """
        self.assertTrue(hasattr(self.state, 'name'),
                        "State instance lacks a 'name' attribute")

    def test_name_assignment(self):
        """
        Test assignment of the name attribute
        """
        self.assertEqual(self.state.name, "California",
                         "State.name has incorrect value.")

    def test_name_type(self):
        """
        Test the type of the name attribute
        """
        self.assertIsInstance(self.state.name, str,
                              "State.name is not of type 'str'.")

    def test_new_name_assignment(self):
        """
        Test updating the name attribute
        """
        self.state.name = "Nevada"
        self.assertEqual(self.state.name, "Nevada",
                         "State.name did not update correctly.")


if __name__ == '__main__':
    unittest.main()
