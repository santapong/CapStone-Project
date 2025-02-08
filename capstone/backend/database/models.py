import uuid
import logging
from sqlalchemy import (
    func,
    UUID, 
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

class SummaryTable(DATABASE_MODEL):
    __tablename__ = 'summary'

    id = Column(Integer, primary_key=True, increment=True)
    question = Column(String)
    question_freq = Column(Integer)

    # Relationship with ChartHistory
    chathistory = relationship('ChatHistory', backref='summary')