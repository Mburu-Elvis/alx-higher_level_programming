#!/usr/bin/python3
"""
script adding State object 'Louisiana' to database hbtn_0e_6_usa

Usage:
    ./11-model_state_insert.py <username> <password> <database>
"""
if __name__ == "__main__":
    from model_state import Base, State
    from sys import argv
    from sqlalchemy import create_engine, Column, String
    from sqlalchemy.orm import sessionmaker

    username = argv[1]
    pwd = argv[2]
    db = argv[3]
    engine_query = f"mysql+mysqldb://{username}:{pwd}@localhost:3306/{db}"
    engine = create_engine(engine_query)
    Session = sessionmaker(bind=engine)
    session = Session()
    lois = State(name="Louisiana")
    session.add(lois)
    session.commit()
    created_state = session.query(State).filter(State.name == lois.name).first()
    print(f"{created_state.id}: {created_state.name}")
    session.close()
