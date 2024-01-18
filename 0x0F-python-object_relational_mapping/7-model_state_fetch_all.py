#!/usr/bin/python3
"""script listing all State objects from hbtn_0e_6_usa database."""
from sys import argv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

username = argv[1]
pwd = argv[2]
db = argv[3]
engine = create_engine(f"mysql+mysqldb://{username}:{pwd}@localhost:3306/{db}")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
for instance in session.query(State).order_by(State.id):
    print(f'{instance.id} : {instance.name}')
