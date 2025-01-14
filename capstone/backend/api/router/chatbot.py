import time
import logging
from fastapi import APIRouter

from capstone.backend.llms.main import ChatModel

from capstone.backend.api.database import DBConnect

logging.getLogger(__name__)

tags = ["Chatbot"]
router_chatbot = APIRouter(prefix='/chatbot')

# NOTE: Wait for LLMS is good.
# TODO: Make it will connect to database.
@router_chatbot.get("/infer", tags=tags)
async def inferenceModel(question):
    start_time = time.time()
    chatbot = ChatModel()
    answer = chatbot.query(question=question)
    time_usage = time.time()-start_time
    logging.info(time_usage)
    return {
        "time usage": time_usage,
        "question": question,
        "answer": answer
        }

# TODO: Make it can connect to database.
@router_chatbot.get("/infer/{model}", tags=tags)
async def inferenceModelSpecific():
    pass

# NOTE: Using for check Model on database.
@router_chatbot.get("/available", tags=tags)
async def availableModel():
    pass


# NOTE: It will have more database.