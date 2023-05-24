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
    def setUp(self):
        self.model = BaseModel()
    
    def test_initialization(self):
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save(self):
        initial_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(initial_updated_at, self.model.updated_at)

    def test_to_dict(self):
        self.model.name = "Test Model"
        self.model.my_number = 42
        self.model_dict = self.model.to_dict()

        self.assertIsInstance(self.model_dict, dict)
        self.assertEqual(self.model_dict['__class__'], 'BaseModel')
        self.assertEqual(self.model_dict['name'], 'Test Model')
        self.assertEqual(self.model_dict['my_number'], 42)
        self.assertIsInstance(self.model_dict['created_at'], str)
        self.assertIsInstance(self.model_dict['updated_at'], str)

    def test_str_representation(self):
        self.model.name = "Test Model"
        self.model.my_number = 42
        self.model_str = str(self.model)

        self.assertEqual(self.model_str, "[BaseModel] ({}) {'name': 'Test Model', 'my_number': 42, 'created_at': {}, 'updated_at': {}}".format(
            self.model.id, self.model.created_at, self.model.updated_at))


if __name__ == '__main__':
    unittest.main()