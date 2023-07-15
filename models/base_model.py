#!/usr/bin/python3
"""
    This module defines a base class for all models in our hbnb clone
"""

import uuid
from datetime import datetime

class BaseModel:
    """
        A base class for all hbnb models
    """
    def __init__(self):
        """
            Assign a unique ID to each instance using uuid.uuid4() and convert it to a string
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            Create a dictionary representation of the instance's attributes
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict