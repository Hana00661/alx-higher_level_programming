#!/usr/bin/python3
"""Write a Python file similar to model_state.py named
model_city.py that contains the class definition of a City"""

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__" :

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    states = session.query(State, City).join(State).all()

    for state, city in states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
