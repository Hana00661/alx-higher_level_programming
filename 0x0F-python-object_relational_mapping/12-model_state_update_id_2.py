#!/usr/bin/python3
"""script that changes the name of a State object from
the database hbtn_0e_6_usa"""

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

    states = session.query(State).filter(State.id == 2).first()
    states.name = 'New Mexico'
    session.commit()
    session.close()
