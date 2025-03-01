from sqlalchemy.orm import declarative_base
from sqlalchemy import (
    func,
    JSON,
    Float,
    Column, 
    String, 
    Integer, 
    ) 

# Define DDL for database.
DATABASE_MODEL = declarative_base()

# Categoty Table
class CategoryTable(DATABASE_MODEL):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String)
    category = Column(String)

# Logs Table
class LogsTable(DATABASE_MODEL):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    llm_model = Column(String)
    prompt  = Column(String)
    question = Column(String)
    answer = Column(String)
    time_usage = Column(Float)
    datetime = Column(String, default=func.now())

# Document Table
class DocumentTable(DATABASE_MODEL):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ids = Column(JSON)
    embedding_model = Column(String)
    document_name = Column(String)
    pages = Column(Integer)
    time_usage = Column(Float)
    datetime = Column(String, default=func.now())