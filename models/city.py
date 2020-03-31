#!/usr/bin/python3
"""This is the city class"""
from sqlalchemy import Column, String, Integer, ForeignKey
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", String(60), ForeignKey('states.id'), nullable=False)
