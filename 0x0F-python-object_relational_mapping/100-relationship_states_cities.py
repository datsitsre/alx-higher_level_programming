#!/usr/bin/python3
"""
List first State class
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """
    Script for accessing data
    """
    uri_db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(uri_db)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_cal = State(name='California')
    state_city = City(name='San Francisco')
    state_cal.cities.append(state_city)

    session.commit()
    session.close()
