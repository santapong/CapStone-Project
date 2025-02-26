import os
import logging

from fastapi.responses import JSONResponse
from fastapi import (
    Depends, 
    APIRouter, 
)

from sqlalchemy import text

from capstone.backend.api.utils import convert_to_table
from capstone.backend.api.utils.dashboard_query import *
from capstone.backend.api.models import SQLModel
from capstone.backend.database import (
    get_db,
    DBConnection,
    )

logging.getLogger(__name__)

tags = ['Dashboard']    
router_dashboard = APIRouter(prefix='/dashboard', tags=tags)

# Using Base 64 to query Database.
@router_dashboard.post('/query')
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

# Query from Database.
@router_dashboard.get("/query")
async def query(
    db: DBConnection = Depends(get_db)
):
    # Get session from database
    session = db.get_session()
    
    # Prepare Data for Dashboard
    queries = {
        "total_user": OVERALL_CHAT,
        "avg_time_usage": TIME_USAGE,
        "user_time": TOP_USER_TIME,
        "top_category": TOP_CATEGORY,
        "history_table": HISTORY_TABLE,
        "document_table": DOCUMENT_TABLE
    }

    combined_data = {key: convert_to_table(session=session, sql=sql) for key, sql in queries.items()}
    
    return JSONResponse(content={"data": combined_data})