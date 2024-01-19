#!/usr/bin/python3
"""script that lists all State objects cantaining a from hbtn_0e_6_usa database

Usage:
    ./9-model_state_filter_a.py <username> <password> <database>
"""
if __name__ == "__main__":
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    username = argv[1]
    pwd = argv[2]
    db = argv[3]
    db_connect = f"mysql+mysqldb://{username}:{pwd}@localhost:3306/{db}"
    engine = create_engine(db_connect)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id).all()
    for row in result:
        print(f"{row.id}: {row.name}")
