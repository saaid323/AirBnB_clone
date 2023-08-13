import os
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCityInstantiation(unittest.TestCase):
    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))


    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCitySave(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def setUp(self):
        self.cy = City()

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_one_save(self):
        first_updated_at = self.cy.updated_at
        self.cy.save()
        self.assertLess(first_updated_at, self.cy.updated_at)


    def test_save_updates_file(self):
        self.cy.save()
        cy_id = "City." + self.cy.id
        with open("file.json", "r") as f:
            self.assertIn(cy_id, f.read())


class TestCityToDict(unittest.TestCase):
    def setUp(self):
        self.cy = City()
        self.cy.id = "123456"
        self.cy.created_at = self.cy.updated_at = datetime.today()


if __name__ == "__main__":
    unittest.main()

