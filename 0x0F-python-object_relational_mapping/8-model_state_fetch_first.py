#!/usr/bin/python3
"""script to print the first state ibject from hbtn_0e_6_usa database

usage:
    ./8-model_state_fetch_first.py <username> <password> <database_name>
"""

if __name__ == "__main__":
    """prevents the code from beign imported by other modules"""
    from model_state import Base, State
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    username = argv[1]
    pwd = argv[2]
    db = argv[3]
    query = f"mysql+mysqldb://{username}:{pwd}@localhost:3306/{db}"
    engine = create_engine(query)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id)
    query.all()
    try:
        result = query.first()
        print(f"{result.id}: {result.name}")
    except Exception as e:
        print()
