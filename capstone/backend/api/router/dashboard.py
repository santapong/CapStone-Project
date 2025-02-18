import os
import logging
import json

from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from fastapi import (
    Request,
    Depends, 
    APIRouter, 
)

from sqlalchemy import text
from capstone.backend.api.models import SQLModel
from capstone.backend.database import (
    get_db,
    DBConnection,
    ChatHistoryTable,
    )
     
router_dashboard = APIRouter(prefix='/dashboard')
tags = ['Dashboard']    

# API for get Data from database
@router_dashboard.post('/data/sql', tags=tags)
def sqlexpress(
        request:SQLModel,
        db: DBConnection = Depends(get_db)
    ):

    # Query data from database from request.
    sql = request.sql
    session = db.get_session()    
    query_data = session.execute(text(sql))

    # Convert data to Json format    print(json_data)
    column_name = [column for column in query_data.keys()]
    row_data = [data for data in query_data.all()]
    json_data = [dict(zip(column_name,row_data)) for row_data in row_data]

    return JSONResponse(content={"data":json_data})



@router_dashboard.post('/data/chatgpt', tags=tags)
def sqlexpress(
        request: SQLModel,
        db: DBConnection = Depends(get_db)
    ):
    # Decode Base64 SQL
    sql_query = request.get_decoded_sql()

    # Query data from database
    session = db.get_session()
    query_data = session.execute(text(sql_query))

    # Convert data to JSON format
    column_name = [column for column in query_data.keys()]
    row_data = [data for data in query_data.all()]
    json_data = [dict(zip(column_name, row_data)) for row_data in row_data]

    return JSONResponse(content={"data": json_data})