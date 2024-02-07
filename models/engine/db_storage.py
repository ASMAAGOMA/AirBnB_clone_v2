#!/usr/bin/python3
"""db storage"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
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
        Returns a dictionary of objects.
        If cls is specified, returns objects of that class.
        """
        dicty = {}
        if cls is None:
            for cls in classes.values():
                objects = self.__session.query(cls).all()
                for obj in objects:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    dicty[key] = obj
        else:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = f"{obj.__class__.__name__}.{obj.id}"
                dicty[key] = obj
        return dicty

    def new(self, obj):
        """Add a new object to the database session"""
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """Commit all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None): 
        """Delete an object from the database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload objects from the database"""
        Base.metadata.create_all(self.__engine)
        if self.__session is not None:
            self.__session.close()
        s = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(s)