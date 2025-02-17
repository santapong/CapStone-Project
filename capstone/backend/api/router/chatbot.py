import time
import logging
import capstone.backend.database.events

from dotenv import load_dotenv
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from capstone.backend.llms import get_RAG, RAGModel
from capstone.backend.api.models import (
    ChatModel,
    ResponseModel,
)
from capstone.backend.database.connection import (
    DBConnection, 
    get_db,
    )
from capstone.backend.database.models import LogsTable
from capstone.backend.llms.prompt_template import rag_prompt

load_dotenv()
logging.getLogger(__name__)

tags = ["Chatbot"]
router_chatbot = APIRouter(prefix='/chatbot')

# TODO: Make it will connect to database.
@router_chatbot.post("/infer", tags=tags, response_model=ResponseModel)
async def inferenceModel(
    request: ChatModel, 
    db: DBConnection = Depends(get_db),
    RAG: RAGModel = Depends(get_RAG)
    ):
    
    # Record Response time to Analysis.
    start_time = time.time()
    answer = RAG.invoke(question=request.question)
    time_usage = time.time()-start_time
    logging.info(time_usage)

    # Insert to database
    db.insert(
        table=LogsTable, 
        prompt=rag_prompt.__name__+" temp=0.5", 
        question=request.question, 
        answer=answer['answer'], 
        time_usage=time_usage
        )
    
    logging.info(len(answer['context']))
    return JSONResponse(content={
        "time usage": time_usage,
        "question": request.question,
        "answer": answer['answer']
        })
