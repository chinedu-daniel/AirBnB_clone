#!/usr/bin/python3
"""
Tests for review
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test case for review
    """

    def setUp(self):
        """
        Set up for the tests
        """
        self.review = Review()
        self.review.text = "California"

    def tearDown(self):
        """
        Clean up after each test
        """
        del self.review

    def test_name_attribute_exists(self):
        """
        Test if the name attribute is present in the review instance
        """
        self.assertTrue(hasattr(self.review, 'name'),
                        "review instance lacks a 'name' attribute")

    def test_name_assignment(self):
        """
        Test assignment of the name attribute
        """
        self.assertEqual(self.review.name, "California",
                         "review.name has incorrect value.")

    def test_name_type(self):
        """
        Test the type of the name attribute
        """
        self.assertIsInstance(self.review.name, str,
                              "review.name is not of type 'str'.")

    def test_new_name_assignment(self):
        """
        Test updating the name attribute
        """
        self.review.name = "Nevada"
        self.assertEqual(self.review.name, "Nevada",
                         "review.name did not update correctly.")


if __name__ == '__main__':
    unittest.main()
