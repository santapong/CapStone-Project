from langchain_core.prompt_values import PromptValue
from langchain_core.prompts import (
    ChatPromptTemplate
    )

# Reference
# https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_crag/
system = """You are a text refiner that corrects only incorrect words while preserving the original structure, punctuation, 
and meaning of the input. Do not change correctly written words. Only fix spelling mistakes or incorrect characters."""

refinement_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        (
            "human",
            "Here is the input text: \n\n {generation} \n Correct only incorrect words while keeping everything else unchanged."
        ),
    ]
)