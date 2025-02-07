import os
import logging

from dotenv import load_dotenv
from fastapi import APIRouter, Depends, Request

from capstone.backend.utils.database import get_db, DBConnection
from capstone.backend.api.schema.model_database import Users

router_dashboard = APIRouter(prefix='/dashboard')

tags = ['Dashboard']

@router_dashboard.get('/history', tags=tags)
def history(full_name:str, db: DBConnection = Depends(get_db)):
    db.insert(Users, fullname=full_name)
    return {"message": "Success"}