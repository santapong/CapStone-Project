from typing import (
    Union, 
    Optional,
    ) 

from langchain_core.messages import HumanMessage
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_community.tools import DuckDuckGoSearchRun

# See how to binding tool to LLM
# https://python.langchain.com/docs/how_to/tool_results_pass_to_model/

# ######################################### #
# |                                       | #
# |         NOT USE THIS FUNCTION         | #
# |                                       | #
# ######################################### #

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

if __name__ == "__main__":
    from langchain_core.tools import Tool
    from langchain_google_community import GoogleSearchAPIWrapper, GoogleSearchRun, GoogleSearchResults

    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    
    wrapper = GoogleSearchAPIWrapper(
        k=10,
        google_cse_id=os.getenv("GOOGLE_CSE_ID"),   
        google_api_key=os.getenv("GOOGLE_API_KEY"),
    )
    tools = GoogleSearchRun(
        api_wrapper=wrapper,
        name="Google Search Enginer",
        description="Goole Search Will Replace Duckduckgo"
    )
    
    test = GoogleSearchResults(
        api_wrapper=wrapper,
        num_results=10
    )
    
    tool = Tool(
    name="google_search",
    description="Search Google for recent results.",
    func=wrapper.run,
    )
    
    print(test.invoke("majorana 1"))
    print(tools.invoke("majorana 1"))
    print(tool.run("majorana 1"))
    # print(tool.invoke("Majorana 1"))