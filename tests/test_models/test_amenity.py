#!/usr/bin/python3
""" test_amenity module for unit testing """
import unittest
from models.amenity import Amenity


class Amenity_Test(unittest.TestCase):
    """Class amenitytest """
    @classmethod
    def setUp(cls):
        """ AmenityTest method """
        cls.a1 = Amenity()

    @classmethod
    def tearDown(cls):
        """
        Method to tear down Amenity classes for use during testing.
        """
        del cls.a1
        return super().tearDownClass()

    def test_class_attrs(self):
        self.assertEqual(self.a1.name, "")
        self.assertIn('id', self.a1.to_dict())
        self.assertIn('created_at', self.a1.to_dict())
        self.assertIn('updated_at', self.a1.to_dict())
        self.assertIsInstance(self.a1.name, str)

    def test_instance_attrs(self):
        self.a1.name = "wifi"
        self.assertEqual(self.a1.name, "wifi")


if __name__ == '__name__':
    unittest.main()
