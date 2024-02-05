#!/usr/bin/python3
""" City Module for HBNB project """
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATETIME
from models.base_model import BaseModel
from sqlalchemy.orm import relationship

class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
