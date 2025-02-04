import time
import logging

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from capstone.backend.llms.main import RAGmodel
from capstone.backend.api.schema.model_api import (
    ChatModel,
    ResponseModel
)
from capstone.backend.api.database import (
    DBConnection,
    DATABASE_CREATE,
    DATABASE_MODEL
    )

logging.getLogger(__name__)

DBConnect = DBConnection(
        create_database=DATABASE_CREATE,
        base_model=DATABASE_MODEL)

RAG = RAGmodel().setModel().setEmbeddings().setVectorDB()

tags = ["Chatbot"]
router_chatbot = APIRouter(prefix='/chatbot')

# TODO: Make it will connect to database.
@router_chatbot.post("/infer", tags=tags, response_model=ResponseModel)
async def inferenceModel(request: ChatModel):
    start_time = time.time()
    answer = RAG.invoke(question=request.question)
    time_usage = time.time()-start_time
    logging.info(time_usage)
    return JSONResponse(content={
        "time usage": time_usage,
        "question": request.question,
        "answer": answer['answer']
        })