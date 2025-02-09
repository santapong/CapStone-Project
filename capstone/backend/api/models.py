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
    start_page: int
    final_page: int

class UploadFileMultiple(BaseModel):
    files: List[UploadFile] = File(...)
