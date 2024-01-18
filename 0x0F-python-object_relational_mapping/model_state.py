#!/usr/bin/python3
"""Module containing class definition of State and an instance Base."""
import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine


Base = declarative_base()

class State(Base):
    """A class that creates a schema for table states"""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
