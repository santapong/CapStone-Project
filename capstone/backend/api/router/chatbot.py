import os
import time
import logging

from dotenv import load_dotenv
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from capstone.backend.llms import RAGModel
from capstone.backend.api.schema.model_api import (
    ChatModel,
    ResponseModel
)
from capstone.backend.database.connection import DBConnection, get_db
from capstone.backend.database.models import LogsTable
from capstone.backend.llms.prompt_template import RAG_prompt_template

load_dotenv()
logging.getLogger(__name__)

RAG = RAGModel()

tags = ["Chatbot"]
router_chatbot = APIRouter(prefix='/chatbot')

# TODO: Make it will connect to database.
@router_chatbot.post("/infer", tags=tags, response_model=ResponseModel)
async def inferenceModel(request: ChatModel, db: DBConnection = Depends(get_db)):
    start_time = time.time()
    answer = RAG.invoke(question=request.question)
    time_usage = time.time()-start_time
    logging.info(time_usage)

    # Save to database
    db.insert(LogsTable, prompt=RAG_prompt_template, question=request.question, answer=answer['answer'], time_usage=time_usage)

    return JSONResponse(content={
        "time usage": time_usage,
        "question": request.question,
        "answer": answer['answer']
        })
