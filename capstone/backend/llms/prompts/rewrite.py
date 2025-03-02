from langchain_core.prompts import ( 
    PromptTemplate,
    ChatPromptTemplate,
    )

# Reference
# https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/
system = """You a question re-writer that converts an input question to a better version that is optimized \n 
     for web search. Look at the input and try to reason about the underlying semantic intent / meaning."""

re_write_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        (
            "human",
            "Here is the initial question: \n\n {question} \n Formulate an improved question.",
        ),
    ]
)