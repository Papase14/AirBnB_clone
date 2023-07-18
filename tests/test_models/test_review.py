#!/usr/bin/python3
"""test_review unit for testing review class"""
import unittest
from models.review import Review


class Review_Test(unittest.TestCase):
    """Review_test class"""
     @classmethod
    def setUp(cls):
        """
        Method to set up Review classes for use during testing.
        """
        cls.r1 = Review()

    @classmethod
    def tearDown(cls):
        """
        Method to tear down Review classes for use during testing.
        """
        del cls.r1
        return super().tearDownClass()

    def test_class_attrs(self):
        self.assertEqual(self.r1.place_id, "")
        self.assertEqual(self.r1.user_id, "")
        self.assertEqual(self.r1.text, "")
        self.assertIn('id', self.r1.to_dict())
        self.assertIn('created_at', self.r1.to_dict())
        self.assertIn('updated_at', self.r1.to_dict())
        self.assertIsInstance(self.r1.place_id, str)
        self.assertIsInstance(self.r1.user_id, str)
        self.assertIsInstance(self.r1.text, str)

    def test_instance_attrs(self):
        self.r1.place_id = "123"
        self.r1.user_id = "123"
        self.r1.text = "Real Review"
        self.assertEqual(self.r1.place_id, "123")
        self.assertEqual(self.r1.user_id, "123")
        self.assertEqual(self.r1.text, "Real Review")


if __name__ == '__name__':
    unittest.main()
