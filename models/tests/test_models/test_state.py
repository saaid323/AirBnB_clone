#!/usr/bin/python3
"""Defines unittests for models/state.py.
Unittest classes:
    TestStateInstantiation
    TestStateSave
    TestStateToDict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestStateInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

    def test_no_args_instantiates(self):
        self.assertIsInstance(State(), State)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertIsInstance(State().id, str)



    def test_custom_attribute(self):
        st = State()
        st.custom_attr = "Test Attribute"
        self.assertEqual("Test Attribute", st.custom_attr)
        st_dict = st.to_dict()
        self.assertIn("custom_attr", st_dict)
        self.assertEqual("Test Attribute", st_dict["custom_attr"])


class TestStateSave(unittest.TestCase):
    """Unittests for testing save method of the State class."""

    @classmethod
    def setUpClass(cls):
        """Setup method for class-level operations."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        """Teardown method for class-level operations."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def setUp(self):
        """Setup method for individual test cases."""
        self.st = State()

    def tearDown(self):
        """Teardown method for individual test cases."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_save_updates_updated_at(self):
        """Test that save updates the updated_at attribute."""
        initial_updated_at = self.st.updated_at
        self.st.save()
        self.assertLess(initial_updated_at, self.st.updated_at)

    def test_save_updates_file(self):
        """Test that save updates the storage file."""
        st_id = f"State.{self.st.id}"
        self.st.save()
        with open("file.json", "r") as f:
            self.assertIn(st_id, f.read())


class TestStateToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the State class."""

    def setUp(self):
        """Setup method for individual test cases."""
        self.st = State()
        self.st.id = "123456"
        self.st.created_at = self.st.updated_at = datetime.today()

    def test_to_dict_type(self):
        """Test if to_dict() returns a dictionary."""
        self.assertIsInstance(self.st.to_dict(), dict)

    def test_to_dict_contains_correct_keys(self):
        """Test if to_dict() contains the correct keys."""
        st_dict = self.st.to_dict()
        self.assertIn("id", st_dict)
        self.assertIn("created_at", st_dict)
        self.assertIn("updated_at", st_dict)
        self.assertIn("__class__", st_dict)

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test if datetime attributes in to_dict() are strings."""
        st_dict = self.st.to_dict()
        self.assertIsInstance(st_dict["id"], str)
        self.assertIsInstance(st_dict["created_at"], str)
        self.assertIsInstance(st_dict["updated_at"], str)

    def test_to_dict_output(self):
        """Test the output of to_dict() with specific data."""
        expected_dict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': self.st.created_at.isoformat(),
            'updated_at': self.st.updated_at.isoformat(),
        }
        self.assertDictEqual(self.st.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
