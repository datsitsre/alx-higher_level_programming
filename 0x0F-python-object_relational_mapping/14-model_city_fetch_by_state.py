#!/usr/bin/python3
"""
List first State class
"""

from sys import argv
from model_state import Base, State
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

    session_instance = session.query(City, State).join(State)

    for c, in query.all():
        print('{}: ({:d}) {}'.format(s.name, c.id, c.name))

    session.commit()
    session.close()
