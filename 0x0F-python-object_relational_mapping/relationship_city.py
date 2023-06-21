#!/usr/bin/python3
"""
Define the City class and Base instance of declarative_base()
"""

from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

class City(Base):
    """
    Class : City
    Attributes : id , name, state_id
    """
    __tablename__ = 'cities'
    id = Column(Integer,unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
