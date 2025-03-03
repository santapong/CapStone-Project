import time
import logging
import os

# Import to use Event of SQLalchemy
import capstone.backend.database.events

from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from capstone.backend.llms import get_RAG, RAGModel, get_agent, Garph
from capstone.backend.api.models import (
    ChatModel,
    ResponseModel,
)
from capstone.backend.database.connection import (
    DBConnection, 
    get_db,
)
from capstone.backend.database.models import LogsTable
from capstone.backend.llms.prompts import rag_prompt

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

tags = ["Chatbot"]
router_chatbot = APIRouter(prefix='/chatbot', tags=tags)

@router_chatbot.post("/infer", response_model=ResponseModel)
async def inference_Model(
    request: ChatModel, 
    RAG: RAGModel= Depends(get_RAG),
    db: DBConnection = Depends(get_db),
):
    start_time = time.time()
    
    try:
        answer = RAG.invoke({"question": request.question})
        time_usage = time.time() - start_time
        logger.info(f"Time usage: {time_usage}s")

        # Insert successful response into database
        db.insert(
            table=LogsTable,
            llm_model=os.getenv("LLM_MODEL"),
            prompt=rag_prompt.__name__, 
            question=request.question, 
            answer=answer['answer'], 
            time_usage=time_usage
        )

        return JSONResponse(content={
            "time usage": time_usage,
            "question": request.question,
            "answer": answer['answer']
        })
    
    except Exception as e:
        time_usage = time.time() - start_time
        error_message = str(e)
        logger.error(f"Error occurred: {error_message}")

        # Insert error details into database
        db.insert(
            table=LogsTable,
            llm_model=os.getenv("LLM_MODEL"),
            prompt=rag_prompt.__name__,
            question=request.question,
            answer="ERROR", 
            time_usage=time_usage
        )

        raise HTTPException(status_code=500, detail="An error occurred while processing your request.")
