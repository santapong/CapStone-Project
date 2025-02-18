import os
import logging

from fastapi.responses import JSONResponse
from fastapi import (
    Depends, 
    APIRouter, 
)

from sqlalchemy import text
from capstone.backend.api.models import SQLModel
from capstone.backend.database import (
    get_db,
    DBConnection,
    )

logging.getLogger(__name__)

router_dashboard = APIRouter(prefix='/dashboard')
tags = ['Dashboard']    

# Using Base 64 to query Database.
@router_dashboard.post('/query', tags=tags)
def SQL_query(
        request: SQLModel,
        db: DBConnection = Depends(get_db)
    ):
    # Decode Base64 SQL
    sql_query = request.get_decoded_sql()

    # logging Debug
    logging.debug(f"Recieve SQL >> {sql_query}")

    # logging info
    logging.info(f"Get SQL query")

    # Query data from database
    session = db.get_session()
    query_data = session.execute(text(sql_query))

    # Convert data to JSON format
    column_name = [column for column in query_data.keys()]
    row_data = [data for data in query_data.all()]
    json_data = [dict(zip(column_name, row_data)) for row_data in row_data]

    return JSONResponse(content={"data": json_data})