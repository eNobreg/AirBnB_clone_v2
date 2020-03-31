#!/usr/bin/python3
"""This is the city class"""
from sqlalchemy import Column, String, Integer, ForeignKey
from models.base_model import BaseModel, Base
import os
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"

    if (os.getenv("HBNB_TYPE_STORAGE") == 'db'):
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    else:
        places = relationship("Place", cascade='all, delete', backref='cities')
