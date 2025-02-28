import os
import logging

from abc import abstractmethod
from dotenv import load_dotenv
from typing import List

from langchain_core.tools.simple import Tool
from langchain.chat_models import init_chat_model
from langchain.tools.retriever import create_retriever_tool
from langchain_core.output_parsers import StrOutputParser
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

from langgraph.graph import END, StateGraph, START

from capstone.backend.llms.core import RAGModel
from capstone.backend.llms.models import GradeDocuments, decision_prompt, AgentState
from capstone.backend.llms.prompts.rag_prompt import rag_prompt
from capstone.backend.llms.utils.register import register_tool

from IPython.display import Image, display

# Parsing ENV parameter from .env
load_dotenv()
logging.getLogger(__name__)

# See Agent Paradigms
# 
# Agentic That have RAG and Duckduckgo seacrh inside.
class AgenticModel(RAGModel):
    def __init__(self):
        
        super().__init__()
        self.__tool_methods = [
            method_name for method_name in dir(self)
            if callable(getattr(self, method_name)) and hasattr(getattr(self, method_name), "_is_tool")
        ]
        self.retriever =  self.get_vector_store().as_retriever()
        self.llm = self.__init_model()
        
    # Intialize Model internal method
    def __init_model(self,
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
    # Not use
    # RAG model tool.
    @register_tool
    def retriever_tool(self)-> Tool:
        tool = create_retriever_tool(
            retriever=self.retriever,
            name="RAG tools",
            description="Use to retrived document about Automation Engineering in KMITL.",
        )
        
        return tool
    
    # Search tool Using Duckduckgo search.
    @register_tool
    def search_tool(self)->DuckDuckGoSearchRun:
        wrapper = DuckDuckGoSearchAPIWrapper(max_results=10)
        tool = DuckDuckGoSearchRun(
            name="Websearh tool from Duckduckgo",
            description="Use to search website via Duckduckgo.",
            api_wrapper=wrapper,
        )
        
        return tool
    
    # Abstract to collect tool inside AgenticModel class.
    @abstractmethod
    def get_tools(self) -> List:
        """Collect tools from AgenticModel"""
        return [getattr(self, method_name)() for method_name in self.__tool_methods]
    
    ## Node

    # NOTE: Pass
    # Using to grading the document that retrive.
    def grade_document(
            self, 
            state: AgentState
        ):
        
        # Set structure of output > yes or no.
        structured_llm_grader = self.llm.with_structured_output(GradeDocuments)
        
        # LLM Chain
        retrieval_grader = decision_prompt | structured_llm_grader
        question = "What age of obama"
        
        # Retrieval Document.
        docs = self.retriever.invoke(question)
        doc_text = docs[0].page_content
        
        # Result expected {"binary_score": "yes"}
        response = retrieval_grader.invoke({"question": question, "context": doc_text})
        
        return {"response":response}

    # NOTE: Pass
    # Retrieval Agent.
    def retrieval_agent(
            self, 
            state: AgentState
        ):
        logging.info("----Retrieve Agent----")
        
        # Get question from Agentstate
        question = state["question"]

        # Retrieval
        documents = self.retriever.invoke(question)
        return {"documents": documents, "question": question}

    # NOTE: Pass
    # Search Agent using Duckduckgo search.
    def search_agent(
            self, 
            state: AgentState 
        ):
        logging.info("---Using Duckduckgo search---")
        
        # Parsing from AgentState
        question = state["question"]
        web_search = state["web_search"]
        
        # Get 
        document = self.search_tool().invoke({"query": question})
        web_search.append(document)
        
        return {"web_search": web_search, "question": question}
        
    # NOTE: Pass
    # Generate Agent
    def generate_agent(
            self, 
            state: AgentState
        ):
        logging.info("---Using RAG Model---")
        
        # Parsing from Agent State.
        question = state["question"]
        document = state["documents"]
        web_search = state["web_search"]
        
        # rag_chain
        rag_chain = rag_prompt() | self.llm | StrOutputParser()
        
        # invoke
        respond = rag_chain.invoke({"context": document, "question":question})
        return {"message": [respond]}
        
    ## Edge
        
    # NOTE: need test
    # Get decision from Grade_document. 
    def decide_to_search(self,
                        state: AgentState
                        ):
        
        
        return {"message"}
        
    
# Create Garph using inheritance to AgenticModel.
class Garph(AgenticModel):
        def __init__(self):
            super().__init__()
            
        # Compile workflow here.
        @abstractmethod
        def compile(self):
            self.workflow = StateGraph(AgentState)
            
            # Build Node
            # Need more node to refined answer.
            self.workflow.add_node("retrieval_agent", self.retrieval_agent)
            self.workflow.add_node("grade_document", self.grade_document)
            self.workflow.add_node("search_agent", self.search_agent)
            self.workflow.add_node("generate_agent", self.generate_agent)
            
            # Build Graph using Edge to connect node to node.
            self.workflow.add_edge(start_key=START, end_key= "retrieval_agent")
            self.workflow.add_edge(start_key="retrieval_agent", end_key="grade_document")
            self.workflow.add_conditional_edges(
                source="grade_document", 
                path=self.decide_to_search,
                path_map={
                    "yes":"generate_agent",
                    "no":"search_agent"
                })
            self.workflow.add_edge(start_key="search_agent", end_key="generate_agent")                        
            self.workflow.add_edge(start_key="generate_agent", end_key=END)
            
            return self.workflow.compile()
        
        @abstractmethod
        def display(self):
            try:
                return display(Image(self.compile().get_graph(xray=True).draw_mermaid_png()))
            except Exception:
                pass

def get_agent():
    yield Garph.complie()
        
if __name__ == "__main__":
    test = Garph()