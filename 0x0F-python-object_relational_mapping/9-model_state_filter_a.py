#!/usr/bin/python3
"""script that lists all State objects that contain the
letter a from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    states = session.query(State).order_by(State.id).\
        filter(State.name.contains('a'))

    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
