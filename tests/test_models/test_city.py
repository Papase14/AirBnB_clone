#!/usr/bin/python3
"""test_city unit test for city class"""
import unittest
from models.city import City


class City_Test(unittest.TestCase):
    """City_Test class"""
    @classmethod
    def setUp(cls):
        """
        Method to set up City classes for use during testing.
        """
        cls.c1 = City()

    @classmethod
    def tearDown(cls):
        """
        Method to tear down City classes for use during testing.
        """
        del cls.c1
        return super().tearDownClass()

    def test_class_attrs(self):
        self.assertEqual(self.c1.state_id, "")
        self.assertEqual(self.c1.name, "")
        self.assertIn('id', self.c1.to_dict())
        self.assertIn('created_at', self.c1.to_dict())
        self.assertIn('updated_at', self.c1.to_dict())
        self.assertIsInstance(self.c1.state_id, str)
        self.assertIsInstance(self.c1.name, str)

    def test_instance_attrs(self):
        self.c1.state_id = "OK"
        self.c1.name = "Pretoria"
        self.assertEqual(self.c1.state_id, "OK")
        self.assertEqual(self.c1.name, "Pretoria")


if __name__ == '__name__':
    unittest.main()
