from datetime import datetime
import base_model
from base_model import BaseModel
from datetime import timedelta
import uuid
import unittest

class testBaseModel (unittest.TestCase):
    """
    Test BaseModel Class
    """
    def setUp(self):
        self.my_model = BaseModel()
    
    def test_idInstance(self):
        """
        Test if id is an instance of the str class
        """
        self.assertIsInstance(self.my_model.id, str)

    def test_timeStamp(self):
        self.assertAlmostEqual(self.my_model.created_at, self.my_model.updated_at, delta=timedelta(microseconds=1000))

    def test_strRep(self):
        self.assertEqual(self.my_model.__str__(), "[{}] ({}) {}".format(self.my_model.__class__.__name__, self.my_model.id, self.my_model.__dict__))
 
if __name__ == '__main__':
    unittest.main()