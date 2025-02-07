import uuid
import logging
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, UUID, func

# Define DDL for database.
DATABASE_MODEL = declarative_base()

# History Table
class ChatHistory(DATABASE_MODEL):
    __tablename__ = 'chathistory'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    question = Column(String)
    answer = Column(String)
    datetime = Column(String, default=func.now())