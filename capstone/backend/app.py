import uvicorn

from fastapi import FastAPI
from capstone.backend.api.router.chatbot import router_chatbot
from capstone.backend.api.router.dashboard import router_dashboard
from capstone.backend.api.router.document import router_document

app = FastAPI()
app.include_router(router_chatbot)
app.include_router(router_dashboard)
app.include_router(router_document)


if __name__ == '__main__':
    uvicorn.run('app:app', reload=True)