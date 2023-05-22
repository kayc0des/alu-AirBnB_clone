import os
import sys
import unittest
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()

    def test_id_is_string(self):
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        initial_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(initial_updated_at, self.model.updated_at)

    @patch('base_model.datetime')
    def test_to_dict_returns_correct_dictionary(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 5, 1, 10, 30)
        expected_dict = {
            '__class__': 'BaseModel',
            'id': self.model.id,
            'created_at': self.model.created_at.isoformat(),
            'updated_at': self.model.updated_at.isoformat()
        }
        self.assertDictEqual(self.model.to_dict(), expected_dict)


if __name__ == '__main__':
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Specify the relative path to the models package
    models_path = os.path.join(script_dir, 'models')

    # Add the models path to the system path
    sys.path.append(models_path)
    
    unittest.main()