import sys
from os.path import abspath, dirname
# Add the parent directory to the system path
parent_dir = abspath(dirname(dirname(__file__)))
sys.path.append(parent_dir)
# Import the BaseModel class from models subdirectory
from models.base_model import BaseModel
import unittest
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test BaseModel Class
    """
    def test_initialization(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_save(self):
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(initial_updated_at, model.updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model.name = "Test Model"
        model.my_number = 42
        model_dict = model.to_dict()

        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['name'], 'Test Model')
        self.assertEqual(model_dict['my_number'], 42)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_str_representation(self):
        model = BaseModel()
        model.name = "Test Model"
        model.my_number = 42
        model_str = str(model)

        self.assertEqual(model_str, "[BaseModel] ({}) {'name': 'Test Model', 'my_number': 42, 'created_at': {}, 'updated_at': {}}".format(
            model.id, model.created_at, model.updated_at))


if __name__ == '__main__':
    unittest.main()