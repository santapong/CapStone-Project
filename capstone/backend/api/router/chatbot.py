import os
import time
import logging

from dotenv import load_dotenv
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from capstone.backend.llms.main import RAGmodel
from capstone.backend.api.schema.model_api import (
    ChatModel,
    ResponseModel
)
from capstone.backend.utils.database import DBConnection, get_db
from capstone.backend.api.schema.model_database import Users

load_dotenv()
logging.getLogger(__name__)

# RAG = RAGmodel().setModel().setEmbeddings().setVectorDB()

tags = ["Chatbot"]
router_chatbot = APIRouter(prefix='/chatbot')

# TODO: Make it will connect to database.
@router_chatbot.post("/infer", tags=tags, response_model=ResponseModel)
async def inferenceModel(request: ChatModel, db: DBConnection = Depends(get_db)):
    start_time = time.time()
    answer = RAG.invoke(question=request.question)
    time_usage = time.time()-start_time
    logging.info(time_usage)
    return JSONResponse(content={
        "time usage": time_usage,
        "question": request.question,
        "answer": answer['answer']
        })

if __name__ == "__main__":
    test = next(get_db())
    test.insert(Users, fullname="test")
    