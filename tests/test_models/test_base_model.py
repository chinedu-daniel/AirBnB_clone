#!/usr/bin/python3
"""
Test suits for the base model
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
from time import sleep


class TestBaseModel(unittest.TestCase):
    """
    Tests attributes and functionality of the BaseModel class.
    """

    def test_basic(self):
        """
        Test basic attribute assignment and type checks for BaseModel.
        """
        instance = BaseModel()
        instance.name = "Nosenti"
        instance.number = 20
        self.assertEqual(instance.name, "Nosenti")
        self.assertEqual(instance.number, 20)
        self.assertTrue(isinstance(instance.id, str))
        self.assertTrue(isinstance(instance.created_at, datetime))
        self.assertTrue(isinstance(instance.updated_at, datetime))

    def test_datetime_attributes(self):
        """
        Test the datetime attributes for correctness and ensure updated_at is
        modified upon attribute changes.
        """
        instance1 = BaseModel()
        sleep(0.05)
        instance2 = BaseModel()
        self.assertTrue(instance1.created_at < instance2.created_at)
        self.assertTrue(instance1.updated_at < instance2.updated_at)

        initial_updated_at = instance1.updated_at
        sleep(0.05)
        instance1.name = "New Name"
        instance1.save()
        self.assertTrue(initial_updated_at < instance1.updated_at)

    def test_to_dict(self):
        """
        Test the dictionary representation method.
        """
        instance = BaseModel()
        instance.name = "Nosenti"
        instance.my_number = 20
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict["name"], "Nosenti")
        self.assertEqual(instance_dict["my_number"], 20)
        self.assertEqual(instance_dict["__class__"], "BaseModel")
        self.assertTrue("created_at" in instance_dict)
        self.assertTrue("updated_at" in instance_dict)
        self.assertEqual(instance.id, instance_dict["id"])

        # Ensuring that datetime attributes are properly stringified
        self.assertIsInstance(instance_dict["created_at"], str)
        self.assertIsInstance(instance_dict["updated_at"], str)


if __name__ == '__main__':
    unittest.main()
