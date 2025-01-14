from fastapi import APIRouter

from capstone.backend.llms.core.main import ChatModel

tags = ["Chatbot"]
router_chatbot = APIRouter(prefix='/chatbot')

@router_chatbot.get("/infer", tags=tags)
async def inferenceModel(question):
    chatbot = ChatModel()
    return {
        "question": question,
        "answer": chatbot.query(question=question)
        }

@router_chatbot.get("/infer/{model}", tags=tags)
async def inferenceModelSpecific():
    pass

@router_chatbot.get("/available", tags=tags)
async def availableModel():
    pass