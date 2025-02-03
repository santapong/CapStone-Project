from pydantic import BaseModel

class ChatModel(BaseModel):
    question: str

class ResponseModel(BaseModel):
    answer: str
    tinme_usage: float
    question: str