import uvicorn

from fastapi import FastAPI
from src.backend.server import *

app = FastAPI()

uvicorn.run('main:app', reload=True)

