#!/usr/bin/python3
"""test_place unit test for Place class"""

import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class ConsoleTestCase(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_quit_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    def test_help_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("help"))

    def test_create_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create"))
            self.assertFalse(self.console.onecmd("create SomeInvalidClassName"))

    def test_show_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show"))
            self.assertFalse(self.console.onecmd("show SomeInvalidClassName"))
            self.assertFalse(self.console.onecmd("show BaseModel"))

    def test_destroy_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy"))
            self.assertFalse(self.console.onecmd("destroy SomeInvalidClassName"))
            self.assertFalse(self.console.onecmd("destroy BaseModel"))


if __name__ == '__main__':
    unittest.main()
