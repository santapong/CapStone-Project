import os
import uvicorn
import logging

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import (
    RedirectResponse
    )

from capstone.backend.logs.logging_config import setup_logging
from capstone.backend.api.router import (
    router_chatbot,
    router_document,
    router_dashboard,
    )

# Setup log and load .env
load_dotenv()
setup_logging()
logging.getLogger(__name__)

# Set API Prefix and API application.
tags = ["Default"]
prefix = os.getenv("PATH_PREFIX", default='/')
app = FastAPI(prefix=prefix)

# Allow frontend to access API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Set redirect to /docs when enter root path ('/')
@app.get('/',tags=tags)
def docs():
    return RedirectResponse(url='/docs')

# Add router for API.
app.include_router(router_chatbot)
app.include_router(router_document)
app.include_router(router_dashboard)

if __name__ == '__main__':
    uvicorn.run('app:app', reload=True)