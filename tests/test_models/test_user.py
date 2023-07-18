#!/usr/bin/python3
"""test_user unit test for user class"""
import unittest
from models.user import User


class User_test(unittest.TestCase):
    """class User_test"""
    @classmethod
    def setUp(cls):
        """
        Method to set up BaseModel classes for use during testing.
        """
        cls.user1 = User()
        cls.user2 = User()

    @classmethod
    def tearDown(cls):
        """
        Method to tear down BaseModel classes for use during testing.
        """
        del cls.user1
        del cls.user2
        return super().tearDownClass()

    def test_class_attrs(self):
        self.assertEqual(self.user1.email, "")
        self.assertEqual(self.user1.password, "")
        self.assertEqual(self.user1.first_name, "")
        self.assertEqual(self.user1.last_name, "")
        self.assertIsInstance(self.user1.email, str)
        self.assertIsInstance(self.user1.password, str)
        self.assertIsInstance(self.user1.first_name, str)
        self.assertIsInstance(self.user1.last_name, str)

    def test_instance_attrs(self):
        test_dict = self.user2.to_dict()
        self.user3 = User(test_dict)
        self.user3.email = "StuPat@outlook.com"
        self.user3.password = "1234"
        self.user3.first_name = "Morake"
        self.user3.last_name = "Zimu"
        user_info = {
            "email": "StuPat@outlook.com",
            "password": "P@ssw0rd",
            "first_name": "Morake",
            "last_name": "Zimu"
        }
        # Non-depricated version of "assertDictContainsSubset"
        test_set = {**self.user3.to_dict(), **user_info}
        self.assertEqual(self.user3.to_dict(), test_set)
        self.assertNotEqual(self.user2, self.user3)


if __name__ == '__name__':
    unittest.main()
