from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate

# Data model for Routing.
class GradeDocuments(BaseModel):
    """ Scoring document That have relate to user's question"""

    binary_score: str = Field(
        description="Documents are relevant to the question, 'yes' or 'no'"
    )

# Prompt
decision_prompt = PromptTemplate(
    template="""You are a grader assessing relevance of a retrieved document to a user question. \n 
    Here is the retrieved document: \n\n {context} \n\n
    Here is the user question: {question} \n
    If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant. \n
    Give a binary_score 'yes' or 'no' score to indicate whether the document is relevant to the question.
    Answer only 'Yes' or 'No' in JSON format.
    Result Example: "["binary_score":"yes"]"
    """,
    input_variables=["context", "question"],
)