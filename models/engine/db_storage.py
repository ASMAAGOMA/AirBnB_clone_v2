#!/usr/bin/python3
"""db storage"""

from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

classes = {"User": User, "Place": Place, "Amenity": Amenity, "State": State
        , "City": City, "Review": Review, }

class DBStorage:
    """database storage"""
    __engine = None
    __session = None
    
    def __init__(self):
        """engine"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                        .format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB), pool_pre_ping=True)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns the list of objects of one type of class.
        If cls is None, returns all objects.
        """
        dicty = {}
        if cls is None:
            for i in classes.values():
                objects = self.__session.query(i).all()
                for object in objects:
                    the_key = object.__class__.__name__ + '.' + object.id
                    dicty = object[the_key]
        else:
            objects = self.__session.query(cls).all()
            for object in objects:
                the_key = object.__class__.__name__ + '.' + object.id
                dicty = object[the_key]
        return dicty

    def new(self, obj):
        """adds a new object"""
        if obj != None:
            self.__session.add(obj)
            self.__session.flush()
            self.__session.refresh()

    def save(self):
        """commits changes"""
        self.__session.commit()

    def delete(self, obj=None): 
        """deletes obj"""
        if obj != None:
            self.__session.query(type(obj)).filter(type(obj).id == obj.id).delete()

    def reload(self):
        """reload"""
        Base.metadata.create_all(self.__engine)
        s = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(s)
