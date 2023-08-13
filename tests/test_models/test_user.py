#!/usr/bin/python3

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_user_default_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_custom_attributes(self):
        user = User(email="user@example.com", password="secret",
                    first_name="John", last_name="Doe")
        self.assertEqual(user.email, "user@example.com")
        self.assertEqual(user.password, "secret")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_user_str_representation(self):
        user = User(email="user@example.com", password="secret",
                    first_name="John", last_name="Doe")
        self.assertEqual(
            str(user),
            "User(id=None, created_at=None, updated_at=None,
                  email='user@example.com', password='secret',
                  first_name='John', last_name='Doe')"
        )

    def test_user_attributes_after_update(self):
        user = User(email="user@example.com", password="secret",
                    first_name="John", last_name="Doe")
        user.update(first_name="Jane", last_name="Smith")
        self.assertEqual(user.first_name, "Jane")
        self.assertEqual(user.last_name, "Smith")

    def test_user_to_dict(self):
        user = User(email="user@example.com", password="secret",
                    first_name="John", last_name="Doe")
        user_dict = user.to_dict()
        self.assertTrue(isinstance(user_dict, dict))
        self.assertEqual(user_dict["email"], "user@example.com")
        self.assertEqual(user_dict["password"], "secret")
        self.assertEqual(user_dict["first_name"], "John")
        self.assertEqual(user_dict["last_name"], "Doe")


if __name__ == '__main__':
    unittest.main()
