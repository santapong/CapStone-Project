from typing import TypedDict, List
from pydantic import BaseModel, Field
from langchain_core.prompt_values import PromptValue
from langchain_core.prompts import ( 
    PromptTemplate,
    ChatPromptTemplate,
    )

# State of Agent between node to edge.
class AgentState(TypedDict):
    
    """
    Data store State in Agent.
    
    # Parameter Using in state
    question: User question from inference.
    generation: LLM answer.
    web_search: Result from websearch.
    documents: Retrieve documents from vector_database.
    
    """
    refine: str
    rewrite: str
    question: str
    generation: str
    web_search: str
    web_result: List[str]
    documents: List[str]



# Data model for Routing.
class GradeDocuments(BaseModel):
    """ Scoring document That have relate to user's question"""

    binary_score: str = Field(
        description="Documents are relevant to the question, 'yes' or 'no'"
    )
