#!/usr/bin/python3
"""  Define the state class  """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declaractive import declarative_base

Base = declarative_base()


class State(Base):
    """
        Class : State
        Attributes : id , name
    """
    __tablename__ = 'states'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
