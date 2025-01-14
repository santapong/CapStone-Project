import os
import uvicorn
import logging

from fastapi import FastAPI
from dotenv import load_dotenv

from capstone.backend.logs.logging_config import setup_logging

from capstone.backend.api.router.dynamic import router_dynamic
from capstone.backend.api.router.chatbot import router_chatbot
from capstone.backend.api.router.document import router_document
from capstone.backend.api.router.dashboard import router_dashboard

load_dotenv()

# Setup logging for more security.
setup_logging()
logging.getLogger(__name__)

app = FastAPI()

app.include_router(router_dynamic)
app.include_router(router_chatbot)
app.include_router(router_dashboard)
app.include_router(router_document)

if __name__ == '__main__':
    uvicorn.run('app:app', reload=True)