import sys
from os.path import abspath, dirname

# Add the parent directory to the system path
parent_dir = abspath(dirname(dirname(__file__)))
sys.path.append(parent_dir)

# Get the absolute path of the models directory
models_dir = os.path.join(script_dir, '../models')

# Add the models_dir to sys.path
sys.path.append(models_dir)

from models.base_model import BaseModel



if __name__ == '__main__':
    unittest.main()