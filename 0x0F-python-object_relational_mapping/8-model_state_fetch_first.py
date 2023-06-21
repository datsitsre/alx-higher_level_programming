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
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session_instance = session.query(State).order_by(State.id).first()

    if session_instance is None:
        print("Nothing")
    else:
        print(session_instance.id, session_instance.name, sep=": ")
