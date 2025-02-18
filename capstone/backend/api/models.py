import base64
from typing import List
from pydantic import BaseModel
from fastapi import UploadFile, File

class ChatModel(BaseModel):
    question: str

class ResponseModel(BaseModel):
    answer: str
    tinme_usage: float
    question: str

class FileLength(BaseModel):
    start_page: int = 0
    final_page: int = 0

class SQLModel(BaseModel):
    sql: str

    def get_decoded_sql(self) -> str:
        return base64.b64decode(self.sql.encode()).decode()