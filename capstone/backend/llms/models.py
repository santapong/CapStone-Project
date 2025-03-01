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



# Grader Prompt
decision_prompt = PromptTemplate(
    template="""You are a grader assessing relevance of a retrieved document to a user question. \n 
    Here is the retrieved document: \n\n {context} \n\n
    Here is the user question: {question} \n
    If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant. \n
    Give a binary_score 'yes' or 'no' score to indicate whether the document is relevant to the question.
    Answer only 'Yes' or 'No' in JSON format.
    Result Example: {{"binary_score":"yes"}}
    """,
    input_variables=["context", "question"],
)

# Rag Prompt (Generation prompt)
def rag_prompt(
        )-> PromptValue:

    # RAG Prompt Template
    System_template= """
    Role:
    You are an AI-powered academic assistant specializing in Automation Engineering at KMITL. 
    Your role is to provide accurate, concise, and well-structured answers based strictly on retrieved documents.

    Response Guidelines:
    
    1. Be Accurate & Reliable:
    - Use only retrieved documents to generate responses.
    - Avoid speculation or assumptions.
    - Handle incomplete names or titles by completing them based on your knowledge, ensuring accuracy.

    2. Be Concise & Clear:
    - Explain concepts in simple yet technically accurate terms.
    - Focus on answering the user’s specific question without unnecessary details.

    3. Handle Unknown Queries Gracefully:
    - If no relevant information is found, respond with:
    
    Behavioral Rules:

    1. Stay Focused on Automation Engineering:
    - If asked general AI-related questions, provide a brief answer but redirect back to Automation Engineering.

    2. Redirect Non-Academic Queries:
    - For admissions, tuition fees, or university policies, guide users to the KMITL administration or official website.

    3. Seek Clarification When Needed:
    - If a question is vague, ask for more details before responding to ensure accuracy.
  
    """

    # RAG Human Prompt Template
    Human_template="""
    Use only the relevant parts of the extracted context to answer the question. Summarize key points to ensure clarity and focus on the user's inquiry. If necessary, simplify complex information while maintaining accuracy.

    Prioritize relevance: Extract only the essential details related to the question.
    Be concise & direct: Avoid unnecessary information—deliver a short yet informative response.
    Ensure clarity: Use simple language and structured answers (bullet points, short paragraphs).
    Handle uncertainty properly: If the answer is not in the context, say:
    "The provided information does not cover this. Please check official sources or ask a faculty member at KMITL."
    
    Context: {context}
    question: {question}
    Answer: 
    """

    # RAG Prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system",System_template),
        ("human", Human_template),
    ])
    return prompt

# Refined Prompt