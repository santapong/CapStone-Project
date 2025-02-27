import os
import logging

from abc import abstractmethod
from dotenv import load_dotenv
from typing import Annotated, Sequence, List
from typing_extensions import TypedDict

from langchain_core.tools.simple import Tool
from langchain_core.messages import BaseMessage
from langchain.chat_models import init_chat_model
from langchain.tools.retriever import create_retriever_tool
from langchain_core.output_parsers import StrOutputParser
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

from langgraph.graph.message import add_messages
from langgraph.graph import END, StateGraph, START
from langgraph.prebuilt import ToolNode, tools_condition

from capstone.backend.llms.core import RAGModel
from capstone.backend.llms.tools.webseacrh import searchtool

from pydantic import BaseModel, Field

from capstone.backend.llms.prompts.decision_prompt import decision_prompt
from capstone.backend.llms.prompts.rag_prompt import rag_prompt
from capstone.backend.llms.utils.register import register_tool

from IPython.display import Image, display

load_dotenv()

# State of Agent between node to edge.
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]



# Data model for decision.
class Decision(BaseModel):
    """ Confident Document That have """

    score: int = Field(description="Decide the score that will using RAG or Search")




# Agentic That have RAG and Duckduckgo seacrh inside.
class AgenticModel(RAGModel):
    def __init__(self):
        super().__init__()
        self.tool_methods = [
            method_name for method_name in dir(self)
            if callable(getattr(self, method_name)) and hasattr(getattr(self, method_name), "_is_tool")
        ]
        
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
    @register_tool
    def retriever_tool(self)-> Tool:
        tool = create_retriever_tool(
            retriever=self.retriever,
            name="Automation Agent",
            description="Use to retrived document about Automation Engineering in KMITL.",
        )
        
        return tool
    
    # Search tool Using Duckduckgo seacrh
    @register_tool
    def search_tool(self)->Tool:
        wrapper = DuckDuckGoSearchAPIWrapper(max_results=10)
        tool = DuckDuckGoSearchRun(api_wrapper=wrapper)
        
        return tool
    
    # Abstract to collect tool inside AgenticModel class.
    @abstractmethod
    def get_tools(self) -> List:
        """Collect tools from AgenticModel"""
        return [getattr(self, method_name)() for method_name in self.tool_methods]
    
    
    # NOTE: is it need to using RAG Here
    # Prompt template
    def decision_document(self,state):
        logging.info(" -- Using decision model -- ")
        
        llm_with_tool = self.llm.with_structured_output(Decision)
        
        chain = decision_prompt | llm_with_tool
        
        message = state["messages"]
        last_message = message[-1]
        
        question = message[0].content
        docs = last_message.content
        
        scored_result = chain.invoke({"question": question, "context": docs})

        score = scored_result.binary_score

        if score >= 50:
            print("---DECISION: DOCS RELEVANT---")
            return "RAG"

        elif score < 50:
            print("---DECISION: DOCS NOT RELEVANT---")
            print(score)
            return "Search"
            
    def start_agent(self, state):
        logging.info("Start Agent")
        
        message = state["messages"]
        model_tools = self.llm.bind_tools(tools=self.get_tools())
        
        response = model_tools.invoke(message)

        return {"messages":[response]}        
    
    def search(self, state):
        logging.info("---Using Duckduckgo search")
        
        messages = state["messages"]
        question = messages[0].content
        last_message = messages[-1]
        
        
    
    def gererate(self, state):
        logging.info("---Using RAG Model---")
        
        messages = state["messages"]
        question = messages[0].content
        last_message = messages[-1]
        
        docs = last_message.content
        
        prompt = rag_prompt()
        
        # rag_chain
        rag_chain = prompt | self.llm | StrOutputParser()
        
        # invoke
        respond = rag_chain.invoke({"context": docs, "question":question})
        return {"message": [respond]}
        
        
# Create Garph using inheritance to AgenticModel.
class Garph(AgenticModel):
        def __init__(self):
            super().__init__()
    
        # Compile workflow here.
        def compile(self):
            self.workflow = StateGraph(AgentState)
            
            
            return self.workflow.compile()
        
        
        def display(self):
            try:
                display(Image(self.compile().get_graph(xray=True).draw_mermaid_png()))
            except Exception:
                pass

def get_agent():
    yield Garph.complie()
        
if __name__ == "__main__":
    test = Garph()
    print(test.compile())