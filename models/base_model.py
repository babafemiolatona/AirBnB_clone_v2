#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = (Column(String(60), nullable=False, primary_key=True))
    created_at = (Column(DateTime, nullable=False, default=datetime.utcnow()))
    updated_at = (Column(DateTime, nullable=False, default=datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        # else:
        #     kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
        #                                              '%Y-%m-%dT%H:%M:%S.%f')
        #     kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
        #                                              '%Y-%m-%dT%H:%M:%S.%f')
        #     del kwargs['__class__']
        #     # self.__dict__.update(kwargs)
        #     for key, value in kwargs.items():
        #         setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary.keys():
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """Delete the current instance from the storage"""
        models.storage.delete(self)
