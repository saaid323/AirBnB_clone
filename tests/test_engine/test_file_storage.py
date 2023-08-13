#!/usr/bin/python3
import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


class TestFileStorage(unittest.TestCase):
    TEST_JSON_FILE = "test_file.json"

    @classmethod
    def setUpClass(cls):
        storage._FileStorage__file_path = cls.TEST_JSON_FILE

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove(cls.TEST_JSON_FILE)
        except FileNotFoundError:
            pass

    def test_all(self):

        base_model = BaseModel()
        user = User()
        storage.new(base_model)
        storage.new(user)
        all_objects = storage.all()
        self.assertIn(base_model, all_objects.values())
        self.assertIn(user, all_objects.values())

    def test_save_reload(self):
        base_model = BaseModel()
        user = User()
        storage.new(base_model)
        storage.new(user)
        storage.save()
        storage.reload()
        reloaded_objects = storage.all()
        self.assertIn(base_model, reloaded_objects.values())
        self.assertIn(user, reloaded_objects.values())

    def test_save_file_content(self):
        base_model = BaseModel()
        user = User()
        storage.new(base_model)
        storage.new(user)
        storage.save()
        with open(self.TEST_JSON_FILE, "r") as f:
            data = json.load(f)
        self.assertIn(f"BaseModel.{base_model.id}", data)
        self.assertIn(f"User.{user.id}", data)


if __name__ == '__main__':
    unittest.main()
