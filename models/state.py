#!/usr/bin/python3
""" State Module for HBNB project """
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATETIME, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models import store_type
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if store_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('city', backref='state', cascade='all, delete, delete-orphan')
    else:
        name = ""

    def cities(self) :
        """cities"""
        from models import storage
        c = []
        cities = storage.all(City)
        for city in cities.values():
            if city.state_id == self.id:
                c.append(city)
        return(c)