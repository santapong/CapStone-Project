import base64
from pydantic import BaseModel

class ChatModel(BaseModel):
    question: str

class ResponseModel(BaseModel):
    answer: str
    time_usage: float
    question: str

class FileLength(BaseModel):
    start_page: int = 0
    final_page: int = 0

class DocumentModel(BaseModel):
    document_name: str
    id: int

class SQLModel(BaseModel):
    sql: str

    def get_decoded_sql(self) -> str:
        return base64.b64decode(self.sql.encode()).decode()