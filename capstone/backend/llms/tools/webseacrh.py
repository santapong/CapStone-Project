import os 

from pprint import pprint
from dotenv import load_dotenv
from typing import (
    List,
    Union, 
    Optional,
    ) 

from langchain_core.messages import HumanMessage
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_community.tools import DuckDuckGoSearchRun

# See how to binding tool to LLM
# https://python.langchain.com/docs/how_to/tool_results_pass_to_model/

def searchtool(
    query: int, 
    model: BaseChatModel,
    max_results: int = 5,
    )-> Union[Optional[str], list[str]]:
    
    # Bind tool to LLM.
    wrapper = DuckDuckGoSearchAPIWrapper(region="wt-wt", time="d", max_results=max_results) # Set Wrapper for Duckduckgo run
    tools = [DuckDuckGoSearchRun(api_wrapper=wrapper)] # Set the tool to binding to LLM
    llm_with_tools = model.bind_tools(tools)

    # Create HumanMassage Query.
    messages = [HumanMessage(query)]
    tools_message = llm_with_tools.invoke(messages)
    
    # Add ToolMessage to Message.
    messages.append(tools_message)
    for tool_call in tools_message.tool_calls:
        selected_tool = {"duckduckgo_search": DuckDuckGoSearchRun(api_wrapper=wrapper)}[tool_call["name"].lower()]
        tool_msg = selected_tool.invoke(tool_call)
        messages.append(tool_msg)
    
    # Query AI with DuckDuckgo Search.    
    answer = llm_with_tools.invoke(messages).content
    
    return answer