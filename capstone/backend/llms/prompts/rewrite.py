from langchain_core.prompts import ( 
    PromptTemplate,
    ChatPromptTemplate,
    )

# Reference
# https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/
system = """You are a question re-writer that enhances the input question for web search. 
Analyze the question to determine the underlying semantic intent and extract the essential keywords for an optimized search.

Your task is:
1. Reformulate the user's question into a clearer, more concise query that is suitable for search engines.
2. Identify and extract the most relevant keywords from the question that will improve search accuracy.

Ensure that the rewritten question retains the original meaning while improving clarity."""

re_write_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        (
            "human",
            "Here is the user's question:\n\n {question} \n\n Reformulate it for better search results and extract important keywords."
        ),
    ]
)
