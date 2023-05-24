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

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]),
                                   my_model_json[key]))
