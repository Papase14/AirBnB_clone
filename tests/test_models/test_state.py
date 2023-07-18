#!/usr/bin/python3
"""test_state unit test for state class"""
import unittest
from models.state import State as State


class State_Test(unittest.TestCase):
    """state_test class"""
    @classmethod
    def setUp(cls):
        """
        Method to set up State classes for use during testing.
        """
        cls.s1 = State()

    @classmethod
    def tearDown(cls):
        """
        Method to tear down State classes for use during testing.
        """
        del cls.s1
        return super().tearDownClass()

    def test_class_attrs(self):
        self.assertEqual(self.s1.name, "")
        self.assertIn('id', self.s1.to_dict())
        self.assertIn('created_at', self.s1.to_dict())
        self.assertIn('updated_at', self.s1.to_dict())
        self.assertIsInstance(self.s1.name, str)

    def test_instance_attrs(self):
        self.s1.name = "MyName"
        self.assertEqual(self.s1.name, "MyName")


if __name__ == '__name__':
    unittest.main()
