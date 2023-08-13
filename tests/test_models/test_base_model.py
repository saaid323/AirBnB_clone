#!/usr/bin/python3
import unittest
from datetime import datetime, timedelta
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_base_model_attributes(self):
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, "id"))
        self.assertTrue(hasattr(base_model, "created_at"))
        self.assertTrue(hasattr(base_model, "updated_at"))

    def test_base_model_id_generation(self):
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    def test_base_model_created_at(self):
        base_model = BaseModel()
        self.assertTrue(isinstance(base_model.created_at, datetime))

    def test_base_model_updated_at_on_creation(self):
        base_model = BaseModel()
        self.assertTrue(isinstance(base_model.updated_at, datetime))

    def test_base_model_updated_at_after_save(self):
        base_model = BaseModel()
        original_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(base_model.updated_at, original_updated_at)

    def test_base_model_to_dict(self):
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertTrue(isinstance(base_model_dict, dict))
        self.assertEqual(base_model_dict["id"], base_model.id)
        self.assertEqual(base_model_dict["__class__"], "BaseModel")
        self.assertTrue("created_at" in base_model_dict)
        self.assertTrue("updated_at" in base_model_dict)

    def test_base_model_to_dict_datetime_format(self):
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertTrue("created_at" in base_model_dict)
        self.assertTrue("updated_at" in base_model_dict)
        created_at_str = base_model_dict["created_at"]
        updated_at_str = base_model_dict["updated_at"]
        self.assertEqual(datetime.strptime(created_at_str, "%Y-%m-%dT%H:%M:%S.%f"), base_model.created_at)
        self.assertEqual(datetime.strptime(updated_at_str, "%Y-%m-%dT%H:%M:%S.%f"), base_model.updated_at)


if __name__ == '__main__':
    unittest.main()
