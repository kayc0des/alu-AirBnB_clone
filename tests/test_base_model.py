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

    def setUp(self):
        self.my_model = BaseModel()

    def test_id_is_string(self):
        self.assertIsInstance(self.my_model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.my_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.my_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        initial_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(initial_updated_at, self.my_model.updated_at)

    @patch('base_model.datetime')
    def test_to_dict_returns_correct_dictionary(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 5, 1, 10, 30)
        expected_dict = {
            '__class__': 'BaseModel',
            'id': self.my_model.id,
            'created_at': self.my_model.created_at.isoformat(),
            'updated_at': self.my_model.updated_at.isoformat()
        }
        self.assertDictEqual(self.my_model.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()