import logging
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, JSON, DateTime, func

# Define DDL for database.
DATABASE_MODEL = declarative_base()

# History Table
class Chat_History(DATABASE_MODEL):
    __tablename__ = 'chathistory'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    person = Column(String)
    prompt = Column(String)

# User Table
class Users(DATABASE_MODEL):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String, nullable=False)


"""
################ NOTE ################
    For PII we cannot logging 
    username inside the logs database

######################################
"""
# Logs database
class Logs(DATABASE_MODEL):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(DateTime, default=func.now())
    user_id = Column(Integer, ForeignKey('users.id'))
    action = Column(String, nullable=False)

# Stats database 
# Need to find more data that need to use
# class status(DATABASE_MODEL):
#     pass
