"""unit test for console"""
import unittest
import pep8
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestConsole(unittest.TestCase):
    """
    Test the console
    """

    def test_pep8_console(self):
        """
        Test that models/console.py conforms to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_count(self):
        """
        Test count
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
        self.assertEqual("Prints the number of instances of a class\n",
                         f.getvalue())

    def test_show(self):
        """
        Test show
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        self.assertEqual("Prints the string representation of an instance\n",
                         f.getvalue())

    def test_destroy(self):
        """
        Test destroy
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
        self.assertEqual("Deletes based on class name and id", f.getvalue())

    def test_update(self):
        """
        Test update
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
        self.assertEqual("Updates based on class name and id", f.getvalue())


if __name__ == '__main__':
    unittest.main()
