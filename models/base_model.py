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
    def __init__(self, *args, **kwargs):
        """
            Assign a unique ID to each instance using and converts to string
        """
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns string rep"""
        f = self.__class__.__name__
        return "[{}] ({}) {}".format(f, self.id, self.__dict__)

    def save(self):
        """updates instance"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
            Create a dictionary representation of the instance's attributes
        """
        obj_dict = {}
        obj_dict.update(self.__dict__)
        # obj_dict.update({'__class__': (str(type(self))
        # .split('.')[-1]).split('\'')[0]})
        obj_dict.update({'__class__': type(self).__name__})
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
