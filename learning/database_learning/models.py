from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

class test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
