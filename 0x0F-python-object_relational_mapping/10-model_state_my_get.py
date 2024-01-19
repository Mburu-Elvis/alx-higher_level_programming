#!/usr/bin/python3
"""
script that prints the State objects with name

usage:
    ./10-model_state_my_get.py <username> <password> <database> <name>
"""
if __name__ == "__main__":
    from model_state import Base, State
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    username = argv[1]
    pwd = argv[2]
    db = argv[3]
    name = argv[4]
    connect_db = f"mysql+mysqldb://{username}:{pwd}@localhost:3306/{db}"
    engine = create_engine(connect_db)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        result = session.query(State).filter(State.name == name).one()
        print(result.id)
    except Exception as e:
        print("Not found")
