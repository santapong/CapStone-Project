from langchain_core.prompt_values import PromptValue
from langchain_core.prompts import (
    ChatPromptTemplate
    )

# TODO: Make it must more good answer.
# rlm/rag-prompt
# see https://smith.langchain.com/hub/rlm/rag-prompt?organizationId=2ee7223e-2f84-4a9b-924e-232565e6e92c
def rag_prompt(
        )-> PromptValue:

    # RAG Prompt Template
    instruction_template = """
    You are the assistant to answering the question. Use only the following parts of the 
    extracted context to answer the question. Additional information may be included, but
    must remain clearly in context. If you do not know the answer in context, say you do
    not know.
 
    Do not attempt to answer if it is not in context.
 
    If the question is in Thai, you must answer in Thai, regardless of the language of the 
    document. If the question is in English, you must answer in English. 

        Context: {context}
        question: {question}
        Answer: 
    """

    # RAG Prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("human", instruction_template),
    ])
    return prompt


# TODO: Adjust To Useful
# Pre-retrieval Template
def pre_retrieval(
        question
    )-> PromptValue:
    # Create Template for pre-retrieval
    template = """

        You are a helpful assistant whose sole task is to take a user's query and expand it into a 
        more detailed and clear question for a bot to answer. Your goal is to increase the detail 
        and clarity of the user's query without adding any additional information yourself. 

        If the user's query is already clear and detailed, do not add unnecessary details or make changes.

        Your role is strictly to expand or clarify the query, not to provide any answers or additional information. 

        If the query is in Thai, you must think and respond in Thai.
        If the query is in English, you must think and respond in English.

        Query: {question}
        Expanded Query:
            
        """
    prompt = ChatPromptTemplate([
        ("system", template),
        ("human", "{question}")
        ])
    
    return prompt.invoke({"question":question})

if __name__ == "__main__":
    test = rag_prompt(question="hellow")
    print(test)