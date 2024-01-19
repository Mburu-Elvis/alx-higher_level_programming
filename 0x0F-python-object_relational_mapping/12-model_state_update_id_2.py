#!/usr/bin/python3
"""
script that changes the name of a State object from hbtn_0e_6_usa database

Usage:
    ./12-model_state_update_id_2.py <username> <password> <database>
"""
if __name__ == "__main__":
    from model_state import Base, State
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    username = argv[1]
    password = argv[2]
    db = argv[3]
    query_engine = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db}"
    engine = create_engine(query_engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_obj = session.query(State).filter(State.id == 2).first()
    state_obj.name = "New Mexico"
    session.commit()
    session.close()
