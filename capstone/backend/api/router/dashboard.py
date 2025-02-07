import os
import logging

from dotenv import load_dotenv
from fastapi import APIRouter, Depends, Request

from capstone.backend.database import (
    get_db,
    DBConnection,
    ChatHistory,
    )
     

router_dashboard = APIRouter(prefix='/dashboard')

tags = ['Dashboard']

@router_dashboard.get('/history', tags=tags)
def history(question:str, answer:str, db: DBConnection = Depends(get_db)):
    db.insert(ChatHistory, question=question, answer=answer)
    return {"message": "Success"}