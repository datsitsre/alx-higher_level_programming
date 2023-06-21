#!/usr/bin/python3
"""
Define the City class and Base instance of declarative_base()
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

datametada = MetaData()
Base = declarative_base(metadata=datametada)


class City(Base):
    """
    Class : City
    Attributes : id , name, state_id
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
