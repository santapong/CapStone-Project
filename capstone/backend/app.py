import os
import uvicorn
import logging

from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from dotenv import load_dotenv

from capstone.backend.api.router.dynamic import router_dynamic
from capstone.backend.api.router.chatbot import router_chatbot
from capstone.backend.api.router.document import router_document
from capstone.backend.api.router.dashboard import router_dashboard

from capstone.backend.logs.logging_config import setup_logging
from capstone.backend.api.database import (
    DBConnection,
    DATABASE_CREATE,
    DATABASE_MODEL
    )

load_dotenv()
logging.getLogger(__name__)

# Database session
DBConnect = DBConnection(
        create_database=DATABASE_CREATE,
        base_model=DATABASE_MODEL)

# Set API Prefix and API application.
prefix = os.getenv("PATH_PREFIX", default='/')
app = FastAPI(prefix=prefix)

# Add router for API.
app.include_router(router_chatbot)
app.include_router(router_document)

if __name__ == '__main__':
    uvicorn.run('app:app', reload=True)