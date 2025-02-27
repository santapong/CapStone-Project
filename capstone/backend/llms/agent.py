import os
import logging

from uuid import uuid4
from abc import abstractmethod
from dotenv import load_dotenv
from typing import Annotated, Sequence
from typing_extensions import TypedDict

from langchain_core.messages import BaseMessage
from langchain.chat_models import init_chat_model
from langchain.tools.retriever import create_retriever_tool
from langchain_core.tools.simple import Tool

from langgraph.graph.message import add_messages

from capstone.backend.llms.core import RAGModel
from capstone.backend.llms.tools.webseacrh import searchtool

from pydantic import BaseModel, Field

load_dotenv()

# State of Agent between node to edge.
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

# Data model for decision.
class grade(BaseModel):
    """ Confident Document That have """

    score: int = Field(description="Decide the score that will using RAG or Search")

# Agentic That have RAG and Duckduckgo seacrh inside.
class AgenticModel(RAGModel):
    def __init__(self):
        super().__init__()
        self.retriever = self.get_vector_store().as_retriever()
        self.llm = self.init_model()
        
    def init_model(self,
                    llm_model:str = os.getenv("LLM_MODEL"),
                    model_provider:str = os.getenv("MODEL_PROVIDER"),
                    temperature: float = os.getenv("TEMPERATURE"),
                    model_base_url: str = os.getenv("MODEL_BASE_URL")
                     ):
        return init_chat_model(
                        model=llm_model, 
                        model_provider=model_provider, 
                        temperature=temperature,
                        base_url=model_base_url,
                    )   
        
    # FIXME: Need to use At vector_database model
    def retriver_tool(self) -> Tool:
        self.retriever_tool = create_retriever_tool(
            retriever=self.retriever,
            name="Automation Agent",
            description="Use to retrived document about Automation Engineering in KMITL.",
        )
        
        return self.retriever_tool
    
    # Search tool Using Duckduckgo seacrh
    def search_tool(self) -> Tool:
        pass
    
    # Prompt template
    def grade_document(self):
        logging.info(" -- Using grade document -- ")
        
        
        
        
if __name__ == "__main__":
    test = AgenticModel()