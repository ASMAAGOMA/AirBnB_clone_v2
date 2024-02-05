#!/usr/bin/python3
""" City Module for HBNB project """
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATETIME, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models import store_type

class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if store_type == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('state.id'), nullable=False)
        places = relationship('Place', backref='cities', cascade='all, delete, delete-orphan')
    else:
        name = ''
        state_id = ''
