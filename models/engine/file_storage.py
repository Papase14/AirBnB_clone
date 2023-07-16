#!/usr/bin/python3
"""
    file_storage module that contains the FileStorage class
    definition and methods
"""

from models.base_model import BaseModel
import json
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity

class FileStorage:
    """
    FileStorage class which serializes instances to a JSON file
    and deserializes JSON files to instances.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns the dictionary.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in `__objects` the `obj` with key `<obj class name>.id`.
        """
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """
        Serializes `__objects` to the JSON file.
        """
        with open(self.__file_path, '+w') as f:
            ObjectDict = {}
            ObjectDict.update(self.__objects)
            for key, val in ObjectDict.items():
                ObjectDict[key] = val.to_dict()
            json.dump(ObjectDict, f)

    def reload(self):
        """
        Deserializes the JSON file to `__objects` if the file exists;
        otherwise, does nothing.
        """
        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            with open(self.__file_path, 'r') as f:
                ObjectDict = {}
                ObjectDict = json.load(f)
                for key, val in ObjectDict.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
