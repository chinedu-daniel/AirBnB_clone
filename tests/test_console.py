#!/usr/bin/python3
"""
Unit tests for console using Mock module from python standard library
Checks console for capturing stdout into a StringIO object
"""

import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """
    Unittest for the console model
    """

    def setUp(self):
        """Setup the test case environment"""
        self.err = ["** class name missing **",
                    "** class doesn't exist **",
                    "** instance id missing **",
                    "** no instance found **"]

        self.cls = ["BaseModel",
                    "User",
                    "State",
                    "City",
                    "Place",
                    "Amenity",
                    "Review"]

    def test_quit(self):
        """Test the quit command"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            cli = HBNBCommand()
            self.assertTrue(cli.onecmd("quit"))
            self.assertEqual('', fake_output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
