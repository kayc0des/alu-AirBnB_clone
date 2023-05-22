#!/usr/bin/python3
import sys
import os

# Get the absolute path of the directory containing test_base_model.py
script_dir = os.path.dirname(os.path.abspath(__file__))

# Get the absolute path of the models directory
models_dir = os.path.join(script_dir, '../models')

# Add the models_dir to sys.path
sys.path.append(models_dir)

from models.base_model import BaseModel



my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))