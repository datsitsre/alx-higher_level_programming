#!/usr/bin/python3
"""
Define the state class and Base instance of declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class : State
    Attributes : id , name
    """
    __tablename__ = 'states'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
