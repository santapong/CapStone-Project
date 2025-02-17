import uuid
import logging
from sqlalchemy import (
    func,
    UUID,
    Float,
    Column, 
    String, 
    Integer, 
    ForeignKey,
    ) 
from sqlalchemy.orm import (
    declarative_base, 
    relationship
    )

# Define DDL for database.
DATABASE_MODEL = declarative_base()

# History Table
class ChatHistoryTable(DATABASE_MODEL):
    __tablename__ = 'chathistory'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    question = Column(String)
    answer = Column(String)
    datetime = Column(String, default=func.now())

# Summary Table
class SummaryTable(DATABASE_MODEL):
    __tablename__ = 'summary'

    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String)
    question_freq = Column(Integer)

    # Relationship with ChartHistory
    # chathistory = relationship('ChatHistoryTable')

class CategoryTable(DATABASE_MODEL):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String)
    category = Column(String)

# Logs Table
class LogsTable(DATABASE_MODEL):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    prompt  = Column(String)
    question = Column(String)
    answer = Column(String)
    time_usage = Column(Float)
    datetime = Column(String, default=func.now())

# Document Table
class DocumentTable(DATABASE_MODEL):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, autoincrement=True)
    document_name = Column(String)
    pages = Column(Integer)
    datetime = Column(String, default=func.now())
