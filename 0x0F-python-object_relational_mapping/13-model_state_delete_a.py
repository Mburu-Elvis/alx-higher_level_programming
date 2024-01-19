#!/usr/bin/python3
"""
script that deletes all State objects with name containing an a,

from the database hbtn_0e_6_usa.
Usage:
    ./13-model_state_delete_a.py <username> <password> <database_name>
"""
if __name__ == "__main__":
    """prevents the module from being imported."""
    from model_state import Base, State
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    username = argv[1]
    password = argv[2]
    database = argv[3]
    query_engine = f"mysql+mysqldb://{username}:{password}@\
        localhost:3306/{database}"
    engine = create_engine(query_engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).filter(State.name.like('%a%')):
        session.delete(instance)
    session.commit()
    session.close()
